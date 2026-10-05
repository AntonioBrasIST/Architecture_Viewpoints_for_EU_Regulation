---
name: connected-view-validator
description: Validates evidence-backed view graphs for zero isolated semantic elements, one weakly connected component, mandatory stakeholder presence, and non-suppressive readability warnings. Use before every view, slide, or model persistence gate.
---

# Connected View Validator

## Graph contract

- Vertices are every semantic element, box, symbol, or callout placed in the view;
  titles, legends, and purely decorative marks are excluded.
- Edges are operator-approved `REL-*` relationships. Direction is ignored only for
  the connectivity calculation; the modeled direction remains unchanged.
- A nested Composition/Aggregation counts as an edge only when the semantic
  relationship exists and the child is actually nested under the matching parent.
- Every vertex must have at least one incident edge (degree at least one).
- The undirected projection must have exactly one connected component.
- The declared stakeholder anchor must be present and therefore have a path to
  every other vertex.

## Execution

Run the repository validator against the approved manifest:

```bash
python3 Methodology/tools/view_graph_validator.py \
  Methodology/StakeHolders/<Stakeholder>/7_view_graph.json
```

Native generators must also project their round-tripped output back to the same
node/relationship membership and run the equivalent checks. Slides additionally
require every semantic callout to have an approved attachment edge.

## Failure and splitting

- An isolated vertex is a blocking error, even when the element is traceable in a
  text catalog.
- Two or more components are a blocking error. Propose one semantically named view
  per component; never invent a bridge or use numbered overflow names.
- Every proposed split must independently contain an evidence-backed stakeholder
  path. If it does not, return the exact element/component upstream for operator
  evidence or exclusion approval.
- Relationship count is unlimited. More than 30 root elements is a warning that
  triggers readability review and an optional thematic split; it never authorizes
  dropping an element or relationship.
