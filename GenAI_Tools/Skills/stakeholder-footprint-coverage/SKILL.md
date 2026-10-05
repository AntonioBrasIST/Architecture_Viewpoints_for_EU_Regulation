---
name: stakeholder-footprint-coverage
description: Builds an evidence-backed, bidirectional coverage ledger between a stakeholder's complete operational footprint and legal requirements that affect it. Use after regulatory consensus and before viewpoint scoping; do not use it to determine binding law, invent operational facts, or draw diagrams.
---

# AI Skill Specification: stakeholder_footprint_coverage

## 1. Semantic Metadata

* **Skill Identifier:** `stakeholder_footprint_coverage`
* **Short Summary:** Proves that every stated operational fact is represented and that every footprint-affecting legal requirement has an evidence-backed operational chain.
* **LLM Routing Description:**
  > "Use this skill after Step 5 article consensus when an operational footprint, stakeholder classification, and legal relevance analysis are available. Do NOT use it to broaden scope from entity-wide applicability alone, choose ArchiMate notation, or assess enterprise compliance."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "stakeholder_footprint_coverage",
  "description": "Creates the approved Footprint-Regulation Coverage Ledger used by Steps 5 through 11.",
  "parameters": {
    "type": "object",
    "properties": {
      "operational_footprint_file": {"type": "string", "description": "Approved Step 3 report with OP-* source IDs."},
      "stakeholder_classification_file": {"type": "string", "description": "Approved Step 4 classification and concern report."},
      "regulatory_relevance_draft": {"type": "string", "description": "Consensus draft containing REQ-* requirements, citations, and approved direct legal-text IDs."}
    },
    "required": ["operational_footprint_file", "stakeholder_classification_file", "regulatory_relevance_draft"]
  },
  "returns": {"type": "object", "description": "An endpoint-specific Coverage Ledger, Regulatory Relationship Ledger, uncovered register, and proposed thematic-stream membership."}
}
```

## 3. Core Logic & Execution Flow

1. **Create operational-source records.** Preserve each approved `OP-*` item from Step 3 and each distinct `CON-*` concern from Step 4. Valid source categories are task, asset/data, dependency, approval, incident interface, concern, and explicit operational gap. Never merge distinct concerns.
2. **Apply the recorded-operational-chain test.** A `REQ-*` is relevant when binding text has a defensible connection to a recorded source item through a task, asset, dependency, approval, incident interface, or concern. Entity-wide applicability by itself is insufficient. Include externally owned duties that pass this test.
3. **Record every evidence-backed edge.** Each edge must state source ID, `REQ-*`, citation, approved direct legal-text IDs unchanged, concise factual basis, effect type, proposed named stream/family, and exactly one ownership state: `Directly performed`, `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner`.
4. **Preserve non-regulatory work.** A source item with no legal edge must be assigned to a role-specific operational-context stream. This is coverage, not an invented legal obligation.
5. **Resolve graph endpoints.** Every coverage row intended for a view must name
   the exact operational element and legal requirement/family endpoints. A broad
   source group, stream assignment, or statement that a duty “affects the work” is
   incomplete until it has an approved `REL-COV-*` representation edge.
6. **Preserve ownership semantics.** Directly performed coverage may use
   Realization when valid. Constrained, externally owned, and unclear-owner
   coverage must use the approved effect, role, approval, or dependency edge and
   never a stakeholder Realization. Invoke `evidence-grounded-relationship-ledger`
   and validate endpoint types and direction.
5. **Build the uncovered register.** List every operational source without a stream/context assignment and every in-scope `REQ-*` without an evidence-backed source edge. Do not infer missing owners, controls, or links.

## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True. Before Step 5 is persisted,
  present textual endpoint names, effect meanings, every `REL-COV-*`, the Coverage
  Ledger, and uncovered register using `Confirm Coverage Resolution`. Do not
  continue while an item lacks an endpoint-specific relationship or remains
  uncovered.
* **Legal-anchor preservation rule:** A legal `REQ-*` without approved direct legal-text IDs is invalid. Do not rematch, reorder, add, or remove IDs here; return it to legal-text-anchor resolution.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | --- | --- | --- |
  | Missing stable source IDs | Halt ledger creation | `Error: Step 3 or Step 4 lacks stable source IDs. Return to the approved extraction output.` |
  | Legal duty lacks a recorded chain | Keep outside stakeholder scope | `Error: No recorded operational chain supports this requirement. Do not include it as stakeholder-relevant.` |
  | Source or in-scope requirement is uncovered | Halt before persistence | `Error: Coverage is incomplete. Present the uncovered register for operator resolution.` |
  | Owner is not stated | Use unclear-owner state only | `Error: Ownership is not evidenced. Do not assign a role; record Not evidenced / unclear owner.` |

* **Loop Prevention Rule:** If the same coverage item remains unresolved after two operator review rounds, stop and request a specific source clarification rather than creating a new inference.

## 5. Required Output Format

```markdown
### Footprint-Regulation Coverage Ledger

| Coverage ID | Operational Source | Source Type | REQ-* / Citation / Legal text IDs | Evidence-backed Effect | Ownership State | Known Owner | Proposed Stream / Family |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Operational Context Coverage

| Coverage ID | Operational Source | Named Context Stream | Evidence |
| --- | --- | --- | --- |

### Uncovered Register

| Item ID | Item Type | Why Uncovered | Operator Resolution Required |
| --- | --- | --- | --- |
```
