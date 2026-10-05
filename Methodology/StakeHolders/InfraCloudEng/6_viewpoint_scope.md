# Viewpoint Scope Definition: Senior Infrastructure Engineer and Cloud Database Administrator

| Scope Dimension | Definition |
| --- | --- |
| **Operational Source** | [3_operational_footprint.md](../InfraCloudEng/3_operational_footprint.md) |
| **Stakeholder Classification** | [4_stakeholder_classification.md](../InfraCloudEng/4_stakeholder_classification.md): senior technical stakeholder, not an architect. |
| **Legislative Source** | [5_regulatory_relevance.md](../InfraCloudEng/5_regulatory_relevance.md), DORA Regulation (EU) 2022/2554, CELEX `32022R2554`; recorded legal index `TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx`. |
| **Immutable Overview Baseline** | [Views/0_dora_regulation_overview.archimate](Views/0_dora_regulation_overview.archimate) and [Views/0_dora_regulation_overview.py](Views/0_dora_regulation_overview.py). This Step 6 scope does not modify either artifact. |
| **Viewpoint Boundary** | The stakeholder's evidenced administration of Starburst, OpenMetadata, and SingleStore, with access, configuration, approved change, monitoring, incident, recovery, testing, dependency, approval, provider, and operational-context interfaces. It includes an external duty only where the approved ledger records an operational effect. |
| **Out of Scope** | Enterprise-wide DORA compliance, policy, audit, authority reporting, board/management ownership, and third-party verification ownership where no stakeholder responsibility is evidenced. The complete regulation remains represented only by immutable View 0. Article 5 remains omitted; `REQ-Art12-11`, `REQ-Art25-04`, and `REQ-Art25-05` are inactive under the confirmed Bank classification. |
| **Scope Justification** | The boundary is the approved Step 5 evidence chain: 162 active `COV-*` records link all relevant legal requirements to approved `OP-*` or `CON-*` sources. The stakeholder directly performs only the entries marked `Directly performed`; all other ownership states remain constraints, external duties, approvals, dependencies, or explicit uncertainty. |

## Immutability and Traceability Contract

- The 162 active coverage relationships, their `REQ-*` endpoints, citations, canonical legal-text IDs, evidence, and ownership states are carried verbatim from Step 5. Step 6 neither re-resolves nor changes a legal anchor.
- For each child listed below, the authoritative direct legal-text ID is the matching `REQ-*` row in the **Granular Requirement Register** in `5_regulatory_relevance.md`; the same child is joined to its exact Step 5 evidence and ownership by the listed `COV-*` / `REL-COV-*` record. This is the binding source for later materialization.
- `REL-ROLE-001` (stakeholder works within Bank), `REL-ROLE-002` (Bank is a DORA-regulated credit institution), and View 0's `REL-ROLE-003` (entity is in scope of DORA) remain unchanged.
- A direct coverage relationship may be modelled as `Realization` only for the listed `Directly performed` entries. `Stakeholder-constrained`, `Externally owned`, and `Not evidenced / unclear owner` entries use their approved non-realization effect.

---

## Viewpoint Inclusions

1. **ICT Risk Governance** `[Governance]` — framework, control-function, audit, review, strategy, tolerance, and authority-reporting interfaces grounded in `COV-001–003`, `006–007`, and `009–019`.
2. **Platform & Asset Management** `[Governance][Technical]` — administered platforms, reliability, capacity dependency, assets, configurations, inventories, and legacy connections in `COV-027–036`, `038–040`, and `042–044`.
3. **Provider Dependencies** `[Governance][Administrative]` — provider-dependent platforms, interconnections, BIA dependencies, and provider training in `COV-026`, `041`, `086`, and `125`. `COV-026` retains `Not evidenced / unclear owner` for outsourced compliance verification.
4. **Access & Security** `[Administrative][Technical]` — Ranger-based access, partial Python automation, secrets, support handoff, security approval, and network interface in `COV-004`, `047–059`, and `064`.
5. **Controlled Change** `[Administrative][Technical]` — GitOps/deployment, risk assessment, ServiceNow recording, approval, validation, patching, and the unknown authorization-status automation in `COV-008`, `021`, `037`, and `060–063`.
6. **Monitoring & Detection** `[Technical]` — Datadog telemetry, detection, alerting, detection tests, and resilience-impact inputs in `COV-020`, `022`, `045`, `065–071`, and `110`.
7. **Continuity Preparedness** `[Governance][Administrative]` — continuity arrangements, impact/dependency inputs, plan assurance, and preparedness tests in `COV-072–074`, `079–080`, `082–085`, `087–092`, and `094`.
8. **Recovery & Restoration** `[Technical]` — SingleStore incident recovery, backup, restoration, recovery integrity, capacity, and service-level inputs in `COV-005`, `023`, `046`, `075–078`, `081`, `093`, `095–104`, and `106–109`. It is represented through the two coherent families **Incident Recovery** and **Backup & Restoration**; this is a family-size split, not a disconnection.
9. **Operational Learning** `[Governance][Administrative]` — post-incident review, improvement inputs, learning, training, and technology monitoring in `COV-111–124` and `126`.
10. **Crisis Communication** `[Administrative]` — communication-plan, disclosure, staffing, and public/media ownership interfaces in `COV-025` and `127–131`.
11. **Incident Management** `[Administrative][Technical]` — incident process, records, root-cause remediation, warning indicators, roles, escalation, and restoration in `COV-132–142`.
12. **Incident Classification** `[Administrative][Technical]` — outage, client, transaction, reputation, duration, data-loss, service, economic, and threat-classification inputs in `COV-143–152`.
13. **Resilience Testing** `[Technical]` — non-production testing, testing governance, DevOps validation, test-finding visibility, and connection testing in `COV-024` and `153–163`.
14. **Role-Specific Operational Context** `[Administrative][Technical]` — the eleven approved `COV-CTX-*` records, retained without inventing legal obligations or relationships.

---

## Detailed Legislative Focus

- **Primary legislative focus:** DORA's technical resilience lifecycle: security and access controls (Arts. 9–10), continuity preparedness (Art. 11), recovery and restoration (Art. 12), operational learning (Art. 13), incident coordination and classification (Arts. 14 and 17–18), and resilience testing (Arts. 24–25).
- **Detail rationale:** These obligations have the densest evidence chain to day-to-day technical work: access provisioning, secret use, GitOps/configuration changes, Datadog alerts, a material SingleStore outage, Ranger backup, restoration, post-incident reporting, and non-production testing. Continuity, recovery, and learning are deliberately separate streams because planning/preparedness, restoration execution, and post-event improvement have different facts, ownership states, and legal children.

---

## Requirement-Family Ledger

`D` = Directly performed; `S` = Stakeholder-constrained; `E` = Externally owned; `U` = Not evidenced / unclear owner. Every listed child retains the exact citation and canonical legal-text ID of its matching `REQ-*` row in Step 5.

| Family Parent | Nested Child Requirements | Coverage IDs / Ownership States | Legal Text / Operational Traceability | Visible External Links |
| --- | --- | --- | --- | --- |
| **ICT Risk Governance** | `REQ-Art6-01–03`, `06–07`, `09–19` | `001–003, 009–011, 016–019` S; `006–007, 012–015` E | DORA Art. 6; maintenance, platform accountability, change review, incident report, outage impact, stakeholder team (`OP-001–004`, `007`, `036`, `043`, `048`, `050`; `CON-006`) | Independent control/audit and authority-reporting duties remain external. |
| **Platform & Asset Mgmt** | `REQ-Art7-01–05`; `REQ-Art8-01–05`, `07–09`, `11–13` | `027, 029` D; `028, 030–036, 038–040, 042–044` S | DORA Arts. 7–8; administered platforms, connectivity, GitOps/configurations, Azure DevOps, dependencies, and historic connection (`OP-002–004`, `006–007`, `014`, `019–021`, `023`, `028`, `031–033`, `048`, `050`; `CON-001`, `005`) | AKS/compute, networking, and technology-support dependencies stay visible. |
| **Provider Dependencies** | `REQ-Art6-26`; `REQ-Art8-10`; `REQ-Art11-15`; `REQ-Art13-16` | `041, 086` S; `125` E; `026` U | DORA Arts. 6, 8, 11, 13; Starburst, OpenMetadata, and SingleStore provider use (`OP-002–004`, `031–033`; operator confirmation) | Provider use is known; outsourced verification owner is not assigned. |
| **Access & Security** | `REQ-Art6-04`; `REQ-Art9-03–15`, `20` | `049, 056` D; `004, 047–048, 050–055, 058–059, 064` S; `057` E | DORA Arts. 6 and 9; access, Ranger policies/automation, Key Vault/root secrets, secure handoff, and network dependency (`OP-005`, `007–009`, `022`, `024`, `031–032`, `034`, `045`, `052`; `CON-002–003`) | Security Team approval and network/compute responsibility remain external. |
| **Controlled Change** | `REQ-Art6-08`, `21`; `REQ-Art8-06`; `REQ-Art9-16–19` | `060` D; `021, 037, 061, 063` S; `008` E; `062` U | DORA Arts. 6, 8, 9; GitOps/AKS work, production records, readiness, authorization, and review (`OP-014–018`, `020`, `023`, `027–028`, `030`, `044`, `046–047`, `050–051`, `056`; `CON-009`) | Authorization and Security Teams remain visible; automation owner is not inferred. |
| **Monitoring & Detection** | `REQ-Art6-20`, `22`; `REQ-Art9-01`; `REQ-Art10-01–07`; `REQ-Art13-01` | `022, 045, 065, 070, 110` D; `020, 066–069, 071` S | DORA Arts. 6, 9, 10, 13; Datadog alerts, logs, testing, outage evidence, and recovery (`OP-016`, `018`, `036–038`) | Monitoring-resource and threshold ownership remain constraints. |
| **Continuity Preparedness** | `REQ-Art11-01–03`, `08–09`, `11–14`, `16–21`, `23` | `072–074, 079, 083–085, 087–088, 090–091` S; `080, 082, 089, 092, 094` E | DORA Art. 11; accountable technologies, outage impact, dependency/BIA evidence, non-production testing, reports, reviews, and incident participants (`OP-013`, `016`, `031–033`, `036`, `039–041`, `043`, `048`, `050`; `CON-006`) | Crisis communications, independent audit, and formal crisis-management ownership remain external. |
| **Incident Recovery** | `REQ-Art6-05`, `23`; `REQ-Art9-02`; `REQ-Art11-04–07`, `10`, `22` | `005, 046, 075–076, 078` D; `023, 077, 081, 093` S | DORA Arts. 6, 9, 11; SingleStore restart, cause investigation, mitigation, native tools, and post-incident report (`OP-037`, `042–043`, `054`; `CON-007`) | Formal containment and plan ownership are not assigned to the stakeholder. |
| **Backup & Restoration** | `REQ-Art12-01–10`, `12–15` | `096–097, 103` D; `095, 098–102, 104, 106–109` S | DORA Art. 12; Ranger backup, secret handling, compute capacity, limited connection queries, and outage evidence (`OP-013`, `016`, `022`, `025`, `031`, `036–037`) | Restoration-environment, capacity, RTO/RPO, and service-level ownership remain constraints/external interfaces. |
| **Operational Learning** | `REQ-Art13-02–15`, `17` | `111–112, 114–120, 122, 124, 126` S; `113, 121, 123` E | DORA Art. 13; reports, maintenance, review, Datadog, incident participants, senior role, and investigation tooling (`OP-001`, `007`, `026`, `037–039`, `043`, `048`, `050`) | Authority/management reporting and strategy monitoring remain external. |
| **Crisis Communication** | `REQ-Art6-25`; `REQ-Art14-01–05` | `130` S; `025, 127–129` E; `131` U | DORA Arts. 6 and 14; support handoff, outage/report evidence, and incident participants (`OP-036`, `039–041`, `043`) | Communication-plan, disclosure, policy, and public/media ownership are not asserted for the stakeholder. |
| **Incident Management** | `REQ-Art17-01–11` | `136–137, 142` D; `132–135, 138, 140` S; `139, 141` E | DORA Art. 17; SingleStore recovery, Datadog alerts, ServiceNow incidents, reports, and incident participants (`OP-029`, `037–043`) | Formal incident-role assignment and senior-management reporting remain external. |
| **Incident Classification** | `REQ-Art18-01–10` | `143–152` S | DORA Art. 18; outage/service impact, Datadog telemetry, and sensitive-secret handling (`OP-024`, `036`, `038`; `CON-006`) | Client, transaction, reputation, geography, economic, and threat classification ownership are not inferred. |
| **Resilience Testing** | `REQ-Art6-24`; `REQ-Art24-01–08`; `REQ-Art25-01–03` | `024, 155, 161–162` D; `153–154, 156–160, 163` S | DORA Arts. 6, 24, 25; non-production and connection testing, DevOps validation, and non-production record visibility (`OP-016–019`, `025`, `051`, `058`; `CON-011`) | Programme, risk approach, independence, resourcing, and test-method selection are not attributed to the stakeholder without evidence. |

---

## Operational and Concern Assignment

All 58 `OP-*` facts and 11 `CON-*` records are assigned. A source may participate in more than one legal coverage edge, but no active `COV-*` is assigned to more than one requirement family.

| Assignment | Sources retained | Treatment |
| --- | --- | --- |
| Legal families above | `OP-001–009`, `OP-013–034`, `OP-036–048`, `OP-050–052`, `OP-054`, `OP-056`, `OP-058`; `CON-001–003`, `CON-005–007`, `CON-009`, `CON-011` | Represent through the matching Step 5 `REL-COV-*` and any exact approved operational relationship required by the candidate graph. |
| Cross-platform colleague support | `OP-010–012` | Context-only candidate graph using `REL-OP-012–015`: Stakeholder → Colleague Assistance → Kafka/Cosmos/Databricks. |
| Investigation tooling | `OP-026` | Also supports operational learning; context candidate graph uses `REL-OP-031–032`: Stakeholder → Log Investigation → LLM Tools. |
| Emergency-change context | `OP-049` | Context candidate graph uses `REL-OP-056–058`: Critical Service Impact → Emergency Change ← Stakeholder → Change Report. |
| Relationshipless context records | `OP-035`, `OP-053`, `OP-055`, `OP-057`; `CON-004`, `CON-008`, `CON-010` | Preserved in `COV-CTX-005–009` and `011`, but not made into diagram nodes because the approved ledger provides no stakeholder-connected relationship. This avoids inventing a link or creating an isolated element. |

---

## Node-and-Relationship Candidate Ledger

### Common legal-view anchor

Every regulatory candidate view includes the approved role chain: **Infrastructure Engineer / Cloud DB Admin** — `REL-ROLE-001` → **Bank** — `REL-ROLE-002` → **DORA-regulated financial entity** — `REL-ROLE-003` → **DORA Resilience Framework**. Each family is semantically composed beneath the framework; each granular child is semantically composed beneath its family; every listed `REL-COV-*` connects the approved operational endpoint to its exact legal child.

| Candidate view | Family containment | Complete coverage-relationship membership | Connectivity result |
| --- | --- | --- | --- |
| ICT Risk Governance | ICT Risk Governance | `REL-COV-001–003`, `006–007`, `009–019` | 1 component; 20 roots |
| Platform & Asset Mgmt | Platform & Asset Mgmt | `REL-COV-027–036`, `038–040`, `042–044` | 1 component; 20 roots |
| Provider Dependencies | Provider Dependencies | `REL-COV-026`, `041`, `086`, `125` | 1 component; 8 roots |
| Access & Security | Access & Security | `REL-COV-004`, `047–059`, `064` | 1 component; 19 roots |
| Controlled Change | Controlled Change | `REL-COV-008`, `021`, `037`, `060–063` | 1 component; 11 roots |
| Monitoring & Detection | Monitoring & Detection | `REL-COV-020`, `022`, `045`, `065–071`, `110` | 1 component; 15 roots |
| Continuity Preparedness | Continuity Preparedness | `REL-COV-072–074`, `079–080`, `082–085`, `087–092`, `094` | 1 component; 20 roots |
| Recovery & Restoration | Incident Recovery; Backup & Restoration | `REL-COV-005`, `023`, `046`, `075–078`, `081`, `093`, `095–104`, `106–109` | 1 component; 27 roots |
| Operational Learning | Operational Learning | `REL-COV-111–124`, `126` | 1 component; 19 roots |
| Crisis Communication | Crisis Communication | `REL-COV-025`, `127–131` | 1 component; 10 roots |
| Incident Management | Incident Management | `REL-COV-132–142` | 1 component; 15 roots |
| Incident Classification | Incident Classification | `REL-COV-143–152` | 1 component; 14 roots |
| Resilience Testing | Resilience Testing | `REL-COV-024`, `153–163` | 1 component; 16 roots |
| Cross-platform Support | Operational-context graph | `REL-OP-012–015` | 1 component; 5 roots |
| Investigation Tooling | Operational-context graph | `REL-OP-031–032` | 1 component; 3 roots |
| Emergency Change Context | Operational-context graph | `REL-OP-056–058` | 1 component; 4 roots |

### Connectivity Validation Record

The candidate topology was checked with `Methodology/tools/view_graph_validator.py` before persistence. It used 13 legal views, 3 connected context views, 14 requirement-family parents, all 162 active `REL-COV-*` relationships, and the approved role chain. The result was **PASS**: every candidate contains the stakeholder anchor, has exactly one weakly connected component, has zero isolated nodes, and has no root-count warning. The semantic partitions are domain splits, not unconnected islands.

## Step 6 Approval Record

- Gate 6.1 — Scope Boundary and Legislative Focus: approved.
- Gate 6.2 — Inclusions and Streams: approved after completeness, duplicate-assignment, and source-coverage validation. `COV-008` and `COV-037` are assigned only to Controlled Change.
- Gate 6.3 — Connectivity and Splits: approved after connected-graph validation.
