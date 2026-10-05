---
name: pyarchimate-model-generator
description: Generates a reproducible pyArchimate Python script and its Archi-compatible .archimate output from approved viewpoint artifacts. Use only after the syntax-reference and ArchiMate-symbol skills have established valid API usage and semantics; do not hand-author XML or bypass thematic-view approval.
---

# AI Skill Specification: pyarchimate_model_generator

## 1. Semantic Metadata

* **Skill Identifier:** `pyarchimate_model_generator`
* **Short Summary:** Materializes an approved ArchiMate viewpoint as a self-contained Python generator and executes it to create an Archi-compatible archive.
* **LLM Routing Description:**
  > "Use this skill to create `Views/3_view_model_pyarchimate.py` and execute it to produce `Views/3_view_model_pyarchimate.archimate` from an approved viewpoint, narrative, and slide diagrams. Do NOT use it for direct XML generation, LikeC4 generation, SVG export, or before every thematic view has operator approval."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "pyarchimate_model_generator",
  "description": "Creates and executes a validated, reproducible pyArchimate generator script.",
  "parameters": {
    "type": "object",
    "properties": {
      "viewpoint_spec_path": {"type": "string", "description": "Absolute path to 7_viewpoint.md.", "required": true},
      "view_explanation_path": {"type": "string", "description": "Absolute path to Views/1_view_explanation.md.", "required": true},
      "slide_diagrams_path": {"type": "string", "description": "Absolute path to Views/2_slide_diagrams.md.", "required": true},
      "regulation_overview_baseline": {"type": "string", "description": "Absolute path to the immutable pyArchimate View 0 archive created by Step 5a.", "required": true},
      "views_directory": {"type": "string", "description": "Absolute Views directory receiving both artifacts.", "required": true},
      "approved_views": {"type": "array", "description": "Operator-approved thematic view purposes, included elements, and relationship connections.", "items": {"type": "object"}, "required": true},
      "coverage_ledger": {"type": "string", "description": "Approved Step 5 Footprint-Regulation Coverage Ledger with no unresolved items, direct legal-text IDs, and family roll-ups.", "required": true},
      "view_graph": {"type": "string", "description": "Approved 7_view_graph.json node and relationship authority.", "required": true}
    },
    "required": ["viewpoint_spec_path", "view_explanation_path", "slide_diagrams_path", "regulation_overview_baseline", "views_directory", "approved_views", "coverage_ledger", "view_graph"]
  },
  "returns": {"type": "object", "description": "Script path, model path, validation results, and execution report."}
}
```

## 3. Core Logic & Execution Flow

1. **Pre-execution verification**
   - Confirm all input files exist, pyArchimate imports, and every thematic view has explicit operator approval.
   - Read the selected immutable contextualized View 0 archive with
     `Model.read(str(path))`. Record separate fingerprints for its legal core and
     approved stakeholder–organization–legal-role chain. Reject other stakeholder
     operations, gaps, compliance status, or Article/annex/catalog nodes.
   - Use `pyarchimate-syntax-reference` before authoring code and `archimate-symbol-validator` for every concept selection.
   - Derive only source-backed elements, relationships, documentation, and thematic membership. Reject an unresolved Coverage Ledger. Retain every `COV-*` and its ownership state in documentation; use realization only for `Directly performed` entries, and model all other states as stated external/dependency context. Ask the operator about missing or ambiguous facts; never invent them.
2. **Generate the script**
   - Write `Views/3_view_model_pyarchimate.py`; resolve output with `Path(__file__).with_suffix(".archimate")`.
   - Build a `Model`, add elements with `m.add(ArchiType.<Element>, name, desc=...)`, and use clean names of at most 25 characters.
   - For each relationship, call `check_valid_relationship(rel_type, source.type, target.type, raise_flg=True)` before `m.add_relationship(...)`.
   - Derive and validate the approved requirement-family ledger before diagramming. Parent names must be concise functional control domains; child names must state a specific action and target. Reject vague standalone labels, legal boilerplate, generic foundation buckets, brackets, and titles over 25 characters. Store citations and legal-text IDs in `desc`: each legal child uses `Legal text IDs: [id; ...]`; each family parent uses `Legal text IDs (child roll-up): [id; ...]`. IDs must exactly equal the approved ledger values; generation never performs legal-text matching.
   - For each family, call `m.add_child(parent.uuid, child.uuid)` for every child and create the parent visual node with `view.add(parent, ...)`. Call `parent_node.add(child)` for each child, then `parent_node.resize(max_in_row=2 or 3)`. The actual parent must be a `Requirement`, `Constraint`, process, or component—not a `Grouping`.
   - Retain Composition/Aggregation relationships without canvas connections only
     when matching visual nesting exists. Add every other visible `REL-*` assigned
     by `7_view_graph.json`; never choose a density-safe subset.
   - Use measured non-overlapping root placement. Relationship count is unlimited.
     More than 30 roots requires recorded operator readability approval, not a
     split or omission. Every view contains the stakeholder and one weak component.
   - Use `apply_layout()` only after a runtime smoke test demonstrates the requested behavior. Do not call it or claim hierarchical layout as a substitute for `Model.add_child`, `parent_node.add`, and `parent_node.resize`.
   - Reproduce the approved baseline's legal core and stakeholder/legal-role chain
     before adding thematic views. Do not write to the baseline script or archive.
   - Do not set child coordinates, child dimensions, bendpoints, or manual routing, and do not emit SVG output.
   - Reject output if any Coverage Ledger entry lacks a thematic view, a legal Requirement/Constraint lacks its approved direct or roll-up IDs, a non-direct state is falsely realized, or `m.check_invalid_relationships()`, `m.check_invalid_nodes()`, or `m.check_invalid_conn()` returns values. Otherwise call `m.write(str(output_path))`.
3. **Execute and verify**
   - Compile and execute the script. Verify both script and archive exist.
   - Round-trip the archive with `Model(...).read(str(output_path))`; project every
     view back to `7_view_graph.json` and run
     `Methodology/tools/view_graph_validator.py --projection` to verify exact nodes/relationships, degree at
     least one, one weak component, stakeholder presence, baseline fingerprints,
     containment, no overlap, and native integrity. A root count above 30 requires
     approval evidence; there is no link threshold.

## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True. Do not save or run the script until every thematic view's purpose, membership, and relationship connections are approved through the question loop.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | :--- | :--- | :--- |
| Input artifact missing | Abort before writing | `Error: Missing required viewpoint artifact. Ask the operator for the path or complete the preceding step.` |
  | Baseline missing or unreadable | Abort before writing | `Error: Immutable regulation overview baseline is missing or unreadable.` |
  | Final View 0 differs from baseline | Abort delivery | `Error: Final View 0 is not semantically equivalent to the approved baseline.` |
  | Thematic view unapproved | Abort before writing | `Error: View approval is incomplete. Present the remaining view membership and relationships to the operator.` |
  | Illegal relationship | Abort relationship creation | `Error: Invalid ArchiMate relationship. Correct the source, target, or relationship type.` |
  | Family containment or packing failure | Do not write model | `Error: Requirement-family containment or root-box packing failed. Correct the family ledger or view membership.` |
  | Validation failure | Do not write model | `Error: Model integrity validation failed. Correct the reported relationships, nodes, or connections.` |
  | Script or archive failure | Preserve 10a/10b outputs | `Error: pyArchimate generation failed. Report the traceback and do not overwrite alternative model artifacts.` |

* **Loop Prevention Rule:** If the same generation or validation error occurs twice in one turn, stop and request operator clarification.
