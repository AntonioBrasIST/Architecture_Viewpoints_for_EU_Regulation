---
name: regulation-overview-designer
description: Designs and validates an immutable stakeholder-contextualized View 0 baseline whose legal core comes from the complete current binding text. Use after legal-role placement and technology selection; do not assess compliance or map operational work beyond the approved role chain.
---

# AI Skill Specification: regulation_overview_designer

## 1. Semantic Metadata

* **Skill Identifier:** `regulation_overview_designer`
* **Short Summary:** Turns a regulation's complete binding text into an approved, source-complete legal awareness map for all affected staff.
* **LLM Routing Description:**
  > "Use this skill after legal-role placement and technology selection. Build the regulation-wide legal core from current binding text, then add only the approved stakeholder–organization–legal-role chain. Do NOT assess compliance, create gaps, or map other operational systems."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "regulation_overview_designer",
  "description": "Designs a technology-neutral legal View 0 contract that a selected native generator materializes as an immutable baseline.",
  "parameters": {
    "type": "object",
    "properties": {
      "target_regulation": {"type": "string", "description": "Law name and authoritative CELEX or ELI identifier.", "required": true},
      "technology": {"type": "string", "enum": ["archimate-xml", "likec4", "pyarchimate"], "description": "Technology selected before this step.", "required": true},
      "views_directory": {"type": "string", "description": "Stakeholder Views directory that contains the Regulations subdirectory.", "required": true},
      "legal_source": {"type": "object", "description": "Current consolidated binding text, its source identifier, retrieval date, and in-force status.", "required": true},
      "legal_index_workbook": {"type": "string", "description": "Matching `<REGULATION>-CELEX:<CELEX>.xlsx` whose Enacting Terms canonical paths are used as verified legal-text IDs.", "required": true}
    },
    "required": ["target_regulation", "technology", "views_directory", "legal_source", "legal_index_workbook"]
  },
  "returns": {
    "type": "object",
    "description": "Approved source inventory plus a visible requirement-family ledger, role-family links, source documentation, View 0 membership, and selected immutable baseline path."
  }
}
```

## 3. Core Logic & Execution Flow

1. **Verify the legal corpus.** Fetch the current consolidated binding text from the authoritative legal source one binding Article at a time, then each binding annex. Record law name, CELEX/ELI, retrieval date, source URL or identifier, and in-force status. Exclude recitals. Do not expand cited external laws, standards, technical standards, or guidance; record them only in documentation.
2. **Verify source completeness without modeling a source catalog.** Record every Article and annex in source documentation and map each visible child requirement to its binding source. Abort if any binding source is unavailable, but do not create Article, annex, legal-title, or hidden catalog-only nodes.
3. **Derive the awareness map with `regulatory-view-structure`.** Create only meaningful legal-control family parents and their target-qualified child requirements. The parent represents a coherent domain; each child is a specific high-level legal duty. Invoke `legal-text-anchor-resolver`: every child Requirement/Constraint receives its exact verified direct Enacting Terms IDs and each parent receives the ordered, deduplicated roll-up of its children. Preserve citations and IDs in documentation, not in a second diagram or off-canvas catalog.
4. **Relate only visible legal content.** Semantically compose every child under its family parent and visually nest it. Link role-family nodes to family parents with legally supported wording such as `must implement`, `must report to`, `must oversee`, or `is contracted by`. Do not render parent-child composition lines; containment communicates that relationship.
5. **Contextualize without changing the legal core.** Add the approved stakeholder
   role, organization actor, legal-role group, and `REL-ROLE-*` chain from Gate
   5.6. Do not add stakeholder processes, applications, technology, implementation
   status, Gap elements, assessments, realization status, or compliance claims.
   Preserve the legal-family fingerprint separately from the role-chain fingerprint.
6. **Enforce one connected Overview.** Invoke `connected-view-validator`. Project
   the proposed Overview into the `7_view_graph.json` schema and run
   `Methodology/tools/view_graph_validator.py` against that temporary projection
   before the map gate and again after approval. Every
   element participates in an approved relationship, nesting-backed Composition/
   Aggregation counts, the stakeholder is present, and the Overview has one weakly
   connected component. There is no relationship-count limit. More than 30 roots
   is a readability warning and approval trigger; persistence remains blocked
   until that approval is recorded. It is never a suppression rule.
7. **Apply approval gates before persistence.**
   - `Confirm Legal Source Completeness`: the complete Article/annex inventory, legal-source metadata, and no missing binding text.
   - `Confirm Obligation Domain`: each source-backed child requirement, role-family link, and documentation.
   - `Confirm Requirement Family`: each parent title, child decomposition, visual nesting, visible external link, every child's direct legal-text IDs, and each parent's ordered child roll-up.
   - `Confirm Overview Map`: all grouped View 0 members, relationship labels, and canvas structure.
8. **Materialize the immutable baseline.** Use the selected technology only after all gates pass. Save directly in `Views/` as `0_<law-slug>_regulation_overview.archimate`, `0_<law-slug>_regulation_overview.c4`, or—when pyArchimate is selected—`0_<law-slug>_regulation_overview.py` plus its sibling archive. Preserve the legal core and approved stakeholder/legal-role chain unchanged; downstream work reproduces both.

## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True. All four approval gates must pass before a baseline is written or a pyArchimate script is executed.
* **Canonical legal-anchor rule:** Resolve only Enacting Terms through the matching workbook. Recitals, amendment provisions, ambiguous paths, and citation-only guesses are invalid. No legal Requirement/Constraint may be materialized without its approved direct IDs or child roll-up.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | :--- | :--- | :--- |
  | Current consolidated text unavailable | Abort | `Error: Current consolidated binding text is unavailable. Do not create an overview baseline.` |
  | Binding Article or annex missing | Abort | `Error: Binding legal source is incomplete. Retrieve or obtain the missing Article or annex before modeling.` |
  | Article, annex, recital, external-law duty, or generic legal heading proposed as a node | Reject it | `Error: View 0 must contain only visible requirement families and role links. Keep source detail in documentation.` |
  | Operational detail beyond the approved role chain proposed | Reject it | `Error: View 0 permits only the immutable legal core and approved stakeholder/legal-role context.` |
  | Unapproved source, domain, or map | Do not persist | `Error: Overview approval is incomplete. Complete the four required review gates.` |
  | Baseline path already exists | Preserve it | `Error: Immutable baseline already exists. Start a new explicit approval cycle rather than modifying it.` |
  | Nested view-output path proposed | Redirect output | `Error: Write View 0 directly to Views/ using the law-prefixed baseline filename; do not create a Regulations subdirectory.` |

* **Loop Prevention Rule:** If the same legal-source completeness error occurs twice in one run, stop and request the missing authoritative source from the operator.
