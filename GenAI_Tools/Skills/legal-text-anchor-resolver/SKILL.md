---
name: legal-text-anchor-resolver
description: Maps approved binding legal duties to verified canonical paths in a law-specific `<REGULATION>-CELEX:<CELEX>.xlsx` index. Use after legal duties are identified and before a Coverage Ledger, View 0 baseline, viewpoint, or model is approved; never use recitals, amendments, or ordinary citations as substitute anchors.
---

# AI Skill Specification: `legal_text_anchor_resolver`

## 1. Semantic Metadata

* **Skill Identifier:** `legal_text_anchor_resolver`
* **Short Summary:** Resolves each in-scope binding duty to one or more exact, canonical enacting-term IDs and carries those IDs into requirement documentation.
* **LLM Routing Description:**
  > "Use this skill after a legal duty is approved as relevant or is selected for the law-wide View 0 baseline. Do NOT use it to decide legal relevance, create diagrams, map recitals, map amendment provisions, or replace an exact canonical ID with an Article citation."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "legal_text_anchor_resolver",
  "description": "Creates a verified legal-text anchor ledger for approved duties.",
  "parameters": {
    "type": "object",
    "properties": {
      "law_identity": {"type": "string", "description": "Law name plus CELEX or ELI identity.", "required": true},
      "legal_index_workbook": {"type": "string", "description": "Verified, law-specific `<REGULATION>-CELEX:<CELEX>.xlsx` path, for example `DORA-CELEX:32022R2554.xlsx`.", "required": true},
      "duty_records": {"type": "array", "description": "Approved REQ-* or View 0 atomic duty records with their binding source text and citation.", "items": {"type": "object"}, "required": true},
      "family_membership": {"type": "array", "description": "Approved parent-to-child requirement-family membership used only to calculate parent roll-ups.", "items": {"type": "object"}, "required": false},
      "usage": {"type": "string", "enum": ["stakeholder-relevance", "regulation-overview"], "description": "The pipeline context creating the anchors.", "required": true}
    },
    "required": ["law_identity", "legal_index_workbook", "duty_records", "usage"]
  },
  "returns": {
    "type": "object",
    "description": "A verified direct-anchor ledger plus ordered, deduplicated parent roll-ups and documentation blocks."
  }
}
```

Each atomic duty record returns this durable form:

```json
{
  "requirement_id": "REQ-* or View0 child ID",
  "direct_legal_text_ids": ["Chap.X, Art.Y, Paragraph Z"],
  "documentation": "Legal text IDs:\n- Chap.X, Art.Y, Paragraph Z"
}
```

Each requirement-family parent returns an ordered, deduplicated union of its children's direct IDs:

```json
{
  "parent_id": "family ID",
  "child_rollup_legal_text_ids": ["Chap.X, Art.Y", "Chap.X, Art.Z"],
  "documentation": "Legal text IDs (child roll-up):\n- Chap.X, Art.Y\n- Chap.X, Art.Z"
}
```

## 3. Core Logic & Execution Flow

1. **Verify the legal index.** Confirm the supplied workbook is named exactly `<REGULATION>-CELEX:<CELEX>.xlsx` (for example `DORA-CELEX:32022R2554.xlsx`), its law label and CELEX match `law_identity`, it uses the `Recitals` and `Enacting Terms` schema expected by `tools/traceability_lookup.py`, and it is available read-only. The displayed canonical path is the legal-text ID for this pipeline only when `verify-anchor` accepts it.

2. **Resolve direct anchors.** For every approved atomic duty, locate the exact binding enacting-term text in the law-specific index. Match against the binding duty itself, never merely the Article citation or an LLM paraphrase. Verify every selected canonical path using:

   ```bash
   python3 tools/traceability_lookup.py verify-anchor --file <REGULATION>-CELEX:<CELEX>.xlsx --id "<canonical path>"
   ```

   Record one or more verified paths in the order the legal text imposes them. A duty with multiple independently binding clauses retains every direct ID.

3. **Reject excluded sources.** Do not accept a `Recital` ID, a path rejected as `AMENDMENT_FORBIDDEN`, an ambiguous path, an absent path, or a path whose indexed text does not force the approved duty. Amendment provisions are excluded from this use case even when the broader Article is otherwise available in the workbook.

4. **Build family roll-ups.** For an approved parent requirement family, concatenate children in their approved nesting order and retain the first occurrence of each direct ID. Parents receive only the labeled child roll-up; they do not invent a direct legal source.

5. **Preserve structured provenance.** Add direct IDs to the Step 5 requirement record and Coverage Ledger, and add direct/roll-up IDs to View 0 and stakeholder requirement-family ledgers. IDs belong in documentation/descriptions only, never in requirement titles, element labels, visible source nodes, slides, or relationship labels.

6. **Obtain approval before persistence.** In stakeholder relevance use `Confirm Legal Text IDs` after consensus and before Coverage Ledger approval. In regulation overview include each child direct-ID set and parent roll-up in its existing `Confirm Requirement Family` review.

## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True. An anchor ledger is legal-source evidence and requires the owning step's explicit approval before persistence.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | --- | --- | --- |
  | Workbook missing, unreadable, misnamed, or wrong schema | Stop | `Error: A verified <REGULATION>-CELEX:<CELEX>.xlsx legal index is required before legal-text IDs can be recorded.` |
  | Duty cannot be matched to exact indexed text | Stop | `Error: Requirement has no exact enacting-term anchor. Do not infer an ID from its citation.` |
  | Recital candidate | Reject it | `Error: Recitals are excluded from legal-text anchoring.` |
  | Amendment candidate | Reject it | `Error: Amendment provisions are excluded from legal-text anchoring.` |
  | Missing or ambiguous canonical path | Stop | `Error: Canonical legal-text ID is not uniquely verifiable. Correct the source mapping.` |
  | Atomic legal Requirement/Constraint has no direct ID | Reject downstream persistence | `Error: Legal requirement lacks approved direct legal-text IDs.` |
  | Parent roll-up differs from ordered child union | Reject downstream persistence | `Error: Parent legal-text roll-up does not match its child requirements.` |

* **Loop Prevention Rule:** If the same duty fails exact matching twice, stop and ask the operator to correct the binding-duty decomposition or legal-index source; never substitute a citation or nearby clause.
