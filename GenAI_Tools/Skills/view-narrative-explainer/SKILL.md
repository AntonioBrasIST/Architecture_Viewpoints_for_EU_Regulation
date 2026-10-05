---
name: view-narrative-explainer
description: Translates a formalized ArchiMate viewpoint specification (7_viewpoint.md), operational footprint (3_operational_footprint.md), and regulatory relevance report (5_regulatory_relevance.md) into a dual-purpose textual explanation guide for any target EU legislation.
---

# AI Skill Specification: view-narrative-explainer

## 1. Semantic Metadata
* **Skill Identifier:** `view-narrative-explainer`
* **Short Summary:** Generates a comprehensive, dual-purpose textual explanation (`1_view_explanation.md`) that articulates both (1) how any target EU legislation directly impacts a stakeholder's operational footprint, and (2) a complete textual guide and walkthrough to the corresponding visual ArchiMate view.
* **LLM Routing Description:**
  > "Use this skill when you need to convert an ArchiMate Viewpoint specification into a clear, dual-purpose textual explanation guide. It requires `7_viewpoint.md`, `3_operational_footprint.md`, and `5_regulatory_relevance.md`. Works for ANY legislation (DORA, NIS2, eIDAS2, GDPR, AI Act, etc.). Outputs `Views/1_view_explanation.md`."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "view-narrative-explainer",
  "description": "Generates a dual-purpose textual explanation guide for a stakeholder viewpoint under any target EU legislation.",
  "parameters": {
    "type": "object",
    "properties": {
      "viewpoint_spec": {
        "type": "string",
        "description": "Contents of 7_viewpoint.md."
      },
      "operational_footprint": {
        "type": "string",
        "description": "Contents of 3_operational_footprint.md."
      },
      "regulatory_relevance": {
        "type": "string",
        "description": "Contents of 5_regulatory_relevance.md."
      },
      "coverage_ledger": {
        "type": "string",
        "description": "Approved Footprint-Regulation Coverage Ledger from Step 5."
      },
      "regulation_overview_baseline": {
        "type": "string",
        "description": "Path to the immutable selected-technology View 0 baseline."
      },
      "view_graph": {
        "type": "string",
        "description": "Contents of the approved 7_view_graph.json."
      }
    },
    "required": ["viewpoint_spec", "operational_footprint", "regulatory_relevance", "coverage_ledger", "regulation_overview_baseline", "view_graph"]
  },
  "returns": {
    "type": "object",
    "description": "A structured markdown document containing operational impact narratives and visual view walkthroughs."
  }
}
```

## 3. Dual-Purpose Design Principles

The output document (`1_view_explanation.md`) MUST serve two explicit functions simultaneously:

### Function 1: Standalone Operational & Compliance Impact Guide
A reader (without any background in Enterprise Architecture or ArchiMate modeling) should be capable of understanding **every single way** in which the target legislation affects, restricts, or enhances their daily operations, tasks, approvals, and dependencies.

### Function 2: Complete Textual Walkthrough of the Visual ArchiMate View
If a reader looks at the visual ArchiMate view (or its XML model), this document MUST act as an exact textual representation and guide to that view, explaining why each element exists, how layers connect, and how relationships flow.

---

## 4. Operational Gap Interpretation Guidelines (`[Gap]`)

**Crucial Nuance on Stakeholder Viewpoint Gaps:**
* An operational gap or missing control identified in a stakeholder's footprint represents a gap **from that specific stakeholder's operational viewpoint and role boundary**.
* It does **NOT** automatically signify an enterprise-wide compliance violation or architectural flaw. The process or control may be executed by another organizational unit, or the stakeholder may simply lack operational visibility into it.
* The explanation MUST use careful, non-judgmental language:
  - **DO NOT state:** "The enterprise fails to comply with Article X" or "This is a compliance failure."
  - **DO state:** "From this stakeholder's operational perspective, this footprint *may indicate a potential operational gap or visibility limitation* regarding Article X compliance."

---

## 5. Required Output Structure (`1_view_explanation.md`)

### Section 1: Executive Overview & Stakeholder Operational Scope
- **View 0 — Stakeholder-Aware Regulation Map:** Reproduce the immutable legal
  core plus the approved stakeholder–organization–legal-role chain. Explain that
  the role chain establishes perspective and does not claim compliance.
- **Target Role & Seniority:** Core role context, organizational level, primary operational focus.
- **Legislative Mandates Summary:** Bulleted overview of applicable articles from target legislation and what they demand operationally.
- **Key Operational Impact Narrative:** A multi-paragraph narrative explaining daily workflows under this regulatory framework.
- **Coverage Statement:** State the named operational-context stream and confirm that every approved `OP-*`, `CON-*`, and in-scope `REQ-*` is assigned to a stream or visible external responsibility.

### Section 2: Per-View Visual Walkthroughs
Create one subsection for every view object in the approved `7_view_graph.json`, using the view's exact approved name. A thematic title may be used only when it is also the name of that formal view. This section is a literal guide to reading the corresponding diagram; it must not be replaced by a thematic operational summary, a list of identifiers, or a generic layer discussion.

For each formal view, include an explicit **How to read this view** subsection containing all of the following:

1. **Reading purpose and stakeholder route:** State the concern answered by the view and guide the reader from the stakeholder anchor through the approved connected graph to the requirement families, dependencies, external roles, or controls. Explain why that route matters to the stakeholder's work.
2. **Visible boxes and containment:** Account for every node in that view's `node_ids` exactly once. For each readable box, state its visible name, ArchiMate element type, what it represents, why source evidence requires it, and whether it is a root box or nested inside a named parent family. A compact table is permitted, but a family-level sentence does not substitute for explaining each visible child box.
3. **Visible arrows:** Account for every relationship in the view whose `visibility` is `visible` exactly once. For each arrow, state its readable source and target names, ArchiMate relationship type, source-to-target direction, evidence-backed meaning, and why it is drawn. State ownership implications where the edge is a coverage relationship; only `Directly performed` may be described as stakeholder realization.
4. **Semantic-only nesting:** Account for every `semantic-only` Composition or Aggregation relationship. Explain the parent-child containment that represents it and explicitly say that no internal arrow is drawn because the nesting carries that meaning.
5. **External boundary and ownership:** Identify each external role, system, approval, dependency, or unclear-owner requirement. Explain why it remains outside the stakeholder's direct control and how the visual relationship represents that boundary.

Use readable names in the walkthrough. Stable IDs may support cross-reference but cannot replace the explanation of a box, arrow, containment, or boundary. `7_view_graph.json` is the complete coverage authority: no node or approved relationship may be represented only by a blanket statement such as “the remaining relationships are listed below.”

The resulting view walkthrough may then include the following operational and compliance context, derived from the target legislation and operational footprint:
- *Stream A: Core Operational Execution & Access Governance*
- *Stream B: Process Integrity, Quality Gates & Approvals*
- *Stream C: Incident Handling, Monitoring & Resiliency*
- *Stream D: Third-Party, Supply Chain & Interoperability Risk*
- *Stream E: Oversight, Auditability & Release Governance*

*(Note: The above streams are generic templates. For instance, in DORA these map to SDLC/Access/Testing/Telemetry, in eIDAS2 to Trust Services/Certificates/Identity, and in NIS2 to Incident Notification/Risk Management).*

For each formal view, after its visual walkthrough:
1. **Operational Reality & Daily Workflow:** How work is conducted day-to-day.
2. **Regulatory Mandates & Constraints:** Direct statutory requirements from the target legislation.
3. **Friction Points & Potential Operational Gaps (`[Gap]`):** Highlighting bottlenecks and explicitly framing items as *potential operational or visibility gaps from this stakeholder's perspective*.
4. **Ownership Boundary:** For each Coverage Ledger entry, state whether work is directly performed, constrained by a dependency or gate, externally owned, or unclear. Do not describe non-direct entries as stakeholder realization.

### Section 3: Layer-by-Layer Architectural View Walkthrough
Detailed guide to the visual view structure across all ArchiMate layers:
- **Strategy & Motivation Layer:** Explaining Requirements (`REQ-*`), Assessments (`ASMT-*`), Constraints (`CST-*`), and Potential Gaps (`GAP-*`).
- **Business Layer:** Explaining Business Actors (`ACT-*`), Roles (`ROL-*`), Processes (`PROC-*`), Events (`EVT-*`), and Governance Objects (`OBJ-*`).
- **Application Layer:** Explaining Application Components (`COMP-*`), Services, Registries, and Artifacts (`ART-*`).
- **Technology Layer:** Explaining Infrastructure Nodes (`NODE-*`), System Software (`SYS-*`), and Execution Environments (`POD-*`).
- **Implementation Layer:** Explaining Work Packages (`WP-*`) and Deliverables (`DEL-*`).

### Section 4: Comprehensive Element, Requirement & Realization Traceability Table
An exhaustive table linking the requirement-family realization chain:
`Coverage ID` | `Operational Source ID` | `Parent Family / Context Stream` | `Requirement ID` | `Source Citation` | `Ownership State` | `Representing Element or External Role` | `Operational Meaning`

Where:
- **Coverage ID / Operational Source ID:** Exact `COV-*`, `OP-*`, or `CON-*` identifiers from the approved ledger; context-only entries have no `REQ-*`.
- **Parent Family / Context Stream:** The meaningful visible control domain or the dedicated role-specific operational-context stream.
- **Requirement ID:** Identifier for the specific statutory requirement (e.g., `REQ-Art9-PR-Gate`).
- **Statutory Requirement / Restriction:** The exact requirement or restriction imposed by the legal text.
- **Ownership State:** Exactly one approved state; only `Directly performed` supports a stakeholder realization relationship.
- **Representing Element or External Role:** The source-backed process/component, approval/dependency, known external owner, or documented unclear-owner state.

---

## 6. Execution Rules & Quality Constraints
- **Interactive Loops (Sequential HITL Validation):** Before compiling and writing `Views/1_view_explanation.md`, the AI must execute two sequential conversational gating loops using the `question` tool:
  * **Loop 8.1 (View Naming & Definition Loop):**
    - You MUST loop through each proposed View/Stream individually to get approval for its name and scope.
    - **Header:** `Confirm View Name`
    - **Question:** `"I propose to draw the following View in this viewpoint: Name: '[View Name]', Scope: [Brief Scope]. Do you agree with including this view and its name?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Loop 8.2 (Detailed Walkthrough Loop):**
    - Once the views are locked, you MUST loop through each view's detailed narrative description and diagram-reading guide individually to get approval.
    - **Header:** `Confirm View Description`
    - **Question:** `"Here is the detailed narrative description and visual reading guide I drafted for [View Name]. It identifies every visible box, nested control, visible arrow and direction, semantic-only relationship, stakeholder route, and external boundary: [Insert Description Draft]. Do you agree with this detailed view description?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Execution Rule:** Write the final `Views/1_view_explanation.md` strictly after 100% of these loops are successfully completed and approved.
- **Legislative Agnosticism:** Must seamlessly handle DORA, NIS2, eIDAS2, GDPR, AI Act, or any other EU legislation without hardcoded assumptions.
- **Zero Hallucination / Zero Assumption:** Preserve the contextualized View 0
  exactly. Use `7_view_graph.json` as the authority for nodes, relationships,
  direction, visibility, and per-view membership; never add, omit, or redirect an
  edge in prose.
- **Diagram-reading fidelity:** Each view must contain a `How to read this view`
  subsection that explicitly covers every graph node, every visible relationship,
  and every semantic-only containment relationship. For visible arrows, name the
  source and target boxes, relationship type, direction, evidence-backed meaning,
  and reason for visibility. For nested controls, name the parent and children and
  explain that nesting, rather than an internal arrow, conveys Composition or
  Aggregation. Explain the stakeholder route and every external boundary. Do not
  claim screen coordinates, left/right ordering, or other canvas facts unless an
  approved rendered view supplies them.
- **Family Consistency:** Preserve the approved requirement-family ledger identically across the walkthrough, slides, and generated model. Do not introduce a generic parent title, a flat child card, or a visible internal composition arrow.
- **Legal-text ID boundary:** Canonical legal-text IDs are formal-model documentation fields only. Do not repeat them in narrative prose, walkthrough headings, tables, or visible labels; retain readable citations instead.
- **Exhaustive Graph Coverage:** Every element and `REL-*` assigned to each view in
  `7_view_graph.json` MUST be referenced and explained, including the stakeholder
  path. The narrative may not treat common stream membership as a relationship.
- **Ledger Fidelity:** Every Coverage Ledger ID must appear once in the traceability table and in at least one stream narrative. Halt rather than omit unresolved coverage.
- **Jargon Bridge:** Plainly explain any ArchiMate terms in clear business/technical language.
