# ArchiMate Viewpoint Definition: DORA Back-end Delivery

| Viewpoint Attribute | Definition |
| --- | --- |
| **Viewpoint Name** | DORA Back-end Delivery |
| **Target Stakeholders** | Back-end Developer; architecture, risk, and delivery reviewers. |
| **Purpose** | Designing — make approved DORA constraints, ownership, and operational relationships usable in view generation without asserting enterprise compliance. |
| **Primary Concerns** | [Governance] Microsoft provider-contract risk; [Administrative] change, testing, and incident interfaces; [Technical] platform, monitoring, continuity, recovery, and remediation constraints. |
| **Allowed Concepts** | Requirement; Business Role; Business Actor; Business Process; Application Process; Business Event; Business Object; Application Component; Contract. |
| **Allowed Relations** | Composition; Assignment; Association; Serving; Triggering; Access; Realization only where coverage ownership is Directly performed. |
| **Visual Rules** | Nest each child Requirement inside its named Requirement family; its Composition is semantic-only when that nesting is rendered. Show all approved non-composition edges. Preserve source IDs, DORA citations, direct legal-text IDs, ownership, and canonical ledger endpoint names in documentation only. |

## Formal view graph

| View | Requirement families | Exact relationship membership | Stakeholder path | Validation |
| --- | --- | --- | --- | --- |
| ICT Asset Governance | ICT Asset Controls (COV-001–015) | REL-COV-001–015; REL-COMP-S001–015; REL-OP-001, REL-OP-066, REL-OP-090, REL-OP-091, REL-OP-093 | Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. | 1 component; 0 isolated; 7 roots; no warning |
| Protection and Change | Data Protection (COV-016–025); Change Controls (COV-026–034) | REL-COV-016–034; REL-COMP-S016–034; REL-OP-002, REL-OP-010, REL-OP-014, REL-OP-066, REL-OP-092, REL-OP-093 | Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. | 1 component; 0 isolated; 9 roots; no warning |
| Detection and Continuity | ICT Detection (COV-035–040); Continuity Response (COV-041–050); Continuity Testing (COV-051–060); Backup and Recovery (COV-061–073) | REL-COV-035–073; REL-COMP-S035–073; REL-OP-001, REL-OP-031, REL-OP-032, REL-OP-079, REL-OP-080, REL-OP-081, REL-OP-082, REL-OP-083, REL-OP-084, REL-OP-085, REL-OP-086, REL-OP-087, REL-OP-088, REL-OP-089, REL-OP-093 | Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. | 1 component; 0 isolated; 19 roots; no warning |
| Incident Learning | ICT Learning (COV-074–091); Incident Management (COV-092–101) | REL-COV-074–101; REL-COMP-S074–101; REL-OP-031, REL-OP-032, REL-OP-066, REL-OP-079, REL-OP-080, REL-OP-081, REL-OP-083, REL-OP-085, REL-OP-089, REL-OP-093 | Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. | 1 component; 0 isolated; 14 roots; no warning |
| Resilience Testing | Resilience Tests (COV-102–109); Test Method Controls (COV-110–121) | REL-COV-102–121; REL-COMP-S102–121; REL-OP-014, REL-OP-016, REL-OP-017, REL-OP-018, REL-OP-019 | Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. | 1 component; 0 isolated; 8 roots; no warning |
| Microsoft Cloud Risk | Provider Risk Controls (COV-122–138); Provider Exit Controls (COV-139–153) | REL-COV-122–153; REL-COMP-S122–153; REL-OP-094, REL-ROLE-001 | Back-end Developer <- Employer Bank -> Microsoft Contract | 1 component; 0 isolated; 5 roots; no warning |

## Requirement-family ledger

| Parent Requirement | View | Nested child count | Child direct legal-text ID roll-up | Containment |
| --- | --- | --- | --- | --- |
| ICT Asset Controls | ICT Asset Governance | 15 | `Chap.II, Section II, Art.7, Paragraph 1, Point a`<br>`Chap.II, Section II, Art.7, Paragraph 1, Point b`<br>`Chap.II, Section II, Art.7, Paragraph 1, Point c`<br>`Chap.II, Section II, Art.7, Paragraph 1, Point d`<br>`Chap.II, Section II, Art.8, Paragraph 1`<br>`Chap.II, Section II, Art.8, Paragraph 2`<br>`Chap.II, Section II, Art.8, Paragraph 3`<br>`Chap.II, Section II, Art.8, Paragraph 4`<br>`Chap.II, Section II, Art.8, Paragraph 5`<br>`Chap.II, Section II, Art.8, Paragraph 6`<br>`Chap.II, Section II, Art.8, Paragraph 7` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Data Protection | Protection and Change | 10 | `Chap.II, Section II, Art.9, Paragraph 1`<br>`Chap.II, Section II, Art.9, Paragraph 2`<br>`Chap.II, Section II, Art.9, Paragraph 3, Point a`<br>`Chap.II, Section II, Art.9, Paragraph 3, Point b`<br>`Chap.II, Section II, Art.9, Paragraph 3, Point c`<br>`Chap.II, Section II, Art.9, Paragraph 3, Point d` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Change Controls | Protection and Change | 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point a`<br>`Chap.II, Section II, Art.9, Paragraph 4, Point b`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1`<br>`Chap.II, Section II, Art.9, Paragraph 4, Point c`<br>`Chap.II, Section II, Art.9, Paragraph 4, Point d`<br>`Chap.II, Section II, Art.9, Paragraph 4, Point e`<br>`Chap.II, Section II, Art.9, Paragraph 4, Point f`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2` | Semantic Composition; matching visual nesting; no internal canvas line. |
| ICT Detection | Detection and Continuity | 6 | `Chap.II, Section II, Art.10, Paragraph 1`<br>`Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1`<br>`Chap.II, Section II, Art.10, Paragraph 2`<br>`Chap.II, Section II, Art.10, Paragraph 3` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Continuity Response | Detection and Continuity | 10 | `Chap.II, Section II, Art.11, Paragraph 1`<br>`Chap.II, Section II, Art.11, Paragraph 2, Point a`<br>`Chap.II, Section II, Art.11, Paragraph 2, Point b`<br>`Chap.II, Section II, Art.11, Paragraph 2, Point c`<br>`Chap.II, Section II, Art.11, Paragraph 2, Point d`<br>`Chap.II, Section II, Art.11, Paragraph 2, Point e`<br>`Chap.II, Section II, Art.11, Paragraph 3`<br>`Chap.II, Section II, Art.11, Paragraph 4`<br>`Chap.II, Section II, Art.11, Paragraph 5` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Continuity Testing | Detection and Continuity | 10 | `Chap.II, Section II, Art.11, Paragraph 5`<br>`Chap.II, Section II, Art.11, Paragraph 6, Point a`<br>`Chap.II, Section II, Art.11, Paragraph 6, Point b`<br>`Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1`<br>`Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2`<br>`Chap.II, Section II, Art.11, Paragraph 7`<br>`Chap.II, Section II, Art.11, Paragraph 8` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Backup and Recovery | Detection and Continuity | 13 | `Chap.II, Section II, Art.12, Paragraph 1, Point a`<br>`Chap.II, Section II, Art.12, Paragraph 1, Point b`<br>`Chap.II, Section II, Art.12, Paragraph 2`<br>`Chap.II, Section II, Art.12, Paragraph 3`<br>`Chap.II, Section II, Art.12, Paragraph 4`<br>`Chap.II, Section II, Art.12, Paragraph 6`<br>`Chap.II, Section II, Art.12, Paragraph 7` | Semantic Composition; matching visual nesting; no internal canvas line. |
| ICT Learning | Incident Learning | 18 | `Chap.II, Section II, Art.13, Paragraph 1`<br>`Chap.II, Section II, Art.13, Paragraph 2`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c`<br>`Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d`<br>`Chap.II, Section II, Art.13, Paragraph 3`<br>`Chap.II, Section II, Art.13, Paragraph 4`<br>`Chap.II, Section II, Art.13, Paragraph 5`<br>`Chap.II, Section II, Art.13, Paragraph 6`<br>`Chap.II, Section II, Art.13, Paragraph 7` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Incident Management | Incident Learning | 10 | `Chap.III, Art.17, Paragraph 1`<br>`Chap.III, Art.17, Paragraph 2`<br>`Chap.III, Art.17, Paragraph 3, Point a`<br>`Chap.III, Art.17, Paragraph 3, Point b`<br>`Chap.III, Art.17, Paragraph 3, Point c`<br>`Chap.III, Art.17, Paragraph 3, Point d`<br>`Chap.III, Art.17, Paragraph 3, Point e`<br>`Chap.III, Art.17, Paragraph 3, Point f` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Resilience Tests | Resilience Testing | 8 | `Chap.IV, Art.24, Paragraph 1`<br>`Chap.IV, Art.24, Paragraph 2`<br>`Chap.IV, Art.24, Paragraph 3`<br>`Chap.IV, Art.24, Paragraph 4`<br>`Chap.IV, Art.24, Paragraph 5`<br>`Chap.IV, Art.24, Paragraph 6` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Test Method Controls | Resilience Testing | 12 | `Chap.IV, Art.25, Paragraph 1` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Provider Risk Controls | Microsoft Cloud Risk | 17 | `Chap.V, Section I, Art.28, Paragraph 1`<br>`Chap.V, Section I, Art.28, Paragraph 1, Point a`<br>`Chap.V, Section I, Art.28, Paragraph 1, Point b`<br>`Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point i`<br>`Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point ii`<br>`Chap.V, Section I, Art.28, Paragraph 2`<br>`Chap.V, Section I, Art.28, Paragraph 3`<br>`Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 1`<br>`Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 2`<br>`Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 3`<br>`Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 4`<br>`Chap.V, Section I, Art.28, Paragraph 4, Point a`<br>`Chap.V, Section I, Art.28, Paragraph 4, Point b`<br>`Chap.V, Section I, Art.28, Paragraph 4, Point c`<br>`Chap.V, Section I, Art.28, Paragraph 4, Point d`<br>`Chap.V, Section I, Art.28, Paragraph 4, Point e` | Semantic Composition; matching visual nesting; no internal canvas line. |
| Provider Exit Controls | Microsoft Cloud Risk | 15 | `Chap.V, Section I, Art.28, Paragraph 5`<br>`Chap.V, Section I, Art.28, Paragraph 6`<br>`Chap.V, Section I, Art.28, Paragraph 6, Sub-Paragraph 1`<br>`Chap.V, Section I, Art.28, Paragraph 7`<br>`Chap.V, Section I, Art.28, Paragraph 7, Point a`<br>`Chap.V, Section I, Art.28, Paragraph 7, Point b`<br>`Chap.V, Section I, Art.28, Paragraph 7, Point c`<br>`Chap.V, Section I, Art.28, Paragraph 7, Point d`<br>`Chap.V, Section I, Art.28, Paragraph 8`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point a`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point b`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point c`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 2`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 3`<br>`Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 4` | Semantic Composition; matching visual nesting; no internal canvas line. |

## Child requirement catalog

Visible titles below are clean labels only. The source requirement ID, full atomic duty, coverage ownership, DORA citation, and verified direct legal-text IDs are documentation fields, not visual node labels.

| Requirement documentation ID | Visible title | Full atomic duty | Coverage / ownership | Citation and verified direct legal-text IDs |
| --- | --- | --- | --- | --- |
| `REQ-Art7-01` | Appropriate ICT systems | Appropriate ICT systems | `COV-001` — Directly performed | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point a` |
| `REQ-Art7-02` | Reliable ICT systems | Reliable ICT systems | `COV-002` — Directly performed | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point b` |
| `REQ-Art7-03` | Processing Capacity | Sufficient processing capacity | `COV-003` — Stakeholder-constrained | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point c` |
| `REQ-Art7-04` | Technological resilience | Technological resilience | `COV-004` — Stakeholder-constrained | Art. 7; `Chap.II, Section II, Art.7, Paragraph 1, Point d` |
| `REQ-Art8-01` | Function Classification | Identify and classify functions | `COV-005` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` |
| `REQ-Art8-02` | Role Documentation | Document roles and responsibilities | `COV-006` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` |
| `REQ-Art8-03` | ICT Asset Documentation | Document information and ICT assets | `COV-007` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` |
| `REQ-Art8-04` | Classification Review | Review classification and documentation | `COV-008` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 1` |
| `REQ-Art8-05` | Identify ICT risk sources | Identify ICT risk sources | `COV-009` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 2` |
| `REQ-Art8-06` | Threat Assessment | Assess threats and risk scenarios | `COV-010` — Stakeholder-constrained | Art. 8; `Chap.II, Section II, Art.8, Paragraph 2` |
| `REQ-Art8-07` | Assess major ICT changes | Assess major ICT changes | `COV-011` — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 3` |
| `REQ-Art8-08` | Asset Dependency Mapping | Map assets and interdependencies | `COV-012` — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 4` |
| `REQ-Art8-09` | Provider Dependencies | Document third-party dependencies | `COV-013` — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 5` |
| `REQ-Art8-10` | Inventory Maintenance | Maintain and update inventories | `COV-014` — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 6` |
| `REQ-Art8-11` | Legacy System Assessment | Assess legacy and connected systems | `COV-015` — Not evidenced / unclear owner | Art. 8; `Chap.II, Section II, Art.8, Paragraph 7` |
| `REQ-Art9-01` | ICT Security Monitoring | Monitor ICT security and functioning | `COV-016` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 1` |
| `REQ-Art9-02` | ICT Security Controls | Deploy ICT security controls | `COV-017` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 1` |
| `REQ-Art9-03` | Resilience Controls | Design resilience controls | `COV-018` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` |
| `REQ-Art9-04` | Continuity Controls | Design continuity controls | `COV-019` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` |
| `REQ-Art9-05` | Uptime Controls | Design availability controls | `COV-020` — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` |
| `REQ-Art9-06` | Data Integrity Protection | Protect data confidentiality and integrity | `COV-021` — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 2` |
| `REQ-Art9-07` | Secure data transfer | Secure data transfer | `COV-022` — Not evidenced / unclear owner | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point a` |
| `REQ-Art9-08` | Access Corruption Control | Prevent corruption and unauthorised access | `COV-023` — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point b` |
| `REQ-Art9-09` | Uptime Integrity Control | Prevent availability and integrity loss | `COV-024` — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point c` |
| `REQ-Art9-10` | Data Management Risks | Protect data from management risks | `COV-025` — Externally owned | Art. 9; `Chap.II, Section II, Art.9, Paragraph 3, Point d` |
| `REQ-Art9-11` | Security Policy Record | Document information security policy | `COV-026` — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point a` |
| `REQ-Art9-12` | Network Segmentation | Manage and segment networks | `COV-027` — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point b`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1` |
| `REQ-Art9-13` | Access Limitation | Limit logical and physical access | `COV-028` — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point c` |
| `REQ-Art9-14` | Strong Auth and Crypto | Use strong authentication and cryptography | `COV-029` — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point d` |
| `REQ-Art9-15` | Change Control | Maintain controlled change management | `COV-030` — Directly performed | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| `REQ-Art9-16` | Record changes | Record changes | `COV-031` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| `REQ-Art9-17` | Test and assess changes | Test and assess changes | `COV-032` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| `REQ-Art9-18` | Change Verification | Approve, implement and verify changes | `COV-033` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| `REQ-Art9-19` | Patch Update Controls | Document patch and update controls | `COV-034` — Stakeholder-constrained | Art. 9; `Chap.II, Section II, Art.9, Paragraph 4, Point f`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2` |
| `REQ-Art10-01` | Anomaly Detection | Detect anomalies and performance issues | `COV-035` — Stakeholder-constrained | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1` |
| `REQ-Art10-02` | Single Failure Points | Identify material single points of failure | `COV-036` — Stakeholder-constrained | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1` |
| `REQ-Art10-03` | Test detection mechanisms | Test detection mechanisms | `COV-037` — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1` |
| `REQ-Art10-04` | Control Alert Thresholds | Use control layers and alert thresholds | `COV-038` — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 2` |
| `REQ-Art10-05` | Incident Responder Alerts | Trigger and notify incident responders | `COV-039` — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 2` |
| `REQ-Art10-06` | Anomaly Monitoring | Resource continuous anomaly monitoring | `COV-040` — Externally owned | Art. 10; `Chap.II, Section II, Art.10, Paragraph 3` |
| `REQ-Art11-01` | ICT Continuity Policy | Maintain ICT business-continuity policy | `COV-041` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 1` |
| `REQ-Art11-02` | Critical Continuity | Ensure critical-function continuity | `COV-042` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point a` |
| `REQ-Art11-03` | Incident Resolution | Respond to and resolve incidents | `COV-043` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point b` |
| `REQ-Art11-04` | Containment Plans | Activate containment and recovery plans | `COV-044` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point c` |
| `REQ-Art11-05` | Disruption Estimates | Estimate disruption impacts and losses | `COV-045` — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point d` |
| `REQ-Art11-06` | Crisis Reporting | Provide crisis communications and reporting | `COV-046` — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 2, Point e` |
| `REQ-Art11-07` | Audited Recovery Plans | Maintain audited response and recovery plans | `COV-047` — Directly performed | Art. 11; `Chap.II, Section II, Art.11, Paragraph 3` |
| `REQ-Art11-08` | Maintain continuity plans | Maintain continuity plans | `COV-048` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 4` |
| `REQ-Art11-09` | Outsourced Function Tests | Test plans for outsourced critical functions | `COV-049` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 4` |
| `REQ-Art11-10` | Business Impact Analysis | Conduct a business-impact analysis | `COV-050` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` |
| `REQ-Art11-11` | Assess critical functions | Assess critical functions | `COV-051` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` |
| `REQ-Art11-12` | Dependency Assessment | Assess dependencies and information assets | `COV-052` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` |
| `REQ-Art11-13` | BIA Asset Redundancy | Align ICT assets and redundancy to BIA | `COV-053` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 5` |
| `REQ-Art11-14` | Annual Plan Tests | Test plans at least annually | `COV-054` — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point a` |
| `REQ-Art11-15` | Critical Change Tests | Test after substantive critical-system change | `COV-055` — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point a` |
| `REQ-Art11-16` | Crisis Comms Tests | Test crisis communications | `COV-056` — Stakeholder-constrained | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Point b` |
| `REQ-Art11-17` | Cyberattack Tests | Test cyberattack and switchover scenarios | `COV-057` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1` |
| `REQ-Art11-18` | Plan Assurance Review | Review plans from testing and assurance | `COV-058` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2` |
| `REQ-Art11-19` | Crisis Control Operation | Operate a crisis-management function | `COV-059` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 7` |
| `REQ-Art11-20` | Disruption Event Records | Keep disruption-event records | `COV-060` — Not evidenced / unclear owner | Art. 11; `Chap.II, Section II, Art.11, Paragraph 8` |
| `REQ-Art12-01` | Document backup policy | Document backup policy | `COV-061` — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point a` |
| `REQ-Art12-02` | Backup Scope Frequency | Set backup scope and frequency | `COV-062` — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point a` |
| `REQ-Art12-03` | Recovery Method Records | Document restoration and recovery methods | `COV-063` — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 1, Point b` |
| `REQ-Art12-04` | Activate backup systems | Activate backup systems | `COV-064` — Not evidenced / unclear owner | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` |
| `REQ-Art12-05` | Backup Data Protection | Protect security and data qualities during backup | `COV-065` — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` |
| `REQ-Art12-06` | Backup Restoration Tests | Periodically test backup and restoration | `COV-066` — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 2` |
| `REQ-Art12-07` | Restoration Protection | Segregate and protect restoration systems | `COV-067` — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 3` |
| `REQ-Art12-08` | Timely Service Recovery | Restore services in a timely way | `COV-068` — Externally owned | Art. 12; `Chap.II, Section II, Art.12, Paragraph 3` |
| `REQ-Art12-09` | Redundant Capacity | Maintain adequate redundant capacity | `COV-069` — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 4` |
| `REQ-Art12-10` | Recovery Time Objective | Set recovery-time objectives | `COV-070` — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 6` |
| `REQ-Art12-11` | Recovery Point Objective | Set recovery-point objectives | `COV-071` — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 6` |
| `REQ-Art12-12` | Recovered Data Reconcile | Check and reconcile recovered data | `COV-072` — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 7` |
| `REQ-Art12-13` | Rebuilt Data Check | Check externally reconstructed data | `COV-073` — Stakeholder-constrained | Art. 12; `Chap.II, Section II, Art.12, Paragraph 7` |
| `REQ-Art13-01` | Vulnerability Information | Gather vulnerability information | `COV-074` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` |
| `REQ-Art13-02` | Cyber Threat Information | Gather cyber-threat information | `COV-075` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` |
| `REQ-Art13-03` | ICT Incident Information | Gather ICT-incident information | `COV-076` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` |
| `REQ-Art13-04` | Resilience Impact Review | Analyse resilience impacts | `COV-077` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 1` |
| `REQ-Art13-05` | Major Incident Review | Review disruptive major incidents | `COV-078` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2` |
| `REQ-Art13-06` | ICT Cause Improvements | Identify causes and ICT improvements | `COV-079` — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2` |
| `REQ-Art13-07` | Review Communications | Communicate review changes when requested | `COV-080` — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1` |
| `REQ-Art13-08` | Procedure Effectiveness | Evaluate procedure and action effectiveness | `COV-081` — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2` |
| `REQ-Art13-09` | Security Alert Review | Review response to security alerts | `COV-082` — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a` |
| `REQ-Art13-10` | Forensic Quality Review | Review forensic-analysis quality | `COV-083` — Externally owned | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b` |
| `REQ-Art13-11` | Escalation Review | Review incident escalation | `COV-084` — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c` |
| `REQ-Art13-12` | Communication Review | Review internal and external communications | `COV-085` — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d` |
| `REQ-Art13-13` | ICT Risk Lessons | Incorporate lessons in ICT risk assessment | `COV-086` — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 3` |
| `REQ-Art13-14` | ICT Risk Component Review | Review ICT risk-management components | `COV-087` — Not evidenced / unclear owner | Art. 13; `Chap.II, Section II, Art.13, Paragraph 3` |
| `REQ-Art13-15` | Resilience Strategy Watch | Monitor resilience strategy and ICT-risk evolution | `COV-088` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 4` |
| `REQ-Art13-16` | Lessons Reporting | Report lessons and recommendations to management | `COV-089` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 5` |
| `REQ-Art13-17` | Resilience Training | Provide mandatory awareness and resilience training | `COV-090` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 6` |
| `REQ-Art13-18` | Technology Monitoring | Monitor relevant technology developments | `COV-091` — Stakeholder-constrained | Art. 13; `Chap.II, Section II, Art.13, Paragraph 7` |
| `REQ-Art17-01` | Incident Process | Establish an incident-management process | `COV-092` — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 1` |
| `REQ-Art17-02` | Incident Threat Records | Record incidents and significant cyber threats | `COV-093` — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 2` |
| `REQ-Art17-03` | Monitoring Integration | Integrate monitoring, handling, follow-up and root-cause treatment | `COV-094` — Stakeholder-constrained | Art. 17; `Chap.III, Art.17, Paragraph 2` |
| `REQ-Art17-04` | Early Warning Indicators | Use early-warning indicators | `COV-095` — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point a` |
| `REQ-Art17-05` | Incident Classification | Identify, log, categorise and classify incidents | `COV-096` — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point b` |
| `REQ-Art17-06` | Incident Role Assignment | Assign incident roles and responsibilities | `COV-097` — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point c` |
| `REQ-Art17-07` | Communication Escalation | Plan communications and escalation | `COV-098` — Externally owned | Art. 17; `Chap.III, Art.17, Paragraph 3, Point d` |
| `REQ-Art17-08` | Major Incident Reporting | Report major incidents to management | `COV-099` — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point e` |
| `REQ-Art17-09` | Mitigate incident impacts | Mitigate incident impacts | `COV-100` — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point f` |
| `REQ-Art17-10` | Secure Service Recovery | Restore secure services promptly | `COV-101` — Directly performed | Art. 17; `Chap.III, Art.17, Paragraph 3, Point f` |
| `REQ-Art24-01` | Resilience Test Programme | Establish a resilience-testing programme | `COV-102` — Directly performed | Art. 24; `Chap.IV, Art.24, Paragraph 1` |
| `REQ-Art24-02` | Weakness Corrections | Identify weaknesses and implement corrections | `COV-103` — Directly performed | Art. 24; `Chap.IV, Art.24, Paragraph 1` |
| `REQ-Art24-03` | Programme Review | Maintain and review the programme | `COV-104` — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 1` |
| `REQ-Art24-04` | Test Method Range | Use a range of tests and methods | `COV-105` — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 2` |
| `REQ-Art24-05` | Risk Based Testing | Apply a risk-based testing approach | `COV-106` — Stakeholder-constrained | Art. 24; `Chap.IV, Art.24, Paragraph 3` |
| `REQ-Art24-06` | Independent Testing | Use independent testers and avoid conflicts | `COV-107` — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 4` |
| `REQ-Art24-07` | Test Finding Remediation | Prioritise and remedy test findings | `COV-108` — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 5` |
| `REQ-Art24-08` | Annual Critical Tests | Test critical-function ICT annually | `COV-109` — Not evidenced / unclear owner | Art. 24; `Chap.IV, Art.24, Paragraph 6` |
| `REQ-Art25-01` | Vulnerability Scans | Perform vulnerability assessments and scans | `COV-110` — Directly performed | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-02` | Open Source Analysis | Perform open-source analyses | `COV-111` — Directly performed | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-03` | Network Security Review | Perform network-security assessments | `COV-112` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-04` | Perform gap analyses | Perform gap analyses | `COV-113` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-05` | Physical Security Review | Perform physical-security reviews | `COV-114` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-06` | Scanning Questionnaires | Use questionnaires and scanning tools | `COV-115` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-07` | Source Code Review | Perform feasible source-code reviews | `COV-116` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-08` | Scenario Tests | Perform scenario-based tests | `COV-117` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-09` | Compatibility Tests | Perform compatibility tests | `COV-118` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-10` | Perform performance tests | Perform performance tests | `COV-119` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-11` | Perform end-to-end tests | Perform end-to-end tests | `COV-120` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art25-12` | Perform penetration tests | Perform penetration tests | `COV-121` — Stakeholder-constrained | Art. 25; `Chap.IV, Art.25, Paragraph 1` |
| `REQ-Art28-01` | ICT Provider Risk Control | Manage ICT third-party risk within ICT risk management | `COV-122` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1` |
| `REQ-Art28-02` | DORA Compliance Duty | Retain responsibility for DORA compliance | `COV-123` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point a` |
| `REQ-Art28-03` | Provider Risk Control | Apply proportional third-party risk management | `COV-124` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b` |
| `REQ-Art28-04` | ICT Dependency Assessment | Assess ICT-related dependencies | `COV-125` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point i` |
| `REQ-Art28-05` | Critical Contract Risk | Assess contractual critical-function risk | `COV-126` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point ii` |
| `REQ-Art28-06` | Provider Risk Policy | Maintain third-party risk strategy and policy | `COV-127` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 2` |
| `REQ-Art28-07` | Provider Risk Review | Have management review third-party risks | `COV-128` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 2` |
| `REQ-Art28-08` | Contract Register | Maintain a third-party contract register | `COV-129` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3` |
| `REQ-Art28-09` | Contract Records | Document and classify contractual arrangements | `COV-130` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 1` |
| `REQ-Art28-10` | Annual Arrangement Report | Report annual arrangement information | `COV-131` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 2` |
| `REQ-Art28-11` | Authority Register Access | Provide the register to competent authorities | `COV-132` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 3` |
| `REQ-Art28-12` | Arrangement Notice | Notify planned critical arrangements | `COV-133` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 4` |
| `REQ-Art28-13` | Service Criticality | Assess whether a service supports a critical function | `COV-134` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point a` |
| `REQ-Art28-14` | Supervisory Check | Assess supervisory contracting conditions | `COV-135` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point b` |
| `REQ-Art28-15` | Concentration Risk | Assess contractual and concentration risks | `COV-136` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point c` |
| `REQ-Art28-16` | Provider Due Diligence | Perform provider due diligence | `COV-137` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point d` |
| `REQ-Art28-17` | Contract Conflict Check | Assess contractual conflicts of interest | `COV-138` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 4, Point e` |
| `REQ-Art28-18` | Secure Provider Selection | Use providers meeting security standards | `COV-139` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 5` |
| `REQ-Art28-19` | Provider Audit Plan | Plan risk-based provider audits | `COV-140` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 6` |
| `REQ-Art28-20` | Skilled Auditor Use | Use suitably skilled auditors | `COV-141` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 6, Sub-Paragraph 1` |
| `REQ-Art28-21` | Termination Rights | Provide contractual termination rights | `COV-142` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7` |
| `REQ-Art28-22` | Significant Breach Exit | Terminate for significant breach | `COV-143` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point a` |
| `REQ-Art28-23` | Risk Change Exit | Terminate for material risk changes | `COV-144` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point b` |
| `REQ-Art28-24` | Provider Weakness Exit | Terminate for provider ICT-risk weaknesses | `COV-145` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point c` |
| `REQ-Art28-25` | Impaired Supervision Exit | Terminate where supervision is impaired | `COV-146` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 7, Point d` |
| `REQ-Art28-26` | Critical Exit Strategy | Maintain critical-function exit strategies | `COV-147` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8` |
| `REQ-Art28-27` | Business Continuity Exit | Exit without business disruption | `COV-148` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point a` |
| `REQ-Art28-28` | Compliance Exit | Exit without limiting regulatory compliance | `COV-149` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point b` |
| `REQ-Art28-29` | Service Continuity Exit | Exit without harming client-service continuity | `COV-150` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point c` |
| `REQ-Art28-30` | Exit Plan Review | Document, test and review exit plans | `COV-151` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 2` |
| `REQ-Art28-31` | Transition Alternatives | Prepare alternative solutions and transition plans | `COV-152` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 3` |
| `REQ-Art28-32` | Exit Contingency Measures | Maintain exit contingency measures | `COV-153` — Stakeholder-constrained | Art. 28; `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 4` |

## Relationship contract

- Every relationship in `7_view_graph.json` retains its stable `REL-*` ID, canonical source and target endpoint names, direction, natural-language meaning, ArchiMate type, evidence references, visibility, and approved status.
- `REL-COV-*` rows are the 153 Step 5 regulatory-effect relationships. All 13 directly performed rows use Realization; the 140 stakeholder-constrained, externally owned, or unclear-owner rows use Association and do not imply developer implementation.
- `REL-COMP-S001` through `REL-COMP-S153` are Composition relationships from one of the 13 named families to the matching child Requirement. They are semantic-only only because the JSON declares matching parent-child nesting.
- `REL-OP-*` and `REL-ROLE-001` are the exact stakeholder paths listed in the formal view graph table. The Microsoft path is Back-end Developer ← Employer Bank → Microsoft Contract; its operator-confirmed contract evidence is retained in the relationship documentation.

## Validation record

- Gate 7.1 — Confirm Metamodel Scope: approved by the operator.
- Gate 7.2 — Confirm View Graph: approved by the operator.
- Targeted metamodel correction: operator-approved. \`Data Offload Flow\` is classified as an Application Process; \`REL-OP-010\` remains the approved Assignment from Offload Service to that process.
- Repository graph validation passed: six views; one weakly connected component each; zero isolated semantic elements; all root counts below 30.
- Title audit passed: all 194 element labels are clean, unique, and 25 characters or fewer.
