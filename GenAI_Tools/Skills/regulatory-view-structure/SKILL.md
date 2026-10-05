---
name: regulatory-view-structure
description: Defines the requirement-family naming, decomposition, containment, and visual-link contract for regulation-overview and stakeholder views. Use after legal or stakeholder requirements are known and before creating narratives, slides, XML, LikeC4, or pyArchimate diagrams; do not use it to determine legal relevance or operational scope.
---

# AI Skill Specification: regulatory_view_structure

## 1. Semantic Metadata

* **Skill Identifier:** `regulatory_view_structure`
* **Short Summary:** Converts approved requirements into clear, nested requirement families that remain semantically traceable while avoiding dense relationship cobwebs.
* **LLM Routing Description:**
  > "Use this skill when a regulation overview or stakeholder view needs a readable visual structure. Do NOT use this skill to decide whether an Article applies, invent duties, or replace the underlying legal and operational analysis."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "regulatory_view_structure",
  "description": "Produces an approved requirement-family ledger and rendering rules for legal and stakeholder views.",
  "parameters": {
    "type": "object",
    "properties": {
      "requirements": {
        "type": "array",
        "description": "Source-backed legal or stakeholder requirements, including citations, approved direct legal-text IDs, and any operational realization links."
      },
      "view_purpose": {
        "type": "string",
        "enum": ["regulation-overview", "stakeholder-view"],
        "description": "Whether the ledger is a contextualized View 0 legal core or a stakeholder-specific thematic view."
      },
      "technology": {
        "type": "string",
        "enum": ["archimate-xml", "likec4", "pyarchimate", "markdown"],
        "description": "Target rendering technology."
      },
      "external_relationships": {
        "type": "array",
        "description": "Approved role-to-family, cross-family, or operational realization relationships eligible for visible rendering."
      },
      "coverage_ledger": {
        "type": "object",
        "description": "Approved OP-*/CON-* to REQ-* coverage edges, ownership states, context-stream assignments, and no unresolved items."
      }
    },
    "required": ["requirements", "view_purpose", "technology", "external_relationships", "coverage_ledger"]
  },
  "returns": {
    "type": "object",
    "description": "A requirement-family ledger containing parents, nested children, direct legal-text IDs, ordered child roll-ups, semantic composition, visible external links, and view membership."
  }
}
```

## 3. Core Logic & Execution Flow

1. **Establish source-backed families.** Group only requirements that address one coherent control domain or stakeholder stream. Every family parent is a meaningful ArchiMate concept (`Requirement`, `Constraint`, process, or component), never a decorative `Grouping`.
2. **Name the parent and children.**
   - A parent names a concise functional domain, for example `ICT Risk Controls`.
   - A child names a specific action and its target, for example `ICT Asset Identification` or `Incident Report Standards`.
   - Names are clean, understandable without an Article number, at most 25 characters, and contain no brackets, status tags, or boilerplate.
   - Reject vague standalone titles such as `Identification`, `Detection`, `Protection`, `Communication`, and `Simplified Framework`; use a target-qualified title instead.
   - Reject generic buckets such as `DORA Foundations` and legal-formula titles such as `Art 1 Subject comprises`.
   - If a source-backed requirement cannot receive a clear parent or child name, halt and ask the operator for naming direction.
3. **Build the family ledger.** For each family record: parent title/type/purpose, each child title/type/source citation/direct legal-text IDs, semantic `Composition` or `Aggregation` link, visual containment order, eligible visible external relationships, and the exact Coverage Ledger IDs it satisfies. A parent stores the ordered, deduplicated roll-up of its children's IDs. Store citations, legal-text IDs, and ownership state in documentation or descriptions on visible nodes; do not create Article, annex, or hidden catalog-only nodes for View 0. IDs never appear in titles, visible labels, or slides. Every relationship also receives an approved `REL-*` record with exact endpoints, direction, meaning, and evidence; coverage or common family membership is not an edge.
4. **Respect ownership semantics.** A `Directly performed` edge may use realization. `Stakeholder-constrained` and `Externally owned` edges must show the evidence-backed approval, dependency, or external role instead; `Not evidenced / unclear owner` must not invent a responsible role. Never render an external obligation as stakeholder realization.
5. **Apply visual containment.** Render each child inside its parent. Retain semantic composition in the model, but omit its visual line because containment already communicates it. Show only unique role-to-family, cross-family, and allowed direct-realization links.
6. **Control readability without suppressing truth.** Relationship count is unlimited. More than 30 root boxes is an advisory warning requiring operator readability review, never automatic node or edge removal. A family holds at most 18 children: use two columns for 1–11 children and three for 12–18. Any split must use independently meaningful domains and each resulting view must remain connected to its stakeholder anchor.
7. **Validate every view graph.** Every semantic element has degree at least one;
   every view includes the stakeholder and exactly one weakly connected component.
   Nesting counts only when backed by Composition/Aggregation. Split genuine
   components into semantically named views and halt if a component lacks an
   approved stakeholder path.
8. **Use technology-specific containment.**
   - **ArchiMate XML:** nested `DiagramObject` children with relative bounds; no `sourceConnection` for a parent-child composition.
   - **LikeC4:** nested model elements and scoped view inclusion; include only external links.
   - **pyArchimate:** use both `Model.add_child(parent.uuid, child.uuid)` and `parent_node.add(child)`, then `parent_node.resize(...)`. Pack measured root boxes without overlap and route only visible external links.
   - **Markdown:** draw parent boxes around child boxes or lists, and omit composition arrows inside the box.
9. **Obtain approval.** Present each family’s parent title, children, nesting, complete relationship set, connectivity result, and any root warning as `Confirm Requirement Family` before persistence.
10. **Render during QA.** Before final approval, render the selected technology’s view and inspect the actual family layout: XML in an Archi-compatible diagram preview, LikeC4 through its renderer, and pyArchimate through an approved transient view preview. Reject overlap, off-canvas children, missing containment, visible internal composition edges, isolated elements, and islands.

## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True. Family naming, decomposition, and visible links require approval before any view is written.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | :--- | :--- | :--- |
| Requirement has no source citation or approved direct legal-text ID | Exclude it from the ledger | `Error: Legal requirement lacks a citation or verified direct legal-text ID. Return it to legal-text-anchor resolution.` |
  | Parent or child has a vague title | Halt family creation | `Error: Requirement-family title is not target-qualified. Ask the operator for a clear functional name.` |
  | Family exceeds 18 children | Split only by coherent domain | `Error: Family exceeds the visual containment limit. Propose meaningful subdomains for approval.` |
  | More than 30 roots | Warn and review | `Warning: View exceeds the advisory root threshold. Present the complete graph and optional coherent split; do not suppress relationships.` |
  | Isolated element or multiple components | Halt or split | `Error: View graph is disconnected. Use approved edges only and obtain operator approval for any component-based split.` |
  | Containment absent from model or canvas | Reject rendering | `Error: Family child is not both semantically composed and visually nested.` |
  | Internal composition line is visible | Remove only the visual connection | `Error: Containment composition must remain semantic-only on the canvas.` |

* **Loop Prevention Rule:** If the same family naming or density error occurs twice, stop and request an operator decision rather than inventing a new grouping.
