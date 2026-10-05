# ArchiMate Viewpoint Definition: DORA Infrastructure Resilience

| Viewpoint Attribute | Definition |
| --- | --- |
| **Viewpoint Name** | DORA Infrastructure Resilience |
| **Target Stakeholders** | Senior Infrastructure Engineer / Cloud Database Administrator and the evidenced Team Lead. |
| **Purpose** | **Informing** — communicate the source-backed link between the stakeholder's operational work and DORA requirements without assessing enterprise compliance or assigning unsupported control ownership. |
| **Scope** | The 162 active Step 5 coverage records, the complete approved operational relationship ledger, the approved role chain, and the immutable DORA View 0 baseline. The viewpoint excludes Article 5 and the three approved inactive conditional requirements. |
| **Primary Concerns** | **[Governance]** accountable ICT-risk, asset, provider, continuity, and learning constraints; **[Administrative]** access, approval, change, incident-record, and communication interfaces; **[Technical]** platform administration, telemetry, recovery, restoration, and testing. |

## Whitelisted ArchiMate Concepts

| Concept | Layer / Aspect | Use in this viewpoint |
| --- | --- | --- |
| Business Role | Business / Active Structure | Infrastructure Engineer / Cloud DBA. |
| Business Actor | Business / Active Structure | Bank, stakeholder team, approval, support, and dependency teams. |
| Business Process | Business / Behaviour | Evidenced administration, change, approval, support, recovery, testing, and reporting work. |
| Business Event | Business / Behaviour | Outage, alert, and critical-service-impact triggers. |
| Business Object | Business / Passive Structure | Business-facing approval and report records where evidence requires them. |
| Application Component | Application / Active Structure | Named technologies and operational tools. |
| Node | Technology / Active Structure | AKS, where represented as the named target environment. |
| Data Object | Application / Passive Structure | Configurations, secrets, ServiceNow records, and database table data. |
| Artifact | Technology / Passive Structure | Configuration artefacts where a distinct deployed/configuration item is evidenced. |
| Requirement | Motivation | DORA framework root, 14 meaningful family parents, and every granular active legal child. |
| Assessment / Gap | Motivation | Only an approved concern or explicit visibility limitation when it has an approved relationship; titles remain clean and status stays in documentation. |

## Whitelisted ArchiMate Relations

| Relation | Permitted use |
| --- | --- |
| Composition | Requirement family to granular legal child, and DORA root to family. Semantic-only only when the same containment is visually nested. |
| Assignment | Approved role or actor to approved business process. |
| Serving | Approved support-team or technology support relationship. |
| Access | Approved work access to configurations, secrets, records, and data. |
| Triggering | Approved operational event or workflow trigger. |
| Flow | Approved transfer of logs, configurations, reports, or other explicit handoff. |
| Specialization | Bank to the DORA financial-entity group. |
| Realization | Only a `Directly performed` coverage source to its granular requirement. |
| Association | Approved stakeholder-constrained, externally owned, unclear-owner, dependency, and other non-realization coverage effects. |

## Representation and Ownership Rules

- The immutable View 0 is reproduced without modification, including `REL-ROLE-001`, `REL-ROLE-002`, and `REL-ROLE-003`.
- Legal family and child titles are meaningful, target-qualified, and clean. Names should normally be 25 characters or fewer for readability; the operator approved retaining exact titles where legal/control inclusion requires them. IDs, citations, legal-text anchors, ownership, and evidence are documentation fields only.
- Every granular legal child has its Step 5 citation and direct legal-text ID. Each parent records the ordered, deduplicated roll-up of its children’s IDs.
- `Directly performed` coverage may be a Realization. `Stakeholder-constrained`, `Externally owned`, and `Not evidenced / unclear owner` coverage is never a stakeholder Realization.
- Composition is semantic-only only when visual nesting expresses the same parent-child structure. All other approved relationships remain visible.
- Every view contains the stakeholder anchor and exactly one weakly connected component. No semantic element is isolated. The readability threshold is 30 roots; no approved view exceeds it.

## Requirement-Family Ledger

| Parent Element | Nested Child Elements | Semantic Relation | Coverage IDs / Ownership | Visible Links | Legal Text / Traceability |
| --- | --- | --- | --- | --- | --- |
| ICT Risk Governance | `REQ-Art6-01–03`, `06–07`, `09–19` | Composition | `001–003, 009–011, 016–019` S; `006–007, 012–015` E | Approved maintenance, team-accountability, review, and reporting links | Step 5 Art. 6 child citations and canonical IDs unchanged. |
| Platform & Asset Mgmt | `REQ-Art7-01–05`; `REQ-Art8-01–05`, `07–09`, `11–13` | Composition | `027,029` D; remaining family COVs S | Approved platform, configuration, dependency, and asset links | Step 5 Arts. 7–8 child citations and canonical IDs unchanged. |
| Provider Dependencies | `REQ-Art6-26`; `REQ-Art8-10`; `REQ-Art11-15`; `REQ-Art13-16` | Composition | `041,086` S; `125` E; `026` U | Approved provider/dependency links; no verification owner invented | Step 5 cited children and canonical IDs unchanged. |
| Access & Security | `REQ-Art6-04`; `REQ-Art9-03–15`, `20` | Composition | `049,056` D; constrained entries S; `057` E | Approved access, secret, approval, and network links | Step 5 cited children and canonical IDs unchanged. |
| Controlled Change | `REQ-Art6-08`, `21`; `REQ-Art8-06`; `REQ-Art9-16–19` | Composition | `060` D; `021,037,061,063` S; `008` E; `062` U | Approved GitOps, ServiceNow, authorization, and review links | Step 5 cited children and canonical IDs unchanged. |
| Monitoring & Detection | `REQ-Art6-20`, `22`; `REQ-Art9-01`; `REQ-Art10-01–07`; `REQ-Art13-01` | Composition | `022,045,065,070,110` D; remaining entries S | Approved Datadog, alert, validation, outage, and recovery links | Step 5 cited children and canonical IDs unchanged. |
| Continuity Preparedness | `REQ-Art11-01–03`, `08–09`, `11–14`, `16–21`, `23` | Composition | Recorded S and E states unchanged | Approved continuity, BIA, test, review, and incident-participant links | Step 5 Art. 11 child citations and canonical IDs unchanged. |
| Incident Recovery | `REQ-Art6-05`, `23`; `REQ-Art9-02`; `REQ-Art11-04–07`, `10`, `22` | Composition | `005,046,075–076,078` D; remaining entries S | Approved recovery, backup, and post-incident links | Step 5 cited children and canonical IDs unchanged. |
| Backup & Restoration | `REQ-Art12-01–10`, `12–15` | Composition | `096–097,103` D; remaining entries S | Approved backup, secret, capacity, and integrity-test links | Step 5 Art. 12 child citations and canonical IDs unchanged. |
| Operational Learning | `REQ-Art13-02–15`, `17` | Composition | S and E states unchanged | Approved review, report, alert, maintenance, and investigation links | Step 5 Art. 13 child citations and canonical IDs unchanged. |
| Crisis Communication | `REQ-Art6-25`; `REQ-Art14-01–05` | Composition | `130` S; `025,127–129` E; `131` U | Approved support-handoff, reporting, and incident-participant links | Step 5 cited children and canonical IDs unchanged. |
| Incident Management | `REQ-Art17-01–11` | Composition | `136–137,142` D; stated S/E entries unchanged | Approved ServiceNow, monitoring, recovery, report, and escalation links | Step 5 Art. 17 child citations and canonical IDs unchanged. |
| Incident Classification | `REQ-Art18-01–10` | Composition | `143–152` S | Approved outage, secret, and monitoring inputs | Step 5 Art. 18 child citations and canonical IDs unchanged. |
| Resilience Testing | `REQ-Art6-24`; `REQ-Art24-01–08`; `REQ-Art25-01–03` | Composition | `024,155,161–162` D; remaining entries S | Approved non-production, validation, and connection-test links | Step 5 Arts. 6, 24, and 25 child citations and canonical IDs unchanged. |

## Approved View Set

1. Immutable DORA Regulation Overview
2. ICT Risk Governance
3. Platform & Asset Management
4. Provider Dependencies
5. Access & Security
6. Controlled Change
7. Monitoring & Detection
8. Continuity Preparedness
9. Recovery & Restoration
10. Operational Learning
11. Crisis Communication
12. Incident Management
13. Incident Classification
14. Resilience Testing
15. Cross-platform Support
16. Investigation Tooling
17. Emergency Change Context

## Approval Record

- Gate 7.1 — Confirm Metamodel Scope: approved.
- Gate 7.2 — Confirm View Graph: approved.
