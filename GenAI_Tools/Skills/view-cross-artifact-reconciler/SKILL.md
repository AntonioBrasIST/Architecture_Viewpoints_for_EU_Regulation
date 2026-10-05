---
name: view-cross-artifact-reconciler
description: Validates and reconciles an immutable regulation overview baseline, generated View artifacts, and an ArchiMate XML, LikeC4, or pyArchimate-generated final model against their viewpoint specification and each other.
---

# AI Skill Specification: view-cross-artifact-reconciler

## 1. Semantic Metadata
* **Skill Identifier:** `view-cross-artifact-reconciler`
* **Short Summary:** Performs a rigorous 5-way cross-audit across the immutable regulation overview baseline, `7_viewpoint.md`, `Views/1_view_explanation.md`, `Views/2_slide_diagrams.md`, and one operator-selected final model. Identifies discrepancies, presents a Discrepancy Audit & Recommendation Report to the human operator, and applies fixes strictly after explicit operator selection.
* **LLM Routing Description:**
  > "Use this skill when you need to audit a selected immutable regulation overview baseline, generated view artifacts, and the matching final model. Requires the baseline, `7_viewpoint.md`, `Views/1_view_explanation.md`, `Views/2_slide_diagrams.md`, and exactly one selected final model. Outputs a Discrepancy Audit Report for operator validation."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "view-cross-artifact-reconciler",
  "description": "Performs a 4-way cross-audit across viewpoint artifacts and compiles an operator discrepancy report.",
  "parameters": {
    "type": "object",
    "properties": {
      "regulation_overview_baseline": {
        "type": "string",
        "description": "Path and contents of the selected immutable baseline at Views/0_<law-slug>_regulation_overview.*."
      },
      "viewpoint_spec": {
        "type": "string",
        "description": "Contents of 7_viewpoint.md."
      },
      "view_graph": {
        "type": "string",
        "description": "Contents of approved 7_view_graph.json."
      },
      "view_explanation": {
        "type": "string",
        "description": "Contents of Views/1_view_explanation.md."
      },
      "slide_diagrams": {
        "type": "string",
        "description": "Contents of Views/2_slide_diagrams.md."
      },
      "model_file": {
        "type": "string",
        "description": "Path and contents of exactly one selected model: Views/3_view_model.archimate, Views/3_view_model.c4, or Views/3_view_model_pyarchimate.archimate."
      },
      "coverage_ledger": {
        "type": "string",
        "description": "Approved Step 5 Footprint-Regulation Coverage Ledger, including direct legal-text IDs and family roll-ups."
      },
      "legal_index_workbook": {
        "type": "string",
        "description": "Matching `<REGULATION>-CELEX:<CELEX>.xlsx` used to resolve and validate every canonical legal-text ID."
      }
    },
    "required": ["regulation_overview_baseline", "viewpoint_spec", "view_graph", "view_explanation", "slide_diagrams", "model_file", "coverage_ledger", "legal_index_workbook"]
  },
  "returns": {
    "type": "object",
    "description": "A structured Discrepancy Audit & Recommendation Report requiring operator decision."
  }
}
```

## 3. 5-Way Cross-Audit Protocol

The reconciliation process MUST evaluate five distinct dimensions:

### Audit Dimension 0: Immutable Contextualized Regulation Overview Baseline
- Read the selected baseline in its native format and derive a requirement-family fingerprint: meaningful parent title/type, child title/order, child citations, direct legal-text IDs, parent roll-ups, semantic compositions, external visible links, and visual containment.
- Resolve every recorded ID through `tools/traceability_lookup.py verify-anchor` against the supplied workbook. Reject a recital, amendment, missing ID, ambiguous ID, or a model/ledger mismatch. A child must have exactly its approved direct ordered IDs; a parent must have exactly the ordered, deduplicated union of its child IDs.
- Verify binding-text completeness and reject Article, annex, legal-heading,
  generic foundation, hidden catalog-only, gap, compliance-status, or stakeholder
  operational nodes. Allow only the approved stakeholder–organization–legal-role
  chain in addition to the legal core.
- Verify final-model View 0 matches separate legal-core and role-chain fingerprints
  and that the baseline remains unchanged.

### Audit Dimension 1: Ground-Truth Coverage (`7_viewpoint.md` vs. All Outputs)
- **Elements Check:** Verify that 100% of elements declared in `7_viewpoint.md` (Part A Catalog) exist in `1_view_explanation.md`, `2_slide_diagrams.md`, and the selected model file.
- **Granular Requirements Check (MANDATORY):** Verify that 100% of the granular statutory requirements (`REQ-*`) and restrictions extracted in Step 5 (`5_regulatory_relevance.md`) and scoped in `7_viewpoint.md` are accounted for in the narrative traceability table (`1_view_explanation.md`), represented in the slide diagrams (`2_slide_diagrams.md`), and mapped as requirement nodes in the model file.
- **Bidirectional Footprint Coverage Check (MANDATORY):** Verify every approved `OP-*` and `CON-*` is represented by a named family/context stream or visible external dependency in every artifact, and every in-scope `REQ-*` has a recorded operational-chain edge. Reject missing, duplicated, mismatched, or unresolved ledger entries.
- **Ownership Check (MANDATORY):** Verify ownership state and `COV-*` ID match across all artifacts. Reject stakeholder realization for `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner` entries.
- **Graph Authority Check:** Validate `7_view_graph.json`, then verify every artifact
  has exactly its assigned nodes and `REL-*` edges. Reject missing/extra/redirected
  relationships, evidence drift, isolated semantic elements, multiple weak
  components, or a missing stakeholder anchor. Semantic-only Composition/
  Aggregation requires matching nesting.
- **Legal Text ID Check (MANDATORY):** Verify every legal Requirement/Constraint in the selected model holds exactly the approved direct IDs or parent roll-up in native documentation (`<documentation>`, LikeC4 `description`, or pyArchimate `desc`). Legal IDs must not appear in element titles, visible labels, narrative prose, or slide diagrams.

### Audit Dimension 2: Target Model Integrity (Selected Model Validation)
- **Title Length & Purity Check (MANDATORY):**
  - **Length Threshold ($\le 25$ chars):** Flag any element title/name exceeding 25 characters in length.
  - **Notation Brackets Check:** Flag any element name containing square bracket symbol annotations (e.g. `[Folded Page]`, `[Right Arrow]`, `[UML Box]`, `[3D Cube]`, `[badge]`, `[Pill]`, `[Doc box]`, `[Flag]`).
  - **Tag-Only Gap Representation Check:** Flag any element title containing `[Gap]` or descriptive sentences (e.g. `- potential visibility limit...`). Gaps must be identified by `#gap` tags or `archimate:Gap` kinds, with explanations stored in descriptions or documentation tags.
  - **For direct ArchiMate XML (`3_view_model.archimate`):**
  - **XML Syntax:** Well-formed XML, correct tags, no unescaped special characters (`&amp;`).
  - **Folder Taxonomy:** Presence of standard 9 root folders in correct order.
  - **Canvas Mapping:** Every `DiagramObject` MUST reference a valid `archimateElement` ID.
  - **Connection Mapping:** Every `sourceConnection` MUST reference a valid `archimateRelationship` ID, and its `source` / `target` attributes MUST point to canvas `DiagramObject` IDs.
  - **Target Connections:** Target `DiagramObject`s MUST list active incoming connection IDs in `targetConnections`.
  - **Family Containment:** Every visible child requirement is nested under its meaningful parent `DiagramObject`, has a corresponding Composition relationship in the model, and has no `sourceConnection` for that containment relationship. Verify non-overlapping root bounds. Relationship count is unlimited; more than 30 roots is an advisory readability finding requiring approval evidence.
- **For pyArchimate Archive (`3_view_model_pyarchimate.archimate`):**
  - **Archive Readability:** Open with `Model(...).read(str(path))`; this output may be an Archi ZIP archive containing `model.xml`, not plain XML.
  - **Model Integrity:** Require zero results from `check_invalid_relationships()`, `check_invalid_nodes()`, and `check_invalid_conn()` after read.
  - **Coverage and Views:** Apply the same title, relationship, and thematic-view checks as direct ArchiMate XML.
  - **Dual Hierarchy:** Verify each child in `Model.get_children(parent)` also appears under the parent visual node via `parent_node.nodes`; reject a visible Composition connection between that pair. Verify root bounds do not overlap.
- **For LikeC4 DSL (`3_view_model.c4`):**
  - **DSL Syntax:** Valid LikeC4 grammar, top-level `specification`, `model`, and `views` blocks.
  - **Identifier Rules:** Valid identifiers without forbidden dots (dots reserved for FQNs).
  - **Scoping & FQN Integrity:** All cross-file or cross-scope element and relationship references use unique, valid FQNs.
  - **Relationship Matchers & Views:** Correct relationship kinds/titles and valid view inclusion predicates (`*`, `_`, `**`).
  - **Nested Scope:** Verify nested family/child model scopes and scoped views render each parent with its direct children; parent-child composition arrows must not be part of the visible relation set.

### Audit Dimension 3: Narrative & Visual Cross-Consistency
- **Terminological Alignment:** Family and child titles, types, citations, and external relationship labels MUST match identically across the requirement-family ledger, text, slides, and model file. Canonical legal-text IDs are documentation-only: compare them between the ledger, baseline, and final model, but reject them in titles, visible labels, narrative prose, or slides. Flag vague standalone child labels or generic parents.
- **Structural Grouping Alignment:** Each family’s parent, child order, semantic containment, and visible external relationships in `1_view_explanation.md` MUST match `2_slide_diagrams.md` and the model view (`ArchimateDiagramModel` in `.archimate` or `view` in `.c4`).
- **Coverage Alignment:** Each thematic view must declare its Coverage Ledger membership; context-only work must remain represented without a fabricated requirement.
- **Connectivity Alignment:** Every narrative view section, slide, and native model
  view must preserve the manifest stakeholder path and one-component graph. A
  layout-oriented omission is a discrepancy, not an allowed density optimization.

### Audit Dimension 4: Operational Gap Interpretation (`[Gap]`)
- **Non-Judgmental Framing:** Verify that operational gaps (`[Gap]`) in text and slides are framed as *potential operational or visibility limits from this stakeholder's viewpoint*, rather than definitive enterprise compliance violations.

---

## 4. Required Discrepancy Audit Report Format

If any conflict, omission, or inconsistency is detected, the agent MUST output the report in this format and pause execution:

```markdown
# View Artifact Cross-Audit & Reconciliation Report

## Audit Status: [DISCREPANCIES FOUND / 100% ALIGNED]

### Summary of Audit Findings
* **Elements Checked:** [X / Total] matched across all 5 artifacts.
* **Relationships Checked:** [Y / Total] matched across all 5 artifacts.
* **Identified Discrepancies:** [N] items require operator decision.

---

### Discrepancy 1: [Short Title]
* **Conflict Location:** [e.g., `Views/1_view_explanation.md` vs. `Views/2_slide_diagrams.md`]
* **Discrepancy Details:** [Detailed description of the conflict, e.g., "Element `COMP-REG` is documented in Text and XML, but omitted from Slide 3."]
* **Proposed Resolution Options:**
  - **Option A (Recommended):** [Action, e.g., "Add `COMP-REG` to Slide 3 in `2_slide_diagrams.md`."]
  - **Option B:** [Alternative action, e.g., "Update text and XML to mark `COMP-REG` as secondary."]
  - **Option C (Manual Operator Directive):** Provide custom instruction.

---

### Operator Action Required
Please select your preferred option for each discrepancy above (e.g., "Option A for Discrepancy 1"). No files will be modified until you provide explicit authorization.
```

---

## 5. Execution Rules & Safety Protocols

- **Interactive Gating Check:** After compiling the Discrepancy Audit, you MUST use the `question` tool to present the reconciliation choices directly to the operator to force an explicit selection before executing any synchronization updates:
  * **Header:** `Confirm Reconciliation`
  * **Question:** `"I have completed the 5-way cross-audit and identified [N] alignment conflicts. Below is the summarized Discrepancy Audit & Recommendation Report: [Report]. Please select your reconciliation action:"`
  * **Options:** `Apply Recommended Fixes (Recommended)`, `Abort and Keep Files` (with custom feedback support)
- **Zero Autonomous Averaging:** The agent MUST NOT autonomously attempt to "average out" discrepancies or modify files without explicit operator choice.
- **Operator Authority:** The human operator's decision is final and overrides any default recommendation.
- **Selective Persistence:** Upon receiving the operator's choice, apply edits strictly to the specified target files and re-verify alignment.
