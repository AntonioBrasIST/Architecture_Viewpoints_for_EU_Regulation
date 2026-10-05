# DORA Infrastructure Resilience — View Explanation

**Pipeline stage:** Step 8 — approved walkthrough draft

## 1. Executive Overview & Stakeholder Operational Scope

### View 0 — Stakeholder-Aware Regulation Map

The immutable baseline starts at **Infra Eng & Cloud DBA**, proceeds through **Bank** and the law-defined **DORA financial entity**, and reaches the **DORA Resilience Framework**. This route establishes the perspective from which the views are read; it does not assert Bank compliance or equate the stakeholder with the regulated entity.

### Target role and operational scope

The stakeholder is a senior Infrastructure Engineer / Cloud Database Administrator. The approved footprint covers internal infrastructure, cloud platform administration, production database administration, on-call recovery, access work, controlled changes, monitoring, and support handoffs for the confirmed Starburst, OpenMetadata, and SingleStore provider-supported platforms.

### Legislative mandate summary

- DORA Articles 6–14, 17–18, 24, and 25 are represented only where the approved coverage ledger records an operational chain.
- The role directly performs only the activities represented by **Realization**; constrained, externally owned, and unclear-owner records remain Associations.
- The view set keeps continuity preparedness, recovery/restoration, and operational learning as separate concerns.

### Coverage statement

All 162 approved coverage records and all 60 approved operational relationships are represented in the graph. Operational context that has no legal coverage remains in its dedicated context view; no legal obligation is inferred from that context.

## 2. Per-View Visual Walkthroughs


### DORA Regulation Overview

#### How to read this view

The view answers the approved concern for **DORA Regulation Overview**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA Scope and Proportion | Constraint | Legal control family nested in the DORA framework. |
| Apply DORA scope | Constraint | Nested DORA legal child (Art. 2(1)). |
| Scale ICT risk controls | Requirement | Nested DORA legal child (Art. 4(1)). |
| ICT Governance | Requirement | Legal control family nested in the DORA framework. |
| Govern ICT risk | Requirement | Nested DORA legal child (Art. 5(1)). |
| ICT Risk Framework | Requirement | Legal control family nested in the DORA framework. |
| Set ICT risk framework | Requirement | Nested DORA legal child (Art. 6(1)). |
| Set ICT control standards | Requirement | Nested DORA legal child (Art. 15(1)). |
| Use simplified framework | Constraint | Nested DORA legal child (Art. 16(1)). |
| ICT Assets and Systems | Requirement | Legal control family nested in the DORA framework. |
| Maintain ICT systems | Requirement | Nested DORA legal child (Art. 7(1)). |
| Identify ICT assets | Requirement | Nested DORA legal child (Art. 8(1)). |
| Security and Detection | Requirement | Legal control family nested in the DORA framework. |
| Protect ICT systems | Requirement | Nested DORA legal child (Art. 9(1)). |
| Detect ICT anomalies | Requirement | Nested DORA legal child (Art. 10(1)). |
| Continuity and Recovery | Requirement | Legal control family nested in the DORA framework. |
| Maintain ICT continuity | Requirement | Nested DORA legal child (Art. 11(1)). |
| Restore ICT systems | Requirement | Nested DORA legal child (Art. 12(1)). |
| Resilience Learning | Requirement | Legal control family nested in the DORA framework. |
| Learn from ICT events | Requirement | Nested DORA legal child (Art. 13(1)). |
| Communicate ICT crises | Requirement | Nested DORA legal child (Art. 14(1)). |
| ICT Incident Reporting | Requirement | Legal control family nested in the DORA framework. |
| Manage ICT incidents | Requirement | Nested DORA legal child (Art. 17(1)). |
| Classify ICT incidents | Requirement | Nested DORA legal child (Art. 18(1)). |
| Report major incidents | Requirement | Nested DORA legal child (Art. 19(1)). |
| Set incident report rules | Requirement | Nested DORA legal child (Art. 20(1)). |
| Centralise ICT reports | Requirement | Nested DORA legal child (Art. 21(1)). |
| Give incident feedback | Requirement | Nested DORA legal child (Art. 22(1)). |
| Cover payment incidents | Requirement | Nested DORA legal child (Art. 23(1)). |
| Resilience Testing | Requirement | Legal control family nested in the DORA framework. |
| Run resilience tests | Requirement | Nested DORA legal child (Art. 24(1)). |
| Perform baseline tests | Requirement | Nested DORA legal child (Art. 25(1)). |
| Run threat-led tests | Requirement | Nested DORA legal child (Art. 26(1)). |
| Use qualified testers | Requirement | Nested DORA legal child (Art. 27(1)). |
| Third-Party ICT Risk | Requirement | Legal control family nested in the DORA framework. |
| Manage provider risk | Requirement | Nested DORA legal child (Art. 28(1)). |
| Assess ICT concentration | Requirement | Nested DORA legal child (Art. 29(1)). |
| Set ICT contract terms | Requirement | Nested DORA legal child (Art. 30(1)). |
| Critical Provider Control | Requirement | Legal control family nested in the DORA framework. |
| Set provider criticality | Requirement | Nested DORA legal child (Art. 31(1)). |
| Establish oversight forum | Requirement | Nested DORA legal child (Art. 32(1)). |
| Plan provider oversight | Requirement | Nested DORA legal child (Art. 33(1)). |
| Coordinate ICT oversight | Requirement | Nested DORA legal child (Art. 34(1)). |
| Exercise oversight powers | Requirement | Nested DORA legal child (Art. 35(1)). |
| Address non-EU oversight | Requirement | Nested DORA legal child (Art. 36(1)). |
| Obtain provider records | Requirement | Nested DORA legal child (Art. 37(1)). |
| Investigate ICT providers | Requirement | Nested DORA legal child (Art. 38(1)). |
| Inspect ICT providers | Requirement | Nested DORA legal child (Art. 39(1)). |
| Oversee ICT providers | Requirement | Nested DORA legal child (Art. 40(1)). |
| Set oversight standards | Requirement | Nested DORA legal child (Art. 41(1)). |
| Act on oversight findings | Requirement | Nested DORA legal child (Art. 42(1)). |
| Fund provider oversight | Requirement | Nested DORA legal child (Art. 43(1)). |
| Cooperate on oversight | Requirement | Nested DORA legal child (Art. 44(1)). |
| Cyber Threat Sharing | Requirement | Legal control family nested in the DORA framework. |
| Share threat intelligence | Requirement | Nested DORA legal child (Art. 45(1)). |
| Supervisory Enforcement | Requirement | Legal control family nested in the DORA framework. |
| Set DORA authorities | Requirement | Nested DORA legal child (Art. 46(1)). |
| Coordinate with NIS2 | Requirement | Nested DORA legal child (Art. 47(1)). |
| Coordinate authorities | Requirement | Nested DORA legal child (Art. 48(1)). |
| Coordinate sector drills | Requirement | Nested DORA legal child (Art. 49(1)). |
| Apply DORA remedies | Requirement | Nested DORA legal child (Art. 50(1)). |
| Exercise remedy powers | Requirement | Nested DORA legal child (Art. 51(1)). |
| Set criminal penalties | Constraint | Nested DORA legal child (Art. 52(1)). |
| Notify enforcement rules | Requirement | Nested DORA legal child (Art. 53(1)). |
| Publish DORA sanctions | Requirement | Nested DORA legal child (Art. 54(1)). |
| Protect oversight secrecy | Constraint | Nested DORA legal child (Art. 55(1)). |
| Protect supervisory data | Constraint | Nested DORA legal child (Art. 56(1)). |
| Legal Rule Lifecycle | Constraint | Legal control family nested in the DORA framework. |
| Govern delegated powers | Constraint | Nested DORA legal child (Art. 57(1)). |
| Review DORA operation | Requirement | Nested DORA legal child (Art. 58(1)). |
| Set DORA effective date | Constraint | Nested DORA legal child (Art. 64(1)). |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → DORA Scope and Proportion | contains the approved legal-control family |
| DORA Scope and Proportion → Apply DORA scope | contains the approved source-backed legal child |
| DORA Scope and Proportion → Scale ICT risk controls | contains the approved source-backed legal child |
| DORA Resilience Framework → ICT Governance | contains the approved legal-control family |
| ICT Governance → Govern ICT risk | contains the approved source-backed legal child |
| DORA Resilience Framework → ICT Risk Framework | contains the approved legal-control family |
| ICT Risk Framework → Set ICT risk framework | contains the approved source-backed legal child |
| ICT Risk Framework → Set ICT control standards | contains the approved source-backed legal child |
| ICT Risk Framework → Use simplified framework | contains the approved source-backed legal child |
| DORA Resilience Framework → ICT Assets and Systems | contains the approved legal-control family |
| ICT Assets and Systems → Maintain ICT systems | contains the approved source-backed legal child |
| ICT Assets and Systems → Identify ICT assets | contains the approved source-backed legal child |
| DORA Resilience Framework → Security and Detection | contains the approved legal-control family |
| Security and Detection → Protect ICT systems | contains the approved source-backed legal child |
| Security and Detection → Detect ICT anomalies | contains the approved source-backed legal child |
| DORA Resilience Framework → Continuity and Recovery | contains the approved legal-control family |
| Continuity and Recovery → Maintain ICT continuity | contains the approved source-backed legal child |
| Continuity and Recovery → Restore ICT systems | contains the approved source-backed legal child |
| DORA Resilience Framework → Resilience Learning | contains the approved legal-control family |
| Resilience Learning → Learn from ICT events | contains the approved source-backed legal child |
| Resilience Learning → Communicate ICT crises | contains the approved source-backed legal child |
| DORA Resilience Framework → ICT Incident Reporting | contains the approved legal-control family |
| ICT Incident Reporting → Manage ICT incidents | contains the approved source-backed legal child |
| ICT Incident Reporting → Classify ICT incidents | contains the approved source-backed legal child |
| ICT Incident Reporting → Report major incidents | contains the approved source-backed legal child |
| ICT Incident Reporting → Set incident report rules | contains the approved source-backed legal child |
| ICT Incident Reporting → Centralise ICT reports | contains the approved source-backed legal child |
| ICT Incident Reporting → Give incident feedback | contains the approved source-backed legal child |
| ICT Incident Reporting → Cover payment incidents | contains the approved source-backed legal child |
| DORA Resilience Framework → Resilience Testing | contains the approved legal-control family |
| Resilience Testing → Run resilience tests | contains the approved source-backed legal child |
| Resilience Testing → Perform baseline tests | contains the approved source-backed legal child |
| Resilience Testing → Run threat-led tests | contains the approved source-backed legal child |
| Resilience Testing → Use qualified testers | contains the approved source-backed legal child |
| DORA Resilience Framework → Third-Party ICT Risk | contains the approved legal-control family |
| Third-Party ICT Risk → Manage provider risk | contains the approved source-backed legal child |
| Third-Party ICT Risk → Assess ICT concentration | contains the approved source-backed legal child |
| Third-Party ICT Risk → Set ICT contract terms | contains the approved source-backed legal child |
| DORA Resilience Framework → Critical Provider Control | contains the approved legal-control family |
| Critical Provider Control → Set provider criticality | contains the approved source-backed legal child |
| Critical Provider Control → Establish oversight forum | contains the approved source-backed legal child |
| Critical Provider Control → Plan provider oversight | contains the approved source-backed legal child |
| Critical Provider Control → Coordinate ICT oversight | contains the approved source-backed legal child |
| Critical Provider Control → Exercise oversight powers | contains the approved source-backed legal child |
| Critical Provider Control → Address non-EU oversight | contains the approved source-backed legal child |
| Critical Provider Control → Obtain provider records | contains the approved source-backed legal child |
| Critical Provider Control → Investigate ICT providers | contains the approved source-backed legal child |
| Critical Provider Control → Inspect ICT providers | contains the approved source-backed legal child |
| Critical Provider Control → Oversee ICT providers | contains the approved source-backed legal child |
| Critical Provider Control → Set oversight standards | contains the approved source-backed legal child |
| Critical Provider Control → Act on oversight findings | contains the approved source-backed legal child |
| Critical Provider Control → Fund provider oversight | contains the approved source-backed legal child |
| Critical Provider Control → Cooperate on oversight | contains the approved source-backed legal child |
| DORA Resilience Framework → Cyber Threat Sharing | contains the approved legal-control family |
| Cyber Threat Sharing → Share threat intelligence | contains the approved source-backed legal child |
| DORA Resilience Framework → Supervisory Enforcement | contains the approved legal-control family |
| Supervisory Enforcement → Set DORA authorities | contains the approved source-backed legal child |
| Supervisory Enforcement → Coordinate with NIS2 | contains the approved source-backed legal child |
| Supervisory Enforcement → Coordinate authorities | contains the approved source-backed legal child |
| Supervisory Enforcement → Coordinate sector drills | contains the approved source-backed legal child |
| Supervisory Enforcement → Apply DORA remedies | contains the approved source-backed legal child |
| Supervisory Enforcement → Exercise remedy powers | contains the approved source-backed legal child |
| Supervisory Enforcement → Set criminal penalties | contains the approved source-backed legal child |
| Supervisory Enforcement → Notify enforcement rules | contains the approved source-backed legal child |
| Supervisory Enforcement → Publish DORA sanctions | contains the approved source-backed legal child |
| Supervisory Enforcement → Protect oversight secrecy | contains the approved source-backed legal child |
| Supervisory Enforcement → Protect supervisory data | contains the approved source-backed legal child |
| DORA Resilience Framework → Legal Rule Lifecycle | contains the approved legal-control family |
| Legal Rule Lifecycle → Govern delegated powers | contains the approved source-backed legal child |
| Legal Rule Lifecycle → Review DORA operation | contains the approved source-backed legal child |
| Legal Rule Lifecycle → Set DORA effective date | contains the approved source-backed legal child |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **DORA Regulation Overview**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.


### ICT Risk Governance

#### How to read this view

The view answers the approved concern for **ICT Risk Governance**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| ICT Risk Governance | Requirement | Legal control family nested in the DORA framework. |
| Change Review | BusinessProcess | Approved operational endpoint: Change Review. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| Stakeholder Team | BusinessActor | Approved operational endpoint: Stakeholder Team. |
| Starburst Administration | BusinessProcess | Approved operational endpoint: Starburst Administration. |
| Support Handoff | BusinessProcess | Approved operational endpoint: Support Handoff. |
| Technology Maintenance | BusinessProcess | Approved operational endpoint: Technology Maintenance. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| ICT Risk Framework | Requirement | Nested in ICT Risk Governance; Sound, comprehensive, documented ICT-risk framework (Art. 6(1)). |
| ICT Risk Response | Requirement | Nested in ICT Risk Governance; Framework enables rapid, efficient, comprehensive ICT-risk response (Art. 6(1)). |
| ICT Asset Protection | Requirement | Nested in ICT Risk Governance; Strategies, policies, procedures, protocols, and tools protect ICT assets (Art. 6(2)). |
| Authority ICT Information | Requirement | Nested in ICT Risk Governance; Supply complete, current ICT-risk information to authorities on request (Art. 6(3)). |
| Independent Risk Control | Requirement | Nested in ICT Risk Governance; Assign ICT-risk oversight to an independent control function (Art. 6(4)). |
| Framework Review | Requirement | Nested in ICT Risk Governance; Document and periodically review the framework (Art. 6(5)). |
| Event-Triggered Review | Requirement | Nested in ICT Risk Governance; Review after major incidents, tests, audits, or supervisory instruction (Art. 6(5)). |
| Framework Improvement | Requirement | Nested in ICT Risk Governance; Continuously improve from implementation and monitoring lessons (Art. 6(5)). |
| Authority Review Report | Requirement | Nested in ICT Risk Governance; Submit framework-review report to authority on request (Art. 6(5)). |
| Independent ICT Audit | Requirement | Nested in ICT Risk Governance; Conduct regular independent internal ICT-risk audits (Art. 6(6)). |
| Auditor Independence | Requirement | Nested in ICT Risk Governance; Ensure auditor ICT skills, expertise, and independence (Art. 6(6)). |
| Risk-Based Audit Plan | Requirement | Nested in ICT Risk Governance; Set audit frequency and focus commensurate with ICT risk (Art. 6(6)). |
| Audit Finding Follow-up | Requirement | Nested in ICT Risk Governance; Formally verify and remediate critical audit findings (Art. 6(7)). |
| Resilience Strategy | Requirement | Nested in ICT Risk Governance; Include a digital operational resilience strategy (Art. 6(8)). |
| Business Strategy Support | Requirement | Nested in ICT Risk Governance; Explain framework support for business strategy and objectives (Art. 6(8)(a)). |
| Disruption Tolerances | Requirement | Nested in ICT Risk Governance; Establish ICT-risk and disruption-impact tolerances (Art. 6(8)(b)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Stakeholder Team → ICT Risk Framework | Association | Team technology accountability is constrained by the framework. Ownership: Stakeholder-constrained. |
| Technology Maintenance → ICT Risk Response | Association | Maintenance work is constrained by the framework response objective. Ownership: Stakeholder-constrained. |
| Starburst Administration → ICT Asset Protection | Association | Administered platforms are the stated ICT assets. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Authority ICT Information | Association | Report is sent to support; authority reporting is outside the role. Ownership: Externally owned. |
| Stakeholder Team → Independent Risk Control | Association | Control-function ownership is not assigned to the stakeholder. Ownership: Externally owned. |
| Change Review → Framework Review | Association | Review work is constrained by the framework-review duty. Ownership: Stakeholder-constrained. |
| Change Review → Event-Triggered Review | Association | Both facts are inputs to, not evidence of ownership of, framework review. Ownership: Stakeholder-constrained. |
| Technology Maintenance → Framework Improvement | Association | Improvement work is constrained by the framework-improvement duty. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Authority Review Report | Association | Authority reporting is not assigned to the stakeholder. Ownership: Externally owned. |
| Stakeholder Team → Independent ICT Audit | Association | Audit ownership is external to the team role. Ownership: Externally owned. |
| Infra Eng & Cloud DBA → Auditor Independence | Association | No auditor role is evidenced. Ownership: Externally owned. |
| Stakeholder Team → Risk-Based Audit Plan | Association | Audit planning is outside the stated role. Ownership: Externally owned. |
| Change Review → Audit Finding Follow-up | Association | Review task can be constrained by audit follow-up. Ownership: Stakeholder-constrained. |
| Stakeholder Team → Resilience Strategy | Association | Team accountability lies within the strategy's scope. Ownership: Stakeholder-constrained. |
| Stakeholder Team → Business Strategy Support | Association | Business-strategy ownership is not assigned to the role. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Disruption Tolerances | Association | Stated outage impact is an input to tolerance setting. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Technology Maintenance | Assignment | updates and reconfigures technology |
| Infra Eng & Cloud DBA → Support Handoff | Assignment | provides technical evidence to support teams |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends logs |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends configurations |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Post-Incident Reporting → Technology Support Team | Flow | transfers the report |
| Stakeholder Team → Technology Maintenance | Assignment | configures accountable technologies |
| Infra Eng & Cloud DBA → Change Review | Assignment | self-checks and reviews completed changes |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → ICT Risk Governance | contains the approved stakeholder-scoped requirement family |
| ICT Risk Governance → ICT Risk Framework | contains the approved granular legal requirement |
| ICT Risk Governance → ICT Risk Response | contains the approved granular legal requirement |
| ICT Risk Governance → ICT Asset Protection | contains the approved granular legal requirement |
| ICT Risk Governance → Authority ICT Information | contains the approved granular legal requirement |
| ICT Risk Governance → Independent Risk Control | contains the approved granular legal requirement |
| ICT Risk Governance → Framework Review | contains the approved granular legal requirement |
| ICT Risk Governance → Event-Triggered Review | contains the approved granular legal requirement |
| ICT Risk Governance → Framework Improvement | contains the approved granular legal requirement |
| ICT Risk Governance → Authority Review Report | contains the approved granular legal requirement |
| ICT Risk Governance → Independent ICT Audit | contains the approved granular legal requirement |
| ICT Risk Governance → Auditor Independence | contains the approved granular legal requirement |
| ICT Risk Governance → Risk-Based Audit Plan | contains the approved granular legal requirement |
| ICT Risk Governance → Audit Finding Follow-up | contains the approved granular legal requirement |
| ICT Risk Governance → Resilience Strategy | contains the approved granular legal requirement |
| ICT Risk Governance → Business Strategy Support | contains the approved granular legal requirement |
| ICT Risk Governance → Disruption Tolerances | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **ICT Risk Governance**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: ICT Risk Framework — Stakeholder-constrained; ICT Risk Response — Stakeholder-constrained; ICT Asset Protection — Stakeholder-constrained; Authority ICT Information — Externally owned; Independent Risk Control — Externally owned; Framework Review — Stakeholder-constrained; Event-Triggered Review — Stakeholder-constrained; Framework Improvement — Stakeholder-constrained; Authority Review Report — Externally owned; Independent ICT Audit — Externally owned; Auditor Independence — Externally owned; Risk-Based Audit Plan — Externally owned; Audit Finding Follow-up — Stakeholder-constrained; Resilience Strategy — Stakeholder-constrained; Business Strategy Support — Stakeholder-constrained; Disruption Tolerances — Stakeholder-constrained.


### Platform & Asset Management

#### How to read this view

The view answers the approved concern for **Platform & Asset Management**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Platform & Asset Mgmt | Requirement | Legal control family nested in the DORA framework. |
| AKS/Compute Team | BusinessActor | Approved operational endpoint: AKS/Compute Team. |
| AKS External Secrets | ApplicationComponent | Approved operational endpoint: AKS External Secrets. |
| Azure DevOps | ApplicationComponent | Approved operational endpoint: Azure DevOps. |
| Azure Key Vault | ApplicationComponent | Approved operational endpoint: Azure Key Vault. |
| Change Review | BusinessProcess | Approved operational endpoint: Change Review. |
| Change Validation | BusinessProcess | Approved operational endpoint: Change Validation. |
| Developer Issue Diagnosis | BusinessProcess | Approved operational endpoint: Developer Issue Diagnosis. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| Issue Correction | BusinessProcess | Approved operational endpoint: Issue Correction. |
| OpenMetadata | ApplicationComponent | Approved operational endpoint: OpenMetadata. |
| OpenMetadata Admin | BusinessProcess | Approved operational endpoint: OpenMetadata Administration. |
| Ranger | ApplicationComponent | Approved operational endpoint: Ranger. |
| ServiceNow Change Request | DataObject | Approved operational endpoint: ServiceNow Change Request. |
| SingleStore | ApplicationComponent | Approved operational endpoint: SingleStore. |
| SingleStore Admin | BusinessProcess | Approved operational endpoint: SingleStore Administration. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| Starburst | ApplicationComponent | Approved operational endpoint: Starburst. |
| Starburst Administration | BusinessProcess | Approved operational endpoint: Starburst Administration. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| YAML Configuration | Artifact | Approved operational endpoint: YAML Configuration. |
| YAML Config Maintenance | BusinessProcess | Approved operational endpoint: YAML Configuration Maintenance. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Updated ICT Systems | Requirement | Nested in Platform & Asset Mgmt; Use and maintain updated ICT systems, protocols, and tools (Art. 7(1)). |
| Proportionate ICT Systems | Requirement | Nested in Platform & Asset Mgmt; Ensure systems are proportionate to operations (Art. 7(1)(a)). |
| Reliable ICT Systems | Requirement | Nested in Platform & Asset Mgmt; Ensure systems are reliable (Art. 7(1)(b)). |
| Sufficient ICT capacity | Requirement | Nested in Platform & Asset Mgmt; Provide sufficient capacity for data and peak volumes (Art. 7(1)(c)). |
| Technological resilience | Requirement | Nested in Platform & Asset Mgmt; Ensure technological resilience under adverse conditions (Art. 7(1)(d)). |
| ICT Asset Documentation | Requirement | Nested in Platform & Asset Mgmt; Identify, classify, and document ICT functions, roles, assets, and dependencies (Art. 8(1)). |
| Asset Review | Requirement | Nested in Platform & Asset Mgmt; Review classification and documentation at least yearly (Art. 8(1)). |
| Identify ICT Risk sources | Requirement | Nested in Platform & Asset Mgmt; Continuously identify ICT-risk sources (Art. 8(2)). |
| Cyber Threat Assessment | Requirement | Nested in Platform & Asset Mgmt; Assess relevant cyber threats, vulnerabilities, and risk scenarios (Art. 8(2)). |
| Review ICT Risk scenarios | Requirement | Nested in Platform & Asset Mgmt; Review ICT-risk scenarios regularly and at least yearly (Art. 8(2)). |
| Identify ICT assets | Requirement | Nested in Platform & Asset Mgmt; Identify all information and ICT assets, including remote/network assets (Art. 8(4)). |
| Map critical ICT assets | Requirement | Nested in Platform & Asset Mgmt; Map information and ICT assets considered critical (Art. 8(4)). |
| Config Dependency Map | Requirement | Nested in Platform & Asset Mgmt; Map configurations, links, and interdependencies (Art. 8(4)). |
| Asset Inventory | Requirement | Nested in Platform & Asset Mgmt; Maintain relevant asset inventories (Art. 8(6)). |
| Inventory Change Update | Requirement | Nested in Platform & Asset Mgmt; Update inventories periodically and after major changes (Art. 8(6)). |
| Legacy System Review | Requirement | Nested in Platform & Asset Mgmt; Assess legacy systems and technology connections regularly (Art. 8(7)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Starburst Administration → Updated ICT Systems | Realization | Maintenance is directly performed. Ownership: Directly performed. |
| Starburst Administration → Proportionate ICT Systems | Association | System scale/proportionality is not assigned to the role. Ownership: Stakeholder-constrained. |
| Change Validation → Reliable ICT Systems | Realization | Availability/connectivity validation is directly performed. Ownership: Directly performed. |
| Infra Issue Resolution → Sufficient ICT capacity | Association | Capacity depends on the stated compute team. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Technological resilience | Association | The incident impact constrains resilience needs. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → ICT Asset Documentation | Association | Existing asset responsibility is a constrained input. Ownership: Stakeholder-constrained. |
| Change Review → Asset Review | Association | Self-review is constrained by the broader duty. Ownership: Stakeholder-constrained. |
| Issue Correction → Identify ICT Risk sources | Association | Named dependencies provide a constrained source record. Ownership: Stakeholder-constrained. |
| Developer Issue Diagnosis → Cyber Threat Assessment | Association | Diagnosis work is constrained; threat assessment owner is unstated. Ownership: Stakeholder-constrained. |
| Issue Correction → Review ICT Risk scenarios | Association | Named dependencies are a constrained risk-scenario input. Ownership: Stakeholder-constrained. |
| Starburst Administration → Identify ICT assets | Association | Named administered technologies are asset evidence. Ownership: Stakeholder-constrained. |
| Starburst Administration → Map critical ICT assets | Association | Criticality mapping owner is unstated. Ownership: Stakeholder-constrained. |
| YAML Config Maintenance → Config Dependency Map | Association | Configurations and integration are explicit. Ownership: Stakeholder-constrained. |
| YAML Configuration → Asset Inventory | Association | Configuration store is constrained by inventory duty. Ownership: Stakeholder-constrained. |
| ServiceNow Change Request → Inventory Change Update | Association | Change work is constrained by update duty. Ownership: Stakeholder-constrained. |
| Azure Key Vault → Legacy System Review | Association | Historic script and connection are constrained risk-assessment inputs. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Starburst Administration | Assignment | administers |
| Starburst Administration → Starburst | Association | administers |
| Infra Eng & Cloud DBA → OpenMetadata Admin | Assignment | administers |
| OpenMetadata Admin → OpenMetadata | Association | administers |
| Infra Eng & Cloud DBA → SingleStore Admin | Assignment | administers |
| SingleStore Admin → SingleStore | Association | administers |
| Infra Eng & Cloud DBA → Developer Issue Diagnosis | Assignment | investigates connection and usage issues |
| Ranger → Starburst | Serving | provides access-control policy capability |
| Infra Eng & Cloud DBA → YAML Config Maintenance | Assignment | changes YAML configurations |
| YAML Config Maintenance → YAML Configuration | Access | reads and changes configuration |
| YAML Configuration → Azure DevOps | Association | is stored in |
| Azure Key Vault → AKS External Secrets | Serving | supplies secrets through the stated connection |
| AKS/Compute Team → Infra Issue Resolution | Serving | provides compute-layer support and correction |
| Technology Support Team → Issue Correction | Serving | provides support and correction |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Platform & Asset Mgmt | contains the approved stakeholder-scoped requirement family |
| Platform & Asset Mgmt → Updated ICT Systems | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Proportionate ICT Systems | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Reliable ICT Systems | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Sufficient ICT capacity | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Technological resilience | contains the approved granular legal requirement |
| Platform & Asset Mgmt → ICT Asset Documentation | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Asset Review | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Identify ICT Risk sources | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Cyber Threat Assessment | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Review ICT Risk scenarios | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Identify ICT assets | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Map critical ICT assets | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Config Dependency Map | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Asset Inventory | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Inventory Change Update | contains the approved granular legal requirement |
| Platform & Asset Mgmt → Legacy System Review | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Platform & Asset Management**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Proportionate ICT Systems — Stakeholder-constrained; Sufficient ICT capacity — Stakeholder-constrained; Technological resilience — Stakeholder-constrained; ICT Asset Documentation — Stakeholder-constrained; Asset Review — Stakeholder-constrained; Identify ICT Risk sources — Stakeholder-constrained; Cyber Threat Assessment — Stakeholder-constrained; Review ICT Risk scenarios — Stakeholder-constrained; Identify ICT assets — Stakeholder-constrained; Map critical ICT assets — Stakeholder-constrained; Config Dependency Map — Stakeholder-constrained; Asset Inventory — Stakeholder-constrained; Inventory Change Update — Stakeholder-constrained; Legacy System Review — Stakeholder-constrained.


### Provider Dependencies

#### How to read this view

The view answers the approved concern for **Provider Dependencies**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Provider Dependencies | Requirement | Legal control family nested in the DORA framework. |
| AKS/Compute Team | BusinessActor | Approved operational endpoint: AKS/Compute Team. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| OpenMetadata | ApplicationComponent | Approved operational endpoint: OpenMetadata. |
| OpenMetadata Admin | BusinessProcess | Approved operational endpoint: OpenMetadata Administration. |
| SingleStore | ApplicationComponent | Approved operational endpoint: SingleStore. |
| SingleStore Admin | BusinessProcess | Approved operational endpoint: SingleStore Administration. |
| Starburst | ApplicationComponent | Approved operational endpoint: Starburst. |
| Starburst Administration | BusinessProcess | Approved operational endpoint: Starburst Administration. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| BIA Dependencies | Requirement | Nested in Provider Dependencies; Consider criticality, dependencies, assets, and interdependencies in BIA (Art. 11(5)). |
| Provider Resilience Training | Requirement | Nested in Provider Dependencies; Include relevant ICT third-party providers in training where appropriate (Art. 13(6)). |
| Retained Verification | Requirement | Nested in Provider Dependencies; Retain compliance-verification responsibility if verification is outsourced (Art. 6(10)). |
| Provider Dependency Record | Requirement | Nested in Provider Dependencies; Document provider-dependent processes and critical-function interconnections (Art. 8(5)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Starburst Administration → Retained Verification | Association | Providers are confirmed, but whether compliance verification is outsourced is unknown. Ownership: Not evidenced / unclear owner. |
| Starburst Administration → Provider Dependency Record | Association | Provider use is confirmed; documentation owner is unstated. Ownership: Stakeholder-constrained. |
| Infra Issue Resolution → BIA Dependencies | Association | Dependencies are explicitly stated. Ownership: Stakeholder-constrained. |
| Starburst Administration → Provider Resilience Training | Association | Third-party training is externally owned. Ownership: Externally owned. |
| Infra Eng & Cloud DBA → Starburst Administration | Assignment | administers |
| Starburst Administration → Starburst | Association | administers |
| Infra Eng & Cloud DBA → OpenMetadata Admin | Assignment | administers |
| OpenMetadata Admin → OpenMetadata | Association | administers |
| Infra Eng & Cloud DBA → SingleStore Admin | Assignment | administers |
| SingleStore Admin → SingleStore | Association | administers |
| AKS/Compute Team → Infra Issue Resolution | Serving | provides compute-layer support and correction |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Provider Dependencies | contains the approved stakeholder-scoped requirement family |
| Provider Dependencies → Retained Verification | contains the approved granular legal requirement |
| Provider Dependencies → Provider Dependency Record | contains the approved granular legal requirement |
| Provider Dependencies → BIA Dependencies | contains the approved granular legal requirement |
| Provider Dependencies → Provider Resilience Training | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Provider Dependencies**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Retained Verification — Not evidenced / unclear owner; Provider Dependency Record — Stakeholder-constrained; BIA Dependencies — Stakeholder-constrained; Provider Resilience Training — Externally owned.

Potential operational or visibility limitation from this stakeholder perspective: Retained Verification has no evidenced responsible owner. This is not a compliance conclusion.


### Access & Security

#### How to read this view

The view answers the approved concern for **Access & Security**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Access & Security | Requirement | Legal control family nested in the DORA framework. |
| Access Automation | BusinessProcess | Approved operational endpoint: Access Automation. |
| Access Provisioning | BusinessProcess | Approved operational endpoint: Access Provisioning. |
| Access Request Approval | BusinessProcess | Approved operational endpoint: Access Request Approval. |
| Azure Key Vault | ApplicationComponent | Approved operational endpoint: Azure Key Vault. |
| Azure Key Vault Secrets | DataObject | Approved operational endpoint: Azure Key Vault Secrets. |
| Connection Resolution | BusinessProcess | Approved operational endpoint: Connection Issue Resolution. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| Networking Team | BusinessActor | Approved operational endpoint: Networking Team. |
| Secret Retrieval | BusinessProcess | Approved operational endpoint: Secret Retrieval. |
| Security Team | BusinessActor | Approved operational endpoint: Security Team. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| Stakeholder Team | BusinessActor | Approved operational endpoint: Stakeholder Team. |
| Starburst Administration | BusinessProcess | Approved operational endpoint: Starburst Administration. |
| Support Handoff | BusinessProcess | Approved operational endpoint: Support Handoff. |
| Technology Maintenance | BusinessProcess | Approved operational endpoint: Technology Maintenance. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Asset Access Protection | Requirement | Nested in Access & Security; Protect assets from damage and unauthorised access or use (Art. 6(2)). |
| Resilient and continuous | Requirement | Nested in Access & Security; Design and implement resilient, continuous, available ICT security (Art. 9(2)). |
| Data Integrity Protection | Requirement | Nested in Access & Security; Preserve data availability, authenticity, integrity, and confidentiality (Art. 9(2)). |
| Appropriate ICT solutions | Requirement | Nested in Access & Security; Use proportionate ICT solutions and processes (Art. 9(3)). |
| Secure transfer means | Requirement | Nested in Access & Security; Secure data-transfer means (Art. 9(3)(a)). |
| Prevent loss and access | Requirement | Nested in Access & Security; Minimise data loss, unauthorised access, and technical flaws (Art. 9(3)(b)). |
| Availability Protection | Requirement | Nested in Access & Security; Prevent loss of availability, integrity, authenticity, and confidentiality (Art. 9(3)(c)). |
| Admin Risk Protection | Requirement | Nested in Access & Security; Protect data from management, processing, and human-error risks (Art. 9(3)(d)). |
| Security Policy | Requirement | Nested in Access & Security; Develop and document information-security policy (Art. 9(4)(a)). |
| Network Management | Requirement | Nested in Access & Security; Establish risk-based network and infrastructure management (Art. 9(4)(b)). |
| Access-rights policies | Requirement | Nested in Access & Security; Limit logical/physical access and administer access rights (Art. 9(4)(c)). |
| Approved Access Functions | Requirement | Nested in Access & Security; Limit access to legitimate, approved functions (Art. 9(4)(c)). |
| Strong Authentication | Requirement | Nested in Access & Security; Use strong authentication and protect cryptographic keys (Art. 9(4)(d)). |
| Encryption Protection | Requirement | Nested in Access & Security; Base encryption protection on classification and risk assessment (Art. 9(4)(d)). |
| Network Segmentation | Requirement | Nested in Access & Security; Permit prompt network severance or segmentation (Art. 9(4)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Access Provisioning → Asset Access Protection | Association | The named access work is constrained by this protection duty. Ownership: Stakeholder-constrained. |
| Starburst Administration → Resilient and continuous | Association | Platform work is constrained by the duty. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Data Integrity Protection | Association | Sensitive-data work is constrained by data protection. Ownership: Stakeholder-constrained. |
| Technology Maintenance → Appropriate ICT solutions | Realization | Maintenance is directly performed. Ownership: Directly performed. |
| Support Handoff → Secure transfer means | Association | Logs/configs are transferred; transfer-security control owner is unstated. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Prevent loss and access | Association | Secret use is constrained by prevention duty. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Availability Protection | Association | Outage impact is a constrained input. Ownership: Stakeholder-constrained. |
| Access Provisioning → Admin Risk Protection | Association | Work is constrained by the protection duty. Ownership: Stakeholder-constrained. |
| Stakeholder Team → Security Policy | Association | Policy ownership is unstated. Ownership: Stakeholder-constrained. |
| Infra Issue Resolution → Network Management | Association | Responsibility rests with dependency teams. Ownership: Stakeholder-constrained. |
| Access Provisioning → Access-rights policies | Realization | Access administration is directly performed. Ownership: Directly performed. |
| Access Request Approval → Approved Access Functions | Association | Approval is externally owned. Ownership: Externally owned. |
| Azure Key Vault → Strong Authentication | Association | Secret store is constrained by this duty. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Encryption Protection | Association | Classification/risk owner is unstated. Ownership: Stakeholder-constrained. |
| Connection Resolution → Network Segmentation | Association | Capability depends on networking team. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Access Provisioning | Assignment | grants access |
| Infra Eng & Cloud DBA → Access Automation | Assignment | automates access-control work with Python |
| Infra Eng & Cloud DBA → Secret Retrieval | Assignment | retrieves credentials to correct issues |
| Secret Retrieval → Azure Key Vault Secrets | Access | accesses passwords and secrets |
| Networking Team → Connection Resolution | Serving | provides support for connection issues |
| Security Team → Access Request Approval | Assignment | performs access approval |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Access & Security | contains the approved stakeholder-scoped requirement family |
| Access & Security → Asset Access Protection | contains the approved granular legal requirement |
| Access & Security → Resilient and continuous | contains the approved granular legal requirement |
| Access & Security → Data Integrity Protection | contains the approved granular legal requirement |
| Access & Security → Appropriate ICT solutions | contains the approved granular legal requirement |
| Access & Security → Secure transfer means | contains the approved granular legal requirement |
| Access & Security → Prevent loss and access | contains the approved granular legal requirement |
| Access & Security → Availability Protection | contains the approved granular legal requirement |
| Access & Security → Admin Risk Protection | contains the approved granular legal requirement |
| Access & Security → Security Policy | contains the approved granular legal requirement |
| Access & Security → Network Management | contains the approved granular legal requirement |
| Access & Security → Access-rights policies | contains the approved granular legal requirement |
| Access & Security → Approved Access Functions | contains the approved granular legal requirement |
| Access & Security → Strong Authentication | contains the approved granular legal requirement |
| Access & Security → Encryption Protection | contains the approved granular legal requirement |
| Access & Security → Network Segmentation | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Access & Security**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Asset Access Protection — Stakeholder-constrained; Resilient and continuous — Stakeholder-constrained; Data Integrity Protection — Stakeholder-constrained; Secure transfer means — Stakeholder-constrained; Prevent loss and access — Stakeholder-constrained; Availability Protection — Stakeholder-constrained; Admin Risk Protection — Stakeholder-constrained; Security Policy — Stakeholder-constrained; Network Management — Stakeholder-constrained; Approved Access Functions — Externally owned; Strong Authentication — Stakeholder-constrained; Encryption Protection — Stakeholder-constrained; Network Segmentation — Stakeholder-constrained.


### Controlled Change

#### How to read this view

The view answers the approved concern for **Controlled Change**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Controlled Change | Requirement | Legal control family nested in the DORA framework. |
| Approved DevOps Change | BusinessProcess | Approved operational endpoint: Approved DevOps Change. |
| Authorization Team | BusinessActor | Approved operational endpoint: Authorization Team. |
| Azure DevOps | ApplicationComponent | Approved operational endpoint: Azure DevOps. |
| Change Review | BusinessProcess | Approved operational endpoint: Change Review. |
| Change Validation | BusinessProcess | Approved operational endpoint: Change Validation. |
| Flux | ApplicationComponent | Approved operational endpoint: Flux. |
| Information Change | BusinessProcess | Approved operational endpoint: Information Change. |
| Non-production Testing | BusinessProcess | Approved operational endpoint: Non-production Testing. |
| Change Authorization | BusinessProcess | Approved operational endpoint: Production Change Authorization. |
| Production Change Record | BusinessProcess | Approved operational endpoint: Production Change Recording. |
| Production Readiness | BusinessEvent | Approved operational event: Production Readiness Decision. |
| ServiceNow Change Request | DataObject | Approved operational endpoint: ServiceNow Change Request. |
| Starburst Config Deploy | BusinessProcess | Approved operational endpoint: Starburst Configuration Deployment. |
| Starburst GitOps Move | BusinessProcess | Approved operational endpoint: Starburst GitOps Migration. |
| Technology Maintenance | BusinessProcess | Approved operational endpoint: Technology Maintenance. |
| YAML Configuration | Artifact | Approved operational endpoint: YAML Configuration. |
| YAML Config Maintenance | BusinessProcess | Approved operational endpoint: YAML Configuration Maintenance. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Control Separation | Requirement | Nested in Controlled Change; Segregate risk management, control, and internal audit functions (Art. 6(4)). |
| ICT Reference Design | Requirement | Nested in Controlled Change; Explain ICT reference architecture and required changes (Art. 6(8)(d)). |
| Major Change Risk Review | Requirement | Nested in Controlled Change; Assess risk for each major ICT infrastructure or process change (Art. 8(3)). |
| Controlled Change Record | Requirement | Nested in Controlled Change; Document controlled ICT change management (Art. 9(4)(e)). |
| Change Test and Approval | Requirement | Nested in Controlled Change; Record, test, assess, approve, implement, and verify changes (Art. 9(4)(e)). |
| Approved Change Protocol | Requirement | Nested in Controlled Change; Obtain management-approved change protocols (Art. 9(4)). |
| Patch and update policy | Requirement | Nested in Controlled Change; Maintain documented patch and update policies (Art. 9(4)(f)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Change Authorization → Control Separation | Association | Separate approval teams are explicit. Ownership: Externally owned. |
| Starburst Config Deploy → ICT Reference Design | Association | Deployment/configuration changes affect the reference architecture. Ownership: Stakeholder-constrained. |
| Starburst GitOps Move → Major Change Risk Review | Association | Major change is explicit; risk-assessment ownership is unstated. Ownership: Stakeholder-constrained. |
| Production Change Record → Controlled Change Record | Realization | Recording is directly performed. Ownership: Directly performed. |
| Information Change → Change Test and Approval | Association | Testing/review is performed; approval is external. Ownership: Stakeholder-constrained. |
| Change Authorization → Approved Change Protocol | Association | Authorization team exists; automation owner is unknown. Ownership: Not evidenced / unclear owner. |
| Technology Maintenance → Patch and update policy | Association | Updates are performed; policy owner unstated. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Starburst GitOps Move | Assignment | migrates deployment approach |
| Flux → Starburst Config Deploy | Serving | deploys Starburst configurations to target AKS |
| Infra Eng & Cloud DBA → Non-production Testing | Assignment | tests changes before production |
| Non-production Testing → Production Readiness | Triggering | establishes the condition to proceed |
| Infra Eng & Cloud DBA → Change Validation | Assignment | validates completed changes |
| Infra Eng & Cloud DBA → YAML Config Maintenance | Assignment | changes YAML configurations |
| YAML Config Maintenance → YAML Configuration | Access | reads and changes configuration |
| YAML Configuration → Azure DevOps | Association | is stored in |
| Infra Eng & Cloud DBA → Production Change Record | Assignment | records production changes |
| Production Change Record → ServiceNow Change Request | Access | creates and updates the record |
| Approved DevOps Change → Information Change | Triggering | authorizes the otherwise prohibited information change |
| Authorization Team → Change Authorization | Assignment | performs authorization |
| Change Authorization → ServiceNow Change Request | Access | records approval status |
| Infra Eng & Cloud DBA → Change Review | Assignment | self-checks and reviews completed changes |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Controlled Change | contains the approved stakeholder-scoped requirement family |
| Controlled Change → Control Separation | contains the approved granular legal requirement |
| Controlled Change → ICT Reference Design | contains the approved granular legal requirement |
| Controlled Change → Major Change Risk Review | contains the approved granular legal requirement |
| Controlled Change → Controlled Change Record | contains the approved granular legal requirement |
| Controlled Change → Change Test and Approval | contains the approved granular legal requirement |
| Controlled Change → Approved Change Protocol | contains the approved granular legal requirement |
| Controlled Change → Patch and update policy | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Controlled Change**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Control Separation — Externally owned; ICT Reference Design — Stakeholder-constrained; Major Change Risk Review — Stakeholder-constrained; Change Test and Approval — Stakeholder-constrained; Approved Change Protocol — Not evidenced / unclear owner; Patch and update policy — Stakeholder-constrained.

Potential operational or visibility limitation from this stakeholder perspective: Approved Change Protocol has no evidenced responsible owner. This is not a compliance conclusion.


### Monitoring & Detection

#### How to read this view

The view answers the approved concern for **Monitoring & Detection**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Monitoring & Detection | Requirement | Legal control family nested in the DORA framework. |
| Change Validation | BusinessProcess | Approved operational endpoint: Change Validation. |
| Datadog Alert | BusinessEvent | Approved operational endpoint: Datadog Alert. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| Non-production Testing | BusinessProcess | Approved operational endpoint: Non-production Testing. |
| Production Readiness | BusinessEvent | Approved operational event: Production Readiness Decision. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Starburst | ApplicationComponent | Approved operational endpoint: Starburst. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Incident Detection | Requirement | Nested in Monitoring & Detection; Detect anomalies, performance issues, and ICT incidents promptly (Art. 10(1)). |
| Material Failure Points | Requirement | Nested in Monitoring & Detection; Identify potential material single points of failure (Art. 10(1)). |
| Test detection mechanisms | Requirement | Nested in Monitoring & Detection; Regularly test detection mechanisms (Art. 10(1)). |
| Layered Detection | Requirement | Nested in Monitoring & Detection; Enable multiple layers of detection control (Art. 10(2)). |
| Alert Thresholds | Requirement | Nested in Monitoring & Detection; Define alert thresholds and incident-response triggers (Art. 10(2)). |
| Response Staff Alerting | Requirement | Nested in Monitoring & Detection; Automatically alert relevant incident-response staff (Art. 10(2)). |
| Monitoring Resources | Requirement | Nested in Monitoring & Detection; Resource monitoring of user activity, anomalies, and cyber-attacks (Art. 10(3)). |
| Incident Impact Analysis | Requirement | Nested in Monitoring & Detection; Gather vulnerability, threat, and incident information and analyse resilience impact (Art. 13(1)). |
| Security KPIs and KRIs | Requirement | Nested in Monitoring & Detection; Set information-security objectives, KPIs, and KRIs (Art. 6(8)(c)). |
| Incident Protection | Requirement | Nested in Monitoring & Detection; Outline incident detection, prevention, and protection mechanisms (Art. 6(8)(e)). |
| ICT Security Monitoring | Requirement | Nested in Monitoring & Detection; Continuously monitor and control ICT security and functioning (Art. 9(1)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Datadog Alert → Security KPIs and KRIs | Association | Monitoring provides a constrained operational input. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Incident Protection | Realization | Detection and recovery are directly performed. Ownership: Directly performed. |
| Datadog Alert → ICT Security Monitoring | Realization | Monitoring is directly performed. Ownership: Directly performed. |
| Datadog Alert → Incident Detection | Realization | Detection is directly performed. Ownership: Directly performed. |
| Infra Issue Resolution → Material Failure Points | Association | Evidence constrains the identification duty. Ownership: Stakeholder-constrained. |
| Non-production Testing → Test detection mechanisms | Association | Detection-test scope/owner is unstated. Ownership: Stakeholder-constrained. |
| Datadog Alert → Layered Detection | Association | Monitoring is a constrained input. Ownership: Stakeholder-constrained. |
| Datadog Alert → Alert Thresholds | Association | Threshold ownership is unstated. Ownership: Stakeholder-constrained. |
| Datadog Alert → Response Staff Alerting | Realization | Automatic alerts are directly evidenced. Ownership: Directly performed. |
| Datadog Alert → Monitoring Resources | Association | Resource allocation is unstated. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Incident Impact Analysis | Realization | Monitoring and outage evidence are directly available to the role. Ownership: Directly performed. |
| Infra Eng & Cloud DBA → Non-production Testing | Assignment | tests changes before production |
| Non-production Testing → Production Readiness | Triggering | establishes the condition to proceed |
| Infra Eng & Cloud DBA → Change Validation | Assignment | validates completed changes |
| Change Validation → Starburst | Association | checks service availability and database connection |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Infra Eng & Cloud DBA → SingleStore Recovery | Assignment | restarts, investigates, and mitigates |
| Datadog Alert → SingleStore Recovery | Triggering | initiates the response |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Monitoring & Detection | contains the approved stakeholder-scoped requirement family |
| Monitoring & Detection → Security KPIs and KRIs | contains the approved granular legal requirement |
| Monitoring & Detection → Incident Protection | contains the approved granular legal requirement |
| Monitoring & Detection → ICT Security Monitoring | contains the approved granular legal requirement |
| Monitoring & Detection → Incident Detection | contains the approved granular legal requirement |
| Monitoring & Detection → Material Failure Points | contains the approved granular legal requirement |
| Monitoring & Detection → Test detection mechanisms | contains the approved granular legal requirement |
| Monitoring & Detection → Layered Detection | contains the approved granular legal requirement |
| Monitoring & Detection → Alert Thresholds | contains the approved granular legal requirement |
| Monitoring & Detection → Response Staff Alerting | contains the approved granular legal requirement |
| Monitoring & Detection → Monitoring Resources | contains the approved granular legal requirement |
| Monitoring & Detection → Incident Impact Analysis | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Monitoring & Detection**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Security KPIs and KRIs — Stakeholder-constrained; Material Failure Points — Stakeholder-constrained; Test detection mechanisms — Stakeholder-constrained; Layered Detection — Stakeholder-constrained; Alert Thresholds — Stakeholder-constrained; Monitoring Resources — Stakeholder-constrained.


### Continuity Preparedness

#### How to read this view

The view answers the approved concern for **Continuity Preparedness**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Continuity Preparedness | Requirement | Legal control family nested in the DORA framework. |
| Change Review | BusinessProcess | Approved operational endpoint: Change Review. |
| DevOps Leads | BusinessActor | Approved operational endpoint: DevOps Leads. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| Non-production Testing | BusinessProcess | Approved operational endpoint: Non-production Testing. |
| Post-Incident Report | BusinessObject | Approved operational endpoint: Post-Incident Report. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| Ranger Backup | BusinessProcess | Approved operational endpoint: Ranger Backup. |
| SingleStore Incident | BusinessProcess | Approved operational endpoint: SingleStore Incident Response. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Stakeholder Team | BusinessActor | Approved operational endpoint: Stakeholder Team. |
| Team Lead | BusinessActor | Approved operational endpoint: Team Lead. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Business Continuity Policy | Requirement | Nested in Continuity Preparedness; Establish comprehensive ICT business-continuity policy (Art. 11(1)). |
| Continuity Arrangements | Requirement | Nested in Continuity Preparedness; Implement policy with documented arrangements, plans, procedures, and mechanisms (Art. 11(2)). |
| Critical Function Continuity | Requirement | Nested in Continuity Preparedness; Ensure continuity of critical or important functions (Art. 11(2)(a)). |
| Incident Impact Estimate | Requirement | Nested in Continuity Preparedness; Estimate preliminary incident impacts, damage, and losses (Art. 11(2)(d)). |
| Crisis Communications | Requirement | Nested in Continuity Preparedness; Implement crisis communications and authority reporting (Art. 11(2)(e)). |
| Recovery Plan Audit | Requirement | Nested in Continuity Preparedness; Subject response and recovery plans to independent audit (Art. 11(3)). |
| Continuity Plan Testing | Requirement | Nested in Continuity Preparedness; Maintain and periodically test continuity plans (Art. 11(4)). |
| Business-impact analysis | Requirement | Nested in Continuity Preparedness; Conduct business-impact analysis (Art. 11(5)). |
| Disruption Impact Assessment | Requirement | Nested in Continuity Preparedness; Assess potential severe-disruption impacts (Art. 11(5)). |
| BIA-aligned redundancy | Requirement | Nested in Continuity Preparedness; Align assets, services, and redundancy with BIA (Art. 11(5)). |
| Continuity Test Schedule | Requirement | Nested in Continuity Preparedness; Test continuity/recovery plans annually and after substantive change (Art. 11(6)(a)). |
| Crisis Comm Tests | Requirement | Nested in Continuity Preparedness; Test crisis-communication plans (Art. 11(6)(b)). |
| Backup Switchover Tests | Requirement | Nested in Continuity Preparedness; Test cyberattack, switchover, backup, and redundancy scenarios (Art. 11(6)). |
| Continuity Plan Review | Requirement | Nested in Continuity Preparedness; Review continuity and recovery plans after tests/audits/reviews (Art. 11(6)). |
| Crisis Management | Requirement | Nested in Continuity Preparedness; Maintain a crisis-management function (Art. 11(7)). |
| Incident Cost Reporting | Requirement | Nested in Continuity Preparedness; Estimate and report annual major-incident costs and losses (Art. 11(10)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Stakeholder Team → Business Continuity Policy | Association | Team technology accountability is constrained by policy. Ownership: Stakeholder-constrained. |
| Stakeholder Team → Continuity Arrangements | Association | Plan/procedure ownership is unstated. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Critical Function Continuity | Association | Stated service impact is a continuity input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Incident Impact Estimate | Association | Outage evidence is a constrained input. Ownership: Stakeholder-constrained. |
| Post-Incident Report → Crisis Communications | Association | Report goes to support; formal reporting is external. Ownership: Externally owned. |
| Change Review → Recovery Plan Audit | Association | Independent audit is external. Ownership: Externally owned. |
| Non-production Testing → Continuity Plan Testing | Association | Testing is not evidenced as continuity-plan testing. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Business-impact analysis | Association | Incident impact is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Disruption Impact Assessment | Association | Incident impact is a constrained input. Ownership: Stakeholder-constrained. |
| Infra Issue Resolution → BIA-aligned redundancy | Association | Redundancy design depends on compute team. Ownership: Stakeholder-constrained. |
| Non-production Testing → Continuity Test Schedule | Association | Test frequency/scope is unstated. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Crisis Comm Tests | Association | Crisis communication testing is external. Ownership: Externally owned. |
| Ranger Backup → Backup Switchover Tests | Association | Backup and testing are stated; scenario scope is unstated. Ownership: Stakeholder-constrained. |
| Change Review → Continuity Plan Review | Association | Review is not identified as plan review. Ownership: Stakeholder-constrained. |
| SingleStore Incident → Crisis Management | Association | Participants exist; formal function ownership is external. Ownership: Externally owned. |
| SingleStore Outage → Incident Cost Reporting | Association | Cost/loss calculation and authority reporting are external. Ownership: Externally owned. |
| Infra Eng & Cloud DBA → Ranger Backup | Assignment | backs up Ranger data before change |
| Infra Eng & Cloud DBA → Non-production Testing | Assignment | tests changes before production |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Team Lead → SingleStore Incident | Assignment | participates in response |
| DevOps Leads → SingleStore Incident | Assignment | participates in response |
| Technology Support Team → SingleStore Incident | Assignment | participates in extreme cases |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Post-Incident Reporting → Technology Support Team | Flow | transfers the report |
| Infra Eng & Cloud DBA → Change Review | Assignment | self-checks and reviews completed changes |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Continuity Preparedness | contains the approved stakeholder-scoped requirement family |
| Continuity Preparedness → Business Continuity Policy | contains the approved granular legal requirement |
| Continuity Preparedness → Continuity Arrangements | contains the approved granular legal requirement |
| Continuity Preparedness → Critical Function Continuity | contains the approved granular legal requirement |
| Continuity Preparedness → Incident Impact Estimate | contains the approved granular legal requirement |
| Continuity Preparedness → Crisis Communications | contains the approved granular legal requirement |
| Continuity Preparedness → Recovery Plan Audit | contains the approved granular legal requirement |
| Continuity Preparedness → Continuity Plan Testing | contains the approved granular legal requirement |
| Continuity Preparedness → Business-impact analysis | contains the approved granular legal requirement |
| Continuity Preparedness → Disruption Impact Assessment | contains the approved granular legal requirement |
| Continuity Preparedness → BIA-aligned redundancy | contains the approved granular legal requirement |
| Continuity Preparedness → Continuity Test Schedule | contains the approved granular legal requirement |
| Continuity Preparedness → Crisis Comm Tests | contains the approved granular legal requirement |
| Continuity Preparedness → Backup Switchover Tests | contains the approved granular legal requirement |
| Continuity Preparedness → Continuity Plan Review | contains the approved granular legal requirement |
| Continuity Preparedness → Crisis Management | contains the approved granular legal requirement |
| Continuity Preparedness → Incident Cost Reporting | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Continuity Preparedness**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Business Continuity Policy — Stakeholder-constrained; Continuity Arrangements — Stakeholder-constrained; Critical Function Continuity — Stakeholder-constrained; Incident Impact Estimate — Stakeholder-constrained; Crisis Communications — Externally owned; Recovery Plan Audit — Externally owned; Continuity Plan Testing — Stakeholder-constrained; Business-impact analysis — Stakeholder-constrained; Disruption Impact Assessment — Stakeholder-constrained; BIA-aligned redundancy — Stakeholder-constrained; Continuity Test Schedule — Stakeholder-constrained; Crisis Comm Tests — Externally owned; Backup Switchover Tests — Stakeholder-constrained; Continuity Plan Review — Stakeholder-constrained; Crisis Management — Externally owned; Incident Cost Reporting — Externally owned.


### Recovery & Restoration

#### How to read this view

The view answers the approved concern for **Recovery & Restoration**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Incident Recovery | Requirement | Legal control family nested in the DORA framework. |
| Backup & Restoration | Requirement | Legal control family nested in the DORA framework. |
| Azure Key Vault Secrets | DataObject | Approved operational endpoint: Azure Key Vault Secrets. |
| DB Connection Testing | BusinessProcess | Approved operational endpoint: Database Connection Testing. |
| Database Table Data | DataObject | Approved operational endpoint: Database Table Data. |
| Datadog Alert | BusinessEvent | Approved operational endpoint: Datadog Alert. |
| Infra Issue Resolution | BusinessProcess | Approved operational endpoint: Infrastructure Issue Resolution. |
| Non-production Testing | BusinessProcess | Approved operational endpoint: Non-production Testing. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| Ranger Backup | BusinessProcess | Approved operational endpoint: Ranger Backup. |
| Secret Retrieval | BusinessProcess | Approved operational endpoint: Secret Retrieval. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Prompt incident response | Requirement | Nested in Incident Recovery; Respond to and resolve incidents promptly and effectively (Art. 11(2)(b)). |
| Recovery Priority | Requirement | Nested in Incident Recovery; Prioritise resumption and recovery actions (Art. 11(2)(b)). |
| Recovery Containment | Requirement | Nested in Incident Recovery; Activate containment measures and plans without delay (Art. 11(2)(c)). |
| Recovery Procedures | Requirement | Nested in Incident Recovery; Maintain tailored response and recovery procedures (Art. 11(2)(c)). |
| Recovery Plans | Requirement | Nested in Incident Recovery; Implement ICT response and recovery plans (Art. 11(3)). |
| Disruption Activity Record | Requirement | Nested in Incident Recovery; Keep disruption-event activity records readily accessible (Art. 11(8)). |
| ICT Data Restoration | Requirement | Nested in Backup & Restoration; Restore ICT systems and data with minimal downtime, disruption, and loss (Art. 12(1)). |
| Backup Scope | Requirement | Nested in Backup & Restoration; Specify backup scope and minimum frequency (Art. 12(1)(a)). |
| Restoration Procedures | Requirement | Nested in Backup & Restoration; Develop restoration and recovery procedures and methods (Art. 12(1)(b)). |
| Activatable Backup | Requirement | Nested in Backup & Restoration; Provide activatable backup systems (Art. 12(2)). |
| Secure backup activation | Requirement | Nested in Backup & Restoration; Preserve security and data properties on backup activation (Art. 12(2)). |
| Backup Recovery Testing | Requirement | Nested in Backup & Restoration; Periodically test backup, restoration, and recovery (Art. 12(2)). |
| Segregated Restoration | Requirement | Nested in Backup & Restoration; Use physically and logically segregated restoration systems (Art. 12(3)). |
| Secure Restoration | Requirement | Nested in Backup & Restoration; Secure restoration systems against unauthorised access and corruption (Art. 12(3)). |
| Timely Restoration | Requirement | Nested in Backup & Restoration; Enable timely restoration using data and system backups (Art. 12(3)). |
| Redundant ICT Capacity | Requirement | Nested in Backup & Restoration; Maintain adequate redundant ICT capacity (Art. 12(4)). |
| RTO RPO Criticality | Requirement | Nested in Backup & Restoration; Set recovery time/point objectives based on criticality and impact (Art. 12(6)). |
| Extreme Service Levels | Requirement | Nested in Backup & Restoration; Meet agreed service levels in extreme scenarios (Art. 12(6)). |
| Recovery integrity checks | Requirement | Nested in Backup & Restoration; Perform recovery integrity checks and reconciliations (Art. 12(7)). |
| External Data Consistency | Requirement | Nested in Backup & Restoration; Ensure consistency of data reconstructed from external stakeholders (Art. 12(7)). |
| ICT Impact Controls | Requirement | Nested in Incident Recovery; Minimise ICT-risk impact through appropriate controls (Art. 6(3)). |
| Resilience Evidence | Requirement | Nested in Incident Recovery; Evidence current digital-resilience situation and preventive effectiveness (Art. 6(8)(f)). |
| Security Impact Control | Requirement | Nested in Incident Recovery; Minimise ICT-risk impact with security tools, policies, and procedures (Art. 9(1)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| SingleStore Recovery → ICT Impact Controls | Realization | Recovery directly mitigates stated service-impact incidents. Ownership: Directly performed. |
| Post-Incident Reporting → Resilience Evidence | Association | Report provides a constrained technical input. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Security Impact Control | Realization | Recovery directly mitigates the incident. Ownership: Directly performed. |
| SingleStore Recovery → Prompt incident response | Realization | Response and remediation are directly performed. Ownership: Directly performed. |
| SingleStore Recovery → Recovery Priority | Realization | Recovery is directly performed. Ownership: Directly performed. |
| SingleStore Recovery → Recovery Containment | Association | Containment-plan ownership is unstated. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Recovery Procedures | Realization | Recovery-tool use is directly performed. Ownership: Directly performed. |
| SingleStore Recovery → Recovery Plans | Association | Recovery is constrained by plan ownership. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Disruption Activity Record | Association | Report provides a constrained record input. Ownership: Stakeholder-constrained. |
| Ranger Backup → ICT Data Restoration | Association | Backup is a constrained recovery input. Ownership: Stakeholder-constrained. |
| Ranger Backup → Backup Scope | Realization | Backup is directly performed; policy scope/frequency is unstated. Ownership: Directly performed. |
| SingleStore Recovery → Restoration Procedures | Realization | Recovery is directly performed. Ownership: Directly performed. |
| Ranger Backup → Activatable Backup | Association | Activation capability is unstated. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Secure backup activation | Association | Secret work is constrained by protection duty. Ownership: Stakeholder-constrained. |
| Non-production Testing → Backup Recovery Testing | Association | Tests are not identified as backup/recovery tests. Ownership: Stakeholder-constrained. |
| Infra Issue Resolution → Segregated Restoration | Association | Restoration-environment design is external. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Secure Restoration | Association | Secret handling is constrained by this duty. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Timely Restoration | Realization | Timely recovery is directly performed. Ownership: Directly performed. |
| Infra Issue Resolution → Redundant ICT Capacity | Association | Capacity depends on compute team. Ownership: Stakeholder-constrained. |
| SingleStore Outage → RTO RPO Criticality | Association | Outage impact is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Extreme Service Levels | Association | Service levels are not owned by the role. Ownership: Stakeholder-constrained. |
| DB Connection Testing → Recovery integrity checks | Association | Query testing is a constrained integrity input. Ownership: Stakeholder-constrained. |
| DB Connection Testing → External Data Consistency | Association | External-data reconstruction is not evidenced. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Ranger Backup | Assignment | backs up Ranger data before change |
| Infra Eng & Cloud DBA → Secret Retrieval | Assignment | retrieves credentials to correct issues |
| Secret Retrieval → Azure Key Vault Secrets | Access | accesses passwords and secrets |
| Infra Eng & Cloud DBA → DB Connection Testing | Assignment | performs limited connection tests |
| DB Connection Testing → Database Table Data | Access | reads limited data through test queries |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Infra Eng & Cloud DBA → SingleStore Recovery | Assignment | restarts, investigates, and mitigates |
| Datadog Alert → SingleStore Recovery | Triggering | initiates the response |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Incident Recovery | contains the approved stakeholder-scoped requirement family |
| DORA Resilience Framework → Backup & Restoration | contains the approved stakeholder-scoped requirement family |
| Incident Recovery → ICT Impact Controls | contains the approved granular legal requirement |
| Incident Recovery → Resilience Evidence | contains the approved granular legal requirement |
| Incident Recovery → Security Impact Control | contains the approved granular legal requirement |
| Incident Recovery → Prompt incident response | contains the approved granular legal requirement |
| Incident Recovery → Recovery Priority | contains the approved granular legal requirement |
| Incident Recovery → Recovery Containment | contains the approved granular legal requirement |
| Incident Recovery → Recovery Procedures | contains the approved granular legal requirement |
| Incident Recovery → Recovery Plans | contains the approved granular legal requirement |
| Incident Recovery → Disruption Activity Record | contains the approved granular legal requirement |
| Backup & Restoration → ICT Data Restoration | contains the approved granular legal requirement |
| Backup & Restoration → Backup Scope | contains the approved granular legal requirement |
| Backup & Restoration → Restoration Procedures | contains the approved granular legal requirement |
| Backup & Restoration → Activatable Backup | contains the approved granular legal requirement |
| Backup & Restoration → Secure backup activation | contains the approved granular legal requirement |
| Backup & Restoration → Backup Recovery Testing | contains the approved granular legal requirement |
| Backup & Restoration → Segregated Restoration | contains the approved granular legal requirement |
| Backup & Restoration → Secure Restoration | contains the approved granular legal requirement |
| Backup & Restoration → Timely Restoration | contains the approved granular legal requirement |
| Backup & Restoration → Redundant ICT Capacity | contains the approved granular legal requirement |
| Backup & Restoration → RTO RPO Criticality | contains the approved granular legal requirement |
| Backup & Restoration → Extreme Service Levels | contains the approved granular legal requirement |
| Backup & Restoration → Recovery integrity checks | contains the approved granular legal requirement |
| Backup & Restoration → External Data Consistency | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Recovery & Restoration**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Resilience Evidence — Stakeholder-constrained; Recovery Containment — Stakeholder-constrained; Recovery Plans — Stakeholder-constrained; Disruption Activity Record — Stakeholder-constrained; ICT Data Restoration — Stakeholder-constrained; Activatable Backup — Stakeholder-constrained; Secure backup activation — Stakeholder-constrained; Backup Recovery Testing — Stakeholder-constrained; Segregated Restoration — Stakeholder-constrained; Secure Restoration — Stakeholder-constrained; Redundant ICT Capacity — Stakeholder-constrained; RTO RPO Criticality — Stakeholder-constrained; Extreme Service Levels — Stakeholder-constrained; Recovery integrity checks — Stakeholder-constrained; External Data Consistency — Stakeholder-constrained.


### Operational Learning

#### How to read this view

The view answers the approved concern for **Operational Learning**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Operational Learning | Requirement | Legal control family nested in the DORA framework. |
| Change Review | BusinessProcess | Approved operational endpoint: Change Review. |
| Datadog Alert | BusinessEvent | Approved operational endpoint: Datadog Alert. |
| DevOps Leads | BusinessActor | Approved operational endpoint: DevOps Leads. |
| LLM Tools | ApplicationComponent | Approved operational endpoint: LLM Tools. |
| Log Investigation | BusinessProcess | Approved operational endpoint: Log Investigation. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| SingleStore Incident | BusinessProcess | Approved operational endpoint: SingleStore Incident Response. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Stakeholder Team | BusinessActor | Approved operational endpoint: Stakeholder Team. |
| Team Lead | BusinessActor | Approved operational endpoint: Team Lead. |
| Technology Maintenance | BusinessProcess | Approved operational endpoint: Technology Maintenance. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Major Incident Review | Requirement | Nested in Operational Learning; Conduct post-major-incident reviews (Art. 13(2)). |
| Improvement Identification | Requirement | Nested in Operational Learning; Identify required improvements to ICT operations or continuity policy (Art. 13(2)). |
| Authority Change Notice | Requirement | Nested in Operational Learning; Communicate review-driven changes to authorities on request (Art. 13(2)). |
| Procedure Effectiveness | Requirement | Nested in Operational Learning; Determine whether procedures and actions were followed/effective (Art. 13(2)). |
| Response Severity Review | Requirement | Nested in Operational Learning; Assess response promptness and incident severity assessment (Art. 13(2)(a)). |
| Forensic Review | Requirement | Nested in Operational Learning; Assess forensic-analysis quality and speed (Art. 13(2)(b)). |
| Escalation Review | Requirement | Nested in Operational Learning; Assess effectiveness of incident escalation (Art. 13(2)(c)). |
| Communication Review | Requirement | Nested in Operational Learning; Assess effectiveness of internal and external communication (Art. 13(2)(d)). |
| Risk Assessment Lessons | Requirement | Nested in Operational Learning; Incorporate lessons into ICT-risk assessment (Art. 13(3)). |
| Framework Component Review | Requirement | Nested in Operational Learning; Review ICT-risk-framework components using those lessons (Art. 13(3)). |
| Strategy Effectiveness | Requirement | Nested in Operational Learning; Monitor resilience-strategy implementation effectiveness (Art. 13(4)). |
| Risk Pattern Mapping | Requirement | Nested in Operational Learning; Map ICT-risk evolution and incident patterns (Art. 13(4)). |
| Senior ICT Report | Requirement | Nested in Operational Learning; Senior ICT staff report findings and recommendations yearly (Art. 13(5)). |
| Resilience Training | Requirement | Nested in Operational Learning; Provide compulsory awareness and resilience training (Art. 13(6)). |
| Technology Monitoring | Requirement | Nested in Operational Learning; Monitor relevant technological developments and current risk-management practices (Art. 13(7)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Post-Incident Reporting → Major Incident Review | Association | Report is input; formal review ownership is unstated. Ownership: Stakeholder-constrained. |
| Technology Maintenance → Improvement Identification | Association | Evidence is constrained by formal review ownership. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Authority Change Notice | Association | Authority communication is external. Ownership: Externally owned. |
| Change Review → Procedure Effectiveness | Association | Review is a constrained input. Ownership: Stakeholder-constrained. |
| Datadog Alert → Response Severity Review | Association | Alert evidence is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Forensic Review | Association | Cause investigation is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Incident → Escalation Review | Association | Escalation participants are explicit. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Communication Review | Association | Support handoff is a constrained communication input. Ownership: Stakeholder-constrained. |
| Change Review → Risk Assessment Lessons | Association | No integration owner is stated. Ownership: Stakeholder-constrained. |
| Technology Maintenance → Framework Component Review | Association | Maintenance is constrained by framework review. Ownership: Stakeholder-constrained. |
| Stakeholder Team → Strategy Effectiveness | Association | Strategy monitoring is external. Ownership: Externally owned. |
| Datadog Alert → Risk Pattern Mapping | Association | Metrics are a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Incident → Senior ICT Report | Association | Management reporting is external. Ownership: Externally owned. |
| Infra Eng & Cloud DBA → Resilience Training | Association | Role is subject to training; training provision owner unstated. Ownership: Stakeholder-constrained. |
| Technology Maintenance → Technology Monitoring | Association | Investigation is a constrained input. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Technology Maintenance | Assignment | updates and reconfigures technology |
| Infra Eng & Cloud DBA → Log Investigation | Assignment | investigates logs and external information |
| Log Investigation → LLM Tools | Association | uses LLMs to parse logs and search information |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Infra Eng & Cloud DBA → SingleStore Recovery | Assignment | restarts, investigates, and mitigates |
| Datadog Alert → SingleStore Recovery | Triggering | initiates the response |
| Team Lead → SingleStore Incident | Assignment | participates in response |
| DevOps Leads → SingleStore Incident | Assignment | participates in response |
| Technology Support Team → SingleStore Incident | Assignment | participates in extreme cases |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Infra Eng & Cloud DBA → Change Review | Assignment | self-checks and reviews completed changes |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Operational Learning | contains the approved stakeholder-scoped requirement family |
| Operational Learning → Major Incident Review | contains the approved granular legal requirement |
| Operational Learning → Improvement Identification | contains the approved granular legal requirement |
| Operational Learning → Authority Change Notice | contains the approved granular legal requirement |
| Operational Learning → Procedure Effectiveness | contains the approved granular legal requirement |
| Operational Learning → Response Severity Review | contains the approved granular legal requirement |
| Operational Learning → Forensic Review | contains the approved granular legal requirement |
| Operational Learning → Escalation Review | contains the approved granular legal requirement |
| Operational Learning → Communication Review | contains the approved granular legal requirement |
| Operational Learning → Risk Assessment Lessons | contains the approved granular legal requirement |
| Operational Learning → Framework Component Review | contains the approved granular legal requirement |
| Operational Learning → Strategy Effectiveness | contains the approved granular legal requirement |
| Operational Learning → Risk Pattern Mapping | contains the approved granular legal requirement |
| Operational Learning → Senior ICT Report | contains the approved granular legal requirement |
| Operational Learning → Resilience Training | contains the approved granular legal requirement |
| Operational Learning → Technology Monitoring | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Operational Learning**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Major Incident Review — Stakeholder-constrained; Improvement Identification — Stakeholder-constrained; Authority Change Notice — Externally owned; Procedure Effectiveness — Stakeholder-constrained; Response Severity Review — Stakeholder-constrained; Forensic Review — Stakeholder-constrained; Escalation Review — Stakeholder-constrained; Communication Review — Stakeholder-constrained; Risk Assessment Lessons — Stakeholder-constrained; Framework Component Review — Stakeholder-constrained; Strategy Effectiveness — Externally owned; Risk Pattern Mapping — Stakeholder-constrained; Senior ICT Report — Externally owned; Resilience Training — Stakeholder-constrained; Technology Monitoring — Stakeholder-constrained.


### Crisis Communication

#### How to read this view

The view answers the approved concern for **Crisis Communication**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Crisis Communication | Requirement | Legal control family nested in the DORA framework. |
| DevOps Leads | BusinessActor | Approved operational endpoint: DevOps Leads. |
| Post-Incident Report | BusinessObject | Approved operational endpoint: Post-Incident Report. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| SingleStore Incident | BusinessProcess | Approved operational endpoint: SingleStore Incident Response. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| Support Handoff | BusinessProcess | Approved operational endpoint: Support Handoff. |
| Team Lead | BusinessActor | Approved operational endpoint: Team Lead. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Crisis Communication Plan | Requirement | Nested in Crisis Communication; Maintain crisis-communication plans (Art. 14(1)). |
| Responsible Disclosure | Requirement | Nested in Crisis Communication; Enable responsible disclosure of major incidents/vulnerabilities (Art. 14(1)). |
| Internal External Policy | Requirement | Nested in Crisis Communication; Implement internal and external communication policies (Art. 14(2)). |
| Response Staff Separation | Requirement | Nested in Crisis Communication; Differentiate ICT-response staff from staff to be informed (Art. 14(2)). |
| Public Media Responsibility | Requirement | Nested in Crisis Communication; Assign public/media incident-communication responsibility (Art. 14(3)). |
| Incident Communication | Requirement | Nested in Crisis Communication; Outline communication strategy for reportable ICT incidents (Art. 6(8)(h)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Post-Incident Reporting → Incident Communication | Association | Communication-strategy ownership is external. Ownership: Externally owned. |
| Post-Incident Report → Crisis Communication Plan | Association | Plan ownership is external. Ownership: Externally owned. |
| SingleStore Outage → Responsible Disclosure | Association | Disclosure is external. Ownership: Externally owned. |
| Post-Incident Reporting → Internal External Policy | Association | Policy ownership is external. Ownership: Externally owned. |
| SingleStore Incident → Response Staff Separation | Association | Participants give a constrained staffing input. Ownership: Stakeholder-constrained. |
| Post-Incident Reporting → Public Media Responsibility | Association | No responsible person is identified. Ownership: Not evidenced / unclear owner. |
| Infra Eng & Cloud DBA → Support Handoff | Assignment | provides technical evidence to support teams |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends logs |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends configurations |
| Team Lead → SingleStore Incident | Assignment | participates in response |
| DevOps Leads → SingleStore Incident | Assignment | participates in response |
| Technology Support Team → SingleStore Incident | Assignment | participates in extreme cases |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Post-Incident Reporting → Technology Support Team | Flow | transfers the report |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Crisis Communication | contains the approved stakeholder-scoped requirement family |
| Crisis Communication → Incident Communication | contains the approved granular legal requirement |
| Crisis Communication → Crisis Communication Plan | contains the approved granular legal requirement |
| Crisis Communication → Responsible Disclosure | contains the approved granular legal requirement |
| Crisis Communication → Internal External Policy | contains the approved granular legal requirement |
| Crisis Communication → Response Staff Separation | contains the approved granular legal requirement |
| Crisis Communication → Public Media Responsibility | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Crisis Communication**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Incident Communication — Externally owned; Crisis Communication Plan — Externally owned; Responsible Disclosure — Externally owned; Internal External Policy — Externally owned; Response Staff Separation — Stakeholder-constrained; Public Media Responsibility — Not evidenced / unclear owner.

Potential operational or visibility limitation from this stakeholder perspective: Public Media Responsibility has no evidenced responsible owner. This is not a compliance conclusion.


### Incident Management

#### How to read this view

The view answers the approved concern for **Incident Management**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Incident Management | Requirement | Legal control family nested in the DORA framework. |
| Datadog Alert | BusinessEvent | Approved operational endpoint: Datadog Alert. |
| DevOps Leads | BusinessActor | Approved operational endpoint: DevOps Leads. |
| Non-prod Support Test | BusinessProcess | Approved operational endpoint: Non-production Support Testing. |
| Post-Incident Reporting | BusinessProcess | Approved operational endpoint: Post-Incident Reporting. |
| ServiceNow Incident | DataObject | Approved operational endpoint: ServiceNow Incident. |
| SingleStore Incident | BusinessProcess | Approved operational endpoint: SingleStore Incident Response. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Support Handoff | BusinessProcess | Approved operational endpoint: Support Handoff. |
| Team Lead | BusinessActor | Approved operational endpoint: Team Lead. |
| Technology Support Team | BusinessActor | Approved operational endpoint: Technology Support Team. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Incident Process | Requirement | Nested in Incident Management; Define, establish, and implement incident management (Art. 17(1)). |
| Incident Response Notice | Requirement | Nested in Incident Management; Detect, manage, and notify ICT-related incidents (Art. 17(1)). |
| Incident Record | Requirement | Nested in Incident Management; Record ICT incidents and significant cyber threats (Art. 17(2)). |
| Incident Lifecycle | Requirement | Nested in Incident Management; Monitor, handle, and follow up incidents consistently (Art. 17(2)). |
| Root Cause Treatment | Requirement | Nested in Incident Management; Identify, document, and address root causes (Art. 17(2)). |
| Early-warning indicators | Requirement | Nested in Incident Management; Maintain early-warning indicators (Art. 17(3)(a)). |
| Incident Tracking | Requirement | Nested in Incident Management; Identify, track, log, categorise, and classify incidents (Art. 17(3)(b)). |
| Incident Role Assignment | Requirement | Nested in Incident Management; Assign roles/responsibilities for incident scenarios (Art. 17(3)(c)). |
| Incident Escalation | Requirement | Nested in Incident Management; Set communication, notification, and escalation procedures (Art. 17(3)(d)). |
| Major-incident reporting | Requirement | Nested in Incident Management; Report major incidents to senior management/body (Art. 17(3)(e)). |
| Incident Impact Control | Requirement | Nested in Incident Management; Mitigate impact and restore secure services promptly (Art. 17(3)(f)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| SingleStore Recovery → Incident Process | Association | Recovery is constrained by process ownership. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Incident Response Notice | Association | Detection/recovery are explicit; notification owner unstated. Ownership: Stakeholder-constrained. |
| Non-prod Support Test → Incident Record | Association | Records are a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Incident Lifecycle | Association | Activity is constrained by broader process ownership. Ownership: Stakeholder-constrained. |
| SingleStore Recovery → Root Cause Treatment | Realization | Cause investigation and mitigation are directly performed. Ownership: Directly performed. |
| Datadog Alert → Early-warning indicators | Realization | Early alerts are directly evidenced. Ownership: Directly performed. |
| Non-prod Support Test → Incident Tracking | Association | Classification ownership is unstated. Ownership: Stakeholder-constrained. |
| SingleStore Incident → Incident Role Assignment | Association | Formal assignment is externally owned. Ownership: Externally owned. |
| SingleStore Incident → Incident Escalation | Association | Handoffs are a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Incident → Major-incident reporting | Association | Management reporting is external. Ownership: Externally owned. |
| SingleStore Recovery → Incident Impact Control | Realization | Recovery is directly performed. Ownership: Directly performed. |
| Infra Eng & Cloud DBA → Non-prod Support Test | Assignment | tests non-production requests |
| Non-prod Support Test → ServiceNow Incident | Access | uses the incident record for requested work |
| Infra Eng & Cloud DBA → Support Handoff | Assignment | provides technical evidence to support teams |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends logs |
| Infra Eng & Cloud DBA → Technology Support Team | Flow | sends configurations |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Infra Eng & Cloud DBA → SingleStore Recovery | Assignment | restarts, investigates, and mitigates |
| Datadog Alert → SingleStore Recovery | Triggering | initiates the response |
| Team Lead → SingleStore Incident | Assignment | participates in response |
| DevOps Leads → SingleStore Incident | Assignment | participates in response |
| Technology Support Team → SingleStore Incident | Assignment | participates in extreme cases |
| Infra Eng & Cloud DBA → Post-Incident Reporting | Assignment | creates the support report |
| Post-Incident Reporting → Technology Support Team | Flow | transfers the report |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Incident Management | contains the approved stakeholder-scoped requirement family |
| Incident Management → Incident Process | contains the approved granular legal requirement |
| Incident Management → Incident Response Notice | contains the approved granular legal requirement |
| Incident Management → Incident Record | contains the approved granular legal requirement |
| Incident Management → Incident Lifecycle | contains the approved granular legal requirement |
| Incident Management → Root Cause Treatment | contains the approved granular legal requirement |
| Incident Management → Early-warning indicators | contains the approved granular legal requirement |
| Incident Management → Incident Tracking | contains the approved granular legal requirement |
| Incident Management → Incident Role Assignment | contains the approved granular legal requirement |
| Incident Management → Incident Escalation | contains the approved granular legal requirement |
| Incident Management → Major-incident reporting | contains the approved granular legal requirement |
| Incident Management → Incident Impact Control | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Incident Management**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Incident Process — Stakeholder-constrained; Incident Response Notice — Stakeholder-constrained; Incident Record — Stakeholder-constrained; Incident Lifecycle — Stakeholder-constrained; Incident Tracking — Stakeholder-constrained; Incident Role Assignment — Externally owned; Incident Escalation — Stakeholder-constrained; Major-incident reporting — Externally owned.


### Incident Classification

#### How to read this view

The view answers the approved concern for **Incident Classification**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Incident Classification | Requirement | Legal control family nested in the DORA framework. |
| Azure Key Vault Secrets | DataObject | Approved operational endpoint: Azure Key Vault Secrets. |
| Datadog Alert | BusinessEvent | Approved operational endpoint: Datadog Alert. |
| Secret Retrieval | BusinessProcess | Approved operational endpoint: Secret Retrieval. |
| SingleStore Outage | BusinessEvent | Approved operational endpoint: SingleStore Outage. |
| SingleStore Recovery | BusinessProcess | Approved operational endpoint: SingleStore Recovery. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Incident classification | Requirement | Nested in Incident Classification; Classify incidents and determine their impact (Art. 18(1)). |
| Client Impact | Requirement | Nested in Incident Classification; Consider affected clients/counterparts (Art. 18(1)(a)). |
| Transaction Impact | Requirement | Nested in Incident Classification; Consider affected transactions (Art. 18(1)(a)). |
| Reputational Impact | Requirement | Nested in Incident Classification; Consider reputational impact (Art. 18(1)(a)). |
| Duration and downtime | Requirement | Nested in Incident Classification; Consider incident duration and downtime (Art. 18(1)(b)). |
| Geographic Spread | Requirement | Nested in Incident Classification; Consider geographical spread (Art. 18(1)(c)). |
| Data-loss criterion | Requirement | Nested in Incident Classification; Consider availability, authenticity, integrity, and confidentiality data losses (Art. 18(1)(d)). |
| Critical Service Impact | Requirement | Nested in Incident Classification; Consider criticality of affected services and operations (Art. 18(1)(e)). |
| Economic-impact criterion | Requirement | Nested in Incident Classification; Consider direct and indirect economic impact (Art. 18(1)(f)). |
| Cyber Threat Rating | Requirement | Nested in Incident Classification; Classify significant cyber threats (Art. 18(2)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| SingleStore Outage → Incident classification | Association | Outage evidence is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Client Impact | Association | Client/counterpart classification is external. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Transaction Impact | Association | Transaction classification is external. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Reputational Impact | Association | Reputation assessment is external. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Duration and downtime | Association | Service impact is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Geographic Spread | Association | Geographical assessment is external. Ownership: Stakeholder-constrained. |
| Secret Retrieval → Data-loss criterion | Association | Data-loss classification is external. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Critical Service Impact | Association | Service impact is a constrained input. Ownership: Stakeholder-constrained. |
| SingleStore Outage → Economic-impact criterion | Association | Economic calculation is external. Ownership: Stakeholder-constrained. |
| Datadog Alert → Cyber Threat Rating | Association | Threat classification is external. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Secret Retrieval | Assignment | retrieves credentials to correct issues |
| Secret Retrieval → Azure Key Vault Secrets | Access | accesses passwords and secrets |
| SingleStore Outage → SingleStore Recovery | Triggering | initiates incident recovery |
| Infra Eng & Cloud DBA → SingleStore Recovery | Assignment | restarts, investigates, and mitigates |
| Datadog Alert → SingleStore Recovery | Triggering | initiates the response |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Incident Classification | contains the approved stakeholder-scoped requirement family |
| Incident Classification → Incident classification | contains the approved granular legal requirement |
| Incident Classification → Client Impact | contains the approved granular legal requirement |
| Incident Classification → Transaction Impact | contains the approved granular legal requirement |
| Incident Classification → Reputational Impact | contains the approved granular legal requirement |
| Incident Classification → Duration and downtime | contains the approved granular legal requirement |
| Incident Classification → Geographic Spread | contains the approved granular legal requirement |
| Incident Classification → Data-loss criterion | contains the approved granular legal requirement |
| Incident Classification → Critical Service Impact | contains the approved granular legal requirement |
| Incident Classification → Economic-impact criterion | contains the approved granular legal requirement |
| Incident Classification → Cyber Threat Rating | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Incident Classification**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Incident classification — Stakeholder-constrained; Client Impact — Stakeholder-constrained; Transaction Impact — Stakeholder-constrained; Reputational Impact — Stakeholder-constrained; Duration and downtime — Stakeholder-constrained; Geographic Spread — Stakeholder-constrained; Data-loss criterion — Stakeholder-constrained; Critical Service Impact — Stakeholder-constrained; Economic-impact criterion — Stakeholder-constrained; Cyber Threat Rating — Stakeholder-constrained.


### Resilience Testing

#### How to read this view

The view answers the approved concern for **Resilience Testing**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Resilience Testing | Requirement | Legal control family nested in the DORA framework. |
| Change Validation | BusinessProcess | Approved operational endpoint: Change Validation. |
| Collaborative Test | BusinessProcess | Approved operational endpoint: Collaborative Validation Test. |
| DB Connection Testing | BusinessProcess | Approved operational endpoint: Database Connection Testing. |
| Database Table Data | DataObject | Approved operational endpoint: Database Table Data. |
| DevOps Team | BusinessActor | Approved operational endpoint: DevOps Team. |
| Emergency Change | BusinessProcess | Approved operational endpoint: Emergency Change. |
| Non-prod Support Test | BusinessProcess | Approved operational endpoint: Non-production Support Testing. |
| Non-production Testing | BusinessProcess | Approved operational endpoint: Non-production Testing. |
| Production Readiness | BusinessEvent | Approved operational event: Production Readiness Decision. |
| ServiceNow Incident | DataObject | Approved operational endpoint: ServiceNow Incident. |
| Starburst | ApplicationComponent | Approved operational endpoint: Starburst. |
| Starburst GitOps Move | BusinessProcess | Approved operational endpoint: Starburst GitOps Migration. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| Test Programme | Requirement | Nested in Resilience Testing; Establish, maintain, and review resilience-testing programme (Art. 24(1)). |
| Test Readiness | Requirement | Nested in Resilience Testing; Assess preparedness, identify gaps, and implement corrections (Art. 24(1)). |
| Test Method Range | Requirement | Nested in Resilience Testing; Include a range of test assessments, methodologies, practices, and tools (Art. 24(2)). |
| Risk-based test approach | Requirement | Nested in Resilience Testing; Apply a risk-based testing approach (Art. 24(3)). |
| Independent test parties | Requirement | Nested in Resilience Testing; Use independent testing parties (Art. 24(4)). |
| Internal-test resources | Requirement | Nested in Resilience Testing; Resource internal testing and avoid conflicts of interest (Art. 24(4)). |
| Test Finding Remediation | Requirement | Nested in Resilience Testing; Prioritise, classify, remedy, and validate test findings (Art. 24(5)). |
| Critical System Testing | Requirement | Nested in Resilience Testing; Test critical ICT systems/applications at least yearly (Art. 24(6)). |
| Appropriate Resilience Tests | Requirement | Nested in Resilience Testing; Execute appropriate resilience tests (Art. 25(1)). |
| Resilience Test Coverage | Requirement | Nested in Resilience Testing; Cover compatibility, performance, end-to-end, and penetration testing as appropriate (Art. 25(1)). |
| Test Method Selection | Requirement | Nested in Resilience Testing; Use applicable assessment, scan, review, and scenario test methods (Art. 25(1)). |
| Operational Resilience Tests | Requirement | Nested in Resilience Testing; Implement digital operational resilience testing (Art. 6(8)(g)). |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Non-production Testing → Operational Resilience Tests | Realization | Testing is directly performed. Ownership: Directly performed. |
| Non-production Testing → Test Programme | Association | Programme ownership is unstated. Ownership: Stakeholder-constrained. |
| Emergency Change → Test Readiness | Association | The stated visibility gap is a constrained test-governance signal. Ownership: Stakeholder-constrained. |
| Non-production Testing → Test Method Range | Realization | Testing is directly performed. Ownership: Directly performed. |
| Non-production Testing → Risk-based test approach | Association | Risk approach is not evidenced. Ownership: Stakeholder-constrained. |
| Collaborative Test → Independent test parties | Association | Independence is not evidenced. Ownership: Stakeholder-constrained. |
| Collaborative Test → Internal-test resources | Association | Resource/conflict controls are not evidenced. Ownership: Stakeholder-constrained. |
| Emergency Change → Test Finding Remediation | Association | Visibility gap is a constrained test-governance signal. Ownership: Stakeholder-constrained. |
| Non-production Testing → Critical System Testing | Association | Frequency/criticality scope is not evidenced. Ownership: Stakeholder-constrained. |
| Non-production Testing → Appropriate Resilience Tests | Realization | Testing is directly performed. Ownership: Directly performed. |
| Change Validation → Resilience Test Coverage | Realization | Connectivity validation is directly performed. Ownership: Directly performed. |
| DB Connection Testing → Test Method Selection | Association | Test-method selection is constrained by the programme. Ownership: Stakeholder-constrained. |
| Infra Eng & Cloud DBA → Starburst GitOps Move | Assignment | migrates deployment approach |
| Infra Eng & Cloud DBA → Non-production Testing | Assignment | tests changes before production |
| Non-production Testing → Production Readiness | Triggering | establishes the condition to proceed |
| Infra Eng & Cloud DBA → Change Validation | Assignment | validates completed changes |
| Change Validation → Starburst | Association | checks service availability and database connection |
| Infra Eng & Cloud DBA → DB Connection Testing | Assignment | performs limited connection tests |
| DB Connection Testing → Database Table Data | Access | reads limited data through test queries |
| Infra Eng & Cloud DBA → Non-prod Support Test | Assignment | tests non-production requests |
| Non-prod Support Test → ServiceNow Incident | Access | uses the incident record for requested work |
| DevOps Team → Collaborative Test | Assignment | performs requested validation testing |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |
| DORA Resilience Framework → Resilience Testing | contains the approved stakeholder-scoped requirement family |
| Resilience Testing → Operational Resilience Tests | contains the approved granular legal requirement |
| Resilience Testing → Test Programme | contains the approved granular legal requirement |
| Resilience Testing → Test Readiness | contains the approved granular legal requirement |
| Resilience Testing → Test Method Range | contains the approved granular legal requirement |
| Resilience Testing → Risk-based test approach | contains the approved granular legal requirement |
| Resilience Testing → Independent test parties | contains the approved granular legal requirement |
| Resilience Testing → Internal-test resources | contains the approved granular legal requirement |
| Resilience Testing → Test Finding Remediation | contains the approved granular legal requirement |
| Resilience Testing → Critical System Testing | contains the approved granular legal requirement |
| Resilience Testing → Appropriate Resilience Tests | contains the approved granular legal requirement |
| Resilience Testing → Resilience Test Coverage | contains the approved granular legal requirement |
| Resilience Testing → Test Method Selection | contains the approved granular legal requirement |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Resilience Testing**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

External or constrained boundary: Test Programme — Stakeholder-constrained; Test Readiness — Stakeholder-constrained; Risk-based test approach — Stakeholder-constrained; Independent test parties — Stakeholder-constrained; Internal-test resources — Stakeholder-constrained; Test Finding Remediation — Stakeholder-constrained; Critical System Testing — Stakeholder-constrained; Test Method Selection — Stakeholder-constrained.


### Cross-platform Support

#### How to read this view

The view answers the approved concern for **Cross-platform Support**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Colleague Assistance | BusinessProcess | Approved operational endpoint: Colleague Assistance. |
| Cosmos | BusinessProcess | Approved operational endpoint: Cosmos. |
| Databricks | BusinessProcess | Approved operational endpoint: Databricks. |
| Kafka | BusinessProcess | Approved operational endpoint: Kafka. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Infra Eng & Cloud DBA → Colleague Assistance | Assignment | assists colleagues |
| Colleague Assistance → Kafka | Association | supports work involving Kafka |
| Colleague Assistance → Cosmos | Association | supports work involving Cosmos |
| Colleague Assistance → Databricks | Association | supports work involving Databricks |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Cross-platform Support**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.


### Investigation Tooling

#### How to read this view

The view answers the approved concern for **Investigation Tooling**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| LLM Tools | ApplicationComponent | Approved operational endpoint: LLM Tools. |
| Log Investigation | BusinessProcess | Approved operational endpoint: Log Investigation. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Infra Eng & Cloud DBA → Log Investigation | Assignment | investigates logs and external information |
| Log Investigation → LLM Tools | Association | uses LLMs to parse logs and search information |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Investigation Tooling**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.


### Emergency Change Context

#### How to read this view

The view answers the approved concern for **Emergency Change Context**. Start at **Infra Eng & Cloud DBA** and follow the stakeholder-to-Bank-to-DORA-entity-to-framework route. The connected elements below show the approved operational evidence, legal family containment, and ownership boundary for this concern.

#### Visible boxes and containment

| Box | ArchiMate type | Why it appears / containment |
| --- | --- | --- |
| Change Report | BusinessObject | Approved operational endpoint: Change Report. |
| Critical Service Impact | BusinessEvent | Approved operational endpoint: Critical Service Impact. |
| Emergency Change | BusinessProcess | Approved operational endpoint: Emergency Change. |
| Bank | BusinessActor | Operator-approved anonymized employing organization label. |
| DORA Resilience Framework | Requirement | Root legal framework for the immutable DORA baseline. |
| DORA financial entity | BusinessActor | Law-defined financial-entity role group; the stakeholder is not equated with this entity. |
| Infra Eng & Cloud DBA | BusinessRole | Full approved role label: Infrastructure Engineer / Cloud Database Administrator. |

#### Visible arrows

| Source → target | ArchiMate relation | Evidence-backed meaning and ownership |
| --- | --- | --- |
| Critical Service Impact → Emergency Change | Triggering | initiates urgent change handling |
| Infra Eng & Cloud DBA → Emergency Change | Assignment | implements required critical changes |
| Emergency Change → Change Report | Access (Write) | writes the change report after emergency action |
| Infra Eng & Cloud DBA → Bank | Association | works within |
| Bank → DORA financial entity | Specialization | is a DORA-regulated credit institution |
| DORA financial entity → DORA Resilience Framework | Association | is in scope of |

#### Semantic-only nesting

The following Composition relationships are represented by matching visual nesting; no internal arrow is drawn.

| Parent → child | Meaning |
| --- | --- |

#### Operational reality, mandates, and ownership boundary

The approved relationships above describe the daily operational reality for **Emergency Change Context**. Requirement boxes state the applicable DORA mandates; only **Realization** arrows are direct stakeholder work. All other coverage arrows are Associations, preserving external or constrained ownership.

## 3. Layer-by-Layer Architectural Walkthrough

- **Motivation layer:** DORA framework roots, requirement families, and granular legal requirements are nested through semantic-only Composition. Citations remain readable documentation; canonical legal-text identifiers are not repeated here.
- **Business layer:** The stakeholder role, Bank, DORA financial entity, teams, processes, events, and business objects express the approved work, approvals, incident, reporting, and support routes.
- **Application and technology layers:** Named platform components, tools, data objects, configuration artefacts, and AKS-related elements appear only where the approved relationship ledger names them.
- **Implementation layer:** No work package or deliverable is represented because none is approved in the operational relationship ledger.

## 4. Comprehensive Element, Requirement & Realization Traceability

| Coverage ID | Operational source IDs | Parent family / context stream | Requirement ID | Source citation | Ownership state | Representing element or external role | Operational meaning |
| --- | --- | --- | --- | --- | --- | --- | --- |
| COV-001 | OP-048 | ICT Risk Governance | REQ-Art6-01 | Art. 6(1) | Stakeholder-constrained | Stakeholder Team | Team technology accountability is constrained by the framework. |
| COV-002 | OP-007 | ICT Risk Governance | REQ-Art6-02 | Art. 6(1) | Stakeholder-constrained | Technology Maintenance | Maintenance work is constrained by the framework response objective. |
| COV-003 | OP-002, OP-003, OP-004 | ICT Risk Governance | REQ-Art6-03 | Art. 6(2) | Stakeholder-constrained | Starburst Administration | Administered platforms are the stated ICT assets. |
| COV-004 | OP-005, OP-009, OP-052, CON-002, CON-003 | Access & Security | REQ-Art6-04 | Art. 6(2) | Stakeholder-constrained | Access Provisioning | The named access work is constrained by this protection duty. |
| COV-005 | OP-037, OP-054, CON-007 | Incident Recovery | REQ-Art6-05 | Art. 6(3) | Directly performed | SingleStore Recovery | Recovery directly mitigates stated service-impact incidents. |
| COV-006 | OP-043 | ICT Risk Governance | REQ-Art6-06 | Art. 6(3) | Externally owned | Post-Incident Reporting | Report is sent to support; authority reporting is outside the role. |
| COV-007 | OP-048 | ICT Risk Governance | REQ-Art6-07 | Art. 6(4) | Externally owned | Stakeholder Team | Control-function ownership is not assigned to the stakeholder. |
| COV-008 | OP-044, OP-045 | Controlled Change | REQ-Art6-08 | Art. 6(4) | Externally owned | Change Authorization | Separate approval teams are explicit. |
| COV-009 | OP-050 | ICT Risk Governance | REQ-Art6-09 | Art. 6(5) | Stakeholder-constrained | Change Review | Review work is constrained by the framework-review duty. |
| COV-010 | OP-050, OP-043 | ICT Risk Governance | REQ-Art6-10 | Art. 6(5) | Stakeholder-constrained | Change Review | Both facts are inputs to, not evidence of ownership of, framework review. |
| COV-011 | OP-007 | ICT Risk Governance | REQ-Art6-11 | Art. 6(5) | Stakeholder-constrained | Technology Maintenance | Improvement work is constrained by the framework-improvement duty. |
| COV-012 | OP-043 | ICT Risk Governance | REQ-Art6-12 | Art. 6(5) | Externally owned | Post-Incident Reporting | Authority reporting is not assigned to the stakeholder. |
| COV-013 | OP-048 | ICT Risk Governance | REQ-Art6-13 | Art. 6(6) | Externally owned | Stakeholder Team | Audit ownership is external to the team role. |
| COV-014 | OP-001 | ICT Risk Governance | REQ-Art6-14 | Art. 6(6) | Externally owned | Infra Eng & Cloud DBA | No auditor role is evidenced. |
| COV-015 | OP-048 | ICT Risk Governance | REQ-Art6-15 | Art. 6(6) | Externally owned | Stakeholder Team | Audit planning is outside the stated role. |
| COV-016 | OP-050 | ICT Risk Governance | REQ-Art6-16 | Art. 6(7) | Stakeholder-constrained | Change Review | Review task can be constrained by audit follow-up. |
| COV-017 | OP-048 | ICT Risk Governance | REQ-Art6-17 | Art. 6(8) | Stakeholder-constrained | Stakeholder Team | Team accountability lies within the strategy's scope. |
| COV-018 | OP-048 | ICT Risk Governance | REQ-Art6-18 | Art. 6(8)(a) | Stakeholder-constrained | Stakeholder Team | Business-strategy ownership is not assigned to the role. |
| COV-019 | OP-036, CON-006 | ICT Risk Governance | REQ-Art6-19 | Art. 6(8)(b) | Stakeholder-constrained | SingleStore Outage | Stated outage impact is an input to tolerance setting. |
| COV-020 | OP-038 | Monitoring & Detection | REQ-Art6-20 | Art. 6(8)(c) | Stakeholder-constrained | Datadog Alert | Monitoring provides a constrained operational input. |
| COV-021 | OP-015, OP-020, OP-023 | Controlled Change | REQ-Art6-21 | Art. 6(8)(d) | Stakeholder-constrained | Starburst Config Deploy | Deployment/configuration changes affect the reference architecture. |
| COV-022 | OP-037, OP-038 | Monitoring & Detection | REQ-Art6-22 | Art. 6(8)(e) | Directly performed | SingleStore Recovery | Detection and recovery are directly performed. |
| COV-023 | OP-043 | Incident Recovery | REQ-Art6-23 | Art. 6(8)(f) | Stakeholder-constrained | Post-Incident Reporting | Report provides a constrained technical input. |
| COV-024 | OP-016, OP-017, OP-025 | Resilience Testing | REQ-Art6-24 | Art. 6(8)(g) | Directly performed | Non-production Testing | Testing is directly performed. |
| COV-025 | OP-043 | Crisis Communication | REQ-Art6-25 | Art. 6(8)(h) | Externally owned | Post-Incident Reporting | Communication-strategy ownership is external. |
| COV-026 | OP-002, OP-003, OP-004 | Provider Dependencies | REQ-Art6-26 | Art. 6(10) | Not evidenced / unclear owner | Starburst Administration | Providers are confirmed, but whether compliance verification is outsourced is unknown. |
| COV-027 | OP-002, OP-003, OP-004, OP-007 | Platform & Asset Mgmt | REQ-Art7-01 | Art. 7(1) | Directly performed | Starburst Administration | Maintenance is directly performed. |
| COV-028 | OP-002, OP-003, OP-004 | Platform & Asset Mgmt | REQ-Art7-02 | Art. 7(1)(a) | Stakeholder-constrained | Starburst Administration | System scale/proportionality is not assigned to the role. |
| COV-029 | OP-019 | Platform & Asset Mgmt | REQ-Art7-03 | Art. 7(1)(b) | Directly performed | Change Validation | Availability/connectivity validation is directly performed. |
| COV-030 | OP-031, CON-005 | Platform & Asset Mgmt | REQ-Art7-04 | Art. 7(1)(c) | Stakeholder-constrained | Infra Issue Resolution | Capacity depends on the stated compute team. |
| COV-031 | OP-036, CON-006 | Platform & Asset Mgmt | REQ-Art7-05 | Art. 7(1)(d) | Stakeholder-constrained | SingleStore Outage | The incident impact constrains resilience needs. |
| COV-032 | OP-001, OP-002, OP-003, OP-004, OP-048 | Platform & Asset Mgmt | REQ-Art8-01 | Art. 8(1) | Stakeholder-constrained | Infra Eng & Cloud DBA | Existing asset responsibility is a constrained input. |
| COV-033 | OP-050 | Platform & Asset Mgmt | REQ-Art8-02 | Art. 8(1) | Stakeholder-constrained | Change Review | Self-review is constrained by the broader duty. |
| COV-034 | OP-031, OP-032, OP-033 | Platform & Asset Mgmt | REQ-Art8-03 | Art. 8(2) | Stakeholder-constrained | Issue Correction | Named dependencies provide a constrained source record. |
| COV-035 | OP-006 | Platform & Asset Mgmt | REQ-Art8-04 | Art. 8(2) | Stakeholder-constrained | Developer Issue Diagnosis | Diagnosis work is constrained; threat assessment owner is unstated. |
| COV-036 | OP-031, OP-032, OP-033 | Platform & Asset Mgmt | REQ-Art8-05 | Art. 8(2) | Stakeholder-constrained | Issue Correction | Named dependencies are a constrained risk-scenario input. |
| COV-037 | OP-014 | Controlled Change | REQ-Art8-06 | Art. 8(3) | Stakeholder-constrained | Starburst GitOps Move | Major change is explicit; risk-assessment ownership is unstated. |
| COV-038 | OP-002, OP-003, OP-004 | Platform & Asset Mgmt | REQ-Art8-07 | Art. 8(4) | Stakeholder-constrained | Starburst Administration | Named administered technologies are asset evidence. |
| COV-039 | OP-002, OP-003, OP-004 | Platform & Asset Mgmt | REQ-Art8-08 | Art. 8(4) | Stakeholder-constrained | Starburst Administration | Criticality mapping owner is unstated. |
| COV-040 | OP-020, OP-021, OP-023 | Platform & Asset Mgmt | REQ-Art8-09 | Art. 8(4) | Stakeholder-constrained | YAML Config Maintenance | Configurations and integration are explicit. |
| COV-041 | OP-002, OP-003, OP-004 | Provider Dependencies | REQ-Art8-10 | Art. 8(5) | Stakeholder-constrained | Starburst Administration | Provider use is confirmed; documentation owner is unstated. |
| COV-042 | OP-021 | Platform & Asset Mgmt | REQ-Art8-11 | Art. 8(6) | Stakeholder-constrained | YAML Configuration | Configuration store is constrained by inventory duty. |
| COV-043 | OP-028 | Platform & Asset Mgmt | REQ-Art8-12 | Art. 8(6) | Stakeholder-constrained | ServiceNow Change Request | Change work is constrained by update duty. |
| COV-044 | OP-014, OP-023, CON-001 | Platform & Asset Mgmt | REQ-Art8-13 | Art. 8(7) | Stakeholder-constrained | Azure Key Vault | Historic script and connection are constrained risk-assessment inputs. |
| COV-045 | OP-038 | Monitoring & Detection | REQ-Art9-01 | Art. 9(1) | Directly performed | Datadog Alert | Monitoring is directly performed. |
| COV-046 | OP-037, OP-038 | Incident Recovery | REQ-Art9-02 | Art. 9(1) | Directly performed | SingleStore Recovery | Recovery directly mitigates the incident. |
| COV-047 | OP-002, OP-003, OP-004, OP-048 | Access & Security | REQ-Art9-03 | Art. 9(2) | Stakeholder-constrained | Starburst Administration | Platform work is constrained by the duty. |
| COV-048 | OP-022, OP-024 | Access & Security | REQ-Art9-04 | Art. 9(2) | Stakeholder-constrained | Secret Retrieval | Sensitive-data work is constrained by data protection. |
| COV-049 | OP-007 | Access & Security | REQ-Art9-05 | Art. 9(3) | Directly performed | Technology Maintenance | Maintenance is directly performed. |
| COV-050 | OP-034 | Access & Security | REQ-Art9-06 | Art. 9(3)(a) | Stakeholder-constrained | Support Handoff | Logs/configs are transferred; transfer-security control owner is unstated. |
| COV-051 | OP-022, OP-024 | Access & Security | REQ-Art9-07 | Art. 9(3)(b) | Stakeholder-constrained | Secret Retrieval | Secret use is constrained by prevention duty. |
| COV-052 | OP-036 | Access & Security | REQ-Art9-08 | Art. 9(3)(c) | Stakeholder-constrained | SingleStore Outage | Outage impact is a constrained input. |
| COV-053 | OP-005, OP-007 | Access & Security | REQ-Art9-09 | Art. 9(3)(d) | Stakeholder-constrained | Access Provisioning | Work is constrained by the protection duty. |
| COV-054 | OP-048 | Access & Security | REQ-Art9-10 | Art. 9(4)(a) | Stakeholder-constrained | Stakeholder Team | Policy ownership is unstated. |
| COV-055 | OP-031, OP-032 | Access & Security | REQ-Art9-11 | Art. 9(4)(b) | Stakeholder-constrained | Infra Issue Resolution | Responsibility rests with dependency teams. |
| COV-056 | OP-005, OP-008, OP-009, OP-052, CON-002, CON-003 | Access & Security | REQ-Art9-12 | Art. 9(4)(c) | Directly performed | Access Provisioning | Access administration is directly performed. |
| COV-057 | OP-045 | Access & Security | REQ-Art9-13 | Art. 9(4)(c) | Externally owned | Access Request Approval | Approval is externally owned. |
| COV-058 | OP-022 | Access & Security | REQ-Art9-14 | Art. 9(4)(d) | Stakeholder-constrained | Azure Key Vault | Secret store is constrained by this duty. |
| COV-059 | OP-022, OP-024 | Access & Security | REQ-Art9-15 | Art. 9(4)(d) | Stakeholder-constrained | Secret Retrieval | Classification/risk owner is unstated. |
| COV-060 | OP-027, OP-028 | Controlled Change | REQ-Art9-16 | Art. 9(4)(e) | Directly performed | Production Change Record | Recording is directly performed. |
| COV-061 | OP-017, OP-030, OP-050 | Controlled Change | REQ-Art9-17 | Art. 9(4)(e) | Stakeholder-constrained | Information Change | Testing/review is performed; approval is external. |
| COV-062 | OP-044, OP-046, OP-047, OP-056, CON-009 | Controlled Change | REQ-Art9-18 | Art. 9(4) | Not evidenced / unclear owner | Change Authorization | Authorization team exists; automation owner is unknown. |
| COV-063 | OP-007 | Controlled Change | REQ-Art9-19 | Art. 9(4)(f) | Stakeholder-constrained | Technology Maintenance | Updates are performed; policy owner unstated. |
| COV-064 | OP-032 | Access & Security | REQ-Art9-20 | Art. 9(4) | Stakeholder-constrained | Connection Resolution | Capability depends on networking team. |
| COV-065 | OP-038 | Monitoring & Detection | REQ-Art10-01 | Art. 10(1) | Directly performed | Datadog Alert | Detection is directly performed. |
| COV-066 | OP-031, OP-036, OP-038 | Monitoring & Detection | REQ-Art10-02 | Art. 10(1) | Stakeholder-constrained | Infra Issue Resolution | Evidence constrains the identification duty. |
| COV-067 | OP-016, OP-018 | Monitoring & Detection | REQ-Art10-03 | Art. 10(1) | Stakeholder-constrained | Non-production Testing | Detection-test scope/owner is unstated. |
| COV-068 | OP-038 | Monitoring & Detection | REQ-Art10-04 | Art. 10(2) | Stakeholder-constrained | Datadog Alert | Monitoring is a constrained input. |
| COV-069 | OP-038 | Monitoring & Detection | REQ-Art10-05 | Art. 10(2) | Stakeholder-constrained | Datadog Alert | Threshold ownership is unstated. |
| COV-070 | OP-038 | Monitoring & Detection | REQ-Art10-06 | Art. 10(2) | Directly performed | Datadog Alert | Automatic alerts are directly evidenced. |
| COV-071 | OP-038 | Monitoring & Detection | REQ-Art10-07 | Art. 10(3) | Stakeholder-constrained | Datadog Alert | Resource allocation is unstated. |
| COV-072 | OP-048 | Continuity Preparedness | REQ-Art11-01 | Art. 11(1) | Stakeholder-constrained | Stakeholder Team | Team technology accountability is constrained by policy. |
| COV-073 | OP-048 | Continuity Preparedness | REQ-Art11-02 | Art. 11(2) | Stakeholder-constrained | Stakeholder Team | Plan/procedure ownership is unstated. |
| COV-074 | OP-036, CON-006 | Continuity Preparedness | REQ-Art11-03 | Art. 11(2)(a) | Stakeholder-constrained | SingleStore Outage | Stated service impact is a continuity input. |
| COV-075 | OP-037, CON-007 | Incident Recovery | REQ-Art11-04 | Art. 11(2)(b) | Directly performed | SingleStore Recovery | Response and remediation are directly performed. |
| COV-076 | OP-037 | Incident Recovery | REQ-Art11-05 | Art. 11(2)(b) | Directly performed | SingleStore Recovery | Recovery is directly performed. |
| COV-077 | OP-037 | Incident Recovery | REQ-Art11-06 | Art. 11(2)(c) | Stakeholder-constrained | SingleStore Recovery | Containment-plan ownership is unstated. |
| COV-078 | OP-042 | Incident Recovery | REQ-Art11-07 | Art. 11(2)(c) | Directly performed | SingleStore Recovery | Recovery-tool use is directly performed. |
| COV-079 | OP-036 | Continuity Preparedness | REQ-Art11-08 | Art. 11(2)(d) | Stakeholder-constrained | SingleStore Outage | Outage evidence is a constrained input. |
| COV-080 | OP-043 | Continuity Preparedness | REQ-Art11-09 | Art. 11(2)(e) | Externally owned | Post-Incident Report | Report goes to support; formal reporting is external. |
| COV-081 | OP-037 | Incident Recovery | REQ-Art11-10 | Art. 11(3) | Stakeholder-constrained | SingleStore Recovery | Recovery is constrained by plan ownership. |
| COV-082 | OP-050 | Continuity Preparedness | REQ-Art11-11 | Art. 11(3) | Externally owned | Change Review | Independent audit is external. |
| COV-083 | OP-016 | Continuity Preparedness | REQ-Art11-12 | Art. 11(4) | Stakeholder-constrained | Non-production Testing | Testing is not evidenced as continuity-plan testing. |
| COV-084 | OP-036 | Continuity Preparedness | REQ-Art11-13 | Art. 11(5) | Stakeholder-constrained | SingleStore Outage | Incident impact is a constrained input. |
| COV-085 | OP-036 | Continuity Preparedness | REQ-Art11-14 | Art. 11(5) | Stakeholder-constrained | SingleStore Outage | Incident impact is a constrained input. |
| COV-086 | OP-031, OP-032, OP-033 | Provider Dependencies | REQ-Art11-15 | Art. 11(5) | Stakeholder-constrained | Infra Issue Resolution | Dependencies are explicitly stated. |
| COV-087 | OP-031 | Continuity Preparedness | REQ-Art11-16 | Art. 11(5) | Stakeholder-constrained | Infra Issue Resolution | Redundancy design depends on compute team. |
| COV-088 | OP-016 | Continuity Preparedness | REQ-Art11-17 | Art. 11(6)(a) | Stakeholder-constrained | Non-production Testing | Test frequency/scope is unstated. |
| COV-089 | OP-043 | Continuity Preparedness | REQ-Art11-18 | Art. 11(6)(b) | Externally owned | Post-Incident Reporting | Crisis communication testing is external. |
| COV-090 | OP-013, OP-016 | Continuity Preparedness | REQ-Art11-19 | Art. 11(6) | Stakeholder-constrained | Ranger Backup | Backup and testing are stated; scenario scope is unstated. |
| COV-091 | OP-050 | Continuity Preparedness | REQ-Art11-20 | Art. 11(6) | Stakeholder-constrained | Change Review | Review is not identified as plan review. |
| COV-092 | OP-039, OP-040, OP-041 | Continuity Preparedness | REQ-Art11-21 | Art. 11(7) | Externally owned | SingleStore Incident | Participants exist; formal function ownership is external. |
| COV-093 | OP-043 | Incident Recovery | REQ-Art11-22 | Art. 11(8) | Stakeholder-constrained | Post-Incident Reporting | Report provides a constrained record input. |
| COV-094 | OP-036, OP-043 | Continuity Preparedness | REQ-Art11-23 | Art. 11(10) | Externally owned | SingleStore Outage | Cost/loss calculation and authority reporting are external. |
| COV-095 | OP-013 | Backup & Restoration | REQ-Art12-01 | Art. 12(1) | Stakeholder-constrained | Ranger Backup | Backup is a constrained recovery input. |
| COV-096 | OP-013 | Backup & Restoration | REQ-Art12-02 | Art. 12(1)(a) | Directly performed | Ranger Backup | Backup is directly performed; policy scope/frequency is unstated. |
| COV-097 | OP-037 | Backup & Restoration | REQ-Art12-03 | Art. 12(1)(b) | Directly performed | SingleStore Recovery | Recovery is directly performed. |
| COV-098 | OP-013 | Backup & Restoration | REQ-Art12-04 | Art. 12(2) | Stakeholder-constrained | Ranger Backup | Activation capability is unstated. |
| COV-099 | OP-022 | Backup & Restoration | REQ-Art12-05 | Art. 12(2) | Stakeholder-constrained | Secret Retrieval | Secret work is constrained by protection duty. |
| COV-100 | OP-016 | Backup & Restoration | REQ-Art12-06 | Art. 12(2) | Stakeholder-constrained | Non-production Testing | Tests are not identified as backup/recovery tests. |
| COV-101 | OP-031 | Backup & Restoration | REQ-Art12-07 | Art. 12(3) | Stakeholder-constrained | Infra Issue Resolution | Restoration-environment design is external. |
| COV-102 | OP-022 | Backup & Restoration | REQ-Art12-08 | Art. 12(3) | Stakeholder-constrained | Secret Retrieval | Secret handling is constrained by this duty. |
| COV-103 | OP-037 | Backup & Restoration | REQ-Art12-09 | Art. 12(3) | Directly performed | SingleStore Recovery | Timely recovery is directly performed. |
| COV-104 | OP-031 | Backup & Restoration | REQ-Art12-10 | Art. 12(4) | Stakeholder-constrained | Infra Issue Resolution | Capacity depends on compute team. |
| COV-106 | OP-036 | Backup & Restoration | REQ-Art12-12 | Art. 12(6) | Stakeholder-constrained | SingleStore Outage | Outage impact is a constrained input. |
| COV-107 | OP-036 | Backup & Restoration | REQ-Art12-13 | Art. 12(6) | Stakeholder-constrained | SingleStore Outage | Service levels are not owned by the role. |
| COV-108 | OP-025 | Backup & Restoration | REQ-Art12-14 | Art. 12(7) | Stakeholder-constrained | DB Connection Testing | Query testing is a constrained integrity input. |
| COV-109 | OP-025 | Backup & Restoration | REQ-Art12-15 | Art. 12(7) | Stakeholder-constrained | DB Connection Testing | External-data reconstruction is not evidenced. |
| COV-110 | OP-036, OP-038 | Monitoring & Detection | REQ-Art13-01 | Art. 13(1) | Directly performed | SingleStore Outage | Monitoring and outage evidence are directly available to the role. |
| COV-111 | OP-043 | Operational Learning | REQ-Art13-02 | Art. 13(2) | Stakeholder-constrained | Post-Incident Reporting | Report is input; formal review ownership is unstated. |
| COV-112 | OP-007, OP-043 | Operational Learning | REQ-Art13-03 | Art. 13(2) | Stakeholder-constrained | Technology Maintenance | Evidence is constrained by formal review ownership. |
| COV-113 | OP-043 | Operational Learning | REQ-Art13-04 | Art. 13(2) | Externally owned | Post-Incident Reporting | Authority communication is external. |
| COV-114 | OP-050 | Operational Learning | REQ-Art13-05 | Art. 13(2) | Stakeholder-constrained | Change Review | Review is a constrained input. |
| COV-115 | OP-038 | Operational Learning | REQ-Art13-06 | Art. 13(2)(a) | Stakeholder-constrained | Datadog Alert | Alert evidence is a constrained input. |
| COV-116 | OP-037 | Operational Learning | REQ-Art13-07 | Art. 13(2)(b) | Stakeholder-constrained | SingleStore Recovery | Cause investigation is a constrained input. |
| COV-117 | OP-039, OP-040 | Operational Learning | REQ-Art13-08 | Art. 13(2)(c) | Stakeholder-constrained | SingleStore Incident | Escalation participants are explicit. |
| COV-118 | OP-043 | Operational Learning | REQ-Art13-09 | Art. 13(2)(d) | Stakeholder-constrained | Post-Incident Reporting | Support handoff is a constrained communication input. |
| COV-119 | OP-050 | Operational Learning | REQ-Art13-10 | Art. 13(3) | Stakeholder-constrained | Change Review | No integration owner is stated. |
| COV-120 | OP-007 | Operational Learning | REQ-Art13-11 | Art. 13(3) | Stakeholder-constrained | Technology Maintenance | Maintenance is constrained by framework review. |
| COV-121 | OP-048 | Operational Learning | REQ-Art13-12 | Art. 13(4) | Externally owned | Stakeholder Team | Strategy monitoring is external. |
| COV-122 | OP-038 | Operational Learning | REQ-Art13-13 | Art. 13(4) | Stakeholder-constrained | Datadog Alert | Metrics are a constrained input. |
| COV-123 | OP-039 | Operational Learning | REQ-Art13-14 | Art. 13(5) | Externally owned | SingleStore Incident | Management reporting is external. |
| COV-124 | OP-001 | Operational Learning | REQ-Art13-15 | Art. 13(6) | Stakeholder-constrained | Infra Eng & Cloud DBA | Role is subject to training; training provision owner unstated. |
| COV-125 | OP-002 | Provider Dependencies | REQ-Art13-16 | Art. 13(6) | Externally owned | Starburst Administration | Third-party training is externally owned. |
| COV-126 | OP-007, OP-026 | Operational Learning | REQ-Art13-17 | Art. 13(7) | Stakeholder-constrained | Technology Maintenance | Investigation is a constrained input. |
| COV-127 | OP-043 | Crisis Communication | REQ-Art14-01 | Art. 14(1) | Externally owned | Post-Incident Report | Plan ownership is external. |
| COV-128 | OP-036, OP-043 | Crisis Communication | REQ-Art14-02 | Art. 14(1) | Externally owned | SingleStore Outage | Disclosure is external. |
| COV-129 | OP-043 | Crisis Communication | REQ-Art14-03 | Art. 14(2) | Externally owned | Post-Incident Reporting | Policy ownership is external. |
| COV-130 | OP-039, OP-040, OP-041 | Crisis Communication | REQ-Art14-04 | Art. 14(2) | Stakeholder-constrained | SingleStore Incident | Participants give a constrained staffing input. |
| COV-131 | OP-043 | Crisis Communication | REQ-Art14-05 | Art. 14(3) | Not evidenced / unclear owner | Post-Incident Reporting | No responsible person is identified. |
| COV-132 | OP-037 | Incident Management | REQ-Art17-01 | Art. 17(1) | Stakeholder-constrained | SingleStore Recovery | Recovery is constrained by process ownership. |
| COV-133 | OP-037, OP-038 | Incident Management | REQ-Art17-02 | Art. 17(1) | Stakeholder-constrained | SingleStore Recovery | Detection/recovery are explicit; notification owner unstated. |
| COV-134 | OP-029, OP-043 | Incident Management | REQ-Art17-03 | Art. 17(2) | Stakeholder-constrained | Non-prod Support Test | Records are a constrained input. |
| COV-135 | OP-037 | Incident Management | REQ-Art17-04 | Art. 17(2) | Stakeholder-constrained | SingleStore Recovery | Activity is constrained by broader process ownership. |
| COV-136 | OP-037 | Incident Management | REQ-Art17-05 | Art. 17(2) | Directly performed | SingleStore Recovery | Cause investigation and mitigation are directly performed. |
| COV-137 | OP-038 | Incident Management | REQ-Art17-06 | Art. 17(3)(a) | Directly performed | Datadog Alert | Early alerts are directly evidenced. |
| COV-138 | OP-029, OP-043 | Incident Management | REQ-Art17-07 | Art. 17(3)(b) | Stakeholder-constrained | Non-prod Support Test | Classification ownership is unstated. |
| COV-139 | OP-039, OP-040, OP-041 | Incident Management | REQ-Art17-08 | Art. 17(3)(c) | Externally owned | SingleStore Incident | Formal assignment is externally owned. |
| COV-140 | OP-039, OP-040, OP-043 | Incident Management | REQ-Art17-09 | Art. 17(3)(d) | Stakeholder-constrained | SingleStore Incident | Handoffs are a constrained input. |
| COV-141 | OP-039 | Incident Management | REQ-Art17-10 | Art. 17(3)(e) | Externally owned | SingleStore Incident | Management reporting is external. |
| COV-142 | OP-037 | Incident Management | REQ-Art17-11 | Art. 17(3)(f) | Directly performed | SingleStore Recovery | Recovery is directly performed. |
| COV-143 | OP-036 | Incident Classification | REQ-Art18-01 | Art. 18(1) | Stakeholder-constrained | SingleStore Outage | Outage evidence is a constrained input. |
| COV-144 | OP-036 | Incident Classification | REQ-Art18-02 | Art. 18(1)(a) | Stakeholder-constrained | SingleStore Outage | Client/counterpart classification is external. |
| COV-145 | OP-036 | Incident Classification | REQ-Art18-03 | Art. 18(1)(a) | Stakeholder-constrained | SingleStore Outage | Transaction classification is external. |
| COV-146 | OP-036 | Incident Classification | REQ-Art18-04 | Art. 18(1)(a) | Stakeholder-constrained | SingleStore Outage | Reputation assessment is external. |
| COV-147 | OP-036 | Incident Classification | REQ-Art18-05 | Art. 18(1)(b) | Stakeholder-constrained | SingleStore Outage | Service impact is a constrained input. |
| COV-148 | OP-036 | Incident Classification | REQ-Art18-06 | Art. 18(1)(c) | Stakeholder-constrained | SingleStore Outage | Geographical assessment is external. |
| COV-149 | OP-024 | Incident Classification | REQ-Art18-07 | Art. 18(1)(d) | Stakeholder-constrained | Secret Retrieval | Data-loss classification is external. |
| COV-150 | OP-036 | Incident Classification | REQ-Art18-08 | Art. 18(1)(e) | Stakeholder-constrained | SingleStore Outage | Service impact is a constrained input. |
| COV-151 | OP-036 | Incident Classification | REQ-Art18-09 | Art. 18(1)(f) | Stakeholder-constrained | SingleStore Outage | Economic calculation is external. |
| COV-152 | OP-038 | Incident Classification | REQ-Art18-10 | Art. 18(2) | Stakeholder-constrained | Datadog Alert | Threat classification is external. |
| COV-153 | OP-016 | Resilience Testing | REQ-Art24-01 | Art. 24(1) | Stakeholder-constrained | Non-production Testing | Programme ownership is unstated. |
| COV-154 | OP-058, CON-011 | Resilience Testing | REQ-Art24-02 | Art. 24(1) | Stakeholder-constrained | Emergency Change | The stated visibility gap is a constrained test-governance signal. |
| COV-155 | OP-016 | Resilience Testing | REQ-Art24-03 | Art. 24(2) | Directly performed | Non-production Testing | Testing is directly performed. |
| COV-156 | OP-016 | Resilience Testing | REQ-Art24-04 | Art. 24(3) | Stakeholder-constrained | Non-production Testing | Risk approach is not evidenced. |
| COV-157 | OP-051 | Resilience Testing | REQ-Art24-05 | Art. 24(4) | Stakeholder-constrained | Collaborative Test | Independence is not evidenced. |
| COV-158 | OP-051 | Resilience Testing | REQ-Art24-06 | Art. 24(4) | Stakeholder-constrained | Collaborative Test | Resource/conflict controls are not evidenced. |
| COV-159 | OP-058, CON-011 | Resilience Testing | REQ-Art24-07 | Art. 24(5) | Stakeholder-constrained | Emergency Change | Visibility gap is a constrained test-governance signal. |
| COV-160 | OP-016 | Resilience Testing | REQ-Art24-08 | Art. 24(6) | Stakeholder-constrained | Non-production Testing | Frequency/criticality scope is not evidenced. |
| COV-161 | OP-016 | Resilience Testing | REQ-Art25-01 | Art. 25(1) | Directly performed | Non-production Testing | Testing is directly performed. |
| COV-162 | OP-019 | Resilience Testing | REQ-Art25-02 | Art. 25(1) | Directly performed | Change Validation | Connectivity validation is directly performed. |
| COV-163 | OP-025 | Resilience Testing | REQ-Art25-03 | Art. 25(1) | Stakeholder-constrained | DB Connection Testing | Test-method selection is constrained by the programme. |

### Operational-context coverage

| Context view | Approved operational relationship | Meaning |
| --- | --- | --- |
| Cross-platform Support | Infra Eng & Cloud DBA → Colleague Assistance | assists colleagues |
| Cross-platform Support | Colleague Assistance → Kafka | supports work involving Kafka |
| Cross-platform Support | Colleague Assistance → Cosmos | supports work involving Cosmos |
| Cross-platform Support | Colleague Assistance → Databricks | supports work involving Databricks |
| Investigation Tooling | Infra Eng & Cloud DBA → Log Investigation | investigates logs and external information |
| Investigation Tooling | Log Investigation → LLM Tools | uses LLMs to parse logs and search information |
| Emergency Change Context | Critical Service Impact → Emergency Change | initiates urgent change handling |
| Emergency Change Context | Infra Eng & Cloud DBA → Emergency Change | implements required critical changes |
| Emergency Change Context | Emergency Change → Change Report | writes the change report after emergency action |
