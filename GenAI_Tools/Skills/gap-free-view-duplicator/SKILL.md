---
name: gap-free-view-duplicator
description: Produces affected-unit-only, copy-faithful gap-free derivatives after independent structural GAP detection and reconciliation. Never modifies source artifacts or processes clean units.
---

# Conditional Gap-Free View Duplicator

## Purpose and boundaries

Run only after Step 11 reconciliation and `artifact-gap-detector`. Preserve the
selected source model/script, contextualized Overview baseline, `7_view_graph.json`,
narrative, slides, Coverage/Relationship Ledgers, and reconciliation evidence.
This skill removes approved structural GAP content; it does not discover,
reclassify, or infer gaps.

## Required inputs

- Reconciled source hashes and reconciliation evidence.
- Normalized per-unit GAP inventory from `artifact-gap-detector`.
- Conditional plan from `Methodology/tools/gap_derivative_plan.py`.
- Approved `7_view_graph.json` and native model identifiers/layout records.

## Conditional transformation contract

1. Inspect narrative sections, slides, and native model views as independent
   units. Process only units listed in `affected_units_only`.
2. Do not clone or transform clean units. They remain available in the unchanged
   source artifact.
3. If every unit is clean, present `Confirm Gap-Free Transformation`, then finish
   without writing any derivative or manifest.
4. If at least one unit is affected, create only the corresponding artifact types:
   - narrative: `Views/5_gap_free_view_explanation.md`;
   - slides: `Views/5_gap_free_slide_diagrams.md`;
   - XML: `Views/5_gap_free_model.archimate`;
   - LikeC4: `Views/5_gap_free_model.c4`;
   - pyArchimate: `Views/5_gap_free_model.py` plus its sibling archive.
5. A produced narrative/deck/model derivative contains affected units only, named
   `<Original> — No Gaps`. It is a delta companion to the source, not a complete
   replacement.
6. When any derivative exists, also write `Views/5_gap_free_manifest.md` with
   source hashes, structural GAP IDs, affected and skipped units, removed attached
   relationships, omissions, output paths, and validation results.

## Copy rules

- Remove only approved `GAP-*` elements/tags and relationships having a removed
  GAP endpoint, plus presentation blocks explicitly traceable to those IDs.
- Never delete ordinary content because its prose says “gap”, “absence”,
  “missing”, “shortfall”, or similar.
- Omit an affected unit only when GAP removal leaves no content; record it.
- Preserve surviving element/relationship identity, meaning, documentation,
  citations, ownership, ordering, nesting, styles, and source metadata.
- XML/pyArchimate: preserve every surviving bound, visual parent, sibling order,
  connection endpoint binding, style, and bendpoint exactly. Leave deleted space
  empty; never re-layout, re-route, resize, pack, or compact.
- LikeC4: preserve declarative ordering, nesting, groups, predicates, view
  settings, and styles, and report native-semantic fidelity.

## Connectivity and native validation

Before writing, invoke `connected-view-validator` on every affected view after
the planned removal using `Methodology/tools/view_graph_validator.py
--remove-from-view ... --remove-node ...`. Reject isolated survivors, multiple weakly connected
components, or a missing stakeholder path. Return such discrepancies to Step 11;
do not add a bridge, duplicate an unsupported stakeholder relation, or silently
remove more content.

Then validate zero surviving structural GAP content/attached edges, zero dangling
references, exact retained copy fidelity, unchanged source hashes, and native
syntax/round-trip integrity. For pyArchimate, compile and run the derivative and
require zero invalid relationships/nodes/connections; reject automatic layout or
routing helpers.

## Human gate

Present one `Confirm Gap-Free Transformation` review containing the independent
per-unit scan, affected-only transformations, clean-unit skips, source hashes,
post-removal connectivity results, omissions, manifest decision, and conditional
output paths. No file may be written or executed until the operator approves.
