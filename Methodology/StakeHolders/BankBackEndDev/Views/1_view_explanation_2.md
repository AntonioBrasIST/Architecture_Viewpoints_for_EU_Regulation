# DORA Back-end Delivery — Textual View Explanation (Revision 2)

## 1. Executive overview and stakeholder operational scope

This is a fresh Step 8 explanation derived from the approved operational footprint, stakeholder classification, DORA relevance and coverage ledger, viewpoint scope, view graph, immutable View 0 baseline, and existing pyArchimate model views. It does not use or overwrite `1_view_explanation.md`; the six walkthroughs below follow the existing model views exactly.

### View 0 — stakeholder-aware DORA regulation map

The immutable View 0 is the regulation-wide legal baseline. Its approved legal core contains these requirement families: Proportionate DORA Use; ICT Risk Governance; ICT Risk Framework; ICT Resilience Strategy; Secure ICT Operations; Detect and Recover; ICT Learning and Response; Incident Management; Resilience Testing; ICT Third-Party Risk; Critical ICT Oversight; Cyber Threat Sharing; DORA Supervision; DORA Legal Lifecycle. It is contextualized by Employer Bank → Back-end Developer and Employer Bank → Credit Institution. That role chain establishes the perspective: Employer Bank is the regulated credit institution and assigns the stakeholder role. It does not say that the individual developer is the regulated entity or that any control is implemented.

### Role, scope and ownership

The stakeholder is an execution-level Back-end Developer. Recorded work comprises C# offloads, ETLs and query services, internal-framework maintenance, implementation, testing, pull-request creation, release coordination, production monitoring, incident escalation participation and software remediation. Functional specifications, work allocation, approvals, deployment infrastructure, formal incident ownership, Microsoft contract oversight and data ownership remain outside this role where the evidence says so. Internal consumer teams own the platform data they consume.

### Applicable DORA mandates

- Articles 7–8: ICT systems and asset controls for framework maintenance, platform development, service updates and the enterprise data platform.
- Article 9: protection and change constraints for data offloads, access, DEV/test readiness and service updates.
- Articles 10–13 and 17: detection, continuity, recovery, learning and incident-management requirements connected to monitoring, escalation and remediation interfaces.
- Articles 24–25: digital operational resilience testing and test-method controls connected to testing, pull requests and review boundaries.
- Article 28: ICT third-party risk and exit controls connected to the confirmed Microsoft cloud-provider contract.

### Operational impact and coverage statement

The platform supports DORA critical or important functions for a large private-bank credit institution. The approved ledger records 153 evidence-backed coverage rows and 25 role-context entries. Every approved operational fact and concern is represented by a coverage relationship, assigned to the role-context stream, or retained as a visible external responsibility. This is an evidence-and-scope statement, not a compliance assessment.

The recorded `[Gap]` is limited cross-project visibility: the stakeholder has context for a smaller project but cannot track all concurrent work across the wider team. It may be a visibility limitation from this role and is not evidence that an enterprise control is missing.

## 2. Per-view visual walkthroughs

### 2.1. ICT Asset Governance

**Reading purpose.** This existing model view is a designing view of ICT Asset Controls (15 nested requirements). It contains 22 boxes, 20 visible arrows and 15 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-001, COV-002, COV-003, COV-004, COV-005, COV-006, COV-007, COV-008, COV-009, COV-010, COV-011, COV-012, COV-013, COV-014, COV-015.

#### Operational reality and daily workflow

Framework maintenance, platform development and service updates support the internal enterprise data platform. The stakeholder maintains the internal framework and develops platform services; only rows recorded as direct are direct realization.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** Dependency friction and platform-outage impact may limit work from this role’s viewpoint; they do not establish that an enterprise control is absent.

**External boundary.** Enterprise Data Platform ownership is not assigned to the Back-end Developer.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| ICT Asset Controls | Requirement | Parent requirement family for 15 approved coverage rows: COV-001, COV-002, COV-003, COV-004, COV-005, COV-006, COV-007, COV-008, COV-009, COV-010, COV-011, COV-012, COV-013, COV-014, COV-015. It is the root container for the nested child requirements. | Root family container |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is OP-001, OP-002, OP-003, OP-038, OP-004. | Root operational / external endpoint |
| Enterprise Data Platform | Application Component | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art8-07, COV-011, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068, REQ-Art8-08, COV-012, REQ-Art8-09, COV-013, REQ-Art8-10, COV-014, REQ-Art8-11, COV-015, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Framework Maintenance | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art7-01, COV-001, OP-004, OP-038, REQ-Art7-02, COV-002. | Root operational / external endpoint |
| Internal Framework | Application Component | Approved operational or external endpoint. Its incident relationship evidence is OP-004. | Root operational / external endpoint |
| Platform Development | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art7-03, COV-003, OP-050, OP-060, CON-006, REQ-Art7-04, COV-004, REQ-Art8-01, COV-005, OP-006, OP-018, OP-019, OP-066, OP-081, OP-082, REQ-Art8-02, COV-006, REQ-Art8-03, COV-007, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Service Update | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art8-04, COV-008, OP-038, OP-041, OP-042, OP-052, CON-001, REQ-Art8-05, COV-009, REQ-Art8-06, COV-010. | Root operational / external endpoint |
| Appropriate ICT systems | Requirement | Atomic DORA requirement: Appropriate ICT systems. It represents COV-001 under ICT Asset Controls (Art. 7). | Nested in ICT Asset Controls |
| Reliable ICT systems | Requirement | Atomic DORA requirement: Reliable ICT systems. It represents COV-002 under ICT Asset Controls (Art. 7). | Nested in ICT Asset Controls |
| Processing Capacity | Requirement | Atomic DORA requirement: Sufficient processing capacity. It represents COV-003 under ICT Asset Controls (Art. 7). | Nested in ICT Asset Controls |
| Technological resilience | Requirement | Atomic DORA requirement: Technological resilience. It represents COV-004 under ICT Asset Controls (Art. 7). | Nested in ICT Asset Controls |
| Function Classification | Requirement | Atomic DORA requirement: Identify and classify functions. It represents COV-005 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Role Documentation | Requirement | Atomic DORA requirement: Document roles and responsibilities. It represents COV-006 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| ICT Asset Documentation | Requirement | Atomic DORA requirement: Document information and ICT assets. It represents COV-007 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Classification Review | Requirement | Atomic DORA requirement: Review classification and documentation. It represents COV-008 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Identify ICT risk sources | Requirement | Atomic DORA requirement: Identify ICT risk sources. It represents COV-009 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Threat Assessment | Requirement | Atomic DORA requirement: Assess threats and risk scenarios. It represents COV-010 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Assess major ICT changes | Requirement | Atomic DORA requirement: Assess major ICT changes. It represents COV-011 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Asset Dependency Mapping | Requirement | Atomic DORA requirement: Map assets and interdependencies. It represents COV-012 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Provider Dependencies | Requirement | Atomic DORA requirement: Document third-party dependencies. It represents COV-013 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Inventory Maintenance | Requirement | Atomic DORA requirement: Maintain and update inventories. It represents COV-014 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |
| Legacy System Assessment | Requirement | Atomic DORA requirement: Assess legacy and connected systems. It represents COV-015 under ICT Asset Controls (Art. 8). | Nested in ICT Asset Controls |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-001 | Framework Maintenance → Appropriate ICT systems — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art7-01, COV-001, OP-004, OP-038. This is the approved direct realization. | Directly performed |
| REL-COV-002 | Framework Maintenance → Reliable ICT systems — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art7-02, COV-002, OP-004, OP-038. This is the approved direct realization. | Directly performed |
| REL-COV-003 | Processing Capacity → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art7-03, COV-003, OP-050, OP-060, CON-006. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-004 | Technological resilience → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art7-04, COV-004, OP-050, OP-060, CON-006. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-005 | Function Classification → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-01, COV-005, OP-006, OP-018, OP-019, OP-066, OP-081, OP-082. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-006 | Role Documentation → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-02, COV-006, OP-006, OP-018, OP-019, OP-066, OP-081, OP-082. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-007 | ICT Asset Documentation → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-03, COV-007, OP-006, OP-018, OP-019, OP-066, OP-081, OP-082. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-008 | Classification Review → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-04, COV-008, OP-038, OP-041, OP-042, OP-052, CON-001. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-009 | Identify ICT risk sources → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-05, COV-009, OP-038, OP-041, OP-042, OP-052, CON-001. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-010 | Threat Assessment → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-06, COV-010, OP-038, OP-041, OP-042, OP-052, CON-001. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-011 | Assess major ICT changes → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-07, COV-011, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-012 | Asset Dependency Mapping → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-08, COV-012, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-013 | Provider Dependencies → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-09, COV-013, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-014 | Inventory Maintenance → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-10, COV-014, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-015 | Legacy System Assessment → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art8-11, COV-015, OP-023, OP-024, OP-025, OP-026, OP-027, OP-028, OP-029, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-OP-001 | Back-end Developer → Platform Development — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |
| REL-OP-066 | Back-end Developer → Service Update — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-038. | — |
| REL-OP-090 | Back-end Developer → Framework Maintenance — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-004. | — |
| REL-OP-091 | Framework Maintenance → Internal Framework — Association | maintains. Drawn because the approved operational or role evidence establishes this exact link: OP-004. | — |
| REL-OP-093 | Back-end Developer → Enterprise Data Platform — Association | develops for. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S001 | ICT Asset Controls → Appropriate ICT systems | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S002 | ICT Asset Controls → Reliable ICT systems | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S003 | ICT Asset Controls → Processing Capacity | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S004 | ICT Asset Controls → Technological resilience | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S005 | ICT Asset Controls → Function Classification | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S006 | ICT Asset Controls → Role Documentation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S007 | ICT Asset Controls → ICT Asset Documentation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S008 | ICT Asset Controls → Classification Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S009 | ICT Asset Controls → Identify ICT risk sources | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S010 | ICT Asset Controls → Threat Assessment | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S011 | ICT Asset Controls → Assess major ICT changes | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S012 | ICT Asset Controls → Asset Dependency Mapping | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S013 | ICT Asset Controls → Provider Dependencies | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S014 | ICT Asset Controls → Inventory Maintenance | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S015 | ICT Asset Controls → Legacy System Assessment | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

### 2.2. Protection and Change

**Reading purpose.** This existing model view is a designing view of Change Controls (9 nested requirements); Data Protection (10 nested requirements). It contains 28 boxes, 25 visible arrows and 19 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-016, COV-017, COV-018, COV-019, COV-020, COV-021, COV-022, COV-023, COV-024, COV-025, COV-026, COV-027, COV-028, COV-029, COV-030, COV-031, COV-032, COV-033, COV-034.

#### Operational reality and daily workflow

The path follows offload development to the data-offload process, DEV/test readiness before a pull request, and later service updates. It captures access and change-control prerequisites.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** Missing access and incomplete specifications are workflow constraints that may reveal a local operational or visibility limitation, not an enterprise-wide compliance conclusion.

**External boundary.** Azure AD Access Control is an external access dependency, not a control operated by the stakeholder.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| Change Controls | Requirement | Parent requirement family for 9 approved coverage rows: COV-026, COV-027, COV-028, COV-029, COV-030, COV-031, COV-032, COV-033, COV-034. It is the root container for the nested child requirements. | Root family container |
| Data Protection | Requirement | Parent requirement family for 10 approved coverage rows: COV-016, COV-017, COV-018, COV-019, COV-020, COV-021, COV-022, COV-023, COV-024, COV-025. It is the root container for the nested child requirements. | Root family container |
| Azure AD Access Control | Application Component | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art9-08, COV-023, OP-017, OP-020, OP-037, OP-053, OP-054, OP-057, CON-002, REQ-Art9-09, COV-024, REQ-Art9-10, COV-025. | Root operational / external endpoint |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is OP-001, OP-008, OP-038, OP-017, OP-037, CON-002, OP-002, OP-003. | Root operational / external endpoint |
| Data Offload Flow | Application Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art9-01, COV-016, OP-006, OP-048, OP-065, OP-081, REQ-Art9-02, COV-017, REQ-Art9-03, COV-018, REQ-Art9-04, COV-019. | Root operational / external endpoint |
| Enterprise Data Platform | Application Component | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art9-05, COV-020, OP-031, OP-032, OP-033, OP-034, OP-035, OP-036, OP-088, REQ-Art9-06, COV-021, REQ-Art9-07, COV-022, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Offload Service | Application Component | Approved operational or external endpoint. Its incident relationship evidence is OP-001, OP-006. | Root operational / external endpoint |
| Service Update | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art9-16, COV-031, OP-038, OP-041, OP-042, REQ-Art9-17, COV-032, REQ-Art9-18, COV-033, REQ-Art9-19, COV-034. | Root operational / external endpoint |
| Test and DEV Readiness | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art9-11, COV-026, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008, REQ-Art9-12, COV-027, REQ-Art9-13, COV-028, REQ-Art9-14, COV-029, REQ-Art9-15, COV-030. | Root operational / external endpoint |
| ICT Security Monitoring | Requirement | Atomic DORA requirement: Monitor ICT security and functioning. It represents COV-016 under Data Protection (Art. 9). | Nested in Data Protection |
| ICT Security Controls | Requirement | Atomic DORA requirement: Deploy ICT security controls. It represents COV-017 under Data Protection (Art. 9). | Nested in Data Protection |
| Resilience Controls | Requirement | Atomic DORA requirement: Design resilience controls. It represents COV-018 under Data Protection (Art. 9). | Nested in Data Protection |
| Continuity Controls | Requirement | Atomic DORA requirement: Design continuity controls. It represents COV-019 under Data Protection (Art. 9). | Nested in Data Protection |
| Uptime Controls | Requirement | Atomic DORA requirement: Design availability controls. It represents COV-020 under Data Protection (Art. 9). | Nested in Data Protection |
| Data Integrity Protection | Requirement | Atomic DORA requirement: Protect data confidentiality and integrity. It represents COV-021 under Data Protection (Art. 9). | Nested in Data Protection |
| Secure data transfer | Requirement | Atomic DORA requirement: Secure data transfer. It represents COV-022 under Data Protection (Art. 9). | Nested in Data Protection |
| Access Corruption Control | Requirement | Atomic DORA requirement: Prevent corruption and unauthorised access. It represents COV-023 under Data Protection (Art. 9). | Nested in Data Protection |
| Uptime Integrity Control | Requirement | Atomic DORA requirement: Prevent availability and integrity loss. It represents COV-024 under Data Protection (Art. 9). | Nested in Data Protection |
| Data Management Risks | Requirement | Atomic DORA requirement: Protect data from management risks. It represents COV-025 under Data Protection (Art. 9). | Nested in Data Protection |
| Security Policy Record | Requirement | Atomic DORA requirement: Document information security policy. It represents COV-026 under Change Controls (Art. 9). | Nested in Change Controls |
| Network Segmentation | Requirement | Atomic DORA requirement: Manage and segment networks. It represents COV-027 under Change Controls (Art. 9). | Nested in Change Controls |
| Access Limitation | Requirement | Atomic DORA requirement: Limit logical and physical access. It represents COV-028 under Change Controls (Art. 9). | Nested in Change Controls |
| Strong Auth and Crypto | Requirement | Atomic DORA requirement: Use strong authentication and cryptography. It represents COV-029 under Change Controls (Art. 9). | Nested in Change Controls |
| Change Control | Requirement | Atomic DORA requirement: Maintain controlled change management. It represents COV-030 under Change Controls (Art. 9). | Nested in Change Controls |
| Record changes | Requirement | Atomic DORA requirement: Record changes. It represents COV-031 under Change Controls (Art. 9). | Nested in Change Controls |
| Test and assess changes | Requirement | Atomic DORA requirement: Test and assess changes. It represents COV-032 under Change Controls (Art. 9). | Nested in Change Controls |
| Change Verification | Requirement | Atomic DORA requirement: Approve, implement and verify changes. It represents COV-033 under Change Controls (Art. 9). | Nested in Change Controls |
| Patch Update Controls | Requirement | Atomic DORA requirement: Document patch and update controls. It represents COV-034 under Change Controls (Art. 9). | Nested in Change Controls |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-016 | ICT Security Monitoring → Data Offload Flow — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-01, COV-016, OP-006, OP-048, OP-065, OP-081. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-017 | ICT Security Controls → Data Offload Flow — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-02, COV-017, OP-006, OP-048, OP-065, OP-081. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-018 | Resilience Controls → Data Offload Flow — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-03, COV-018, OP-006, OP-048, OP-065, OP-081. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-019 | Continuity Controls → Data Offload Flow — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-04, COV-019, OP-006, OP-048, OP-065, OP-081. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-020 | Uptime Controls → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-05, COV-020, OP-031, OP-032, OP-033, OP-034, OP-035, OP-036, OP-088. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-021 | Data Integrity Protection → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-06, COV-021, OP-031, OP-032, OP-033, OP-034, OP-035, OP-036, OP-088. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-022 | Secure data transfer → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-07, COV-022, OP-031, OP-032, OP-033, OP-034, OP-035, OP-036, OP-088. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-023 | Azure AD Access Control → Access Corruption Control — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-08, COV-023, OP-017, OP-020, OP-037, OP-053, OP-054, OP-057, CON-002. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-024 | Azure AD Access Control → Uptime Integrity Control — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-09, COV-024, OP-017, OP-020, OP-037, OP-053, OP-054, OP-057, CON-002. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-025 | Azure AD Access Control → Data Management Risks — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-10, COV-025, OP-017, OP-020, OP-037, OP-053, OP-054, OP-057, CON-002. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-026 | Test and DEV Readiness → Security Policy Record — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-11, COV-026, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008. This is the approved direct realization. | Directly performed |
| REL-COV-027 | Test and DEV Readiness → Network Segmentation — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-12, COV-027, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008. This is the approved direct realization. | Directly performed |
| REL-COV-028 | Test and DEV Readiness → Access Limitation — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-13, COV-028, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008. This is the approved direct realization. | Directly performed |
| REL-COV-029 | Test and DEV Readiness → Strong Auth and Crypto — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-14, COV-029, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008. This is the approved direct realization. | Directly performed |
| REL-COV-030 | Test and DEV Readiness → Change Control — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-15, COV-030, OP-008, OP-009, OP-010, OP-011, OP-012, OP-013, OP-047, OP-064, OP-082, OP-084, OP-085, CON-008. This is the approved direct realization. | Directly performed |
| REL-COV-031 | Record changes → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-16, COV-031, OP-038, OP-041, OP-042. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-032 | Test and assess changes → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-17, COV-032, OP-038, OP-041, OP-042. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-033 | Change Verification → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-18, COV-033, OP-038, OP-041, OP-042. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-034 | Patch Update Controls → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art9-19, COV-034, OP-038, OP-041, OP-042. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-OP-002 | Back-end Developer → Offload Service — Association | develops. Drawn because the approved operational or role evidence establishes this exact link: OP-001. | — |
| REL-OP-010 | Offload Service → Data Offload Flow — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-006. | — |
| REL-OP-014 | Back-end Developer → Test and DEV Readiness — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-008. | — |
| REL-OP-066 | Back-end Developer → Service Update — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-038. | — |
| REL-OP-092 | Azure AD Access Control → Back-end Developer — Association | restricts. Drawn because the approved operational or role evidence establishes this exact link: OP-017, OP-037, CON-002. | — |
| REL-OP-093 | Back-end Developer → Enterprise Data Platform — Association | develops for. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S016 | Data Protection → ICT Security Monitoring | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S017 | Data Protection → ICT Security Controls | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S018 | Data Protection → Resilience Controls | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S019 | Data Protection → Continuity Controls | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S020 | Data Protection → Uptime Controls | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S021 | Data Protection → Data Integrity Protection | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S022 | Data Protection → Secure data transfer | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S023 | Data Protection → Access Corruption Control | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S024 | Data Protection → Uptime Integrity Control | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S025 | Data Protection → Data Management Risks | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S026 | Change Controls → Security Policy Record | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S027 | Change Controls → Network Segmentation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S028 | Change Controls → Access Limitation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S029 | Change Controls → Strong Auth and Crypto | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S030 | Change Controls → Change Control | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S031 | Change Controls → Record changes | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S032 | Change Controls → Test and assess changes | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S033 | Change Controls → Change Verification | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S034 | Change Controls → Patch Update Controls | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

### 2.3. Detection and Continuity

**Reading purpose.** This existing model view is a designing view of Backup and Recovery (13 nested requirements); Continuity Testing (10 nested requirements); ICT Detection (6 nested requirements); Continuity Response (10 nested requirements). It contains 58 boxes, 54 visible arrows and 39 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-035, COV-036, COV-037, COV-038, COV-039, COV-040, COV-041, COV-042, COV-043, COV-044, COV-045, COV-046, COV-047, COV-048, COV-049, COV-050, COV-051, COV-052, COV-053, COV-054, COV-055, COV-056, COV-057, COV-058, COV-059, COV-060, COV-061, COV-062, COV-063, COV-064, COV-065, COV-066, COV-067, COV-068, COV-069, COV-070, COV-071, COV-072, COV-073.

#### Operational reality and daily workflow

The path follows production monitoring through Datadog, an alarm and incident escalation to software or infrastructure remediation. Platform links connect this route to continuity and recovery requirements.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** No outage workaround or Infrastructure Team remediation method is evidenced. These are evidence limitations and may be visibility limitations, not missing enterprise recovery controls.

**External boundary.** Datadog, the Monitoring Team, the Infrastructure Team and remediation responsibilities remain outside the stakeholder’s direct control.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| Backup and Recovery | Requirement | Parent requirement family for 13 approved coverage rows: COV-061, COV-062, COV-063, COV-064, COV-065, COV-066, COV-067, COV-068, COV-069, COV-070, COV-071, COV-072, COV-073. It is the root container for the nested child requirements. | Root family container |
| Continuity Testing | Requirement | Parent requirement family for 10 approved coverage rows: COV-051, COV-052, COV-053, COV-054, COV-055, COV-056, COV-057, COV-058, COV-059, COV-060. It is the root container for the nested child requirements. | Root family container |
| ICT Detection | Requirement | Parent requirement family for 6 approved coverage rows: COV-035, COV-036, COV-037, COV-038, COV-039, COV-040. It is the root container for the nested child requirements. | Root family container |
| Continuity Response | Requirement | Parent requirement family for 10 approved coverage rows: COV-041, COV-042, COV-043, COV-044, COV-045, COV-046, COV-047, COV-048, COV-049, COV-050. It is the root container for the nested child requirements. | Root family container |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is OP-001, OP-002, OP-003, OP-014. | Root operational / external endpoint |
| Datadog | Application Component | Approved operational or external endpoint. Its incident relationship evidence is OP-014, OP-076. | Root operational / external endpoint |
| Datadog Alarm | Business Event | Approved operational or external endpoint. Its incident relationship evidence is OP-070. | Root operational / external endpoint |
| Enterprise Data Platform | Application Component | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art11-01, COV-041, OP-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080, REQ-Art11-02, COV-042, REQ-Art11-03, COV-043, REQ-Art11-04, COV-044, REQ-Art11-11, COV-051, OP-062, OP-063, REQ-Art11-12, COV-052, REQ-Art11-13, COV-053, REQ-Art12-01, COV-061, REQ-Art12-02, COV-062, REQ-Art12-03, COV-063, REQ-Art12-04, COV-064, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Incident Escalation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art10-03, COV-037, OP-070, OP-072, OP-076, REQ-Art10-04, COV-038, REQ-Art10-05, COV-039, REQ-Art10-06, COV-040, REQ-Art11-08, COV-048, OP-060, OP-071, OP-079, OP-080, REQ-Art11-09, COV-049, REQ-Art11-10, COV-050, REQ-Art11-17, COV-057, OP-073, OP-074, OP-075, OP-077, OP-078, REQ-Art11-18, COV-058, REQ-Art11-19, COV-059, REQ-Art11-20, COV-060. | Root operational / external endpoint |
| Infrastructure Problem | Business Event | Approved operational or external endpoint. Its incident relationship evidence is OP-074. | Root operational / external endpoint |
| Infra Remediation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art12-05, COV-065, OP-027, OP-028, OP-029, OP-063, OP-074, OP-075, OP-078, REQ-Art12-06, COV-066, REQ-Art12-07, COV-067, REQ-Art12-08, COV-068, OP-071, OP-073, OP-076. | Root operational / external endpoint |
| Infrastructure Team | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-075. | Root operational / external endpoint |
| Monitoring Team | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-070. | Root operational / external endpoint |
| Platform Development | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art11-14, COV-054, OP-060, OP-068, REQ-Art11-15, COV-055, REQ-Art11-16, COV-056, REQ-Art12-09, COV-069, OP-048, OP-065, OP-078, OP-080, REQ-Art12-10, COV-070, REQ-Art12-11, COV-071, REQ-Art12-12, COV-072, REQ-Art12-13, COV-073, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Production Monitoring | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art10-01, COV-035, OP-014, OP-070, OP-072, REQ-Art10-02, COV-036. | Root operational / external endpoint |
| Responsible Dev Team | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-075. | Root operational / external endpoint |
| Software Error | Business Event | Approved operational or external endpoint. Its incident relationship evidence is OP-074. | Root operational / external endpoint |
| Software Fix | Business Object | Approved operational or external endpoint. Its incident relationship evidence is OP-077. | Root operational / external endpoint |
| Software Remediation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art11-05, COV-045, OP-071, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, REQ-Art11-06, COV-046, REQ-Art11-07, COV-047. | Root operational / external endpoint |
| Anomaly Detection | Requirement | Atomic DORA requirement: Detect anomalies and performance issues. It represents COV-035 under ICT Detection (Art. 10). | Nested in ICT Detection |
| Single Failure Points | Requirement | Atomic DORA requirement: Identify material single points of failure. It represents COV-036 under ICT Detection (Art. 10). | Nested in ICT Detection |
| Test detection mechanisms | Requirement | Atomic DORA requirement: Test detection mechanisms. It represents COV-037 under ICT Detection (Art. 10). | Nested in ICT Detection |
| Control Alert Thresholds | Requirement | Atomic DORA requirement: Use control layers and alert thresholds. It represents COV-038 under ICT Detection (Art. 10). | Nested in ICT Detection |
| Incident Responder Alerts | Requirement | Atomic DORA requirement: Trigger and notify incident responders. It represents COV-039 under ICT Detection (Art. 10). | Nested in ICT Detection |
| Anomaly Monitoring | Requirement | Atomic DORA requirement: Resource continuous anomaly monitoring. It represents COV-040 under ICT Detection (Art. 10). | Nested in ICT Detection |
| ICT Continuity Policy | Requirement | Atomic DORA requirement: Maintain ICT business-continuity policy. It represents COV-041 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Critical Continuity | Requirement | Atomic DORA requirement: Ensure critical-function continuity. It represents COV-042 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Incident Resolution | Requirement | Atomic DORA requirement: Respond to and resolve incidents. It represents COV-043 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Containment Plans | Requirement | Atomic DORA requirement: Activate containment and recovery plans. It represents COV-044 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Disruption Estimates | Requirement | Atomic DORA requirement: Estimate disruption impacts and losses. It represents COV-045 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Crisis Reporting | Requirement | Atomic DORA requirement: Provide crisis communications and reporting. It represents COV-046 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Audited Recovery Plans | Requirement | Atomic DORA requirement: Maintain audited response and recovery plans. It represents COV-047 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Maintain continuity plans | Requirement | Atomic DORA requirement: Maintain continuity plans. It represents COV-048 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Outsourced Function Tests | Requirement | Atomic DORA requirement: Test plans for outsourced critical functions. It represents COV-049 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Business Impact Analysis | Requirement | Atomic DORA requirement: Conduct a business-impact analysis. It represents COV-050 under Continuity Response (Art. 11). | Nested in Continuity Response |
| Assess critical functions | Requirement | Atomic DORA requirement: Assess critical functions. It represents COV-051 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Dependency Assessment | Requirement | Atomic DORA requirement: Assess dependencies and information assets. It represents COV-052 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| BIA Asset Redundancy | Requirement | Atomic DORA requirement: Align ICT assets and redundancy to BIA. It represents COV-053 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Annual Plan Tests | Requirement | Atomic DORA requirement: Test plans at least annually. It represents COV-054 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Critical Change Tests | Requirement | Atomic DORA requirement: Test after substantive critical-system change. It represents COV-055 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Crisis Comms Tests | Requirement | Atomic DORA requirement: Test crisis communications. It represents COV-056 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Cyberattack Tests | Requirement | Atomic DORA requirement: Test cyberattack and switchover scenarios. It represents COV-057 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Plan Assurance Review | Requirement | Atomic DORA requirement: Review plans from testing and assurance. It represents COV-058 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Crisis Control Operation | Requirement | Atomic DORA requirement: Operate a crisis-management function. It represents COV-059 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Disruption Event Records | Requirement | Atomic DORA requirement: Keep disruption-event records. It represents COV-060 under Continuity Testing (Art. 11). | Nested in Continuity Testing |
| Document backup policy | Requirement | Atomic DORA requirement: Document backup policy. It represents COV-061 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Backup Scope Frequency | Requirement | Atomic DORA requirement: Set backup scope and frequency. It represents COV-062 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Recovery Method Records | Requirement | Atomic DORA requirement: Document restoration and recovery methods. It represents COV-063 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Activate backup systems | Requirement | Atomic DORA requirement: Activate backup systems. It represents COV-064 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Backup Data Protection | Requirement | Atomic DORA requirement: Protect security and data qualities during backup. It represents COV-065 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Backup Restoration Tests | Requirement | Atomic DORA requirement: Periodically test backup and restoration. It represents COV-066 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Restoration Protection | Requirement | Atomic DORA requirement: Segregate and protect restoration systems. It represents COV-067 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Timely Service Recovery | Requirement | Atomic DORA requirement: Restore services in a timely way. It represents COV-068 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Redundant Capacity | Requirement | Atomic DORA requirement: Maintain adequate redundant capacity. It represents COV-069 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Recovery Time Objective | Requirement | Atomic DORA requirement: Set recovery-time objectives. It represents COV-070 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Recovery Point Objective | Requirement | Atomic DORA requirement: Set recovery-point objectives. It represents COV-071 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Recovered Data Reconcile | Requirement | Atomic DORA requirement: Check and reconcile recovered data. It represents COV-072 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |
| Rebuilt Data Check | Requirement | Atomic DORA requirement: Check externally reconstructed data. It represents COV-073 under Backup and Recovery (Art. 12). | Nested in Backup and Recovery |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-035 | Anomaly Detection → Production Monitoring — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-01, COV-035, OP-014, OP-070, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-036 | Single Failure Points → Production Monitoring — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-02, COV-036, OP-014, OP-070, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-037 | Incident Escalation → Test detection mechanisms — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-03, COV-037, OP-070, OP-072, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-038 | Incident Escalation → Control Alert Thresholds — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-04, COV-038, OP-070, OP-072, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-039 | Incident Escalation → Incident Responder Alerts — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-05, COV-039, OP-070, OP-072, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-040 | Incident Escalation → Anomaly Monitoring — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art10-06, COV-040, OP-070, OP-072, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-041 | ICT Continuity Policy → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-01, COV-041, OP-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-042 | Critical Continuity → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-02, COV-042, OP-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-043 | Incident Resolution → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-03, COV-043, OP-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-044 | Containment Plans → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-04, COV-044, OP-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-045 | Software Remediation → Disruption Estimates — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-05, COV-045, OP-071, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-COV-046 | Software Remediation → Crisis Reporting — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-06, COV-046, OP-071, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-COV-047 | Software Remediation → Audited Recovery Plans — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-07, COV-047, OP-071, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-COV-048 | Maintain continuity plans → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-08, COV-048, OP-060, OP-071, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-049 | Outsourced Function Tests → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-09, COV-049, OP-060, OP-071, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-050 | Business Impact Analysis → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-10, COV-050, OP-060, OP-071, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-051 | Assess critical functions → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-11, COV-051, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-052 | Dependency Assessment → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-12, COV-052, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-053 | BIA Asset Redundancy → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-13, COV-053, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-054 | Annual Plan Tests → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-14, COV-054, OP-060, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-055 | Critical Change Tests → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-15, COV-055, OP-060, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-056 | Crisis Comms Tests → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-16, COV-056, OP-060, OP-068. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-057 | Cyberattack Tests → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-17, COV-057, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-058 | Plan Assurance Review → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-18, COV-058, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-059 | Crisis Control Operation → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-19, COV-059, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-060 | Disruption Event Records → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art11-20, COV-060, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-061 | Document backup policy → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-01, COV-061, OP-062, OP-063, OP-073, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-062 | Backup Scope Frequency → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-02, COV-062, OP-062, OP-063, OP-073, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-063 | Recovery Method Records → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-03, COV-063, OP-062, OP-063, OP-073, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-064 | Activate backup systems → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-04, COV-064, OP-062, OP-063, OP-073, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-065 | Infra Remediation → Backup Data Protection — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-05, COV-065, OP-027, OP-028, OP-029, OP-063, OP-074, OP-075, OP-078. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-066 | Infra Remediation → Backup Restoration Tests — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-06, COV-066, OP-027, OP-028, OP-029, OP-063, OP-074, OP-075, OP-078. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-067 | Infra Remediation → Restoration Protection — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-07, COV-067, OP-027, OP-028, OP-029, OP-063, OP-074, OP-075, OP-078. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-068 | Infra Remediation → Timely Service Recovery — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-08, COV-068, OP-027, OP-028, OP-029, OP-063, OP-074, OP-075, OP-078. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-069 | Redundant Capacity → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-09, COV-069, OP-048, OP-065, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-070 | Recovery Time Objective → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-10, COV-070, OP-048, OP-065, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-071 | Recovery Point Objective → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-11, COV-071, OP-048, OP-065, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-072 | Recovered Data Reconcile → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-12, COV-072, OP-048, OP-065, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-073 | Rebuilt Data Check → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art12-13, COV-073, OP-048, OP-065, OP-078, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-OP-001 | Back-end Developer → Platform Development — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |
| REL-OP-031 | Back-end Developer → Production Monitoring — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-014. | — |
| REL-OP-032 | Datadog → Production Monitoring — Serving | serves. Drawn because the approved operational or role evidence establishes this exact link: OP-014. | — |
| REL-OP-079 | Datadog Alarm → Incident Escalation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-070. | — |
| REL-OP-080 | Monitoring Team → Incident Escalation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-070. | — |
| REL-OP-081 | Incident Escalation → Software Remediation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-071, OP-073. | — |
| REL-OP-082 | Incident Escalation → Infra Remediation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-071, OP-073. | — |
| REL-OP-083 | Responsible Dev Team → Software Remediation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-075. | — |
| REL-OP-084 | Infrastructure Team → Infra Remediation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-075. | — |
| REL-OP-085 | Datadog → Software Remediation — Serving | serves. Drawn because the approved operational or role evidence establishes this exact link: OP-076. | — |
| REL-OP-086 | Datadog → Infra Remediation — Serving | serves. Drawn because the approved operational or role evidence establishes this exact link: OP-076. | — |
| REL-OP-087 | Software Error → Software Remediation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-074. | — |
| REL-OP-088 | Infrastructure Problem → Infra Remediation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-074. | — |
| REL-OP-089 | Software Remediation → Software Fix — Access | writes. Drawn because the approved operational or role evidence establishes this exact link: OP-077. | — |
| REL-OP-093 | Back-end Developer → Enterprise Data Platform — Association | develops for. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S035 | ICT Detection → Anomaly Detection | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S036 | ICT Detection → Single Failure Points | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S037 | ICT Detection → Test detection mechanisms | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S038 | ICT Detection → Control Alert Thresholds | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S039 | ICT Detection → Incident Responder Alerts | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S040 | ICT Detection → Anomaly Monitoring | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S041 | Continuity Response → ICT Continuity Policy | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S042 | Continuity Response → Critical Continuity | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S043 | Continuity Response → Incident Resolution | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S044 | Continuity Response → Containment Plans | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S045 | Continuity Response → Disruption Estimates | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S046 | Continuity Response → Crisis Reporting | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S047 | Continuity Response → Audited Recovery Plans | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S048 | Continuity Response → Maintain continuity plans | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S049 | Continuity Response → Outsourced Function Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S050 | Continuity Response → Business Impact Analysis | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S051 | Continuity Testing → Assess critical functions | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S052 | Continuity Testing → Dependency Assessment | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S053 | Continuity Testing → BIA Asset Redundancy | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S054 | Continuity Testing → Annual Plan Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S055 | Continuity Testing → Critical Change Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S056 | Continuity Testing → Crisis Comms Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S057 | Continuity Testing → Cyberattack Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S058 | Continuity Testing → Plan Assurance Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S059 | Continuity Testing → Crisis Control Operation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S060 | Continuity Testing → Disruption Event Records | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S061 | Backup and Recovery → Document backup policy | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S062 | Backup and Recovery → Backup Scope Frequency | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S063 | Backup and Recovery → Recovery Method Records | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S064 | Backup and Recovery → Activate backup systems | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S065 | Backup and Recovery → Backup Data Protection | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S066 | Backup and Recovery → Backup Restoration Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S067 | Backup and Recovery → Restoration Protection | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S068 | Backup and Recovery → Timely Service Recovery | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S069 | Backup and Recovery → Redundant Capacity | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S070 | Backup and Recovery → Recovery Time Objective | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S071 | Backup and Recovery → Recovery Point Objective | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S072 | Backup and Recovery → Recovered Data Reconcile | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S073 | Backup and Recovery → Rebuilt Data Check | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

### 2.4. Incident Learning

**Reading purpose.** This existing model view is a designing view of Incident Management (10 nested requirements); ICT Learning (18 nested requirements). It contains 42 boxes, 38 visible arrows and 28 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-074, COV-075, COV-076, COV-077, COV-078, COV-079, COV-080, COV-081, COV-082, COV-083, COV-084, COV-085, COV-086, COV-087, COV-088, COV-089, COV-090, COV-091, COV-092, COV-093, COV-094, COV-095, COV-096, COV-097, COV-098, COV-099, COV-100, COV-101.

#### Operational reality and daily workflow

The monitoring and escalation route explains learning, service update and software remediation requirements. It retains named owners rather than attributing escalation or formal incident work to the developer.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** Limited cross-project visibility may affect what the stakeholder can observe outside the smaller project. This is a viewpoint limitation, not evidence that learning or incident management is absent.

**External boundary.** Monitoring, escalation and remediation remain with named external teams or unclear-owner endpoints where the ledger says so.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| Incident Management | Requirement | Parent requirement family for 10 approved coverage rows: COV-092, COV-093, COV-094, COV-095, COV-096, COV-097, COV-098, COV-099, COV-100, COV-101. It is the root container for the nested child requirements. | Root family container |
| ICT Learning | Requirement | Parent requirement family for 18 approved coverage rows: COV-074, COV-075, COV-076, COV-077, COV-078, COV-079, COV-080, COV-081, COV-082, COV-083, COV-084, COV-085, COV-086, COV-087, COV-088, COV-089, COV-090, COV-091. It is the root container for the nested child requirements. | Root family container |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is OP-014, OP-038, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Datadog | Application Component | Approved operational or external endpoint. Its incident relationship evidence is OP-014, OP-076. | Root operational / external endpoint |
| Datadog Alarm | Business Event | Approved operational or external endpoint. Its incident relationship evidence is OP-070. | Root operational / external endpoint |
| Enterprise Data Platform | Application Component | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art13-11, COV-084, OP-061, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080, REQ-Art13-12, COV-085, REQ-Art13-13, COV-086, REQ-Art13-14, COV-087, OP-001, OP-002, OP-003. | Root operational / external endpoint |
| Incident Escalation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art13-06, COV-079, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, REQ-Art13-07, COV-080, REQ-Art13-08, COV-081, REQ-Art13-09, COV-082, REQ-Art13-10, COV-083, REQ-Art17-01, COV-092, REQ-Art17-02, COV-093, REQ-Art17-03, COV-094, REQ-Art17-04, COV-095, REQ-Art17-05, COV-096, REQ-Art17-06, COV-097, REQ-Art17-07, COV-098. | Root operational / external endpoint |
| Monitoring Team | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-070. | Root operational / external endpoint |
| Platform Development | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art13-01, COV-074, OP-014, OP-038, OP-042, OP-048, REQ-Art13-02, COV-075, REQ-Art13-03, COV-076, REQ-Art13-04, COV-077, REQ-Art13-05, COV-078. | Root operational / external endpoint |
| Production Monitoring | Business Process | Approved operational or external endpoint. Its incident relationship evidence is OP-014. | Root operational / external endpoint |
| Responsible Dev Team | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-075. | Root operational / external endpoint |
| Service Update | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art13-15, COV-088, OP-038, OP-067, OP-087, REQ-Art13-16, COV-089, REQ-Art13-17, COV-090, REQ-Art13-18, COV-091. | Root operational / external endpoint |
| Software Fix | Business Object | Approved operational or external endpoint. Its incident relationship evidence is OP-077. | Root operational / external endpoint |
| Software Remediation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art17-08, COV-099, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, REQ-Art17-09, COV-100, REQ-Art17-10, COV-101, OP-071. | Root operational / external endpoint |
| Vulnerability Information | Requirement | Atomic DORA requirement: Gather vulnerability information. It represents COV-074 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Cyber Threat Information | Requirement | Atomic DORA requirement: Gather cyber-threat information. It represents COV-075 under ICT Learning (Art. 13). | Nested in ICT Learning |
| ICT Incident Information | Requirement | Atomic DORA requirement: Gather ICT-incident information. It represents COV-076 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Resilience Impact Review | Requirement | Atomic DORA requirement: Analyse resilience impacts. It represents COV-077 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Major Incident Review | Requirement | Atomic DORA requirement: Review disruptive major incidents. It represents COV-078 under ICT Learning (Art. 13). | Nested in ICT Learning |
| ICT Cause Improvements | Requirement | Atomic DORA requirement: Identify causes and ICT improvements. It represents COV-079 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Review Communications | Requirement | Atomic DORA requirement: Communicate review changes when requested. It represents COV-080 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Procedure Effectiveness | Requirement | Atomic DORA requirement: Evaluate procedure and action effectiveness. It represents COV-081 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Security Alert Review | Requirement | Atomic DORA requirement: Review response to security alerts. It represents COV-082 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Forensic Quality Review | Requirement | Atomic DORA requirement: Review forensic-analysis quality. It represents COV-083 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Escalation Review | Requirement | Atomic DORA requirement: Review incident escalation. It represents COV-084 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Communication Review | Requirement | Atomic DORA requirement: Review internal and external communications. It represents COV-085 under ICT Learning (Art. 13). | Nested in ICT Learning |
| ICT Risk Lessons | Requirement | Atomic DORA requirement: Incorporate lessons in ICT risk assessment. It represents COV-086 under ICT Learning (Art. 13). | Nested in ICT Learning |
| ICT Risk Component Review | Requirement | Atomic DORA requirement: Review ICT risk-management components. It represents COV-087 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Resilience Strategy Watch | Requirement | Atomic DORA requirement: Monitor resilience strategy and ICT-risk evolution. It represents COV-088 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Lessons Reporting | Requirement | Atomic DORA requirement: Report lessons and recommendations to management. It represents COV-089 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Resilience Training | Requirement | Atomic DORA requirement: Provide mandatory awareness and resilience training. It represents COV-090 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Technology Monitoring | Requirement | Atomic DORA requirement: Monitor relevant technology developments. It represents COV-091 under ICT Learning (Art. 13). | Nested in ICT Learning |
| Incident Process | Requirement | Atomic DORA requirement: Establish an incident-management process. It represents COV-092 under Incident Management (Art. 17). | Nested in Incident Management |
| Incident Threat Records | Requirement | Atomic DORA requirement: Record incidents and significant cyber threats. It represents COV-093 under Incident Management (Art. 17). | Nested in Incident Management |
| Monitoring Integration | Requirement | Atomic DORA requirement: Integrate monitoring, handling, follow-up and root-cause treatment. It represents COV-094 under Incident Management (Art. 17). | Nested in Incident Management |
| Early Warning Indicators | Requirement | Atomic DORA requirement: Use early-warning indicators. It represents COV-095 under Incident Management (Art. 17). | Nested in Incident Management |
| Incident Classification | Requirement | Atomic DORA requirement: Identify, log, categorise and classify incidents. It represents COV-096 under Incident Management (Art. 17). | Nested in Incident Management |
| Incident Role Assignment | Requirement | Atomic DORA requirement: Assign incident roles and responsibilities. It represents COV-097 under Incident Management (Art. 17). | Nested in Incident Management |
| Communication Escalation | Requirement | Atomic DORA requirement: Plan communications and escalation. It represents COV-098 under Incident Management (Art. 17). | Nested in Incident Management |
| Major Incident Reporting | Requirement | Atomic DORA requirement: Report major incidents to management. It represents COV-099 under Incident Management (Art. 17). | Nested in Incident Management |
| Mitigate incident impacts | Requirement | Atomic DORA requirement: Mitigate incident impacts. It represents COV-100 under Incident Management (Art. 17). | Nested in Incident Management |
| Secure Service Recovery | Requirement | Atomic DORA requirement: Restore secure services promptly. It represents COV-101 under Incident Management (Art. 17). | Nested in Incident Management |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-074 | Vulnerability Information → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-01, COV-074, OP-014, OP-038, OP-042, OP-048. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-075 | Cyber Threat Information → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-02, COV-075, OP-014, OP-038, OP-042, OP-048. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-076 | ICT Incident Information → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-03, COV-076, OP-014, OP-038, OP-042, OP-048. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-077 | Resilience Impact Review → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-04, COV-077, OP-014, OP-038, OP-042, OP-048. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-078 | Major Incident Review → Platform Development — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-05, COV-078, OP-014, OP-038, OP-042, OP-048. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-079 | Incident Escalation → ICT Cause Improvements — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-06, COV-079, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-080 | Incident Escalation → Review Communications — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-07, COV-080, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-081 | Incident Escalation → Procedure Effectiveness — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-08, COV-081, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-082 | Incident Escalation → Security Alert Review — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-09, COV-082, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-083 | Incident Escalation → Forensic Quality Review — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-10, COV-083, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-084 | Escalation Review → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-11, COV-084, OP-061, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-085 | Communication Review → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-12, COV-085, OP-061, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-086 | ICT Risk Lessons → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-13, COV-086, OP-061, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-087 | ICT Risk Component Review → Enterprise Data Platform — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-14, COV-087, OP-061, OP-062, OP-063, OP-070, OP-071, OP-072, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078, OP-079, OP-080. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-088 | Resilience Strategy Watch → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-15, COV-088, OP-038, OP-067, OP-087. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-089 | Lessons Reporting → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-16, COV-089, OP-038, OP-067, OP-087. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-090 | Resilience Training → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-17, COV-090, OP-038, OP-067, OP-087. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-091 | Technology Monitoring → Service Update — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art13-18, COV-091, OP-038, OP-067, OP-087. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-092 | Incident Process → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-01, COV-092, OP-070, OP-071, OP-072, OP-073. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-093 | Incident Threat Records → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-02, COV-093, OP-070, OP-071, OP-072, OP-073. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-094 | Monitoring Integration → Incident Escalation — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-03, COV-094, OP-070, OP-071, OP-072, OP-073. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-095 | Incident Escalation → Early Warning Indicators — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-04, COV-095, OP-070, OP-071, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-096 | Incident Escalation → Incident Classification — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-05, COV-096, OP-070, OP-071, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-097 | Incident Escalation → Incident Role Assignment — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-06, COV-097, OP-070, OP-071, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-098 | Incident Escalation → Communication Escalation — Association | supports. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-07, COV-098, OP-070, OP-071, OP-072. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Externally owned |
| REL-COV-099 | Software Remediation → Major Incident Reporting — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-08, COV-099, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-COV-100 | Software Remediation → Mitigate incident impacts — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-09, COV-100, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-COV-101 | Software Remediation → Secure Service Recovery — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art17-10, COV-101, OP-073, OP-074, OP-075, OP-076, OP-077, OP-078. This is the approved direct realization. | Directly performed |
| REL-OP-031 | Back-end Developer → Production Monitoring — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-014. | — |
| REL-OP-032 | Datadog → Production Monitoring — Serving | serves. Drawn because the approved operational or role evidence establishes this exact link: OP-014. | — |
| REL-OP-066 | Back-end Developer → Service Update — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-038. | — |
| REL-OP-079 | Datadog Alarm → Incident Escalation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-070. | — |
| REL-OP-080 | Monitoring Team → Incident Escalation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-070. | — |
| REL-OP-081 | Incident Escalation → Software Remediation — Triggering | triggers. Drawn because the approved operational or role evidence establishes this exact link: OP-071, OP-073. | — |
| REL-OP-083 | Responsible Dev Team → Software Remediation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-075. | — |
| REL-OP-085 | Datadog → Software Remediation — Serving | serves. Drawn because the approved operational or role evidence establishes this exact link: OP-076. | — |
| REL-OP-089 | Software Remediation → Software Fix — Access | writes. Drawn because the approved operational or role evidence establishes this exact link: OP-077. | — |
| REL-OP-093 | Back-end Developer → Enterprise Data Platform — Association | develops for. Drawn because the approved operational or role evidence establishes this exact link: OP-001, OP-002, OP-003. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S074 | ICT Learning → Vulnerability Information | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S075 | ICT Learning → Cyber Threat Information | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S076 | ICT Learning → ICT Incident Information | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S077 | ICT Learning → Resilience Impact Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S078 | ICT Learning → Major Incident Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S079 | ICT Learning → ICT Cause Improvements | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S080 | ICT Learning → Review Communications | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S081 | ICT Learning → Procedure Effectiveness | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S082 | ICT Learning → Security Alert Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S083 | ICT Learning → Forensic Quality Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S084 | ICT Learning → Escalation Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S085 | ICT Learning → Communication Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S086 | ICT Learning → ICT Risk Lessons | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S087 | ICT Learning → ICT Risk Component Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S088 | ICT Learning → Resilience Strategy Watch | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S089 | ICT Learning → Lessons Reporting | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S090 | ICT Learning → Resilience Training | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S091 | ICT Learning → Technology Monitoring | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S092 | Incident Management → Incident Process | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S093 | Incident Management → Incident Threat Records | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S094 | Incident Management → Monitoring Integration | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S095 | Incident Management → Early Warning Indicators | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S096 | Incident Management → Incident Classification | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S097 | Incident Management → Incident Role Assignment | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S098 | Incident Management → Communication Escalation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S099 | Incident Management → Major Incident Reporting | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S100 | Incident Management → Mitigate incident impacts | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S101 | Incident Management → Secure Service Recovery | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

### 2.5. Resilience Testing

**Reading purpose.** This existing model view is a designing view of Resilience Tests (8 nested requirements); Test Method Controls (12 nested requirements). It contains 28 boxes, 25 visible arrows and 20 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements. The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-102, COV-103, COV-104, COV-105, COV-106, COV-107, COV-108, COV-109, COV-110, COV-111, COV-112, COV-113, COV-114, COV-115, COV-116, COV-117, COV-118, COV-119, COV-120, COV-121.

#### Operational reality and daily workflow

The path follows test-and-DEV readiness and pull-request creation, then the technically knowledgeable reviewer’s review. It connects those activities to resilience-test and test-method controls.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** The footprint establishes technical validation but not developer ownership of review. This is an ownership limitation, not a conclusion that testing controls are missing.

**External boundary.** Technical Reviewer and Pull Request Review are outside the developer’s direct realization boundary unless the ledger states direct performance.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| Resilience Tests | Requirement | Parent requirement family for 8 approved coverage rows: COV-102, COV-103, COV-104, COV-105, COV-106, COV-107, COV-108, COV-109. It is the root container for the nested child requirements. | Root family container |
| Test Method Controls | Requirement | Parent requirement family for 12 approved coverage rows: COV-110, COV-111, COV-112, COV-113, COV-114, COV-115, COV-116, COV-117, COV-118, COV-119, COV-120, COV-121. It is the root container for the nested child requirements. | Root family container |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is OP-008. | Root operational / external endpoint |
| Pull Request | Business Object | Approved operational or external endpoint. Its incident relationship evidence is OP-008, OP-009. | Root operational / external endpoint |
| Pull Request Creation | Business Process | Approved operational or external endpoint. Its incident relationship evidence is OP-008. | Root operational / external endpoint |
| Pull Request Review | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art24-06, COV-107, OP-009, OP-047, OP-064, REQ-Art24-07, COV-108, REQ-Art24-08, COV-109. | Root operational / external endpoint |
| Technical Reviewer | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-009. | Root operational / external endpoint |
| Test and DEV Readiness | Business Process | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art24-01, COV-102, OP-008, OP-048, OP-050, REQ-Art24-02, COV-103, REQ-Art24-03, COV-104, OP-059, OP-060, REQ-Art24-04, COV-105, REQ-Art24-05, COV-106, REQ-Art25-01, COV-110, REQ-Art25-02, COV-111, REQ-Art25-03, COV-112, REQ-Art25-04, COV-113, REQ-Art25-05, COV-114, REQ-Art25-06, COV-115, REQ-Art25-07, COV-116, REQ-Art25-08, COV-117, REQ-Art25-09, COV-118, REQ-Art25-10, COV-119, REQ-Art25-11, COV-120, REQ-Art25-12, COV-121. | Root operational / external endpoint |
| Resilience Test Programme | Requirement | Atomic DORA requirement: Establish a resilience-testing programme. It represents COV-102 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Weakness Corrections | Requirement | Atomic DORA requirement: Identify weaknesses and implement corrections. It represents COV-103 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Programme Review | Requirement | Atomic DORA requirement: Maintain and review the programme. It represents COV-104 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Test Method Range | Requirement | Atomic DORA requirement: Use a range of tests and methods. It represents COV-105 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Risk Based Testing | Requirement | Atomic DORA requirement: Apply a risk-based testing approach. It represents COV-106 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Independent Testing | Requirement | Atomic DORA requirement: Use independent testers and avoid conflicts. It represents COV-107 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Test Finding Remediation | Requirement | Atomic DORA requirement: Prioritise and remedy test findings. It represents COV-108 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Annual Critical Tests | Requirement | Atomic DORA requirement: Test critical-function ICT annually. It represents COV-109 under Resilience Tests (Art. 24). | Nested in Resilience Tests |
| Vulnerability Scans | Requirement | Atomic DORA requirement: Perform vulnerability assessments and scans. It represents COV-110 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Open Source Analysis | Requirement | Atomic DORA requirement: Perform open-source analyses. It represents COV-111 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Network Security Review | Requirement | Atomic DORA requirement: Perform network-security assessments. It represents COV-112 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Perform gap analyses | Requirement | Atomic DORA requirement: Perform gap analyses. It represents COV-113 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Physical Security Review | Requirement | Atomic DORA requirement: Perform physical-security reviews. It represents COV-114 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Scanning Questionnaires | Requirement | Atomic DORA requirement: Use questionnaires and scanning tools. It represents COV-115 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Source Code Review | Requirement | Atomic DORA requirement: Perform feasible source-code reviews. It represents COV-116 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Scenario Tests | Requirement | Atomic DORA requirement: Perform scenario-based tests. It represents COV-117 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Compatibility Tests | Requirement | Atomic DORA requirement: Perform compatibility tests. It represents COV-118 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Perform performance tests | Requirement | Atomic DORA requirement: Perform performance tests. It represents COV-119 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Perform end-to-end tests | Requirement | Atomic DORA requirement: Perform end-to-end tests. It represents COV-120 under Test Method Controls (Art. 25). | Nested in Test Method Controls |
| Perform penetration tests | Requirement | Atomic DORA requirement: Perform penetration tests. It represents COV-121 under Test Method Controls (Art. 25). | Nested in Test Method Controls |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-102 | Test and DEV Readiness → Resilience Test Programme — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-01, COV-102, OP-008, OP-048, OP-050. This is the approved direct realization. | Directly performed |
| REL-COV-103 | Test and DEV Readiness → Weakness Corrections — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-02, COV-103, OP-008, OP-048, OP-050. This is the approved direct realization. | Directly performed |
| REL-COV-104 | Programme Review → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-03, COV-104, OP-008, OP-048, OP-059, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-105 | Test Method Range → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-04, COV-105, OP-008, OP-048, OP-059, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-106 | Risk Based Testing → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-05, COV-106, OP-008, OP-048, OP-059, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-107 | Independent Testing → Pull Request Review — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-06, COV-107, OP-009, OP-047, OP-064. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-108 | Test Finding Remediation → Pull Request Review — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-07, COV-108, OP-009, OP-047, OP-064. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-109 | Annual Critical Tests → Pull Request Review — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art24-08, COV-109, OP-009, OP-047, OP-064. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Not evidenced / unclear owner |
| REL-COV-110 | Test and DEV Readiness → Vulnerability Scans — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-01, COV-110, OP-008, OP-048. This is the approved direct realization. | Directly performed |
| REL-COV-111 | Test and DEV Readiness → Open Source Analysis — Realization | realizes. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-02, COV-111, OP-008, OP-048. This is the approved direct realization. | Directly performed |
| REL-COV-112 | Network Security Review → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-03, COV-112, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-113 | Perform gap analyses → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-04, COV-113, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-114 | Physical Security Review → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-05, COV-114, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-115 | Scanning Questionnaires → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-06, COV-115, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-116 | Source Code Review → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-07, COV-116, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-117 | Scenario Tests → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-08, COV-117, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-118 | Compatibility Tests → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-09, COV-118, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-119 | Perform performance tests → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-10, COV-119, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-120 | Perform end-to-end tests → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-11, COV-120, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-121 | Perform penetration tests → Test and DEV Readiness — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art25-12, COV-121, OP-008, OP-048, OP-050. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-OP-014 | Back-end Developer → Test and DEV Readiness — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-008. | — |
| REL-OP-016 | Back-end Developer → Pull Request Creation — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-008. | — |
| REL-OP-017 | Pull Request Creation → Pull Request — Access | writes. Drawn because the approved operational or role evidence establishes this exact link: OP-008. | — |
| REL-OP-018 | Technical Reviewer → Pull Request Review — Assignment | performs. Drawn because the approved operational or role evidence establishes this exact link: OP-009. | — |
| REL-OP-019 | Pull Request Review → Pull Request — Access | reads. Drawn because the approved operational or role evidence establishes this exact link: OP-009. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S102 | Resilience Tests → Resilience Test Programme | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S103 | Resilience Tests → Weakness Corrections | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S104 | Resilience Tests → Programme Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S105 | Resilience Tests → Test Method Range | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S106 | Resilience Tests → Risk Based Testing | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S107 | Resilience Tests → Independent Testing | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S108 | Resilience Tests → Test Finding Remediation | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S109 | Resilience Tests → Annual Critical Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S110 | Test Method Controls → Vulnerability Scans | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S111 | Test Method Controls → Open Source Analysis | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S112 | Test Method Controls → Network Security Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S113 | Test Method Controls → Perform gap analyses | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S114 | Test Method Controls → Physical Security Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S115 | Test Method Controls → Scanning Questionnaires | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S116 | Test Method Controls → Source Code Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S117 | Test Method Controls → Scenario Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S118 | Test Method Controls → Compatibility Tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S119 | Test Method Controls → Perform performance tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S120 | Test Method Controls → Perform end-to-end tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S121 | Test Method Controls → Perform penetration tests | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

### 2.6. Microsoft Cloud Risk

**Reading purpose.** This existing model view is a designing view of Provider Exit Controls (15 nested requirements); Provider Risk Controls (17 nested requirements). It contains 37 boxes, 34 visible arrows and 32 semantic-only containment relationships.

#### How to read this view

Begin at the **Back-end Developer** and follow the approved stakeholder route: Back-end Developer <- Employer Bank -> Microsoft Contract The route connects evidenced work to requirements without converting dependencies, approvals, external teams or contract obligations into developer implementation.

**Coverage in this stream:** COV-122, COV-123, COV-124, COV-125, COV-126, COV-127, COV-128, COV-129, COV-130, COV-131, COV-132, COV-133, COV-134, COV-135, COV-136, COV-137, COV-138, COV-139, COV-140, COV-141, COV-142, COV-143, COV-144, COV-145, COV-146, COV-147, COV-148, COV-149, COV-150, COV-151, COV-152, COV-153.

#### Operational reality and daily workflow

The path follows Employer Bank to the Back-end Developer and the confirmed Employer Bank–Microsoft Contract relationship. It connects the cloud-provider dependency to Article 28 risk and exit controls.

#### Regulatory constraints, potential gaps and ownership boundary

**Constraint and ownership rule.** Each visible regulatory-effect arrow preserves its approved ownership state. Only `Directly performed` is stakeholder realization; `Stakeholder-constrained`, `Externally owned` and `Not evidenced / unclear owner` remain a constraint, dependency, external responsibility or unclear-owner boundary.

**Potential operational or visibility limitation.** The record establishes a contract dependency, not stakeholder contract negotiation, management or oversight. Any lack of visibility is a role boundary rather than a compliance conclusion.

**External boundary.** Employer Bank and Microsoft Contract are external to the execution role; Article 28 rows are contract constraints, not developer realization.

#### Visible boxes and containment

| Box | ArchiMate element type | What it represents and why it is present | Containment |
| --- | --- | --- | --- |
| Provider Exit Controls | Requirement | Parent requirement family for 15 approved coverage rows: COV-139, COV-140, COV-141, COV-142, COV-143, COV-144, COV-145, COV-146, COV-147, COV-148, COV-149, COV-150, COV-151, COV-152, COV-153. It is the root container for the nested child requirements. | Root family container |
| Provider Risk Controls | Requirement | Parent requirement family for 17 approved coverage rows: COV-122, COV-123, COV-124, COV-125, COV-126, COV-127, COV-128, COV-129, COV-130, COV-131, COV-132, COV-133, COV-134, COV-135, COV-136, COV-137, COV-138. It is the root container for the nested child requirements. | Root family container |
| Back-end Developer | Business Role | Approved operational or external endpoint. Its incident relationship evidence is ROLE-Employer-Bank. | Root operational / external endpoint |
| Employer Bank | Business Actor | Approved operational or external endpoint. Its incident relationship evidence is OP-023, SRC-Operator-Microsoft-Contract, ROLE-Employer-Bank. | Root operational / external endpoint |
| Microsoft Contract | Contract | Approved operational or external endpoint. Its incident relationship evidence is REQ-Art28-01, COV-122, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060, REQ-Art28-02, COV-123, REQ-Art28-03, COV-124, REQ-Art28-04, COV-125, REQ-Art28-05, COV-126, REQ-Art28-06, COV-127, REQ-Art28-07, COV-128, REQ-Art28-08, COV-129, REQ-Art28-09, COV-130, REQ-Art28-10, COV-131, REQ-Art28-11, COV-132, REQ-Art28-12, COV-133, REQ-Art28-13, COV-134, REQ-Art28-14, COV-135, REQ-Art28-15, COV-136, REQ-Art28-16, COV-137, REQ-Art28-17, COV-138, REQ-Art28-18, COV-139, REQ-Art28-19, COV-140, REQ-Art28-20, COV-141, REQ-Art28-21, COV-142, REQ-Art28-22, COV-143, REQ-Art28-23, COV-144, REQ-Art28-24, COV-145, REQ-Art28-25, COV-146, REQ-Art28-26, COV-147, REQ-Art28-27, COV-148, REQ-Art28-28, COV-149, REQ-Art28-29, COV-150, REQ-Art28-30, COV-151, REQ-Art28-31, COV-152, REQ-Art28-32, COV-153, SRC-Operator-Microsoft-Contract. | Root operational / external endpoint |
| ICT Provider Risk Control | Requirement | Atomic DORA requirement: Manage ICT third-party risk within ICT risk management. It represents COV-122 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| DORA Compliance Duty | Requirement | Atomic DORA requirement: Retain responsibility for DORA compliance. It represents COV-123 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Provider Risk Control | Requirement | Atomic DORA requirement: Apply proportional third-party risk management. It represents COV-124 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| ICT Dependency Assessment | Requirement | Atomic DORA requirement: Assess ICT-related dependencies. It represents COV-125 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Critical Contract Risk | Requirement | Atomic DORA requirement: Assess contractual critical-function risk. It represents COV-126 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Provider Risk Policy | Requirement | Atomic DORA requirement: Maintain third-party risk strategy and policy. It represents COV-127 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Provider Risk Review | Requirement | Atomic DORA requirement: Have management review third-party risks. It represents COV-128 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Contract Register | Requirement | Atomic DORA requirement: Maintain a third-party contract register. It represents COV-129 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Contract Records | Requirement | Atomic DORA requirement: Document and classify contractual arrangements. It represents COV-130 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Annual Arrangement Report | Requirement | Atomic DORA requirement: Report annual arrangement information. It represents COV-131 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Authority Register Access | Requirement | Atomic DORA requirement: Provide the register to competent authorities. It represents COV-132 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Arrangement Notice | Requirement | Atomic DORA requirement: Notify planned critical arrangements. It represents COV-133 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Service Criticality | Requirement | Atomic DORA requirement: Assess whether a service supports a critical function. It represents COV-134 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Supervisory Check | Requirement | Atomic DORA requirement: Assess supervisory contracting conditions. It represents COV-135 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Concentration Risk | Requirement | Atomic DORA requirement: Assess contractual and concentration risks. It represents COV-136 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Provider Due Diligence | Requirement | Atomic DORA requirement: Perform provider due diligence. It represents COV-137 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Contract Conflict Check | Requirement | Atomic DORA requirement: Assess contractual conflicts of interest. It represents COV-138 under Provider Risk Controls (Art. 28). | Nested in Provider Risk Controls |
| Secure Provider Selection | Requirement | Atomic DORA requirement: Use providers meeting security standards. It represents COV-139 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Provider Audit Plan | Requirement | Atomic DORA requirement: Plan risk-based provider audits. It represents COV-140 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Skilled Auditor Use | Requirement | Atomic DORA requirement: Use suitably skilled auditors. It represents COV-141 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Termination Rights | Requirement | Atomic DORA requirement: Provide contractual termination rights. It represents COV-142 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Significant Breach Exit | Requirement | Atomic DORA requirement: Terminate for significant breach. It represents COV-143 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Risk Change Exit | Requirement | Atomic DORA requirement: Terminate for material risk changes. It represents COV-144 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Provider Weakness Exit | Requirement | Atomic DORA requirement: Terminate for provider ICT-risk weaknesses. It represents COV-145 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Impaired Supervision Exit | Requirement | Atomic DORA requirement: Terminate where supervision is impaired. It represents COV-146 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Critical Exit Strategy | Requirement | Atomic DORA requirement: Maintain critical-function exit strategies. It represents COV-147 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Business Continuity Exit | Requirement | Atomic DORA requirement: Exit without business disruption. It represents COV-148 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Compliance Exit | Requirement | Atomic DORA requirement: Exit without limiting regulatory compliance. It represents COV-149 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Service Continuity Exit | Requirement | Atomic DORA requirement: Exit without harming client-service continuity. It represents COV-150 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Exit Plan Review | Requirement | Atomic DORA requirement: Document, test and review exit plans. It represents COV-151 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Transition Alternatives | Requirement | Atomic DORA requirement: Prepare alternative solutions and transition plans. It represents COV-152 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |
| Exit Contingency Measures | Requirement | Atomic DORA requirement: Maintain exit contingency measures. It represents COV-153 under Provider Exit Controls (Art. 28). | Nested in Provider Exit Controls |

#### Visible arrows

| Relationship | Direction and ArchiMate type | Evidence-backed meaning and reason for visibility | Ownership implication |
| --- | --- | --- | --- |
| REL-COV-122 | ICT Provider Risk Control → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-01, COV-122, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-123 | DORA Compliance Duty → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-02, COV-123, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-124 | Provider Risk Control → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-03, COV-124, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-125 | ICT Dependency Assessment → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-04, COV-125, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-126 | Critical Contract Risk → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-05, COV-126, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-127 | Provider Risk Policy → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-06, COV-127, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-128 | Provider Risk Review → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-07, COV-128, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-129 | Contract Register → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-08, COV-129, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-130 | Contract Records → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-09, COV-130, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-131 | Annual Arrangement Report → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-10, COV-131, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-132 | Authority Register Access → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-11, COV-132, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-133 | Arrangement Notice → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-12, COV-133, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-134 | Service Criticality → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-13, COV-134, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-135 | Supervisory Check → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-14, COV-135, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-136 | Concentration Risk → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-15, COV-136, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-137 | Provider Due Diligence → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-16, COV-137, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-138 | Contract Conflict Check → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-17, COV-138, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-139 | Secure Provider Selection → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-18, COV-139, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-140 | Provider Audit Plan → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-19, COV-140, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-141 | Skilled Auditor Use → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-20, COV-141, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-142 | Termination Rights → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-21, COV-142, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-143 | Significant Breach Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-22, COV-143, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-144 | Risk Change Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-23, COV-144, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-145 | Provider Weakness Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-24, COV-145, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-146 | Impaired Supervision Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-25, COV-146, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-147 | Critical Exit Strategy → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-26, COV-147, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-148 | Business Continuity Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-27, COV-148, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-149 | Compliance Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-28, COV-149, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-150 | Service Continuity Exit → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-29, COV-150, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-151 | Exit Plan Review → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-30, COV-151, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-152 | Transition Alternatives → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-31, COV-152, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-COV-153 | Exit Contingency Measures → Microsoft Contract — Association | legally applies to / constrains. Drawn as the approved regulatory-effect edge; evidence: REQ-Art28-32, COV-153, OP-023, OP-024, OP-025, OP-026, OP-068, OP-060. This is a constraint, external responsibility, or unclear-owner boundary—not developer realization. | Stakeholder-constrained |
| REL-OP-094 | Employer Bank → Microsoft Contract — Association | is party to. Drawn because the approved operational or role evidence establishes this exact link: OP-023, SRC-Operator-Microsoft-Contract. | — |
| REL-ROLE-001 | Employer Bank → Back-end Developer — Assignment | assigns the stakeholder role. Drawn because the approved operational or role evidence establishes this exact link: ROLE-Employer-Bank. | — |

#### Semantic-only nesting

The following Composition relationships are not drawn as internal arrows. In the existing view, the child requirement is nested inside its named parent family; that nesting carries the containment meaning.

| Relationship | Nested parent → child | Meaning carried by containment |
| --- | --- | --- |
| REL-COMP-S122 | Provider Risk Controls → ICT Provider Risk Control | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S123 | Provider Risk Controls → DORA Compliance Duty | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S124 | Provider Risk Controls → Provider Risk Control | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S125 | Provider Risk Controls → ICT Dependency Assessment | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S126 | Provider Risk Controls → Critical Contract Risk | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S127 | Provider Risk Controls → Provider Risk Policy | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S128 | Provider Risk Controls → Provider Risk Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S129 | Provider Risk Controls → Contract Register | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S130 | Provider Risk Controls → Contract Records | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S131 | Provider Risk Controls → Annual Arrangement Report | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S132 | Provider Risk Controls → Authority Register Access | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S133 | Provider Risk Controls → Arrangement Notice | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S134 | Provider Risk Controls → Service Criticality | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S135 | Provider Risk Controls → Supervisory Check | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S136 | Provider Risk Controls → Concentration Risk | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S137 | Provider Risk Controls → Provider Due Diligence | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S138 | Provider Risk Controls → Contract Conflict Check | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S139 | Provider Exit Controls → Secure Provider Selection | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S140 | Provider Exit Controls → Provider Audit Plan | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S141 | Provider Exit Controls → Skilled Auditor Use | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S142 | Provider Exit Controls → Termination Rights | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S143 | Provider Exit Controls → Significant Breach Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S144 | Provider Exit Controls → Risk Change Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S145 | Provider Exit Controls → Provider Weakness Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S146 | Provider Exit Controls → Impaired Supervision Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S147 | Provider Exit Controls → Critical Exit Strategy | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S148 | Provider Exit Controls → Business Continuity Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S149 | Provider Exit Controls → Compliance Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S150 | Provider Exit Controls → Service Continuity Exit | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S151 | Provider Exit Controls → Exit Plan Review | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S152 | Provider Exit Controls → Transition Alternatives | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |
| REL-COMP-S153 | Provider Exit Controls → Exit Contingency Measures | Composition: contains the scoped requirement; no internal arrow is drawn because visual nesting communicates the approved parent-child relationship. |

## 3. Layer-by-layer ArchiMate guide

The six stakeholder views use ArchiMate as a vocabulary for the approved evidence-backed graph. A **Requirement** expresses a DORA demand; a **Business Role**, **Business Actor**, **Business Process**, **Business Event** or **Business Object** expresses people, work, events and information; an **Application Component** or **Application Process** expresses software structure or software behaviour; and a **Contract** expresses the recorded Microsoft agreement boundary.

- **Motivation layer:** 13 named parent requirement families and 153 child Requirements. Families contain their statutory duties; Composition is nesting, not an internal arrow.
- **Business layer:** the stakeholder role, actors, development, monitoring, escalation, remediation, readiness, pull-request and service-update processes, with their events and business objects.
- **Application layer:** Enterprise Data Platform, Internal Framework, Offload Service, Azure AD Access Control and Datadog, plus the Data Offload Flow application process, only where approved evidence supports them.
- **Technology layer:** no Technology Node, System Software or execution-environment element is placed in the six formal views. Kubernetes and infrastructure facts remain external context or named external dependencies; this explanation does not invent technical ownership.
- **Implementation and migration layer:** no Work Package or Deliverable is placed in the approved graph. Development and remediation remain represented by their approved business/application endpoints.

## 4. Comprehensive element, requirement and realization traceability

Each approved coverage row appears once below. Readable article citations are retained; canonical legal-text identifiers are deliberately excluded. The representing endpoint comes from the approved directional regulatory-effect relationship, and the operational meaning is copied from the approved Step 5 ledger.

| Coverage ID | Operational source ID(s) | Parent family / context stream | Requirement ID | Source citation | Ownership state | Representing element or external role | Operational meaning |
| --- | --- | --- | --- | --- | --- | --- |
| COV-001 | OP-004, OP-038 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art7-01 | Art. 7 | Directly performed | Framework Maintenance | Framework Maintenance realizes REQ-Art7-01 |
| COV-002 | OP-004, OP-038 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art7-02 | Art. 7 | Directly performed | Framework Maintenance | Framework Maintenance realizes REQ-Art7-02 |
| COV-003 | OP-050, OP-060, CON-006 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art7-03 | Art. 7 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art7-03 |
| COV-004 | OP-050, OP-060, CON-006 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art7-04 | Art. 7 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art7-04 |
| COV-005 | OP-006, OP-018–019, OP-066, OP-081–082 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-01 | Art. 8 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art8-01 |
| COV-006 | OP-006, OP-018–019, OP-066, OP-081–082 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-02 | Art. 8 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art8-02 |
| COV-007 | OP-006, OP-018–019, OP-066, OP-081–082 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-03 | Art. 8 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art8-03 |
| COV-008 | OP-038, OP-041–042, OP-052, CON-001 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-04 | Art. 8 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art8-04 |
| COV-009 | OP-038, OP-041–042, OP-052, CON-001 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-05 | Art. 8 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art8-05 |
| COV-010 | OP-038, OP-041–042, OP-052, CON-001 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-06 | Art. 8 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art8-06 |
| COV-011 | OP-023–026, OP-027–029, OP-068 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-07 | Art. 8 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art8-07 |
| COV-012 | OP-023–026, OP-027–029, OP-068 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-08 | Art. 8 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art8-08 |
| COV-013 | OP-023–026, OP-027–029, OP-068 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-09 | Art. 8 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art8-09 |
| COV-014 | OP-023–026, OP-027–029, OP-068 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-10 | Art. 8 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art8-10 |
| COV-015 | OP-023–026, OP-027–029, OP-068 | ICT Asset Controls / ICT Systems & Asset Governance | REQ-Art8-11 | Art. 8 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art8-11 |
| COV-016 | OP-006, OP-048, OP-065, OP-081 | Data Protection / Protection & Controlled Change | REQ-Art9-01 | Art. 9 | Stakeholder-constrained | Data Offload Flow | Data Offload Flow is constrained by REQ-Art9-01 |
| COV-017 | OP-006, OP-048, OP-065, OP-081 | Data Protection / Protection & Controlled Change | REQ-Art9-02 | Art. 9 | Stakeholder-constrained | Data Offload Flow | Data Offload Flow is constrained by REQ-Art9-02 |
| COV-018 | OP-006, OP-048, OP-065, OP-081 | Data Protection / Protection & Controlled Change | REQ-Art9-03 | Art. 9 | Stakeholder-constrained | Data Offload Flow | Data Offload Flow is constrained by REQ-Art9-03 |
| COV-019 | OP-006, OP-048, OP-065, OP-081 | Data Protection / Protection & Controlled Change | REQ-Art9-04 | Art. 9 | Stakeholder-constrained | Data Offload Flow | Data Offload Flow is constrained by REQ-Art9-04 |
| COV-020 | OP-031–036, OP-088 | Data Protection / Protection & Controlled Change | REQ-Art9-05 | Art. 9 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art9-05 |
| COV-021 | OP-031–036, OP-088 | Data Protection / Protection & Controlled Change | REQ-Art9-06 | Art. 9 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art9-06 |
| COV-022 | OP-031–036, OP-088 | Data Protection / Protection & Controlled Change | REQ-Art9-07 | Art. 9 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art9-07 |
| COV-023 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | Data Protection / Protection & Controlled Change | REQ-Art9-08 | Art. 9 | Externally owned | Azure AD Access Control | Azure AD / Internal Service Access realizes part of REQ-Art9-08 |
| COV-024 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | Data Protection / Protection & Controlled Change | REQ-Art9-09 | Art. 9 | Externally owned | Azure AD Access Control | Azure AD / Internal Service Access realizes part of REQ-Art9-09 |
| COV-025 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | Data Protection / Protection & Controlled Change | REQ-Art9-10 | Art. 9 | Externally owned | Azure AD Access Control | Azure AD / Internal Service Access realizes part of REQ-Art9-10 |
| COV-026 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Change Controls / Protection & Controlled Change | REQ-Art9-11 | Art. 9 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art9-11 |
| COV-027 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Change Controls / Protection & Controlled Change | REQ-Art9-12 | Art. 9 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art9-12 |
| COV-028 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Change Controls / Protection & Controlled Change | REQ-Art9-13 | Art. 9 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art9-13 |
| COV-029 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Change Controls / Protection & Controlled Change | REQ-Art9-14 | Art. 9 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art9-14 |
| COV-030 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Change Controls / Protection & Controlled Change | REQ-Art9-15 | Art. 9 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art9-15 |
| COV-031 | OP-038, OP-041–042 | Change Controls / Protection & Controlled Change | REQ-Art9-16 | Art. 9 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art9-16 |
| COV-032 | OP-038, OP-041–042 | Change Controls / Protection & Controlled Change | REQ-Art9-17 | Art. 9 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art9-17 |
| COV-033 | OP-038, OP-041–042 | Change Controls / Protection & Controlled Change | REQ-Art9-18 | Art. 9 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art9-18 |
| COV-034 | OP-038, OP-041–042 | Change Controls / Protection & Controlled Change | REQ-Art9-19 | Art. 9 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art9-19 |
| COV-035 | OP-014, OP-070, OP-072 | ICT Detection / Detection & Continuity | REQ-Art10-01 | Art. 10 | Stakeholder-constrained | Production Monitoring | Production Monitoring is constrained by REQ-Art10-01 |
| COV-036 | OP-014, OP-070, OP-072 | ICT Detection / Detection & Continuity | REQ-Art10-02 | Art. 10 | Stakeholder-constrained | Production Monitoring | Production Monitoring is constrained by REQ-Art10-02 |
| COV-037 | OP-070, OP-072, OP-076 | ICT Detection / Detection & Continuity | REQ-Art10-03 | Art. 10 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art10-03 |
| COV-038 | OP-070, OP-072, OP-076 | ICT Detection / Detection & Continuity | REQ-Art10-04 | Art. 10 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art10-04 |
| COV-039 | OP-070, OP-072, OP-076 | ICT Detection / Detection & Continuity | REQ-Art10-05 | Art. 10 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art10-05 |
| COV-040 | OP-070, OP-072, OP-076 | ICT Detection / Detection & Continuity | REQ-Art10-06 | Art. 10 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art10-06 |
| COV-041 | OP-060, OP-070–080; operator critical-function clarification | Continuity Response / Detection & Continuity | REQ-Art11-01 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-01 |
| COV-042 | OP-060, OP-070–080; operator critical-function clarification | Continuity Response / Detection & Continuity | REQ-Art11-02 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-02 |
| COV-043 | OP-060, OP-070–080; operator critical-function clarification | Continuity Response / Detection & Continuity | REQ-Art11-03 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-03 |
| COV-044 | OP-060, OP-070–080; operator critical-function clarification | Continuity Response / Detection & Continuity | REQ-Art11-04 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-04 |
| COV-045 | OP-071, OP-073–078 | Continuity Response / Detection & Continuity | REQ-Art11-05 | Art. 11 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art11-05 |
| COV-046 | OP-071, OP-073–078 | Continuity Response / Detection & Continuity | REQ-Art11-06 | Art. 11 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art11-06 |
| COV-047 | OP-071, OP-073–078 | Continuity Response / Detection & Continuity | REQ-Art11-07 | Art. 11 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art11-07 |
| COV-048 | OP-060, OP-071, OP-079–080 | Continuity Response / Detection & Continuity | REQ-Art11-08 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-08 |
| COV-049 | OP-060, OP-071, OP-079–080 | Continuity Response / Detection & Continuity | REQ-Art11-09 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-09 |
| COV-050 | OP-060, OP-071, OP-079–080 | Continuity Response / Detection & Continuity | REQ-Art11-10 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-10 |
| COV-051 | OP-062–063, OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-11 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-11 |
| COV-052 | OP-062–063, OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-12 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-12 |
| COV-053 | OP-062–063, OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-13 | Art. 11 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art11-13 |
| COV-054 | OP-060, OP-068 | Continuity Testing / Detection & Continuity | REQ-Art11-14 | Art. 11 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art11-14 |
| COV-055 | OP-060, OP-068 | Continuity Testing / Detection & Continuity | REQ-Art11-15 | Art. 11 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art11-15 |
| COV-056 | OP-060, OP-068 | Continuity Testing / Detection & Continuity | REQ-Art11-16 | Art. 11 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art11-16 |
| COV-057 | OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-17 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-17 |
| COV-058 | OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-18 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-18 |
| COV-059 | OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-19 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-19 |
| COV-060 | OP-070–080 | Continuity Testing / Detection & Continuity | REQ-Art11-20 | Art. 11 | Not evidenced / unclear owner | Incident Escalation | Incident Escalation is subject to REQ-Art11-20 |
| COV-061 | OP-062–063, OP-073, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-01 | Art. 12 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art12-01 |
| COV-062 | OP-062–063, OP-073, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-02 | Art. 12 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art12-02 |
| COV-063 | OP-062–063, OP-073, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-03 | Art. 12 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art12-03 |
| COV-064 | OP-062–063, OP-073, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-04 | Art. 12 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art12-04 |
| COV-065 | OP-027–029, OP-063, OP-074–075, OP-078 | Backup and Recovery / Detection & Continuity | REQ-Art12-05 | Art. 12 | Externally owned | Infra Remediation | Infrastructure Remediation realizes part of REQ-Art12-05 |
| COV-066 | OP-027–029, OP-063, OP-074–075, OP-078 | Backup and Recovery / Detection & Continuity | REQ-Art12-06 | Art. 12 | Externally owned | Infra Remediation | Infrastructure Remediation realizes part of REQ-Art12-06 |
| COV-067 | OP-027–029, OP-063, OP-074–075, OP-078 | Backup and Recovery / Detection & Continuity | REQ-Art12-07 | Art. 12 | Externally owned | Infra Remediation | Infrastructure Remediation realizes part of REQ-Art12-07 |
| COV-068 | OP-027–029, OP-063, OP-074–075, OP-078 | Backup and Recovery / Detection & Continuity | REQ-Art12-08 | Art. 12 | Externally owned | Infra Remediation | Infrastructure Remediation realizes part of REQ-Art12-08 |
| COV-069 | OP-048, OP-065, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-09 | Art. 12 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art12-09 |
| COV-070 | OP-048, OP-065, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-10 | Art. 12 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art12-10 |
| COV-071 | OP-048, OP-065, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-11 | Art. 12 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art12-11 |
| COV-072 | OP-048, OP-065, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-12 | Art. 12 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art12-12 |
| COV-073 | OP-048, OP-065, OP-078, OP-080 | Backup and Recovery / Detection & Continuity | REQ-Art12-13 | Art. 12 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art12-13 |
| COV-074 | OP-014, OP-038, OP-042, OP-048 | ICT Learning / Learning & Incident Management | REQ-Art13-01 | Art. 13 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art13-01 |
| COV-075 | OP-014, OP-038, OP-042, OP-048 | ICT Learning / Learning & Incident Management | REQ-Art13-02 | Art. 13 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art13-02 |
| COV-076 | OP-014, OP-038, OP-042, OP-048 | ICT Learning / Learning & Incident Management | REQ-Art13-03 | Art. 13 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art13-03 |
| COV-077 | OP-014, OP-038, OP-042, OP-048 | ICT Learning / Learning & Incident Management | REQ-Art13-04 | Art. 13 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art13-04 |
| COV-078 | OP-014, OP-038, OP-042, OP-048 | ICT Learning / Learning & Incident Management | REQ-Art13-05 | Art. 13 | Stakeholder-constrained | Platform Development | Platform Development is constrained by REQ-Art13-05 |
| COV-079 | OP-070–076 | ICT Learning / Learning & Incident Management | REQ-Art13-06 | Art. 13 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art13-06 |
| COV-080 | OP-070–076 | ICT Learning / Learning & Incident Management | REQ-Art13-07 | Art. 13 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art13-07 |
| COV-081 | OP-070–076 | ICT Learning / Learning & Incident Management | REQ-Art13-08 | Art. 13 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art13-08 |
| COV-082 | OP-070–076 | ICT Learning / Learning & Incident Management | REQ-Art13-09 | Art. 13 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art13-09 |
| COV-083 | OP-070–076 | ICT Learning / Learning & Incident Management | REQ-Art13-10 | Art. 13 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art13-10 |
| COV-084 | OP-061–063, OP-070–080 | ICT Learning / Learning & Incident Management | REQ-Art13-11 | Art. 13 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art13-11 |
| COV-085 | OP-061–063, OP-070–080 | ICT Learning / Learning & Incident Management | REQ-Art13-12 | Art. 13 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art13-12 |
| COV-086 | OP-061–063, OP-070–080 | ICT Learning / Learning & Incident Management | REQ-Art13-13 | Art. 13 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art13-13 |
| COV-087 | OP-061–063, OP-070–080 | ICT Learning / Learning & Incident Management | REQ-Art13-14 | Art. 13 | Not evidenced / unclear owner | Enterprise Data Platform | Enterprise Data Platform is subject to REQ-Art13-14 |
| COV-088 | OP-038, OP-067, OP-087 | ICT Learning / Learning & Incident Management | REQ-Art13-15 | Art. 13 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art13-15 |
| COV-089 | OP-038, OP-067, OP-087 | ICT Learning / Learning & Incident Management | REQ-Art13-16 | Art. 13 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art13-16 |
| COV-090 | OP-038, OP-067, OP-087 | ICT Learning / Learning & Incident Management | REQ-Art13-17 | Art. 13 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art13-17 |
| COV-091 | OP-038, OP-067, OP-087 | ICT Learning / Learning & Incident Management | REQ-Art13-18 | Art. 13 | Stakeholder-constrained | Service Update | Service Update is constrained by REQ-Art13-18 |
| COV-092 | OP-070–073 | Incident Management / Learning & Incident Management | REQ-Art17-01 | Art. 17 | Stakeholder-constrained | Incident Escalation | Incident Escalation is constrained by REQ-Art17-01 |
| COV-093 | OP-070–073 | Incident Management / Learning & Incident Management | REQ-Art17-02 | Art. 17 | Stakeholder-constrained | Incident Escalation | Incident Escalation is constrained by REQ-Art17-02 |
| COV-094 | OP-070–073 | Incident Management / Learning & Incident Management | REQ-Art17-03 | Art. 17 | Stakeholder-constrained | Incident Escalation | Incident Escalation is constrained by REQ-Art17-03 |
| COV-095 | OP-070–072 | Incident Management / Learning & Incident Management | REQ-Art17-04 | Art. 17 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art17-04 |
| COV-096 | OP-070–072 | Incident Management / Learning & Incident Management | REQ-Art17-05 | Art. 17 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art17-05 |
| COV-097 | OP-070–072 | Incident Management / Learning & Incident Management | REQ-Art17-06 | Art. 17 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art17-06 |
| COV-098 | OP-070–072 | Incident Management / Learning & Incident Management | REQ-Art17-07 | Art. 17 | Externally owned | Incident Escalation | Incident Escalation realizes part of REQ-Art17-07 |
| COV-099 | OP-073–078 | Incident Management / Learning & Incident Management | REQ-Art17-08 | Art. 17 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art17-08 |
| COV-100 | OP-073–078 | Incident Management / Learning & Incident Management | REQ-Art17-09 | Art. 17 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art17-09 |
| COV-101 | OP-073–078 | Incident Management / Learning & Incident Management | REQ-Art17-10 | Art. 17 | Directly performed | Software Remediation | Software Remediation realizes REQ-Art17-10 |
| COV-102 | OP-008, OP-048, OP-050 | Resilience Tests / Resilience Testing | REQ-Art24-01 | Art. 24 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art24-01 |
| COV-103 | OP-008, OP-048, OP-050 | Resilience Tests / Resilience Testing | REQ-Art24-02 | Art. 24 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art24-02 |
| COV-104 | OP-008, OP-048, OP-059–060 | Resilience Tests / Resilience Testing | REQ-Art24-03 | Art. 24 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art24-03 |
| COV-105 | OP-008, OP-048, OP-059–060 | Resilience Tests / Resilience Testing | REQ-Art24-04 | Art. 24 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art24-04 |
| COV-106 | OP-008, OP-048, OP-059–060 | Resilience Tests / Resilience Testing | REQ-Art24-05 | Art. 24 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art24-05 |
| COV-107 | OP-009, OP-047, OP-064 | Resilience Tests / Resilience Testing | REQ-Art24-06 | Art. 24 | Not evidenced / unclear owner | Pull Request Review | Pull Request Review is subject to REQ-Art24-06 |
| COV-108 | OP-009, OP-047, OP-064 | Resilience Tests / Resilience Testing | REQ-Art24-07 | Art. 24 | Not evidenced / unclear owner | Pull Request Review | Pull Request Review is subject to REQ-Art24-07 |
| COV-109 | OP-009, OP-047, OP-064 | Resilience Tests / Resilience Testing | REQ-Art24-08 | Art. 24 | Not evidenced / unclear owner | Pull Request Review | Pull Request Review is subject to REQ-Art24-08 |
| COV-110 | OP-008, OP-048 | Test Method Controls / Resilience Testing | REQ-Art25-01 | Art. 25 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art25-01 |
| COV-111 | OP-008, OP-048 | Test Method Controls / Resilience Testing | REQ-Art25-02 | Art. 25 | Directly performed | Test and DEV Readiness | Test and DEV Readiness realizes REQ-Art25-02 |
| COV-112 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-03 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-03 |
| COV-113 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-04 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-04 |
| COV-114 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-05 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-05 |
| COV-115 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-06 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-06 |
| COV-116 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-07 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-07 |
| COV-117 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-08 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-08 |
| COV-118 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-09 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-09 |
| COV-119 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-10 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-10 |
| COV-120 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-11 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-11 |
| COV-121 | OP-008, OP-048, OP-050 | Test Method Controls / Resilience Testing | REQ-Art25-12 | Art. 25 | Stakeholder-constrained | Test and DEV Readiness | Test and DEV Readiness is constrained by REQ-Art25-12 |
| COV-122 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-01 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-01 |
| COV-123 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-02 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-02 |
| COV-124 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-03 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-03 |
| COV-125 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-04 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-04 |
| COV-126 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-05 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-05 |
| COV-127 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-06 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-06 |
| COV-128 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-07 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-07 |
| COV-129 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-08 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-08 |
| COV-130 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-09 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-09 |
| COV-131 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-10 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-10 |
| COV-132 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-11 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-11 |
| COV-133 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-12 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-12 |
| COV-134 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-13 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-13 |
| COV-135 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-14 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-14 |
| COV-136 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-15 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-15 |
| COV-137 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-16 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-16 |
| COV-138 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Risk Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-17 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-17 |
| COV-139 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-18 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-18 |
| COV-140 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-19 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-19 |
| COV-141 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-20 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-20 |
| COV-142 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-21 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-21 |
| COV-143 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-22 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-22 |
| COV-144 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-23 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-23 |
| COV-145 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-24 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-24 |
| COV-146 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-25 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-25 |
| COV-147 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-26 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-26 |
| COV-148 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-27 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-27 |
| COV-149 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-28 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-28 |
| COV-150 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-29 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-29 |
| COV-151 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-30 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-30 |
| COV-152 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-31 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-31 |
| COV-153 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | Provider Exit Controls / Microsoft Cloud Third-Party Risk | REQ-Art28-32 | Art. 28 | Stakeholder-constrained | Microsoft Contract | Microsoft Contract is subject to REQ-Art28-32 |

## 5. Fidelity record

The explanation accounts for 349 per-view relationship memberships across the six existing model views. Each view is a single weakly connected component with no isolated semantic elements according to the approved graph validator. It preserves family nesting, relationship direction, relationship type, evidence references and ownership distinction; it does not make a compliance claim.
