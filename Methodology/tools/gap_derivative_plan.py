#!/usr/bin/env python3
"""Plan conditional Step 12 outputs from a normalized per-unit GAP inventory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


OUTPUTS = {
    "narrative": "Views/5_gap_free_view_explanation.md",
    "slides": "Views/5_gap_free_slide_diagrams.md",
    "archimate": "Views/5_gap_free_model.archimate",
    "likec4": "Views/5_gap_free_model.c4",
    "pyarchimate": "Views/5_gap_free_model.py",
}


def plan_derivatives(inventory: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    plans: list[dict[str, Any]] = []
    outputs: list[str] = []

    artifacts = inventory.get("artifacts", [])
    if not isinstance(artifacts, list):
        return {"valid": False, "errors": ["artifacts must be an array"], "any_gaps": False}

    for artifact in artifacts:
        if not isinstance(artifact, dict):
            errors.append("every artifact must be an object")
            continue
        kind = artifact.get("kind")
        units = artifact.get("units", [])
        if kind not in OUTPUTS or not isinstance(units, list):
            errors.append(f"invalid artifact kind or units: {kind!r}")
            continue
        affected: list[str] = []
        skipped: list[str] = []
        removals: dict[str, list[str]] = {}
        for unit in units:
            if not isinstance(unit, dict) or not isinstance(unit.get("id"), str):
                errors.append(f"{kind}: every unit requires an id")
                continue
            gap_ids = unit.get("gap_ids", [])
            if not isinstance(gap_ids, list) or not all(
                isinstance(gap_id, str) and gap_id.startswith("GAP-") for gap_id in gap_ids
            ):
                errors.append(f"{kind}/{unit.get('id')}: gap_ids must contain only structural GAP-* ids")
                continue
            if gap_ids:
                affected.append(unit["id"])
                removals[unit["id"]] = gap_ids
            else:
                skipped.append(unit["id"])
        if affected:
            output = OUTPUTS[kind]
            outputs.append(output)
            if kind == "pyarchimate":
                outputs.append("Views/5_gap_free_model.archimate")
            plans.append(
                {
                    "kind": kind,
                    "source": artifact.get("path"),
                    "source_hash": artifact.get("sha256"),
                    "affected_units_only": affected,
                    "skipped_clean_units": skipped,
                    "removals": removals,
                    "output": output,
                }
            )

    any_gaps = bool(plans)
    return {
        "valid": not errors,
        "errors": errors,
        "any_gaps": any_gaps,
        "write_manifest": any_gaps,
        "manifest": "Views/5_gap_free_manifest.md" if any_gaps else None,
        "outputs": outputs,
        "plans": plans,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path)
    args = parser.parse_args(argv)
    try:
        inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
        return 1
    report = plan_derivatives(inventory)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
