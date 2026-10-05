# Visual Slide Deck: DORA Back-end Delivery

Legend: `→` approved flow or direct realization; `⇢` approved constraint or support boundary; nested requirement lists represent semantic Composition without an internal arrow. `COV-*` labels identify coverage membership, not element names. Readable Article references are used; canonical legal-text identifiers are intentionally omitted.

---

## Slide 0: DORA Regulation Overview

### Visual Diagram Sketch

```text
┌─────────────────────┐    assigns role     ┌────────────────┐    credit institution   ┌────────────────────┐
│ Back-end Developer  │◄────────────────────│ Employer Bank  │────────────────────────►│ Credit Institution │
└─────────────────────┘                     └────────────────┘                         └─────────┬──────────┘
                                                                                                   │ must apply
                                                                                                   ▼
┌──────────────────────────────────────── Immutable DORA Legal Core ────────────────────────────────────────┐
│ Proportionate DORA Use (2)       ICT Risk Governance (12)       ICT Risk Framework (12)                    │
│ ICT Resilience Strategy (8)      Secure ICT Operations (8)      Detect and Recover (8)                     │
│ ICT Learning and Response (11)   Incident Management (12)       Resilience Testing (12)                    │
│ ICT Third-Party Risk (18)        Critical ICT Oversight (12)    Cyber Threat Sharing (5)                   │
│ DORA Supervision (11)            DORA Legal Lifecycle (3)                                             │
│ Each family nests its approved child requirements. The baseline adds no stakeholder operation, gap, or      │
│ compliance status.                                                                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

- The immutable overview reproduces the approved stakeholder-to-employer-to-credit-institution context and 14 legal families with 134 nested child requirements.
- It is a regulation context slide only. The stakeholder-specific operational graph begins on Slide 1.

### Operational Takeaway

- The developer is not equated with the regulated entity.
- View 0 provides the legal context without making a compliance claim.

---

## Slide 1: ICT Asset Governance

**Coverage:** COV-001–015  
**Projection:** exactly V1 — 22 elements, 35 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
┌─────────────────────┐ performs ┌───────────────────────┐ maintains ┌────────────────────┐
│ Back-end Developer  │─────────►│ Framework Maintenance │──────────►│ Internal Framework │
└──────────┬──────────┘          └───────────┬───────────┘           └────────────────────┘
           ├────────────► Platform Development
           ├────────────► Service Update
           └────────────► Enterprise Data Platform
                         └── approved constraints, direct realization, and ownership boundaries appear in the inventory
```

> **Attached role-context annotation — not a semantic graph element:** CTX-001–025 retain specification/mainframe dependencies, tooling, provisioning, work allocation, decision intake, and approved cross-project/recovery visibility limits. This note is attached to Back-end Developer and adds no relationship or implementation claim.

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| ICT Asset Controls | Appropriate ICT systems • Reliable ICT systems • Processing Capacity • Technological resilience • Function Classification • Role Documentation • ICT Asset Documentation • Classification Review • Identify ICT risk sources • Threat Assessment • Assess major ICT changes • Asset Dependency Mapping • Provider Dependencies • Inventory Maintenance • Legacy System Assessment | COV-001–015 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-001` | Back-end Developer performs Platform Development | Assignment |
| `REL-OP-066` | Back-end Developer performs Service Update | Assignment |
| `REL-OP-090` | Back-end Developer performs Framework Maintenance | Assignment |
| `REL-OP-091` | Framework Maintenance maintains Internal Framework | Association |
| `REL-OP-093` | Back-end Developer develops for Enterprise Data Platform | Association |
| `REL-COV-001` | Framework Maintenance realizes REQ-Art7-01 | Realization — Directly performed |
| `REL-COV-002` | Framework Maintenance realizes REQ-Art7-02 | Realization — Directly performed |
| `REL-COV-003` | REQ-Art7-03 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-004` | REQ-Art7-04 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-005` | REQ-Art8-01 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-006` | REQ-Art8-02 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-007` | REQ-Art8-03 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-008` | REQ-Art8-04 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-009` | REQ-Art8-05 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-010` | REQ-Art8-06 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-011` | REQ-Art8-07 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-012` | REQ-Art8-08 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-013` | REQ-Art8-09 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-014` | REQ-Art8-10 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-015` | REQ-Art8-11 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COMP-S001` | ICT Asset Controls contains the scoped requirement REQ-Art7-01 | Composition — visually nested |
| `REL-COMP-S002` | ICT Asset Controls contains the scoped requirement REQ-Art7-02 | Composition — visually nested |
| `REL-COMP-S003` | ICT Asset Controls contains the scoped requirement REQ-Art7-03 | Composition — visually nested |
| `REL-COMP-S004` | ICT Asset Controls contains the scoped requirement REQ-Art7-04 | Composition — visually nested |
| `REL-COMP-S005` | ICT Asset Controls contains the scoped requirement REQ-Art8-01 | Composition — visually nested |
| `REL-COMP-S006` | ICT Asset Controls contains the scoped requirement REQ-Art8-02 | Composition — visually nested |
| `REL-COMP-S007` | ICT Asset Controls contains the scoped requirement REQ-Art8-03 | Composition — visually nested |
| `REL-COMP-S008` | ICT Asset Controls contains the scoped requirement REQ-Art8-04 | Composition — visually nested |
| `REL-COMP-S009` | ICT Asset Controls contains the scoped requirement REQ-Art8-05 | Composition — visually nested |
| `REL-COMP-S010` | ICT Asset Controls contains the scoped requirement REQ-Art8-06 | Composition — visually nested |
| `REL-COMP-S011` | ICT Asset Controls contains the scoped requirement REQ-Art8-07 | Composition — visually nested |
| `REL-COMP-S012` | ICT Asset Controls contains the scoped requirement REQ-Art8-08 | Composition — visually nested |
| `REL-COMP-S013` | ICT Asset Controls contains the scoped requirement REQ-Art8-09 | Composition — visually nested |
| `REL-COMP-S014` | ICT Asset Controls contains the scoped requirement REQ-Art8-10 | Composition — visually nested |
| `REL-COMP-S015` | ICT Asset Controls contains the scoped requirement REQ-Art8-11 | Composition — visually nested |

### Operational Takeaway

- Framework Maintenance directly realizes the two recorded system requirements. All other coverage entries are explicit workflow constraints or unclear-owner boundaries.
- Stakeholder path: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements..
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Slide 2: Protection and Change

**Coverage:** COV-016–034  
**Projection:** exactly V2 — 28 elements, 44 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
┌─────────────────────┐ develops ┌─────────────────┐ performs ┌───────────────────┐
│ Back-end Developer  │─────────►│ Offload Service │─────────►│ Data Offload Flow │
└───────┬─────────────┘          └─────────────────┘          └───────────────────┘
        ├────────────► Test and DEV Readiness
        ├────────────► Service Update
        └────────────► Enterprise Data Platform
Azure AD Access Control ── restricts ──► Back-end Developer
```

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| Change Controls | Security Policy Record • Network Segmentation • Access Limitation • Strong Auth and Crypto • Change Control • Record changes • Test and assess changes • Change Verification • Patch Update Controls | COV-026–034 |
| Data Protection | ICT Security Monitoring • ICT Security Controls • Resilience Controls • Continuity Controls • Uptime Controls • Data Integrity Protection • Secure data transfer • Access Corruption Control • Uptime Integrity Control • Data Management Risks | COV-016–025 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-002` | Back-end Developer develops Offload Service | Association |
| `REL-OP-010` | Offload Service performs Data Offload Flow | Assignment |
| `REL-OP-014` | Back-end Developer performs Test and DEV Readiness | Assignment |
| `REL-OP-066` | Back-end Developer performs Service Update | Assignment |
| `REL-OP-092` | Azure AD / Internal Service Access restricts Back-end Developer | Association |
| `REL-OP-093` | Back-end Developer develops for Enterprise Data Platform | Association |
| `REL-COV-016` | REQ-Art9-01 legally applies to / constrains Data Offload Flow | Association — Stakeholder-constrained |
| `REL-COV-017` | REQ-Art9-02 legally applies to / constrains Data Offload Flow | Association — Stakeholder-constrained |
| `REL-COV-018` | REQ-Art9-03 legally applies to / constrains Data Offload Flow | Association — Stakeholder-constrained |
| `REL-COV-019` | REQ-Art9-04 legally applies to / constrains Data Offload Flow | Association — Stakeholder-constrained |
| `REL-COV-020` | REQ-Art9-05 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-021` | REQ-Art9-06 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-022` | REQ-Art9-07 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-023` | Azure AD / Internal Service Access supports REQ-Art9-08 | Association — Externally owned |
| `REL-COV-024` | Azure AD / Internal Service Access supports REQ-Art9-09 | Association — Externally owned |
| `REL-COV-025` | Azure AD / Internal Service Access supports REQ-Art9-10 | Association — Externally owned |
| `REL-COV-026` | Test and DEV Readiness realizes REQ-Art9-11 | Realization — Directly performed |
| `REL-COV-027` | Test and DEV Readiness realizes REQ-Art9-12 | Realization — Directly performed |
| `REL-COV-028` | Test and DEV Readiness realizes REQ-Art9-13 | Realization — Directly performed |
| `REL-COV-029` | Test and DEV Readiness realizes REQ-Art9-14 | Realization — Directly performed |
| `REL-COV-030` | Test and DEV Readiness realizes REQ-Art9-15 | Realization — Directly performed |
| `REL-COV-031` | REQ-Art9-16 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-032` | REQ-Art9-17 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-033` | REQ-Art9-18 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-034` | REQ-Art9-19 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COMP-S016` | Data Protection contains the scoped requirement REQ-Art9-01 | Composition — visually nested |
| `REL-COMP-S017` | Data Protection contains the scoped requirement REQ-Art9-02 | Composition — visually nested |
| `REL-COMP-S018` | Data Protection contains the scoped requirement REQ-Art9-03 | Composition — visually nested |
| `REL-COMP-S019` | Data Protection contains the scoped requirement REQ-Art9-04 | Composition — visually nested |
| `REL-COMP-S020` | Data Protection contains the scoped requirement REQ-Art9-05 | Composition — visually nested |
| `REL-COMP-S021` | Data Protection contains the scoped requirement REQ-Art9-06 | Composition — visually nested |
| `REL-COMP-S022` | Data Protection contains the scoped requirement REQ-Art9-07 | Composition — visually nested |
| `REL-COMP-S023` | Data Protection contains the scoped requirement REQ-Art9-08 | Composition — visually nested |
| `REL-COMP-S024` | Data Protection contains the scoped requirement REQ-Art9-09 | Composition — visually nested |
| `REL-COMP-S025` | Data Protection contains the scoped requirement REQ-Art9-10 | Composition — visually nested |
| `REL-COMP-S026` | Change Controls contains the scoped requirement REQ-Art9-11 | Composition — visually nested |
| `REL-COMP-S027` | Change Controls contains the scoped requirement REQ-Art9-12 | Composition — visually nested |
| `REL-COMP-S028` | Change Controls contains the scoped requirement REQ-Art9-13 | Composition — visually nested |
| `REL-COMP-S029` | Change Controls contains the scoped requirement REQ-Art9-14 | Composition — visually nested |
| `REL-COMP-S030` | Change Controls contains the scoped requirement REQ-Art9-15 | Composition — visually nested |
| `REL-COMP-S031` | Change Controls contains the scoped requirement REQ-Art9-16 | Composition — visually nested |
| `REL-COMP-S032` | Change Controls contains the scoped requirement REQ-Art9-17 | Composition — visually nested |
| `REL-COMP-S033` | Change Controls contains the scoped requirement REQ-Art9-18 | Composition — visually nested |
| `REL-COMP-S034` | Change Controls contains the scoped requirement REQ-Art9-19 | Composition — visually nested |

### Operational Takeaway

- Azure AD/Internal Service Access is external support; Test and DEV Readiness is the only direct realization path on this slide.
- Stakeholder path: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements..
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Slide 3: Detection and Continuity

**Coverage:** COV-035–073  
**Projection:** exactly V3 — 58 elements, 93 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
Back-end Developer ── performs ──► Production Monitoring ◄── serves ── Datadog
        │ develops for
        ├──────────────► Enterprise Data Platform
        └──────────────► Platform Development

Datadog Alarm ── triggers ──► Incident Escalation ◄── performed by ── Monitoring Team
                                      ├── triggers ──► Software Remediation ◄── Responsible Dev Team
                                      └── triggers ──► Infra Remediation ◄── Infrastructure Team
Datadog serves both remediation paths; errors and problems trigger their matching remediation.
```

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| Backup and Recovery | Document backup policy • Backup Scope Frequency • Recovery Method Records • Activate backup systems • Backup Data Protection • Backup Restoration Tests • Restoration Protection • Timely Service Recovery • Redundant Capacity • Recovery Time Objective • Recovery Point Objective • Recovered Data Reconcile • Rebuilt Data Check | COV-061–073 |
| Continuity Testing | Assess critical functions • Dependency Assessment • BIA Asset Redundancy • Annual Plan Tests • Critical Change Tests • Crisis Comms Tests • Cyberattack Tests • Plan Assurance Review • Crisis Control Operation • Disruption Event Records | COV-051–060 |
| ICT Detection | Anomaly Detection • Single Failure Points • Test detection mechanisms • Control Alert Thresholds • Incident Responder Alerts • Anomaly Monitoring | COV-035–040 |
| Continuity Response | ICT Continuity Policy • Critical Continuity • Incident Resolution • Containment Plans • Disruption Estimates • Crisis Reporting • Audited Recovery Plans • Maintain continuity plans • Outsourced Function Tests • Business Impact Analysis | COV-041–050 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-001` | Back-end Developer performs Platform Development | Assignment |
| `REL-OP-031` | Back-end Developer performs Production Monitoring | Assignment |
| `REL-OP-032` | Datadog serves Production Monitoring | Serving |
| `REL-OP-079` | Datadog Alarm triggers Incident Escalation | Triggering |
| `REL-OP-080` | Monitoring Team performs Incident Escalation | Assignment |
| `REL-OP-081` | Incident Escalation triggers Software Remediation | Triggering |
| `REL-OP-082` | Incident Escalation triggers Infrastructure Remediation | Triggering |
| `REL-OP-083` | Responsible Development Team performs Software Remediation | Assignment |
| `REL-OP-084` | Infrastructure Team performs Infrastructure Remediation | Assignment |
| `REL-OP-085` | Datadog serves Software Remediation | Serving |
| `REL-OP-086` | Datadog serves Infrastructure Remediation | Serving |
| `REL-OP-087` | Software Error triggers Software Remediation | Triggering |
| `REL-OP-088` | Infrastructure Problem triggers Infrastructure Remediation | Triggering |
| `REL-OP-089` | Software Remediation writes Software Fix | Access |
| `REL-OP-093` | Back-end Developer develops for Enterprise Data Platform | Association |
| `REL-COV-035` | REQ-Art10-01 legally applies to / constrains Production Monitoring | Association — Stakeholder-constrained |
| `REL-COV-036` | REQ-Art10-02 legally applies to / constrains Production Monitoring | Association — Stakeholder-constrained |
| `REL-COV-037` | Incident Escalation supports REQ-Art10-03 | Association — Externally owned |
| `REL-COV-038` | Incident Escalation supports REQ-Art10-04 | Association — Externally owned |
| `REL-COV-039` | Incident Escalation supports REQ-Art10-05 | Association — Externally owned |
| `REL-COV-040` | Incident Escalation supports REQ-Art10-06 | Association — Externally owned |
| `REL-COV-041` | REQ-Art11-01 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-042` | REQ-Art11-02 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-043` | REQ-Art11-03 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-044` | REQ-Art11-04 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-045` | Software Remediation realizes REQ-Art11-05 | Realization — Directly performed |
| `REL-COV-046` | Software Remediation realizes REQ-Art11-06 | Realization — Directly performed |
| `REL-COV-047` | Software Remediation realizes REQ-Art11-07 | Realization — Directly performed |
| `REL-COV-048` | REQ-Art11-08 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-049` | REQ-Art11-09 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-050` | REQ-Art11-10 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-051` | REQ-Art11-11 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-052` | REQ-Art11-12 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-053` | REQ-Art11-13 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-054` | REQ-Art11-14 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-055` | REQ-Art11-15 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-056` | REQ-Art11-16 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-057` | REQ-Art11-17 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-058` | REQ-Art11-18 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-059` | REQ-Art11-19 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-060` | REQ-Art11-20 legally applies to / constrains Incident Escalation | Association — Not evidenced / unclear owner |
| `REL-COV-061` | REQ-Art12-01 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-062` | REQ-Art12-02 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-063` | REQ-Art12-03 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-064` | REQ-Art12-04 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-065` | Infrastructure Remediation supports REQ-Art12-05 | Association — Externally owned |
| `REL-COV-066` | Infrastructure Remediation supports REQ-Art12-06 | Association — Externally owned |
| `REL-COV-067` | Infrastructure Remediation supports REQ-Art12-07 | Association — Externally owned |
| `REL-COV-068` | Infrastructure Remediation supports REQ-Art12-08 | Association — Externally owned |
| `REL-COV-069` | REQ-Art12-09 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-070` | REQ-Art12-10 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-071` | REQ-Art12-11 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-072` | REQ-Art12-12 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-073` | REQ-Art12-13 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COMP-S035` | ICT Detection contains the scoped requirement REQ-Art10-01 | Composition — visually nested |
| `REL-COMP-S036` | ICT Detection contains the scoped requirement REQ-Art10-02 | Composition — visually nested |
| `REL-COMP-S037` | ICT Detection contains the scoped requirement REQ-Art10-03 | Composition — visually nested |
| `REL-COMP-S038` | ICT Detection contains the scoped requirement REQ-Art10-04 | Composition — visually nested |
| `REL-COMP-S039` | ICT Detection contains the scoped requirement REQ-Art10-05 | Composition — visually nested |
| `REL-COMP-S040` | ICT Detection contains the scoped requirement REQ-Art10-06 | Composition — visually nested |
| `REL-COMP-S041` | Continuity Response contains the scoped requirement REQ-Art11-01 | Composition — visually nested |
| `REL-COMP-S042` | Continuity Response contains the scoped requirement REQ-Art11-02 | Composition — visually nested |
| `REL-COMP-S043` | Continuity Response contains the scoped requirement REQ-Art11-03 | Composition — visually nested |
| `REL-COMP-S044` | Continuity Response contains the scoped requirement REQ-Art11-04 | Composition — visually nested |
| `REL-COMP-S045` | Continuity Response contains the scoped requirement REQ-Art11-05 | Composition — visually nested |
| `REL-COMP-S046` | Continuity Response contains the scoped requirement REQ-Art11-06 | Composition — visually nested |
| `REL-COMP-S047` | Continuity Response contains the scoped requirement REQ-Art11-07 | Composition — visually nested |
| `REL-COMP-S048` | Continuity Response contains the scoped requirement REQ-Art11-08 | Composition — visually nested |
| `REL-COMP-S049` | Continuity Response contains the scoped requirement REQ-Art11-09 | Composition — visually nested |
| `REL-COMP-S050` | Continuity Response contains the scoped requirement REQ-Art11-10 | Composition — visually nested |
| `REL-COMP-S051` | Continuity Testing contains the scoped requirement REQ-Art11-11 | Composition — visually nested |
| `REL-COMP-S052` | Continuity Testing contains the scoped requirement REQ-Art11-12 | Composition — visually nested |
| `REL-COMP-S053` | Continuity Testing contains the scoped requirement REQ-Art11-13 | Composition — visually nested |
| `REL-COMP-S054` | Continuity Testing contains the scoped requirement REQ-Art11-14 | Composition — visually nested |
| `REL-COMP-S055` | Continuity Testing contains the scoped requirement REQ-Art11-15 | Composition — visually nested |
| `REL-COMP-S056` | Continuity Testing contains the scoped requirement REQ-Art11-16 | Composition — visually nested |
| `REL-COMP-S057` | Continuity Testing contains the scoped requirement REQ-Art11-17 | Composition — visually nested |
| `REL-COMP-S058` | Continuity Testing contains the scoped requirement REQ-Art11-18 | Composition — visually nested |
| `REL-COMP-S059` | Continuity Testing contains the scoped requirement REQ-Art11-19 | Composition — visually nested |
| `REL-COMP-S060` | Continuity Testing contains the scoped requirement REQ-Art11-20 | Composition — visually nested |
| `REL-COMP-S061` | Backup and Recovery contains the scoped requirement REQ-Art12-01 | Composition — visually nested |
| `REL-COMP-S062` | Backup and Recovery contains the scoped requirement REQ-Art12-02 | Composition — visually nested |
| `REL-COMP-S063` | Backup and Recovery contains the scoped requirement REQ-Art12-03 | Composition — visually nested |
| `REL-COMP-S064` | Backup and Recovery contains the scoped requirement REQ-Art12-04 | Composition — visually nested |
| `REL-COMP-S065` | Backup and Recovery contains the scoped requirement REQ-Art12-05 | Composition — visually nested |
| `REL-COMP-S066` | Backup and Recovery contains the scoped requirement REQ-Art12-06 | Composition — visually nested |
| `REL-COMP-S067` | Backup and Recovery contains the scoped requirement REQ-Art12-07 | Composition — visually nested |
| `REL-COMP-S068` | Backup and Recovery contains the scoped requirement REQ-Art12-08 | Composition — visually nested |
| `REL-COMP-S069` | Backup and Recovery contains the scoped requirement REQ-Art12-09 | Composition — visually nested |
| `REL-COMP-S070` | Backup and Recovery contains the scoped requirement REQ-Art12-10 | Composition — visually nested |
| `REL-COMP-S071` | Backup and Recovery contains the scoped requirement REQ-Art12-11 | Composition — visually nested |
| `REL-COMP-S072` | Backup and Recovery contains the scoped requirement REQ-Art12-12 | Composition — visually nested |
| `REL-COMP-S073` | Backup and Recovery contains the scoped requirement REQ-Art12-13 | Composition — visually nested |

### Operational Takeaway

- Direct realization is limited to Software Remediation. Monitoring, escalation, infrastructure work, continuity, and backup ownership remain exactly as recorded.
- Stakeholder path: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements..
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Slide 4: Incident Learning

**Coverage:** COV-074–101  
**Projection:** exactly V4 — 42 elements, 66 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
Back-end Developer ── performs ──► Production Monitoring ◄── serves ── Datadog
        ├── performs ──► Service Update
        └── develops for ► Enterprise Data Platform

Datadog Alarm ── triggers ──► Incident Escalation ◄── performed by ── Monitoring Team
                                      │ triggers
                                      ▼
                             Software Remediation ◄── performed by ── Responsible Dev Team
                                      │ writes
                                      ▼
                                 Software Fix
```

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| Incident Management | Incident Process • Incident Threat Records • Monitoring Integration • Early Warning Indicators • Incident Classification • Incident Role Assignment • Communication Escalation • Major Incident Reporting • Mitigate incident impacts • Secure Service Recovery | COV-092–101 |
| ICT Learning | Vulnerability Information • Cyber Threat Information • ICT Incident Information • Resilience Impact Review • Major Incident Review • ICT Cause Improvements • Review Communications • Procedure Effectiveness • Security Alert Review • Forensic Quality Review • Escalation Review • Communication Review • ICT Risk Lessons • ICT Risk Component Review • Resilience Strategy Watch • Lessons Reporting • Resilience Training • Technology Monitoring | COV-074–091 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-031` | Back-end Developer performs Production Monitoring | Assignment |
| `REL-OP-032` | Datadog serves Production Monitoring | Serving |
| `REL-OP-066` | Back-end Developer performs Service Update | Assignment |
| `REL-OP-079` | Datadog Alarm triggers Incident Escalation | Triggering |
| `REL-OP-080` | Monitoring Team performs Incident Escalation | Assignment |
| `REL-OP-081` | Incident Escalation triggers Software Remediation | Triggering |
| `REL-OP-083` | Responsible Development Team performs Software Remediation | Assignment |
| `REL-OP-085` | Datadog serves Software Remediation | Serving |
| `REL-OP-089` | Software Remediation writes Software Fix | Access |
| `REL-OP-093` | Back-end Developer develops for Enterprise Data Platform | Association |
| `REL-COV-074` | REQ-Art13-01 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-075` | REQ-Art13-02 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-076` | REQ-Art13-03 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-077` | REQ-Art13-04 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-078` | REQ-Art13-05 legally applies to / constrains Platform Development | Association — Stakeholder-constrained |
| `REL-COV-079` | Incident Escalation supports REQ-Art13-06 | Association — Externally owned |
| `REL-COV-080` | Incident Escalation supports REQ-Art13-07 | Association — Externally owned |
| `REL-COV-081` | Incident Escalation supports REQ-Art13-08 | Association — Externally owned |
| `REL-COV-082` | Incident Escalation supports REQ-Art13-09 | Association — Externally owned |
| `REL-COV-083` | Incident Escalation supports REQ-Art13-10 | Association — Externally owned |
| `REL-COV-084` | REQ-Art13-11 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-085` | REQ-Art13-12 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-086` | REQ-Art13-13 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-087` | REQ-Art13-14 legally applies to / constrains Enterprise Data Platform | Association — Not evidenced / unclear owner |
| `REL-COV-088` | REQ-Art13-15 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-089` | REQ-Art13-16 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-090` | REQ-Art13-17 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-091` | REQ-Art13-18 legally applies to / constrains Service Update | Association — Stakeholder-constrained |
| `REL-COV-092` | REQ-Art17-01 legally applies to / constrains Incident Escalation | Association — Stakeholder-constrained |
| `REL-COV-093` | REQ-Art17-02 legally applies to / constrains Incident Escalation | Association — Stakeholder-constrained |
| `REL-COV-094` | REQ-Art17-03 legally applies to / constrains Incident Escalation | Association — Stakeholder-constrained |
| `REL-COV-095` | Incident Escalation supports REQ-Art17-04 | Association — Externally owned |
| `REL-COV-096` | Incident Escalation supports REQ-Art17-05 | Association — Externally owned |
| `REL-COV-097` | Incident Escalation supports REQ-Art17-06 | Association — Externally owned |
| `REL-COV-098` | Incident Escalation supports REQ-Art17-07 | Association — Externally owned |
| `REL-COV-099` | Software Remediation realizes REQ-Art17-08 | Realization — Directly performed |
| `REL-COV-100` | Software Remediation realizes REQ-Art17-09 | Realization — Directly performed |
| `REL-COV-101` | Software Remediation realizes REQ-Art17-10 | Realization — Directly performed |
| `REL-COMP-S074` | ICT Learning contains the scoped requirement REQ-Art13-01 | Composition — visually nested |
| `REL-COMP-S075` | ICT Learning contains the scoped requirement REQ-Art13-02 | Composition — visually nested |
| `REL-COMP-S076` | ICT Learning contains the scoped requirement REQ-Art13-03 | Composition — visually nested |
| `REL-COMP-S077` | ICT Learning contains the scoped requirement REQ-Art13-04 | Composition — visually nested |
| `REL-COMP-S078` | ICT Learning contains the scoped requirement REQ-Art13-05 | Composition — visually nested |
| `REL-COMP-S079` | ICT Learning contains the scoped requirement REQ-Art13-06 | Composition — visually nested |
| `REL-COMP-S080` | ICT Learning contains the scoped requirement REQ-Art13-07 | Composition — visually nested |
| `REL-COMP-S081` | ICT Learning contains the scoped requirement REQ-Art13-08 | Composition — visually nested |
| `REL-COMP-S082` | ICT Learning contains the scoped requirement REQ-Art13-09 | Composition — visually nested |
| `REL-COMP-S083` | ICT Learning contains the scoped requirement REQ-Art13-10 | Composition — visually nested |
| `REL-COMP-S084` | ICT Learning contains the scoped requirement REQ-Art13-11 | Composition — visually nested |
| `REL-COMP-S085` | ICT Learning contains the scoped requirement REQ-Art13-12 | Composition — visually nested |
| `REL-COMP-S086` | ICT Learning contains the scoped requirement REQ-Art13-13 | Composition — visually nested |
| `REL-COMP-S087` | ICT Learning contains the scoped requirement REQ-Art13-14 | Composition — visually nested |
| `REL-COMP-S088` | ICT Learning contains the scoped requirement REQ-Art13-15 | Composition — visually nested |
| `REL-COMP-S089` | ICT Learning contains the scoped requirement REQ-Art13-16 | Composition — visually nested |
| `REL-COMP-S090` | ICT Learning contains the scoped requirement REQ-Art13-17 | Composition — visually nested |
| `REL-COMP-S091` | ICT Learning contains the scoped requirement REQ-Art13-18 | Composition — visually nested |
| `REL-COMP-S092` | Incident Management contains the scoped requirement REQ-Art17-01 | Composition — visually nested |
| `REL-COMP-S093` | Incident Management contains the scoped requirement REQ-Art17-02 | Composition — visually nested |
| `REL-COMP-S094` | Incident Management contains the scoped requirement REQ-Art17-03 | Composition — visually nested |
| `REL-COMP-S095` | Incident Management contains the scoped requirement REQ-Art17-04 | Composition — visually nested |
| `REL-COMP-S096` | Incident Management contains the scoped requirement REQ-Art17-05 | Composition — visually nested |
| `REL-COMP-S097` | Incident Management contains the scoped requirement REQ-Art17-06 | Composition — visually nested |
| `REL-COMP-S098` | Incident Management contains the scoped requirement REQ-Art17-07 | Composition — visually nested |
| `REL-COMP-S099` | Incident Management contains the scoped requirement REQ-Art17-08 | Composition — visually nested |
| `REL-COMP-S100` | Incident Management contains the scoped requirement REQ-Art17-09 | Composition — visually nested |
| `REL-COMP-S101` | Incident Management contains the scoped requirement REQ-Art17-10 | Composition — visually nested |

### Operational Takeaway

- Direct realization is limited to Software Remediation for reporting, mitigation, and recovery. The monitoring and escalation boundaries remain external or unclear where recorded.
- Stakeholder path: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements..
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Slide 5: Resilience Testing

**Coverage:** COV-102–121  
**Projection:** exactly V5 — 28 elements, 45 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
Back-end Developer ── performs ──► Test and DEV Readiness
        │
        └── performs ──► Pull Request Creation ── writes ──► Pull Request
                                                               ▲
Technical Reviewer ── performs ──► Pull Request Review ── reads ──┘
```

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| Resilience Tests | Resilience Test Programme • Weakness Corrections • Programme Review • Test Method Range • Risk Based Testing • Independent Testing • Test Finding Remediation • Annual Critical Tests | COV-102–109 |
| Test Method Controls | Vulnerability Scans • Open Source Analysis • Network Security Review • Perform gap analyses • Physical Security Review • Scanning Questionnaires • Source Code Review • Scenario Tests • Compatibility Tests • Perform performance tests • Perform end-to-end tests • Perform penetration tests | COV-110–121 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-014` | Back-end Developer performs Test and DEV Readiness | Assignment |
| `REL-OP-016` | Back-end Developer performs Pull Request Creation | Assignment |
| `REL-OP-017` | Pull Request Creation writes Pull Request | Access |
| `REL-OP-018` | Technical Reviewer performs Pull Request Review | Assignment |
| `REL-OP-019` | Pull Request Review reads Pull Request | Access |
| `REL-COV-102` | Test and DEV Readiness realizes REQ-Art24-01 | Realization — Directly performed |
| `REL-COV-103` | Test and DEV Readiness realizes REQ-Art24-02 | Realization — Directly performed |
| `REL-COV-104` | REQ-Art24-03 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-105` | REQ-Art24-04 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-106` | REQ-Art24-05 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-107` | REQ-Art24-06 legally applies to / constrains Pull Request Review | Association — Not evidenced / unclear owner |
| `REL-COV-108` | REQ-Art24-07 legally applies to / constrains Pull Request Review | Association — Not evidenced / unclear owner |
| `REL-COV-109` | REQ-Art24-08 legally applies to / constrains Pull Request Review | Association — Not evidenced / unclear owner |
| `REL-COV-110` | Test and DEV Readiness realizes REQ-Art25-01 | Realization — Directly performed |
| `REL-COV-111` | Test and DEV Readiness realizes REQ-Art25-02 | Realization — Directly performed |
| `REL-COV-112` | REQ-Art25-03 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-113` | REQ-Art25-04 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-114` | REQ-Art25-05 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-115` | REQ-Art25-06 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-116` | REQ-Art25-07 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-117` | REQ-Art25-08 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-118` | REQ-Art25-09 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-119` | REQ-Art25-10 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-120` | REQ-Art25-11 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COV-121` | REQ-Art25-12 legally applies to / constrains Test and DEV Readiness | Association — Stakeholder-constrained |
| `REL-COMP-S102` | Resilience Tests contains the scoped requirement REQ-Art24-01 | Composition — visually nested |
| `REL-COMP-S103` | Resilience Tests contains the scoped requirement REQ-Art24-02 | Composition — visually nested |
| `REL-COMP-S104` | Resilience Tests contains the scoped requirement REQ-Art24-03 | Composition — visually nested |
| `REL-COMP-S105` | Resilience Tests contains the scoped requirement REQ-Art24-04 | Composition — visually nested |
| `REL-COMP-S106` | Resilience Tests contains the scoped requirement REQ-Art24-05 | Composition — visually nested |
| `REL-COMP-S107` | Resilience Tests contains the scoped requirement REQ-Art24-06 | Composition — visually nested |
| `REL-COMP-S108` | Resilience Tests contains the scoped requirement REQ-Art24-07 | Composition — visually nested |
| `REL-COMP-S109` | Resilience Tests contains the scoped requirement REQ-Art24-08 | Composition — visually nested |
| `REL-COMP-S110` | Test Method Controls contains the scoped requirement REQ-Art25-01 | Composition — visually nested |
| `REL-COMP-S111` | Test Method Controls contains the scoped requirement REQ-Art25-02 | Composition — visually nested |
| `REL-COMP-S112` | Test Method Controls contains the scoped requirement REQ-Art25-03 | Composition — visually nested |
| `REL-COMP-S113` | Test Method Controls contains the scoped requirement REQ-Art25-04 | Composition — visually nested |
| `REL-COMP-S114` | Test Method Controls contains the scoped requirement REQ-Art25-05 | Composition — visually nested |
| `REL-COMP-S115` | Test Method Controls contains the scoped requirement REQ-Art25-06 | Composition — visually nested |
| `REL-COMP-S116` | Test Method Controls contains the scoped requirement REQ-Art25-07 | Composition — visually nested |
| `REL-COMP-S117` | Test Method Controls contains the scoped requirement REQ-Art25-08 | Composition — visually nested |
| `REL-COMP-S118` | Test Method Controls contains the scoped requirement REQ-Art25-09 | Composition — visually nested |
| `REL-COMP-S119` | Test Method Controls contains the scoped requirement REQ-Art25-10 | Composition — visually nested |
| `REL-COMP-S120` | Test Method Controls contains the scoped requirement REQ-Art25-11 | Composition — visually nested |
| `REL-COMP-S121` | Test Method Controls contains the scoped requirement REQ-Art25-12 | Composition — visually nested |

### Operational Takeaway

- Test and DEV Readiness realizes the approved direct testing entries. Pull Request Review is not attributed to the Back-end Developer.
- Stakeholder path: Back-end Developer is connected through approved operational relationships to each coverage endpoint and its nested DORA requirements..
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Slide 6: Microsoft Cloud Risk

**Coverage:** COV-122–153  
**Projection:** exactly V6 — 37 elements, 66 relationships, one component, no isolated elements.

### Visual Diagram Sketch

```text
Back-end Developer ◄── assigned role ── Employer Bank ── party to ──► Microsoft Contract
                                                                              │
                                                                              ▼
                                               Provider Risk Controls and Provider Exit Controls
                                               constrain the contract; no developer contract-management behavior
```

### Component Breakdown

| Requirement family | Nested child controls | Coverage membership |
| --- | --- | --- |
| Provider Exit Controls | Secure Provider Selection • Provider Audit Plan • Skilled Auditor Use • Termination Rights • Significant Breach Exit • Risk Change Exit • Provider Weakness Exit • Impaired Supervision Exit • Critical Exit Strategy • Business Continuity Exit • Compliance Exit • Service Continuity Exit • Exit Plan Review • Transition Alternatives • Exit Contingency Measures | COV-139–153 |
| Provider Risk Controls | ICT Provider Risk Control • DORA Compliance Duty • Provider Risk Control • ICT Dependency Assessment • Critical Contract Risk • Provider Risk Policy • Provider Risk Review • Contract Register • Contract Records • Annual Arrangement Report • Authority Register Access • Arrangement Notice • Service Criticality • Supervisory Check • Concentration Risk • Provider Due Diligence • Contract Conflict Check | COV-122–138 |

### Relationship Inventory

Every approved relationship assigned to this slide is listed below. Composition appears as matching nesting rather than an internal diagram arrow.

| Relationship | Textual relationship | Type / ownership |
| --- | --- | --- |
| `REL-OP-094` | Employer Bank is party to Microsoft Contract | Association |
| `REL-ROLE-001` | Employer Bank assigns the stakeholder role Back-end Developer | Assignment |
| `REL-COV-122` | REQ-Art28-01 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-123` | REQ-Art28-02 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-124` | REQ-Art28-03 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-125` | REQ-Art28-04 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-126` | REQ-Art28-05 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-127` | REQ-Art28-06 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-128` | REQ-Art28-07 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-129` | REQ-Art28-08 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-130` | REQ-Art28-09 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-131` | REQ-Art28-10 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-132` | REQ-Art28-11 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-133` | REQ-Art28-12 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-134` | REQ-Art28-13 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-135` | REQ-Art28-14 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-136` | REQ-Art28-15 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-137` | REQ-Art28-16 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-138` | REQ-Art28-17 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-139` | REQ-Art28-18 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-140` | REQ-Art28-19 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-141` | REQ-Art28-20 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-142` | REQ-Art28-21 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-143` | REQ-Art28-22 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-144` | REQ-Art28-23 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-145` | REQ-Art28-24 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-146` | REQ-Art28-25 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-147` | REQ-Art28-26 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-148` | REQ-Art28-27 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-149` | REQ-Art28-28 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-150` | REQ-Art28-29 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-151` | REQ-Art28-30 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-152` | REQ-Art28-31 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COV-153` | REQ-Art28-32 legally applies to / constrains Microsoft Contract | Association — Stakeholder-constrained |
| `REL-COMP-S122` | Provider Risk Controls contains the scoped requirement REQ-Art28-01 | Composition — visually nested |
| `REL-COMP-S123` | Provider Risk Controls contains the scoped requirement REQ-Art28-02 | Composition — visually nested |
| `REL-COMP-S124` | Provider Risk Controls contains the scoped requirement REQ-Art28-03 | Composition — visually nested |
| `REL-COMP-S125` | Provider Risk Controls contains the scoped requirement REQ-Art28-04 | Composition — visually nested |
| `REL-COMP-S126` | Provider Risk Controls contains the scoped requirement REQ-Art28-05 | Composition — visually nested |
| `REL-COMP-S127` | Provider Risk Controls contains the scoped requirement REQ-Art28-06 | Composition — visually nested |
| `REL-COMP-S128` | Provider Risk Controls contains the scoped requirement REQ-Art28-07 | Composition — visually nested |
| `REL-COMP-S129` | Provider Risk Controls contains the scoped requirement REQ-Art28-08 | Composition — visually nested |
| `REL-COMP-S130` | Provider Risk Controls contains the scoped requirement REQ-Art28-09 | Composition — visually nested |
| `REL-COMP-S131` | Provider Risk Controls contains the scoped requirement REQ-Art28-10 | Composition — visually nested |
| `REL-COMP-S132` | Provider Risk Controls contains the scoped requirement REQ-Art28-11 | Composition — visually nested |
| `REL-COMP-S133` | Provider Risk Controls contains the scoped requirement REQ-Art28-12 | Composition — visually nested |
| `REL-COMP-S134` | Provider Risk Controls contains the scoped requirement REQ-Art28-13 | Composition — visually nested |
| `REL-COMP-S135` | Provider Risk Controls contains the scoped requirement REQ-Art28-14 | Composition — visually nested |
| `REL-COMP-S136` | Provider Risk Controls contains the scoped requirement REQ-Art28-15 | Composition — visually nested |
| `REL-COMP-S137` | Provider Risk Controls contains the scoped requirement REQ-Art28-16 | Composition — visually nested |
| `REL-COMP-S138` | Provider Risk Controls contains the scoped requirement REQ-Art28-17 | Composition — visually nested |
| `REL-COMP-S139` | Provider Exit Controls contains the scoped requirement REQ-Art28-18 | Composition — visually nested |
| `REL-COMP-S140` | Provider Exit Controls contains the scoped requirement REQ-Art28-19 | Composition — visually nested |
| `REL-COMP-S141` | Provider Exit Controls contains the scoped requirement REQ-Art28-20 | Composition — visually nested |
| `REL-COMP-S142` | Provider Exit Controls contains the scoped requirement REQ-Art28-21 | Composition — visually nested |
| `REL-COMP-S143` | Provider Exit Controls contains the scoped requirement REQ-Art28-22 | Composition — visually nested |
| `REL-COMP-S144` | Provider Exit Controls contains the scoped requirement REQ-Art28-23 | Composition — visually nested |
| `REL-COMP-S145` | Provider Exit Controls contains the scoped requirement REQ-Art28-24 | Composition — visually nested |
| `REL-COMP-S146` | Provider Exit Controls contains the scoped requirement REQ-Art28-25 | Composition — visually nested |
| `REL-COMP-S147` | Provider Exit Controls contains the scoped requirement REQ-Art28-26 | Composition — visually nested |
| `REL-COMP-S148` | Provider Exit Controls contains the scoped requirement REQ-Art28-27 | Composition — visually nested |
| `REL-COMP-S149` | Provider Exit Controls contains the scoped requirement REQ-Art28-28 | Composition — visually nested |
| `REL-COMP-S150` | Provider Exit Controls contains the scoped requirement REQ-Art28-29 | Composition — visually nested |
| `REL-COMP-S151` | Provider Exit Controls contains the scoped requirement REQ-Art28-30 | Composition — visually nested |
| `REL-COMP-S152` | Provider Exit Controls contains the scoped requirement REQ-Art28-31 | Composition — visually nested |
| `REL-COMP-S153` | Provider Exit Controls contains the scoped requirement REQ-Art28-32 | Composition — visually nested |

### Operational Takeaway

- Every coverage relationship is stakeholder-constrained on the Microsoft Contract. No Article 28 control is presented as developer realization.
- Stakeholder path: Back-end Developer <- Employer Bank -> Microsoft Contract.
- Potential operational or visibility limits are role-bound observations, not enterprise compliance findings.

---

## Deck Validation Record

- Slide 0 reproduces the immutable overview context; it contains no stakeholder-operation or gap claim.
- Slides 1–6 use the exact node and relationship membership of V1–V6 in `7_view_graph.json`.
- Slide 1 carries the operator-approved CTX-001–025 attached annotation. It is not a semantic graph node and does not change V1.
- The six normalized slide projections validate as exact graph projections with one connected component each and no isolated elements.
- The deck covers COV-001–153 and preserves externally owned, stakeholder-constrained, and unclear-owner boundaries without developer realization.
- Slide 0 and Slides 1–6 were individually approved by the operator.
