# Viewpoint Scope Definition: Back-end Developer

| Scope Dimension | Definition |
| --- | --- |
| **Operational Source** | `Methodology/StakeHolders/BankBackEndDev_2/3_operational_footprint.md` |
| **Stakeholder Source** | `Methodology/StakeHolders/BankBackEndDev_2/4_stakeholder_classification.md` |
| **Legislative and Coverage Source** | `Methodology/StakeHolders/BankBackEndDev_2/5_regulatory_relevance.md` |
| **Immutable Baseline** | `Methodology/StakeHolders/BankBackEndDev_2/Views/0_dora_regulation_overview.archimate` |
| **Viewpoint Boundary** | The Back-end Developer's evidenced C# platform work, release/change constraints, direct testing and software remediation, monitoring and incident interfaces, and recorded external dependencies. Microsoft-cloud contract obligations are represented only as constraints on an external contract. |
| **Scope Justification** | The scope is the approved intersection of 89 operational facts, eight concerns, 153 coverage rows, and 153 regulatory-effect relationships. It distinguishes the developer's direct work from stakeholder-constrained, externally owned, and unclear-owner work; it makes no compliance claim. |

## Boundary and exclusions

Included are framework maintenance, platform development, data offload work, DEV/test readiness, pull-request/release activity, production monitoring, incident/remediation interfaces, Azure AD/internal service-access constraints, enterprise-platform dependencies, and the Microsoft cloud contract.

Excluded are enterprise-wide DORA governance, unverified infrastructure recovery methods, Monitoring Team operations, formal incident classification/reporting ownership, contract negotiation and provider oversight execution, data ownership decisions, and work outside the stakeholder's limited project context. Those matters remain either external/unclear ownership in a thematic view or outside this stakeholder boundary. The complete law remains represented only in immutable View 0.

## Detailed legislative focus

- **Primary focus:** Article 28 ICT third-party risk, represented by COV-122–153. Microsoft is the cloud provider and a contract exists; the 32 approved Article 28 requirements constrain the recorded contract dependency.
- **Secondary focus:** Articles 24–25 resilience testing (COV-102–121) and Articles 10–13 and 17 continuity, learning, and incident handling (COV-035–101), because they directly constrain release, monitoring, escalation, and remediation work.
- **Anchor rule:** Every child requirement below preserves the approved direct Enacting Terms identifier(s) verbatim. Article citations and anchors are documentation, not visual node titles.

## Viewpoint inclusions

| Stream | Perspective | Inclusion and ownership treatment |
| --- | --- | --- |
| ICT Asset Governance | Technical / Governance | Framework maintenance, platform development, service update, and enterprise-platform inventory/risk constraints. Only Framework Maintenance is direct; enterprise-platform ownership stays unclear. |
| Protection & Change | Technical / Administrative | Data offload flow, access control, DEV/test readiness, change controls, and service updates. Azure AD/internal access remains external. |
| Detection & Continuity | Technical / Administrative | Production monitoring, escalation, software and infrastructure remediation, continuity and recovery constraints. Infrastructure and monitoring remain external; platform continuity ownership is explicitly unclear where recorded. |
| Incident Learning | Administrative / Technical | Incident learning, escalation, service updates, and software remediation. External and unclear ownership is preserved. |
| Resilience Testing | Technical / Administrative | Test and DEV readiness, pull-request review, and Article 24–25 testing constraints. Pull-request-review ownership is not inferred. |
| Microsoft Cloud Risk | Governance / Administrative | Microsoft Contract and all Article 28 third-party-risk constraints. No contract-management behavior is attributed to the stakeholder. |
| Role Context | Administrative / Technical | CTX-001–025: specification/mainframe, tools, provisioning, work allocation, decision intake, and evidence/visibility limitations. This is retained as scope evidence, not a standalone diagram. |

## Formal view ledger and connectivity

All ranges below are inclusive; no approved relationship is omitted. Each formal view includes the Back-end Developer and forms one weakly connected component. Requirement-family compositions are semantic-only and will be rendered as matching visual nesting.

| View | Stakeholder path and essential approved relationships | Regulatory-effect relationships | Connectivity / root result |
| --- | --- | --- | --- |
| ICT Asset Governance | Back-end Developer → Framework Maintenance → Internal Framework (REL-OP-090–091); Back-end Developer → Platform Development (REL-OP-001); Back-end Developer → Service Update (REL-OP-066); Back-end Developer → Enterprise Data Platform (REL-OP-093) | REL-COV-001–015; REL-COMP-S001–015 | One component; no isolated nodes; planned nested roots below 30. |
| Protection & Change | Back-end Developer → Offload Service → Data Offload Flow (REL-OP-002, REL-OP-010); Back-end Developer → Test and DEV Readiness (REL-OP-014); Azure AD / Internal Service Access → Back-end Developer (REL-OP-092); Back-end Developer → Service Update / Enterprise Data Platform (REL-OP-066, REL-OP-093) | REL-COV-016–034; REL-COMP-S016–034 | One component; no isolated nodes; planned nested roots below 30. |
| Detection & Continuity | Back-end Developer → Production Monitoring ← Datadog; Datadog Alarm → Incident Escalation → Software / Infrastructure Remediation (REL-OP-031–032, REL-OP-079–089); Back-end Developer → Platform Development / Enterprise Data Platform (REL-OP-001, REL-OP-093) | REL-COV-035–073; REL-COMP-S035–073 | One component; no isolated nodes; planned nested roots below 30. |
| Incident Learning | Back-end Developer → Production Monitoring ← Datadog; Datadog Alarm → Incident Escalation → Software Remediation (REL-OP-031–032, REL-OP-079–081, REL-OP-083, REL-OP-085, REL-OP-089); Back-end Developer → Service Update / Enterprise Data Platform (REL-OP-066, REL-OP-093) | REL-COV-074–101; REL-COMP-S074–101 | One component; no isolated nodes; planned nested roots below 30. |
| Resilience Testing | Back-end Developer → Test and DEV Readiness / Pull Request Creation; Technical Reviewer → Pull Request Review; review reads Pull Request (REL-OP-014–019) | REL-COV-102–121; REL-COMP-S102–121 | One component; no isolated nodes; planned nested roots below 30. |
| Microsoft Cloud Risk | Back-end Developer ← Employer Bank → Microsoft Contract (REL-ROLE-001, REL-OP-094) | REL-COV-122–153; REL-COMP-S122–153 | One component; no isolated nodes; planned nested roots below 30. |

**Connectivity validation basis:** the complete approved projection contains 237 nodes and 249 relationships, with one weakly connected component and zero isolated elements. Role Context is ledger-only so that context facts without an independent regulatory relationship are preserved without creating a disconnected diagram.

## Role-context coverage

| Context IDs | Operational source(s) | Retained context |
| --- | --- | --- |
| CTX-001–002 | OP-005, OP-007 | Specification and Mainframe dependency / source-system context |
| CTX-003–004 | OP-015–016 | Development-tool context |
| CTX-005–007 | OP-020–022 | Licence and VPN provisioning |
| CTX-008–010 | OP-027–029 | Infrastructure provisioning |
| CTX-011–012 | OP-039–040 | Work allocation and planning |
| CTX-013–016 | OP-043–046 | Decision and requirement intake |
| CTX-017 | OP-051 | Demand context |
| CTX-018 | OP-061, CON-007 | Cross-project visibility limitation |
| CTX-019–020 | OP-062–063 | Recovery-evidence limitations; no missing control inferred |
| CTX-021 | OP-067 | C#/.NET technology context |
| CTX-022 | OP-069 | Management and architect collaboration |
| CTX-023–024 | OP-086–087 | IDE and mandatory-tool context |
| CTX-025 | OP-089 | Wider-team visibility limitation |

**Uncovered register:** empty. The 71 remaining approved source records are represented by COV-001–153; the 26 context records above retain explicit CTX coverage.

## Requirement-family ledger

### ICT Asset Governance

**Approved Step 5 stream:** ICT Systems & Asset Governance  
**Scope containment:** REL-COMP-S001–015; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.II, Section II, Art.7, Paragraph 1, Point a`; `Chap.II, Section II, Art.7, Paragraph 1, Point b`; `Chap.II, Section II, Art.7, Paragraph 1, Point c`; `Chap.II, Section II, Art.7, Paragraph 1, Point d`; `Chap.II, Section II, Art.8, Paragraph 1`; `Chap.II, Section II, Art.8, Paragraph 2`; `Chap.II, Section II, Art.8, Paragraph 3`; `Chap.II, Section II, Art.8, Paragraph 4`; `Chap.II, Section II, Art.8, Paragraph 5`; `Chap.II, Section II, Art.8, Paragraph 6`; `Chap.II, Section II, Art.8, Paragraph 7`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art7-01 — Appropriate ICT systems | COV-001 — Directly performed | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point a` | Framework Maintenance realizes REQ-Art7-01 | REL-COMP-S001 |
| REQ-Art7-02 — Reliable ICT systems | COV-002 — Directly performed | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point b` | Framework Maintenance realizes REQ-Art7-02 | REL-COMP-S002 |
| REQ-Art7-03 — Sufficient processing capacity | COV-003 — Stakeholder-constrained | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point c` | Platform Development is constrained by REQ-Art7-03 | REL-COMP-S003 |
| REQ-Art7-04 — Technological resilience | COV-004 — Stakeholder-constrained | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point d` | Platform Development is constrained by REQ-Art7-04 | REL-COMP-S004 |
| REQ-Art8-01 — Identify and classify functions | COV-005 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` | Platform Development is constrained by REQ-Art8-01 | REL-COMP-S005 |
| REQ-Art8-02 — Document roles and responsibilities | COV-006 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` | Platform Development is constrained by REQ-Art8-02 | REL-COMP-S006 |
| REQ-Art8-03 — Document information and ICT assets | COV-007 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` | Platform Development is constrained by REQ-Art8-03 | REL-COMP-S007 |
| REQ-Art8-04 — Review classification and documentation | COV-008 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` | Service Update is constrained by REQ-Art8-04 | REL-COMP-S008 |
| REQ-Art8-05 — Identify ICT risk sources | COV-009 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 2` | Service Update is constrained by REQ-Art8-05 | REL-COMP-S009 |
| REQ-Art8-06 — Assess threats and risk scenarios | COV-010 — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 2` | Service Update is constrained by REQ-Art8-06 | REL-COMP-S010 |
| REQ-Art8-07 — Assess major ICT changes | COV-011 — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 3` | Enterprise Data Platform is subject to REQ-Art8-07 | REL-COMP-S011 |
| REQ-Art8-08 — Map assets and interdependencies | COV-012 — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 4` | Enterprise Data Platform is subject to REQ-Art8-08 | REL-COMP-S012 |
| REQ-Art8-09 — Document third-party dependencies | COV-013 — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 5` | Enterprise Data Platform is subject to REQ-Art8-09 | REL-COMP-S013 |
| REQ-Art8-10 — Maintain and update inventories | COV-014 — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 6` | Enterprise Data Platform is subject to REQ-Art8-10 | REL-COMP-S014 |
| REQ-Art8-11 — Assess legacy and connected systems | COV-015 — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 7` | Enterprise Data Platform is subject to REQ-Art8-11 | REL-COMP-S015 |

### Protection & Change

**Approved Step 5 stream:** Protection & Controlled Change  
**Scope containment:** REL-COMP-S016–034; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.II, Section II, Art.9, Paragraph 1`; `Chap.II, Section II, Art.9, Paragraph 2`; `Chap.II, Section II, Art.9, Paragraph 3, Point a`; `Chap.II, Section II, Art.9, Paragraph 3, Point b`; `Chap.II, Section II, Art.9, Paragraph 3, Point c`; `Chap.II, Section II, Art.9, Paragraph 3, Point d`; `Chap.II, Section II, Art.9, Paragraph 4, Point a`; `Chap.II, Section II, Art.9, Paragraph 4, Point b`; `Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1`; `Chap.II, Section II, Art.9, Paragraph 4, Point c`; `Chap.II, Section II, Art.9, Paragraph 4, Point d`; `Chap.II, Section II, Art.9, Paragraph 4, Point e`; `Chap.II, Section II, Art.9, Paragraph 4, Point f`; `Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art9-01 — Monitor ICT security and functioning | COV-016 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 1` | Data Offload Flow is constrained by REQ-Art9-01 | REL-COMP-S016 |
| REQ-Art9-02 — Deploy ICT security controls | COV-017 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 1` | Data Offload Flow is constrained by REQ-Art9-02 | REL-COMP-S017 |
| REQ-Art9-03 — Design resilience controls | COV-018 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` | Data Offload Flow is constrained by REQ-Art9-03 | REL-COMP-S018 |
| REQ-Art9-04 — Design continuity controls | COV-019 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` | Data Offload Flow is constrained by REQ-Art9-04 | REL-COMP-S019 |
| REQ-Art9-05 — Design availability controls | COV-020 — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` | Enterprise Data Platform is subject to REQ-Art9-05 | REL-COMP-S020 |
| REQ-Art9-06 — Protect data confidentiality and integrity | COV-021 — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` | Enterprise Data Platform is subject to REQ-Art9-06 | REL-COMP-S021 |
| REQ-Art9-07 — Secure data transfer | COV-022 — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point a` | Enterprise Data Platform is subject to REQ-Art9-07 | REL-COMP-S022 |
| REQ-Art9-08 — Prevent corruption and unauthorised access | COV-023 — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point b` | Azure AD / Internal Service Access realizes part of REQ-Art9-08 | REL-COMP-S023 |
| REQ-Art9-09 — Prevent availability and integrity loss | COV-024 — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point c` | Azure AD / Internal Service Access realizes part of REQ-Art9-09 | REL-COMP-S024 |
| REQ-Art9-10 — Protect data from management risks | COV-025 — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point d` | Azure AD / Internal Service Access realizes part of REQ-Art9-10 | REL-COMP-S025 |
| REQ-Art9-11 — Document information security policy | COV-026 — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point a` | Test and DEV Readiness realizes REQ-Art9-11 | REL-COMP-S026 |
| REQ-Art9-12 — Manage and segment networks | COV-027 — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point b`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1` | Test and DEV Readiness realizes REQ-Art9-12 | REL-COMP-S027 |
| REQ-Art9-13 — Limit logical and physical access | COV-028 — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point c` | Test and DEV Readiness realizes REQ-Art9-13 | REL-COMP-S028 |
| REQ-Art9-14 — Use strong authentication and cryptography | COV-029 — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point d` | Test and DEV Readiness realizes REQ-Art9-14 | REL-COMP-S029 |
| REQ-Art9-15 — Maintain controlled change management | COV-030 — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` | Test and DEV Readiness realizes REQ-Art9-15 | REL-COMP-S030 |
| REQ-Art9-16 — Record changes | COV-031 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` | Service Update is constrained by REQ-Art9-16 | REL-COMP-S031 |
| REQ-Art9-17 — Test and assess changes | COV-032 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` | Service Update is constrained by REQ-Art9-17 | REL-COMP-S032 |
| REQ-Art9-18 — Approve, implement and verify changes | COV-033 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` | Service Update is constrained by REQ-Art9-18 | REL-COMP-S033 |
| REQ-Art9-19 — Document patch and update controls | COV-034 — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point f`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2` | Service Update is constrained by REQ-Art9-19 | REL-COMP-S034 |

### Detection & Continuity

**Approved Step 5 stream:** Detection & Continuity  
**Scope containment:** REL-COMP-S035–073; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.II, Section II, Art.10, Paragraph 1`; `Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1`; `Chap.II, Section II, Art.10, Paragraph 2`; `Chap.II, Section II, Art.10, Paragraph 3`; `Chap.II, Section II, Art.11, Paragraph 1`; `Chap.II, Section II, Art.11, Paragraph 2, Point a`; `Chap.II, Section II, Art.11, Paragraph 2, Point b`; `Chap.II, Section II, Art.11, Paragraph 2, Point c`; `Chap.II, Section II, Art.11, Paragraph 2, Point d`; `Chap.II, Section II, Art.11, Paragraph 2, Point e`; `Chap.II, Section II, Art.11, Paragraph 3`; `Chap.II, Section II, Art.11, Paragraph 4`; `Chap.II, Section II, Art.11, Paragraph 5`; `Chap.II, Section II, Art.11, Paragraph 6, Point a`; `Chap.II, Section II, Art.11, Paragraph 6, Point b`; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1`; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2`; `Chap.II, Section II, Art.11, Paragraph 7`; `Chap.II, Section II, Art.11, Paragraph 8`; `Chap.II, Section II, Art.12, Paragraph 1, Point a`; `Chap.II, Section II, Art.12, Paragraph 1, Point b`; `Chap.II, Section II, Art.12, Paragraph 2`; `Chap.II, Section II, Art.12, Paragraph 3`; `Chap.II, Section II, Art.12, Paragraph 4`; `Chap.II, Section II, Art.12, Paragraph 6`; `Chap.II, Section II, Art.12, Paragraph 7`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art10-01 — Detect anomalies and performance issues | COV-035 — Stakeholder-constrained | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1` | Production Monitoring is constrained by REQ-Art10-01 | REL-COMP-S035 |
| REQ-Art10-02 — Identify material single points of failure | COV-036 — Stakeholder-constrained | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1` | Production Monitoring is constrained by REQ-Art10-02 | REL-COMP-S036 |
| REQ-Art10-03 — Test detection mechanisms | COV-037 — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1` | Incident Escalation realizes part of REQ-Art10-03 | REL-COMP-S037 |
| REQ-Art10-04 — Use control layers and alert thresholds | COV-038 — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 2` | Incident Escalation realizes part of REQ-Art10-04 | REL-COMP-S038 |
| REQ-Art10-05 — Trigger and notify incident responders | COV-039 — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 2` | Incident Escalation realizes part of REQ-Art10-05 | REL-COMP-S039 |
| REQ-Art10-06 — Resource continuous anomaly monitoring | COV-040 — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 3` | Incident Escalation realizes part of REQ-Art10-06 | REL-COMP-S040 |
| REQ-Art11-01 — Maintain ICT business-continuity policy | COV-041 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 1` | Enterprise Data Platform is subject to REQ-Art11-01 | REL-COMP-S041 |
| REQ-Art11-02 — Ensure critical-function continuity | COV-042 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point a` | Enterprise Data Platform is subject to REQ-Art11-02 | REL-COMP-S042 |
| REQ-Art11-03 — Respond to and resolve incidents | COV-043 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point b` | Enterprise Data Platform is subject to REQ-Art11-03 | REL-COMP-S043 |
| REQ-Art11-04 — Activate containment and recovery plans | COV-044 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point c` | Enterprise Data Platform is subject to REQ-Art11-04 | REL-COMP-S044 |
| REQ-Art11-05 — Estimate disruption impacts and losses | COV-045 — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point d` | Software Remediation realizes REQ-Art11-05 | REL-COMP-S045 |
| REQ-Art11-06 — Provide crisis communications and reporting | COV-046 — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point e` | Software Remediation realizes REQ-Art11-06 | REL-COMP-S046 |
| REQ-Art11-07 — Maintain audited response and recovery plans | COV-047 — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 3` | Software Remediation realizes REQ-Art11-07 | REL-COMP-S047 |
| REQ-Art11-08 — Maintain continuity plans | COV-048 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 4` | Incident Escalation is subject to REQ-Art11-08 | REL-COMP-S048 |
| REQ-Art11-09 — Test plans for outsourced critical functions | COV-049 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 4` | Incident Escalation is subject to REQ-Art11-09 | REL-COMP-S049 |
| REQ-Art11-10 — Conduct a business-impact analysis | COV-050 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` | Incident Escalation is subject to REQ-Art11-10 | REL-COMP-S050 |
| REQ-Art11-11 — Assess critical functions | COV-051 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` | Enterprise Data Platform is subject to REQ-Art11-11 | REL-COMP-S051 |
| REQ-Art11-12 — Assess dependencies and information assets | COV-052 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` | Enterprise Data Platform is subject to REQ-Art11-12 | REL-COMP-S052 |
| REQ-Art11-13 — Align ICT assets and redundancy to BIA | COV-053 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` | Enterprise Data Platform is subject to REQ-Art11-13 | REL-COMP-S053 |
| REQ-Art11-14 — Test plans at least annually | COV-054 — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point a` | Platform Development is constrained by REQ-Art11-14 | REL-COMP-S054 |
| REQ-Art11-15 — Test after substantive critical-system change | COV-055 — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point a` | Platform Development is constrained by REQ-Art11-15 | REL-COMP-S055 |
| REQ-Art11-16 — Test crisis communications | COV-056 — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point b` | Platform Development is constrained by REQ-Art11-16 | REL-COMP-S056 |
| REQ-Art11-17 — Test cyberattack and switchover scenarios | COV-057 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1` | Incident Escalation is subject to REQ-Art11-17 | REL-COMP-S057 |
| REQ-Art11-18 — Review plans from testing and assurance | COV-058 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2` | Incident Escalation is subject to REQ-Art11-18 | REL-COMP-S058 |
| REQ-Art11-19 — Operate a crisis-management function | COV-059 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 7` | Incident Escalation is subject to REQ-Art11-19 | REL-COMP-S059 |
| REQ-Art11-20 — Keep disruption-event records | COV-060 — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 8` | Incident Escalation is subject to REQ-Art11-20 | REL-COMP-S060 |
| REQ-Art12-01 — Document backup policy | COV-061 — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point a` | Enterprise Data Platform is subject to REQ-Art12-01 | REL-COMP-S061 |
| REQ-Art12-02 — Set backup scope and frequency | COV-062 — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point a` | Enterprise Data Platform is subject to REQ-Art12-02 | REL-COMP-S062 |
| REQ-Art12-03 — Document restoration and recovery methods | COV-063 — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point b` | Enterprise Data Platform is subject to REQ-Art12-03 | REL-COMP-S063 |
| REQ-Art12-04 — Activate backup systems | COV-064 — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` | Enterprise Data Platform is subject to REQ-Art12-04 | REL-COMP-S064 |
| REQ-Art12-05 — Protect security and data qualities during backup | COV-065 — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` | Infrastructure Remediation realizes part of REQ-Art12-05 | REL-COMP-S065 |
| REQ-Art12-06 — Periodically test backup and restoration | COV-066 — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` | Infrastructure Remediation realizes part of REQ-Art12-06 | REL-COMP-S066 |
| REQ-Art12-07 — Segregate and protect restoration systems | COV-067 — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 3` | Infrastructure Remediation realizes part of REQ-Art12-07 | REL-COMP-S067 |
| REQ-Art12-08 — Restore services in a timely way | COV-068 — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 3` | Infrastructure Remediation realizes part of REQ-Art12-08 | REL-COMP-S068 |
| REQ-Art12-09 — Maintain adequate redundant capacity | COV-069 — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 4` | Platform Development is constrained by REQ-Art12-09 | REL-COMP-S069 |
| REQ-Art12-10 — Set recovery-time objectives | COV-070 — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 6` | Platform Development is constrained by REQ-Art12-10 | REL-COMP-S070 |
| REQ-Art12-11 — Set recovery-point objectives | COV-071 — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 6` | Platform Development is constrained by REQ-Art12-11 | REL-COMP-S071 |
| REQ-Art12-12 — Check and reconcile recovered data | COV-072 — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 7` | Platform Development is constrained by REQ-Art12-12 | REL-COMP-S072 |
| REQ-Art12-13 — Check externally reconstructed data | COV-073 — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 7` | Platform Development is constrained by REQ-Art12-13 | REL-COMP-S073 |

### Incident Learning

**Approved Step 5 stream:** Learning & Incident Management  
**Scope containment:** REL-COMP-S074–101; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.II, Section II, Art.13, Paragraph 1`; `Chap.II, Section II, Art.13, Paragraph 2`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c`; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d`; `Chap.II, Section II, Art.13, Paragraph 3`; `Chap.II, Section II, Art.13, Paragraph 4`; `Chap.II, Section II, Art.13, Paragraph 5`; `Chap.II, Section II, Art.13, Paragraph 6`; `Chap.II, Section II, Art.13, Paragraph 7`; `Chap.III, Art.17, Paragraph 1`; `Chap.III, Art.17, Paragraph 2`; `Chap.III, Art.17, Paragraph 3, Point a`; `Chap.III, Art.17, Paragraph 3, Point b`; `Chap.III, Art.17, Paragraph 3, Point c`; `Chap.III, Art.17, Paragraph 3, Point d`; `Chap.III, Art.17, Paragraph 3, Point e`; `Chap.III, Art.17, Paragraph 3, Point f`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art13-01 — Gather vulnerability information | COV-074 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` | Platform Development is constrained by REQ-Art13-01 | REL-COMP-S074 |
| REQ-Art13-02 — Gather cyber-threat information | COV-075 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` | Platform Development is constrained by REQ-Art13-02 | REL-COMP-S075 |
| REQ-Art13-03 — Gather ICT-incident information | COV-076 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` | Platform Development is constrained by REQ-Art13-03 | REL-COMP-S076 |
| REQ-Art13-04 — Analyse resilience impacts | COV-077 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` | Platform Development is constrained by REQ-Art13-04 | REL-COMP-S077 |
| REQ-Art13-05 — Review disruptive major incidents | COV-078 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2` | Platform Development is constrained by REQ-Art13-05 | REL-COMP-S078 |
| REQ-Art13-06 — Identify causes and ICT improvements | COV-079 — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2` | Incident Escalation realizes part of REQ-Art13-06 | REL-COMP-S079 |
| REQ-Art13-07 — Communicate review changes when requested | COV-080 — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1` | Incident Escalation realizes part of REQ-Art13-07 | REL-COMP-S080 |
| REQ-Art13-08 — Evaluate procedure and action effectiveness | COV-081 — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2` | Incident Escalation realizes part of REQ-Art13-08 | REL-COMP-S081 |
| REQ-Art13-09 — Review response to security alerts | COV-082 — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a` | Incident Escalation realizes part of REQ-Art13-09 | REL-COMP-S082 |
| REQ-Art13-10 — Review forensic-analysis quality | COV-083 — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b` | Incident Escalation realizes part of REQ-Art13-10 | REL-COMP-S083 |
| REQ-Art13-11 — Review incident escalation | COV-084 — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c` | Enterprise Data Platform is subject to REQ-Art13-11 | REL-COMP-S084 |
| REQ-Art13-12 — Review internal and external communications | COV-085 — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d` | Enterprise Data Platform is subject to REQ-Art13-12 | REL-COMP-S085 |
| REQ-Art13-13 — Incorporate lessons in ICT risk assessment | COV-086 — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 3` | Enterprise Data Platform is subject to REQ-Art13-13 | REL-COMP-S086 |
| REQ-Art13-14 — Review ICT risk-management components | COV-087 — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 3` | Enterprise Data Platform is subject to REQ-Art13-14 | REL-COMP-S087 |
| REQ-Art13-15 — Monitor resilience strategy and ICT-risk evolution | COV-088 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 4` | Service Update is constrained by REQ-Art13-15 | REL-COMP-S088 |
| REQ-Art13-16 — Report lessons and recommendations to management | COV-089 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 5` | Service Update is constrained by REQ-Art13-16 | REL-COMP-S089 |
| REQ-Art13-17 — Provide mandatory awareness and resilience training | COV-090 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 6` | Service Update is constrained by REQ-Art13-17 | REL-COMP-S090 |
| REQ-Art13-18 — Monitor relevant technology developments | COV-091 — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 7` | Service Update is constrained by REQ-Art13-18 | REL-COMP-S091 |
| REQ-Art17-01 — Establish an incident-management process | COV-092 — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 1` | Incident Escalation is constrained by REQ-Art17-01 | REL-COMP-S092 |
| REQ-Art17-02 — Record incidents and significant cyber threats | COV-093 — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 2` | Incident Escalation is constrained by REQ-Art17-02 | REL-COMP-S093 |
| REQ-Art17-03 — Integrate monitoring, handling, follow-up and root-cause treatment | COV-094 — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 2` | Incident Escalation is constrained by REQ-Art17-03 | REL-COMP-S094 |
| REQ-Art17-04 — Use early-warning indicators | COV-095 — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point a` | Incident Escalation realizes part of REQ-Art17-04 | REL-COMP-S095 |
| REQ-Art17-05 — Identify, log, categorise and classify incidents | COV-096 — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point b` | Incident Escalation realizes part of REQ-Art17-05 | REL-COMP-S096 |
| REQ-Art17-06 — Assign incident roles and responsibilities | COV-097 — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point c` | Incident Escalation realizes part of REQ-Art17-06 | REL-COMP-S097 |
| REQ-Art17-07 — Plan communications and escalation | COV-098 — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point d` | Incident Escalation realizes part of REQ-Art17-07 | REL-COMP-S098 |
| REQ-Art17-08 — Report major incidents to management | COV-099 — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point e` | Software Remediation realizes REQ-Art17-08 | REL-COMP-S099 |
| REQ-Art17-09 — Mitigate incident impacts | COV-100 — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point f` | Software Remediation realizes REQ-Art17-09 | REL-COMP-S100 |
| REQ-Art17-10 — Restore secure services promptly | COV-101 — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point f` | Software Remediation realizes REQ-Art17-10 | REL-COMP-S101 |

### Resilience Testing

**Approved Step 5 stream:** Resilience Testing  
**Scope containment:** REL-COMP-S102–121; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.IV, Art.24, Paragraph 1`; `Chap.IV, Art.24, Paragraph 2`; `Chap.IV, Art.24, Paragraph 3`; `Chap.IV, Art.24, Paragraph 4`; `Chap.IV, Art.24, Paragraph 5`; `Chap.IV, Art.24, Paragraph 6`; `Chap.IV, Art.25, Paragraph 1`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art24-01 — Establish a resilience-testing programme | COV-102 — Directly performed | Art. 24; `Chap.IV, Art.24, Paragraph 1` | Test and DEV Readiness realizes REQ-Art24-01 | REL-COMP-S102 |
| REQ-Art24-02 — Identify weaknesses and implement corrections | COV-103 — Directly performed | Art. 24; `Chap.IV, Art.24, Paragraph 1` | Test and DEV Readiness realizes REQ-Art24-02 | REL-COMP-S103 |
| REQ-Art24-03 — Maintain and review the programme | COV-104 — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art24-03 | REL-COMP-S104 |
| REQ-Art24-04 — Use a range of tests and methods | COV-105 — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 2` | Test and DEV Readiness is constrained by REQ-Art24-04 | REL-COMP-S105 |
| REQ-Art24-05 — Apply a risk-based testing approach | COV-106 — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 3` | Test and DEV Readiness is constrained by REQ-Art24-05 | REL-COMP-S106 |
| REQ-Art24-06 — Use independent testers and avoid conflicts | COV-107 — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 4` | Pull Request Review is subject to REQ-Art24-06 | REL-COMP-S107 |
| REQ-Art24-07 — Prioritise and remedy test findings | COV-108 — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 5` | Pull Request Review is subject to REQ-Art24-07 | REL-COMP-S108 |
| REQ-Art24-08 — Test critical-function ICT annually | COV-109 — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 6` | Pull Request Review is subject to REQ-Art24-08 | REL-COMP-S109 |
| REQ-Art25-01 — Perform vulnerability assessments and scans | COV-110 — Directly performed | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness realizes REQ-Art25-01 | REL-COMP-S110 |
| REQ-Art25-02 — Perform open-source analyses | COV-111 — Directly performed | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness realizes REQ-Art25-02 | REL-COMP-S111 |
| REQ-Art25-03 — Perform network-security assessments | COV-112 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-03 | REL-COMP-S112 |
| REQ-Art25-04 — Perform gap analyses | COV-113 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-04 | REL-COMP-S113 |
| REQ-Art25-05 — Perform physical-security reviews | COV-114 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-05 | REL-COMP-S114 |
| REQ-Art25-06 — Use questionnaires and scanning tools | COV-115 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-06 | REL-COMP-S115 |
| REQ-Art25-07 — Perform feasible source-code reviews | COV-116 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-07 | REL-COMP-S116 |
| REQ-Art25-08 — Perform scenario-based tests | COV-117 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-08 | REL-COMP-S117 |
| REQ-Art25-09 — Perform compatibility tests | COV-118 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-09 | REL-COMP-S118 |
| REQ-Art25-10 — Perform performance tests | COV-119 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-10 | REL-COMP-S119 |
| REQ-Art25-11 — Perform end-to-end tests | COV-120 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-11 | REL-COMP-S120 |
| REQ-Art25-12 — Perform penetration tests | COV-121 — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` | Test and DEV Readiness is constrained by REQ-Art25-12 | REL-COMP-S121 |

### Microsoft Cloud Risk

**Approved Step 5 stream:** Microsoft Cloud Third-Party Risk  
**Scope containment:** REL-COMP-S122–153; each is an approved semantic Composition from this family to the corresponding child below and will be visually nested.  
**Parent legal-ID roll-up (ordered, deduplicated):** `Chap.V, Section I, Art.28, Paragraph 1`; `Chap.V, Section I, Art.28, Paragraph 1, Point a`; `Chap.V, Section I, Art.28, Paragraph 1, Point b`; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point i`; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point ii`; `Chap.V, Section I, Art.28, Paragraph 2`; `Chap.V, Section I, Art.28, Paragraph 3`; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 1`; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 2`; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 3`; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 4`; `Chap.V, Section I, Art.28, Paragraph 4, Point a`; `Chap.V, Section I, Art.28, Paragraph 4, Point b`; `Chap.V, Section I, Art.28, Paragraph 4, Point c`; `Chap.V, Section I, Art.28, Paragraph 4, Point d`; `Chap.V, Section I, Art.28, Paragraph 4, Point e`; `Chap.V, Section I, Art.28, Paragraph 5`; `Chap.V, Section I, Art.28, Paragraph 6`; `Chap.V, Section I, Art.28, Paragraph 6, Sub-Paragraph 1`; `Chap.V, Section I, Art.28, Paragraph 7`; `Chap.V, Section I, Art.28, Paragraph 7, Point a`; `Chap.V, Section I, Art.28, Paragraph 7, Point b`; `Chap.V, Section I, Art.28, Paragraph 7, Point c`; `Chap.V, Section I, Art.28, Paragraph 7, Point d`; `Chap.V, Section I, Art.28, Paragraph 8`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point a`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point b`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point c`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 2`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 3`; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 4`

| Child requirement | Coverage / ownership | Citation and unchanged direct legal-text ID(s) | Approved endpoint/effect | Composition |
| --- | --- | --- | --- | --- |
| REQ-Art28-01 — Manage ICT third-party risk within ICT risk management | COV-122 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1` | Microsoft Contract is subject to REQ-Art28-01 | REL-COMP-S122 |
| REQ-Art28-02 — Retain responsibility for DORA compliance | COV-123 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point a` | Microsoft Contract is subject to REQ-Art28-02 | REL-COMP-S123 |
| REQ-Art28-03 — Apply proportional third-party risk management | COV-124 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b` | Microsoft Contract is subject to REQ-Art28-03 | REL-COMP-S124 |
| REQ-Art28-04 — Assess ICT-related dependencies | COV-125 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point i` | Microsoft Contract is subject to REQ-Art28-04 | REL-COMP-S125 |
| REQ-Art28-05 — Assess contractual critical-function risk | COV-126 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point ii` | Microsoft Contract is subject to REQ-Art28-05 | REL-COMP-S126 |
| REQ-Art28-06 — Maintain third-party risk strategy and policy | COV-127 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 2` | Microsoft Contract is subject to REQ-Art28-06 | REL-COMP-S127 |
| REQ-Art28-07 — Have management review third-party risks | COV-128 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 2` | Microsoft Contract is subject to REQ-Art28-07 | REL-COMP-S128 |
| REQ-Art28-08 — Maintain a third-party contract register | COV-129 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3` | Microsoft Contract is subject to REQ-Art28-08 | REL-COMP-S129 |
| REQ-Art28-09 — Document and classify contractual arrangements | COV-130 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 1` | Microsoft Contract is subject to REQ-Art28-09 | REL-COMP-S130 |
| REQ-Art28-10 — Report annual arrangement information | COV-131 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 2` | Microsoft Contract is subject to REQ-Art28-10 | REL-COMP-S131 |
| REQ-Art28-11 — Provide the register to competent authorities | COV-132 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 3` | Microsoft Contract is subject to REQ-Art28-11 | REL-COMP-S132 |
| REQ-Art28-12 — Notify planned critical arrangements | COV-133 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 4` | Microsoft Contract is subject to REQ-Art28-12 | REL-COMP-S133 |
| REQ-Art28-13 — Assess whether a service supports a critical function | COV-134 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point a` | Microsoft Contract is subject to REQ-Art28-13 | REL-COMP-S134 |
| REQ-Art28-14 — Assess supervisory contracting conditions | COV-135 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point b` | Microsoft Contract is subject to REQ-Art28-14 | REL-COMP-S135 |
| REQ-Art28-15 — Assess contractual and concentration risks | COV-136 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point c` | Microsoft Contract is subject to REQ-Art28-15 | REL-COMP-S136 |
| REQ-Art28-16 — Perform provider due diligence | COV-137 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point d` | Microsoft Contract is subject to REQ-Art28-16 | REL-COMP-S137 |
| REQ-Art28-17 — Assess contractual conflicts of interest | COV-138 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point e` | Microsoft Contract is subject to REQ-Art28-17 | REL-COMP-S138 |
| REQ-Art28-18 — Use providers meeting security standards | COV-139 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 5` | Microsoft Contract is subject to REQ-Art28-18 | REL-COMP-S139 |
| REQ-Art28-19 — Plan risk-based provider audits | COV-140 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 6` | Microsoft Contract is subject to REQ-Art28-19 | REL-COMP-S140 |
| REQ-Art28-20 — Use suitably skilled auditors | COV-141 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 6, Sub-Paragraph 1` | Microsoft Contract is subject to REQ-Art28-20 | REL-COMP-S141 |
| REQ-Art28-21 — Provide contractual termination rights | COV-142 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7` | Microsoft Contract is subject to REQ-Art28-21 | REL-COMP-S142 |
| REQ-Art28-22 — Terminate for significant breach | COV-143 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point a` | Microsoft Contract is subject to REQ-Art28-22 | REL-COMP-S143 |
| REQ-Art28-23 — Terminate for material risk changes | COV-144 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point b` | Microsoft Contract is subject to REQ-Art28-23 | REL-COMP-S144 |
| REQ-Art28-24 — Terminate for provider ICT-risk weaknesses | COV-145 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point c` | Microsoft Contract is subject to REQ-Art28-24 | REL-COMP-S145 |
| REQ-Art28-25 — Terminate where supervision is impaired | COV-146 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point d` | Microsoft Contract is subject to REQ-Art28-25 | REL-COMP-S146 |
| REQ-Art28-26 — Maintain critical-function exit strategies | COV-147 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8` | Microsoft Contract is subject to REQ-Art28-26 | REL-COMP-S147 |
| REQ-Art28-27 — Exit without business disruption | COV-148 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point a` | Microsoft Contract is subject to REQ-Art28-27 | REL-COMP-S148 |
| REQ-Art28-28 — Exit without limiting regulatory compliance | COV-149 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point b` | Microsoft Contract is subject to REQ-Art28-28 | REL-COMP-S149 |
| REQ-Art28-29 — Exit without harming client-service continuity | COV-150 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point c` | Microsoft Contract is subject to REQ-Art28-29 | REL-COMP-S150 |
| REQ-Art28-30 — Document, test and review exit plans | COV-151 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 2` | Microsoft Contract is subject to REQ-Art28-30 | REL-COMP-S151 |
| REQ-Art28-31 — Prepare alternative solutions and transition plans | COV-152 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 3` | Microsoft Contract is subject to REQ-Art28-31 | REL-COMP-S152 |
| REQ-Art28-32 — Maintain exit contingency measures | COV-153 — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 4` | Microsoft Contract is subject to REQ-Art28-32 | REL-COMP-S153 |

## Validation record

- Gate 6.1 — Confirm Scope Boundary: approved by the operator.
- Gate 6.2 — Confirm Inclusions & Streams: approved by the operator.
- Connectivity clarification — REL-OP-090–094 approved by the operator and appended to the Step 5 evidence record.
- Relationship-type correction — operator-approved external coverage associations are retained as external support, never stakeholder realization.
- Gate 6.3 — Confirm Connectivity & Splits: approved by the operator.
- The document preserves all 153 approved coverage requirements and their direct legal-text anchors unchanged.
