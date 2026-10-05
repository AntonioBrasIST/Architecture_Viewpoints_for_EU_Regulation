---
name: informal-markdown-diagram-designer
description: Generates condensed, presentation-style markdown diagrams ("slides") using plain ASCII to visually convey regulatory impacts and operational constraints without requiring formal ArchiMate notation.
---

# AI Skill Specification: informal-markdown-diagram-designer

## 1. Semantic Metadata
* **Skill Identifier:** `informal-markdown-diagram-designer`
* **Short Summary:** Translates a viewpoint specification (`7_viewpoint.md`) and textual explanation (`Views/1_view_explanation.md`) into a structured markdown slide deck (`Views/2_slide_diagrams.md`) containing condensed ASCII diagrams that explain regulatory impact dimensions for any EU legislation.
* **LLM Routing Description:**
  > "Use this skill when you need to create condensed, ASCII slide-like markdown diagrams illustrating regulatory impacts and operational constraints under any EU legislation (DORA, NIS2, eIDAS2, GDPR, etc.). Requires `7_viewpoint.md` and `Views/1_view_explanation.md`. Outputs `Views/2_slide_diagrams.md`."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "informal-markdown-diagram-designer",
    "description": "Generates condensed ASCII markdown slide diagrams covering regulatory impact dimensions under any EU legislation.",
  "parameters": {
    "type": "object",
    "properties": {
      "viewpoint_spec": {
        "type": "string",
        "description": "Contents of 7_viewpoint.md."
      },
      "view_explanation": {
        "type": "string",
        "description": "Contents of Views/1_view_explanation.md."
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
    "required": ["viewpoint_spec", "view_explanation", "regulation_overview_baseline", "view_graph"]
  },
  "returns": {
    "type": "object",
    "description": "A markdown document containing slide-like sections with condensed ASCII diagrams and short narrative callouts."
  }
}
```

## 3. Core Principles & Design Rules

1. **Condensed ASCII aesthetic:** Diagrams must use fenced `text` blocks and plain ASCII characters only: `+`, `-`, `|`, `<`, `>`, `^`, `v`, and ordinary text. Do not use Mermaid, Unicode box-drawing characters, UML syntax, or another diagram language.
2. **Slide-Deck Structure:** Start with **Slide 0: Regulation Overview Map**,
   reproducing the immutable legal core and approved stakeholder/legal-role chain.
   Every later slide mirrors one approved stakeholder view graph.
3. **Legislative Agnosticism:** Works seamlessly for any EU legislation (DORA, NIS2, eIDAS2, GDPR, AI Act, etc.). Adapt slide titles and diagram components dynamically to match the specific law in question.
4. **Condensed visual summary with complete textual coverage:** Each stakeholder slide is a condensed visual summary of one formal view. Its ASCII sketch shows the stakeholder, principal operational path, relevant external dependencies, and every requirement-family parent in that view. The Component Breakdown and Relationship Inventory, rather than the sketch, provide complete granular-requirement and relationship coverage.
5. **Operational Gap Nuance (`[Gap]`):** Operational gaps identified in a footprint represent limitations *from that specific stakeholder's viewpoint or operational boundary*. They must be framed as *potential operational or visibility gaps from this stakeholder's perspective* ("may indicate a potential gap"), not definitive enterprise compliance violations. Slide 0 contains the approved stakeholder-role context but no gaps, status, or other stakeholder operations.
6. **Standardized Slide Layout:** Each slide MUST follow a 4-part structure:
   - **Slide Header:** Descriptive title and thematic dimension.
   - **Condensed ASCII Diagram:** A readable family-level diagram. Show the stakeholder, principal approved operational path, relevant external dependencies, and every parent requirement family as a labelled box. Show only selected approved relationships needed to make the operational story understandable.
   - **Component Breakdown:** Every granular child requirement, stated in readable language with its readable citation, ownership state, and operational relevance. Child requirements may be listed here rather than drawn as boxes.
   - **Relationship Inventory:** Every approved relationship, stated in readable source, relation, target, ArchiMate type, and ownership terms. This inventory supplements the sketch; it does not claim that every relationship is drawn.
   - **Operational Takeaway:** 2-3 bullet points highlighting the compliance rule and daily operational reality.
7. **Family visibility and fidelity audit:** Internally compare each slide with its formal view in `7_view_graph.json`. Before presentation, verify that every requirement-family parent is visibly named in the ASCII sketch, every granular child requirement appears in the Component Breakdown, every approved relationship appears in the Relationship Inventory, and every arrow drawn in the sketch corresponds to an approved relationship. Validate the source graph for stakeholder presence and connectedness, but do not call the condensed sketch an exact graph projection.
8. **Ownership-safe presentation:** In the sketch and supporting text, describe `Directly performed` work as stakeholder realization only where the approved relationship permits it. Describe constrained work as a constraint or dependency, externally owned work through its identified external role or system, and unclear ownership as a documented boundary. Never invent an owner.
9. **Reader-facing language boundary:** Do not display `REQ-*`, `OP-*`, `CON-*`, `COV-*`, or `REL-*` identifiers, canonical legal-text IDs, or internal graph identifiers in slide titles, diagrams, labels, callouts, tables, legends, or validation records. Use readable names and Article citations. Internal identifiers may be used only for the agent's completeness audit.

---

## 4. Required Output Format Template (`2_slide_diagrams.md`)

```markdown
# Visual Slide Deck: Stakeholder Operational Impact & Compliance Views

Each slide contains a condensed ASCII summary. Its accompanying tables retain
the detailed requirements and complete relationship record; the diagram is not
an exact graphical projection of the formal view.

---

## Slide 1: [Thematic Dimension Title]

### Visual Diagram Sketch
```
+------------------------+       +------------------------+
| Stakeholder             |------>| Primary work activity  |
+------------------------+       +------------------------+
                                      |
                                      v
                            +------------------------+
                            | External system or role |
                            +------------------------+

Requirement families represented in this summary:
+------------------------+  +------------------------+
| Requirement Family A   |  | Requirement Family B   |
| Detailed controls      |  | Detailed controls      |
| are listed below       |  | are listed below       |
+------------------------+  +------------------------+
```

### Component Breakdown
| Requirement family | Detailed controls and readable citations | Ownership and operational relevance |
| --- | --- | --- |
| [Family name] | [Readable child-control names and Article references] | [Directly performed, constrained, externally owned, or unclear ownership] |

### Relationship Inventory
| Source | Relationship | Target | ArchiMate type | Ownership or boundary |
| --- | --- | --- | --- | --- |
| [Readable source] | [Readable meaning] | [Readable target] | [Type] | [Approved ownership or boundary] |

### Operational Takeaway
* Specific compliance rule or constraint governing this workflow.
* Summary of the daily operational reality for the stakeholder.

---

[Repeat for Slide 2, Slide 3, Slide 4, ..., until 100% of viewpoint elements & relationships are covered]
```

## 5. Execution & Quality Constraints
- **Interactive Slide-by-Slide Gating Loop:** Before compiling and writing `Views/2_slide_diagrams.md`, you MUST loop through each planned slide individually and present it to the operator using the `question` tool:
  * **Header:** `Confirm Slide [N] Diagram`
  * **Question:** `"For Slide [N]: '[Slide Title]', here is the condensed ASCII diagram, its visible requirement families, its selected visual relationships, and the detailed controls and relationship record retained in the tables: [Insert ASCII Preview]. Do you agree with this slide's visual summary and supporting detail?"`
  * **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Execution Rule:** Iterate sequentially for every planned slide. Save the final markdown file strictly after 100% of individual slides are approved.
- **Complete textual coverage:** Every granular requirement, approved relationship, major workflow, friction point, and potential operational or visibility limitation in the formal view must appear in the Component Breakdown, Relationship Inventory, or Operational Takeaway. Include a role-specific operational-context slide where routine work has no statutory edge.
- **Condensed-diagram fidelity:** Every requirement-family parent in the formal view must appear as a visible labelled box in the ASCII sketch. Every sketch arrow must match an approved relationship, but the sketch need not draw every approved relationship or granular child requirement. Never label the sketch an exact graph projection.
- **No internal IDs:** All reader-facing slide content must use readable names and citations only. Internal IDs support completeness checking but must not be emitted in the deck.
- **Visual Clarity:** Ensure ASCII diagrams are clean, well-aligned, and readable in a standard plain-text editor.
