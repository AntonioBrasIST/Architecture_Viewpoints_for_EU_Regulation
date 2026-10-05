# View Artifact Cross-Audit & Reconciliation Report

## Audit status: 100% aligned

**Selected model:** \`3_view_model_pyarchimate.archimate\`  
**Immutable baseline:** \`0_dora_regulation_overview.archimate\`  
**Legal index:** \`TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx\`

The Step 11 five-way reconciliation audited the approved View 0 baseline,
Step 7 viewpoint and graph, narrative, slide deck, Step 5 coverage ledger,
and selected pyArchimate archive. This report records no enterprise compliance
conclusion.

## Approved reconciliation action

The operator approved the recommended fixes.

1. **Deduplicated parent legal-ID roll-ups**
   - Updated the 12 affected requirement-family roll-ups in
     \`7_view_graph.json\` and \`7_viewpoint.md\`.
   - Preserved child order and every direct legal-text ID.
   - Updated the reproducible pyArchimate script's approved graph hash and
     regenerated the archive.

2. **Aligned formal visible titles**
   - Updated 135 narrative traceability rows to show the approved formal
     requirement title followed by the unchanged statutory duty.
   - Added the formal titles \`Responsible Dev Team\` and \`Infra Remediation\`
     alongside their approved ledger endpoint names in the narrative.
   - Used \`Azure AD Access Control\` and \`Infra Remediation\` as the corresponding
     visible diagram labels in the slide deck.

No coverage ID, ownership state, direct legal-text ID, relationship ID,
endpoint, direction, ArchiMate type, or baseline content was changed.

## Validation evidence

| Check | Result |
| --- | --- |
| Step 5 coverage rows ↔ Step 7 requirements | 153 of 153 matched; no ownership mismatch |
| Stakeholder legal anchors | 110 unique anchors verified against the legal index |
| View 0 legal anchors | 138 unique anchors verified against the legal index |
| Graph manifest | 194 nodes and 334 relationships; all six views have one component and zero isolated elements |
| Narrative and slides | All graph titles, requirements, coverage IDs, and relationship IDs present; no canonical \`Chap.\` identifier exposed |
| Native archive | 343 elements, 483 relationships, 7 views; no invalid relationships, nodes, or connections |
| Thematic visual projection | Exact node and non-composition connection membership; all requirement children visually nested under their composed family |
| Layout | No thematic root-box overlaps |
| View 0 preservation | 151 elements, 150 relationships, and the overview view preserved unchanged |

## Result

The selected pyArchimate model and all supporting artifacts are synchronized
with the approved Step 7 graph and Step 5 coverage evidence.
