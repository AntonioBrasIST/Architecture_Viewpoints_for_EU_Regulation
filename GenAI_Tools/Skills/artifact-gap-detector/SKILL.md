---
name: artifact-gap-detector
description: Inventories structurally approved GAP content independently in narrative sections, slides, and native model views. Use at Step 12 before gap-free duplication; do not classify ordinary prose as a GAP or modify source artifacts.
---

# Artifact GAP Detector

## Purpose

Perform the read-only first phase of Step 12 and decide exactly which contained
units require transformation.

## Unit-level scan

Inspect independently:

- every named narrative view section;
- every slide;
- every view in the selected XML, LikeC4, or pyArchimate model.

Recognize only approved `GAP-*` records, ArchiMate `Gap` elements, LikeC4
`gap`/`#gap` elements, their exact presentation references, and relationships
incident to those elements. Words such as “gap”, “absence”, “missing”, or “risk”
are not structural classifications.

Return a normalized inventory:

```json
{
  "artifacts": [{
    "kind": "narrative|slides|archimate|likec4|pyarchimate",
    "path": "source path",
    "sha256": "source hash",
    "units": [{"id": "textual unit name", "gap_ids": ["GAP-..."]}]
  }]
}
```

Feed it to `Methodology/tools/gap_derivative_plan.py`. Clean units and clean
artifact types are skipped. If every unit is clean, the Step 12 gate is still
presented but no derivative and no manifest is written. If any unit is affected,
only affected units are transformed and `Views/5_gap_free_manifest.md` records
the inventory, hashes, skips, removals, and outputs.

After proposed removal, invoke `connected-view-validator` through
`Methodology/tools/view_graph_validator.py --remove-from-view ... --remove-node
...`. Any isolated survivor, multiple components, or missing stakeholder path
returns the batch to Step 11; the detector and duplicator must not invent bridges
or silently remove more data.
