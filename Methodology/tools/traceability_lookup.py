#!/usr/bin/env python3
"""Query a fixed-schema EU-law traceability workbook as JSON.

The tool deliberately exposes exact, canonical identifiers only. It does not
perform text search or fuzzy ID matching because those can lose legal-location
precision.

The input file must be named ``<REGULATION>-CELEX:<CELEX>.xlsx``; for example,
``DORA-CELEX:32022R2554.xlsx``. This makes the workbook's legal identity
visible to operators and prevents using one law's index for another law.

Operator-facing commands:
* ``row-id``: return the canonical path for an Enacting Terms row number.
* ``row-text``: return the text for an Enacting Terms row number.
* ``text-by-id``: return a unique recital or Enacting Terms row by exact ID.
* ``verify-anchor``: accept only a unique, non-amendment Enacting Terms ID for
  use as a legal Requirement/Constraint traceability anchor.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from openpyxl import load_workbook
    from openpyxl.utils.exceptions import InvalidFileException
except ImportError:  # Kept import-safe so callers receive structured JSON.
    load_workbook = None
    InvalidFileException = Exception


RECITAL_SHEET = "Recitals"
ENACTING_TERMS_SHEET = "Enacting Terms"
RECITAL_HEADERS = ("Number", "Text")
ENACTING_HEADERS = (
    "Part",
    "Title",
    "Chapter",
    "Section",
    "Article",
    "Paragraph",
    "Sub-Paragraph",
    "Point",
    "Point Sub-Paragraph",
    "Sub-Point",
    "Indent",
    "Text",
)
# The first eleven columns form the legal hierarchy; the twelfth is the text.
ID_COLUMNS = ENACTING_HEADERS[:-1]
ID_PREFIXES = (
    ("Part", "Part "),
    ("Title", "Title "),
    ("Chapter", "Chap."),
    ("Section", "Section "),
    ("Article", "Art."),
    ("Paragraph", "Paragraph "),
    ("Sub-Paragraph", "Sub-Paragraph "),
    ("Point", "Point "),
    ("Point Sub-Paragraph", "P.Sub-Paragraph "),
    ("Sub-Point", "Sub-Point "),
    ("Indent", "Indent "),
)

EXIT_USAGE = 2
EXIT_WORKBOOK = 3
EXIT_LOOKUP = 4
# Amendment Articles are deliberately excluded from legal-duty anchoring.
# The expression identifies their Article-heading text during workbook loading.
AMENDMENT_HEADING = re.compile(r"^(?:amendments?\s+to\b|amending\b)", re.IGNORECASE)
# File names are part of the legal-source contract. CELEX identifiers use the
# sector/year/type/number structure demonstrated by 32022R2554 and 32022L2555.
LEGAL_INDEX_FILENAME = re.compile(
    r"^(?P<law>[A-Za-z][A-Za-z0-9-]*)-CELEX:(?P<celex>3\d{4}[RL]\d{4})\.xlsx$"
)


class TraceabilityError(Exception):
    """An expected error that has a stable JSON code and process exit status."""

    def __init__(self, code: str, message: str, exit_code: int, **details: Any) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.exit_code = exit_code
        self.details = details


class JsonArgumentParser(argparse.ArgumentParser):
    """Argparse variant that does not leak non-JSON errors to stderr/stdout."""

    def error(self, message: str) -> None:
        raise TraceabilityError("INVALID_ARGUMENTS", message, EXIT_USAGE)


@dataclass(frozen=True)
class TraceabilityRow:
    """One workbook row plus its stable, human-readable legal location.

    ``global_row`` is the one-based row within Enacting Terms data (excluding
    the heading row). It is absent for recitals because they use a separate
    worksheet and are never valid anchors.
    """
    sheet: str
    worksheet_row: int
    canonical_id: str
    text: str
    global_row: int | None = None
    is_amendment: bool = False

    def success_payload(self) -> dict[str, Any]:
        """Build the full JSON representation returned for a successful lookup."""
        payload: dict[str, Any] = {
            "sheet": self.sheet,
            "worksheet_row": self.worksheet_row,
            "id": self.canonical_id,
            "text": self.text,
        }
        if self.global_row is not None:
            payload["global_row"] = self.global_row
        return payload

    def reference_payload(self) -> dict[str, Any]:
        """Build the safe, text-free reference used in ambiguity/error responses."""
        payload: dict[str, Any] = {
            "sheet": self.sheet,
            "worksheet_row": self.worksheet_row,
            "id": self.canonical_id,
        }
        if self.global_row is not None:
            payload["global_row"] = self.global_row
        return payload


def cell_text(value: Any) -> str:
    """Normalise a workbook cell for comparison without changing its meaning.

    Empty cells become ``""`` and populated values have surrounding whitespace
    removed. All later ID construction uses this one conversion rule.
    """

    if value is None:
        return ""
    return str(value).strip()


def format_enacting_id(values: Iterable[Any]) -> str:
    """Create the displayed canonical path from the Enacting Terms hierarchy.

    The workbook may omit hierarchy levels. This function retains every
    non-empty level in its prescribed order, for example
    ``Chap.I, Art.3, Paragraph 1, Point a``.
    """

    formatted = []
    for (_, prefix), value in zip(ID_PREFIXES, values, strict=True):
        cleaned = cell_text(value)
        if cleaned:
            formatted.append(f"{prefix}{cleaned}")
    return ", ".join(formatted)


def validate_canonical_id(identifier: str) -> bool:
    """Reject malformed IDs before an exact workbook lookup.

    This deliberately does not correct case, spacing, or hierarchy order: the
    operator must use the exact value returned by ``row-id`` or ``text-by-id``.
    """

    if identifier.startswith("Recital "):
        return bool(identifier.removeprefix("Recital ")) and "," not in identifier

    tokens = identifier.split(", ")
    if not identifier or ", ".join(tokens) != identifier:
        return False

    previous_index = -1
    for token in tokens:
        found_index = next(
            (
                index
                for index, (_, prefix) in enumerate(ID_PREFIXES)
                if token.startswith(prefix) and len(token) > len(prefix)
            ),
            None,
        )
        if found_index is None or found_index <= previous_index:
            return False
        prefix = ID_PREFIXES[found_index][1]
        value = token.removeprefix(prefix)
        if value != value.strip():
            return False
        previous_index = found_index
    return True


class TraceabilityWorkbook:
    """Load, validate, and query one law-specific workbook without modifying it."""

    def __init__(self, path: str) -> None:
        """Open a named legal index and build recital and enacting-term indexes.

        The file name independently identifies the regulation and CELEX number;
        callers still validate the workbook's contents and schema below.
        """
        if load_workbook is None:
            raise TraceabilityError(
                "DEPENDENCY_MISSING",
                "openpyxl is required. Install dependencies with: pip install -r tools/requirements.txt",
                EXIT_WORKBOOK,
            )

        self.path = Path(path)
        if self.path.suffix.lower() != ".xlsx":
            raise TraceabilityError(
                "UNSUPPORTED_FILE",
                "Only .xlsx workbooks are supported.",
                EXIT_WORKBOOK,
            )
        if not self.path.is_file():
            raise TraceabilityError(
                "FILE_NOT_FOUND",
                f"Workbook does not exist: {self.path}",
                EXIT_WORKBOOK,
            )
        filename_match = LEGAL_INDEX_FILENAME.fullmatch(self.path.name)
        if filename_match is None:
            raise TraceabilityError(
                "INVALID_LEGAL_INDEX_NAME",
                "Workbook name must use <REGULATION>-CELEX:<CELEX>.xlsx, for example DORA-CELEX:32022R2554.xlsx.",
                EXIT_WORKBOOK,
            )

        # Retain the filename identity for callers that need to compare it with
        # the selected regulation before accepting legal-text anchors.
        self.law_name = filename_match.group("law")
        self.celex = filename_match.group("celex")

        try:
            self.workbook = load_workbook(self.path, read_only=True, data_only=True)
        except (InvalidFileException, OSError, ValueError) as exc:
            raise TraceabilityError(
                "INVALID_WORKBOOK",
                f"Unable to read workbook: {exc}",
                EXIT_WORKBOOK,
            ) from exc

        self._validate_schema()
        self._recitals = self._read_recitals()
        self._enacting_rows = self._read_enacting_terms()

    def close(self) -> None:
        """Release the read-only workbook handle after every command."""
        self.workbook.close()

    def _validate_schema(self) -> None:
        """Ensure this is a compatible named legal-index workbook before reading law text."""
        required_sheets = {RECITAL_SHEET, ENACTING_TERMS_SHEET}
        missing_sheets = required_sheets - set(self.workbook.sheetnames)
        if missing_sheets:
            raise TraceabilityError(
                "SCHEMA_MISMATCH",
                "Workbook is missing required sheets.",
                EXIT_WORKBOOK,
                missing_sheets=sorted(missing_sheets),
            )

        self._validate_headers(RECITAL_SHEET, RECITAL_HEADERS)
        self._validate_headers(ENACTING_TERMS_SHEET, ENACTING_HEADERS)

    def _validate_headers(self, sheet_name: str, expected: tuple[str, ...]) -> None:
        """Require the fixed column order so canonical paths cannot silently drift."""
        worksheet = self.workbook[sheet_name]
        actual = tuple(cell_text(value) for value in next(worksheet.iter_rows(max_row=1, values_only=True)))
        if actual != expected:
            raise TraceabilityError(
                "SCHEMA_MISMATCH",
                f"Unexpected headers in '{sheet_name}'.",
                EXIT_WORKBOOK,
                expected_headers=list(expected),
                actual_headers=list(actual),
            )

    def _read_recitals(self) -> list[TraceabilityRow]:
        """Index recital rows for ordinary lookup, but never mark them as anchors."""
        worksheet = self.workbook[RECITAL_SHEET]
        rows: list[TraceabilityRow] = []
        for worksheet_row, values in enumerate(
            worksheet.iter_rows(min_row=2, values_only=True), start=2
        ):
            number, text = values
            number_text = cell_text(number)
            if not number_text:
                continue
            rows.append(
                TraceabilityRow(
                    sheet=RECITAL_SHEET,
                    worksheet_row=worksheet_row,
                    canonical_id=f"Recital {number_text}",
                    text=cell_text(text),
                )
            )
        return rows

    def _read_enacting_terms(self) -> list[TraceabilityRow]:
        """Index enacting terms and flag all rows belonging to amendment Articles.

        The first pass finds Article headings such as ``Amendments to ...``.
        The second pass emits every enacting row and marks rows sharing that
        Article context. Keeping this classification at load time makes
        ``verify-anchor`` deterministic even where amendment paths are repeated.
        """
        worksheet = self.workbook[ENACTING_TERMS_SHEET]
        raw_rows: list[tuple[int, tuple[Any, ...]]] = []
        amendment_articles: set[tuple[str, str, str, str, str]] = set()
        # First pass: retain usable rows and identify amendment Article contexts.
        for global_row, values in enumerate(worksheet.iter_rows(min_row=2, values_only=True), start=1):
            ids = values[:-1]
            if not any(cell_text(value) for value in ids):
                continue
            raw_rows.append((global_row, values))
            article_context = tuple(cell_text(value) for value in ids[:5])
            is_article_heading = bool(article_context[-1]) and not any(
                cell_text(value) for value in ids[5:]
            )
            if is_article_heading and AMENDMENT_HEADING.match(cell_text(values[-1])):
                amendment_articles.add(article_context)

        rows: list[TraceabilityRow] = []
        # Second pass: generate lookup rows carrying the inherited amendment flag.
        for global_row, values in raw_rows:
            ids = values[:-1]
            rows.append(
                TraceabilityRow(
                    sheet=ENACTING_TERMS_SHEET,
                    worksheet_row=global_row + 1,
                    global_row=global_row,
                    canonical_id=format_enacting_id(ids),
                    text=cell_text(values[-1]),
                    is_amendment=tuple(cell_text(value) for value in ids[:5]) in amendment_articles,
                )
            )
        return rows

    def verify_enacting_anchor(self, identifier: str) -> TraceabilityRow:
        """Validate a legal-duty anchor against this law's binding Enacting Terms.

        Unlike ``text_by_id``, this operation excludes recitals and amendment
        provisions and requires one unique matching row. Use it before storing
        an ID in Requirement/Constraint documentation.
        """

        if identifier.startswith("Recital "):
            raise TraceabilityError(
                "RECITAL_FORBIDDEN",
                "Recitals cannot be used as legal-text anchors.",
                EXIT_LOOKUP,
            )
        if not validate_canonical_id(identifier):
            raise TraceabilityError(
                "MALFORMED_ID",
                "ID must use the exact canonical format emitted by row-id.",
                EXIT_LOOKUP,
            )

        matches = [row for row in self._enacting_rows if row.canonical_id == identifier]
        if not matches:
            raise TraceabilityError(
                "NOT_FOUND",
                f"No enacting-term row matches ID: {identifier}",
                EXIT_LOOKUP,
            )
        if all(row.is_amendment for row in matches):
            raise TraceabilityError(
                "AMENDMENT_FORBIDDEN",
                "Amendment provisions cannot be used as legal-text anchors.",
                EXIT_LOOKUP,
                matches=[row.reference_payload() for row in matches],
            )
        if len(matches) > 1:
            raise TraceabilityError(
                "AMBIGUOUS_ID",
                f"ID maps to {len(matches)} rows; use a non-amendment canonical path.",
                EXIT_LOOKUP,
                matches=[row.reference_payload() for row in matches],
            )
        row = matches[0]
        return row

    def text_by_id(self, identifier: str) -> TraceabilityRow:
        """Look up exactly one recital or enacting row without anchor restrictions."""
        if not validate_canonical_id(identifier):
            raise TraceabilityError(
                "MALFORMED_ID",
                "ID must use the exact canonical format emitted by row-id.",
                EXIT_LOOKUP,
            )

        matches = [
            row
            for row in (*self._recitals, *self._enacting_rows)
            if row.canonical_id == identifier
        ]
        if not matches:
            raise TraceabilityError(
                "NOT_FOUND",
                f"No row matches ID: {identifier}",
                EXIT_LOOKUP,
            )
        if len(matches) > 1:
            raise TraceabilityError(
                "AMBIGUOUS_ID",
                f"ID maps to {len(matches)} rows; use row-id or row-text.",
                EXIT_LOOKUP,
                matches=[row.reference_payload() for row in matches],
            )
        return matches[0]

    def enacting_row(self, global_row: int) -> TraceabilityRow:
        """Return the enacting-term row addressed by its one-based data-row number."""
        if global_row < 1:
            raise TraceabilityError(
                "INVALID_ROW",
                "Row must be a positive enacting-terms data-row number.",
                EXIT_LOOKUP,
            )
        if global_row > len(self._enacting_rows):
            raise TraceabilityError(
                "ROW_OUT_OF_RANGE",
                f"Row {global_row} is outside the enacting-terms data range 1-{len(self._enacting_rows)}.",
                EXIT_LOOKUP,
            )
        return self._enacting_rows[global_row - 1]


def build_parser() -> JsonArgumentParser:
    """Declare the small command-line contract shared by humans and agents."""
    parser = JsonArgumentParser(add_help=False)
    subcommands = parser.add_subparsers(dest="operation", required=True)

    for operation in ("text-by-id", "row-id", "row-text", "verify-anchor"):
        command = subcommands.add_parser(operation, add_help=False)
        command.add_argument("--file", required=True)
        if operation in ("text-by-id", "verify-anchor"):
            command.add_argument("--id", dest="identifier", required=True)
        else:
            command.add_argument("--row", type=int, required=True)
    return parser


def run(arguments: list[str]) -> dict[str, Any]:
    """Dispatch one command and shape its successful response as JSON data.

    ``row-id`` suppresses text and ``row-text`` suppresses the canonical ID so
    callers receive only the field they asked for. Other commands return both.
    """
    parser = build_parser()
    args = parser.parse_args(arguments)
    workbook = TraceabilityWorkbook(args.file)
    try:
        if args.operation == "text-by-id":
            row = workbook.text_by_id(args.identifier)
        elif args.operation == "verify-anchor":
            row = workbook.verify_enacting_anchor(args.identifier)
        else:
            row = workbook.enacting_row(args.row)
        # Echo the regulation identity parsed from the required filename so a
        # caller can prove it queried the intended law rather than only a
        # similarly structured workbook.
        payload: dict[str, Any] = {
            "ok": True,
            "operation": args.operation,
            "law": workbook.law_name,
            "celex": workbook.celex,
        }
        payload.update(row.success_payload())
        if args.operation == "row-id":
            payload.pop("text")
        elif args.operation == "row-text":
            payload.pop("id")
        return payload
    finally:
        workbook.close()


def main(arguments: list[str] | None = None) -> int:
    """Run the CLI and emit exactly one JSON object on success or failure.

    Stable error codes and non-zero exit statuses allow agents and shell users
    to distinguish malformed input, workbook failures, and lookup failures.
    """
    try:
        payload = run(sys.argv[1:] if arguments is None else arguments)
    except TraceabilityError as exc:
        payload = {"ok": False, "code": exc.code, "message": exc.message}
        payload.update(exc.details)
        print(json.dumps(payload, ensure_ascii=False))
        return exc.exit_code
    except Exception as exc:  # Avoid stack traces contaminating the agent contract.
        print(
            json.dumps(
                {
                    "ok": False,
                    "code": "UNEXPECTED_ERROR",
                    "message": str(exc),
                },
                ensure_ascii=False,
            )
        )
        return EXIT_WORKBOOK
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
