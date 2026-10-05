# DORA Regulatory Relevance Analysis — AT3

**Stakeholder:** Back-end Developer  
**Employing organisation:** Employer Bank  
**Legal status confirmed by operator:** one organisation, a non-exempt, non-micro DORA financial entity classified as a credit institution.  
**Target regulation:** Regulation (EU) 2022/2554 (DORA), CELEX 32022R2554  
**Status:** Approved Step 5 relevance, traceability, coverage, and legal-role record. It is not a compliance assessment.

## Scope and evidence basis

The AT3 input artefacts are intentionally byte-identical to the BankBackEndDev_2 artefacts, including their historical internal directory reference. They were assessed as AT3 evidence without editing them.

The approved operational chain is: C#/.NET back-end development and data offload work; DEV/PR/QUA/PROD release controls; Azure AD and internal-service access; Azure, Kubernetes, Cosmos DB and the Enterprise Data Platform dependencies; Datadog monitoring; incident escalation and remediation. The operator confirmed that the Enterprise Data Platform supports a critical or important function.

The developer is not equated with the regulated entity. DORA applies to Employer Bank in its capacity as a credit institution; the developer's work is assessed only where it supports or is constrained by that entity-level duty.

## Legal-index provenance and anchor validation

| Field | Recorded value |
| --- | --- |
| Source | Regulation (EU) 2022/2554, CELEX 32022R2554 |
| Matrix selector | DORA |
| Generated index | TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx |
| Regenerated | 2026-09-29 |
| SHA-256 | c7bd1c4fe6920b58caf7e970775b532687f17e4b5d22f6d98bb1f1f9912b555e |
| Index validation | traceability_lookup.py row-id --row 1 resolved Chap.I on Enacting Terms, worksheet row 2 |
| Anchor validation | All 79 unique direct Enacting Terms paths used by the 121 requirements resolved uniquely; 0 failures |
| Role anchor | Chap.I, Art.2, Paragraph 1, Point a resolved as credit institutions |
| Source limits | Only enacting terms are anchors. No recital, amendment, or ordinary citation is used as an anchor. |

## Consensus and screening record

Three independent readings (literal legal duty, systemic architecture, and operational-gap focus) read the DORA text article-by-article and debated disagreements. Their strict unanimous intersection was retained. The operator approved the active set and then explicitly chose not to force-include the split candidates.

| DORA area | Result | Reason for result |
| --- | --- | --- |
| Arts. 1–4 | Context only | Subject matter, scope, definitions, and proportionality inform the assessment but do not create a separate AT3 operational requirement set. |
| Arts. 5–6 | Omitted | Governance and ICT-risk-management framework responsibilities have no recorded stakeholder-framework participation. |
| Arts. 7–13 | Included | Direct connection to maintained systems, data flows, access, controlled releases, monitoring, continuity/recovery evidence, and critical-function impact. |
| Art. 14 | Omitted | No evidence of the developer's crisis-communication responsibility. |
| Arts. 15–16 | Context only | ESA standards and simplified-framework alternative; neither is a stakeholder operational duty selected here. |
| Art. 17 | Included | Datadog detection, Monitoring Team escalation, remediation, and recovery form an operational incident chain. |
| Arts. 18–19 | Omitted | No evidence that AT3 classifies major incidents or owns regulatory reporting. |
| Arts. 20–23 | Omitted/context | Competent-authority/ESA provisions and payment-incident scope lack a recorded AT3 handoff. |
| Arts. 24–25 | Included | Unit testing, pull-request review, environment controls, and the critical-function clarification create a direct resilience-testing relevance. |
| Arts. 26–27 | Omitted | No TLPT programme, test-lead authority, or test scope is evidenced. |
| Art. 28 | Omitted by approved scope decision | Providers are known, but no ICT contractual arrangement, contract register, due-diligence, audit, or termination-right evidence was supplied. The operator declined force-inclusion. |
| Arts. 29–30 | Omitted | Contractual terms and critical/important-function contracting chain are not evidenced. |
| Arts. 31–64 | Omitted/context | Third-party oversight, supervisory powers, enforcement, amendments, and final provisions do not yield a recorded AT3 operational duty. |

**Approved active articles:** 7, 8, 9, 10, 11, 12, 13, 17, 24, and 25.  
**Approved active atomic requirements:** 121.

## Atomic requirement register

Each row is an independently traceable requirement. The row provides: (1) the binding duty, (2) the direct canonical legal-text anchor, and (3) the AT3 operational link and scope boundary. “Constrained” and “support” describe relevance, not proof that the duty is satisfied.

### Article 7 — ICT systems, protocols and tools

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art7-01 | Appropriate ICT systems | Chap.II, Section II, Art.7, Paragraph 1, Point a | Framework maintenance is directly performed; evidence OP-004, OP-038. |
| REQ-Art7-02 | Reliable ICT systems | Chap.II, Section II, Art.7, Paragraph 1, Point b | Framework maintenance is directly performed; evidence OP-004, OP-038. |
| REQ-Art7-03 | Sufficient processing capacity | Chap.II, Section II, Art.7, Paragraph 1, Point c | Platform development is constrained by capacity/resilience needs; evidence OP-001–004, OP-050, OP-060, CON-006. |
| REQ-Art7-04 | Technological resilience | Chap.II, Section II, Art.7, Paragraph 1, Point d | Platform development is constrained by resilience needs; evidence OP-001–004, OP-050, OP-060, CON-006. |

### Article 8 — Identification

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art8-01 | Identify and classify functions | Chap.II, Section II, Art.8, Paragraph 1 | Platform development is constrained; evidence OP-001–003, OP-006, OP-018–019, OP-066, OP-081–082. |
| REQ-Art8-02 | Document roles and responsibilities | Chap.II, Section II, Art.8, Paragraph 1 | Platform development is constrained; same operational evidence as REQ-Art8-01. |
| REQ-Art8-03 | Document information and ICT assets | Chap.II, Section II, Art.8, Paragraph 1 | Platform development is constrained; same operational evidence as REQ-Art8-01. |
| REQ-Art8-04 | Review classification and documentation | Chap.II, Section II, Art.8, Paragraph 1 | Service updates are constrained; evidence OP-038, OP-041–042, OP-052, CON-001. |
| REQ-Art8-05 | Identify ICT-risk sources | Chap.II, Section II, Art.8, Paragraph 2 | Service updates are constrained; evidence OP-038, OP-041–042, OP-052, CON-001. |
| REQ-Art8-06 | Assess threats and risk scenarios | Chap.II, Section II, Art.8, Paragraph 2 | Service updates are constrained; evidence OP-038, OP-041–042, OP-052, CON-001. |
| REQ-Art8-07 | Assess major ICT changes | Chap.II, Section II, Art.8, Paragraph 3 | Enterprise Data Platform activity is relevant; owner and formal risk assessment are not evidenced; OP-023–029, OP-068. |
| REQ-Art8-08 | Map assets and interdependencies | Chap.II, Section II, Art.8, Paragraph 4 | Enterprise Data Platform dependencies are relevant; ownership is unclear; OP-023–029, OP-068. |
| REQ-Art8-09 | Document third-party dependencies | Chap.II, Section II, Art.8, Paragraph 5 | Enterprise Data Platform dependencies are relevant; documentation ownership is unclear; OP-023–029, OP-068. |
| REQ-Art8-10 | Maintain and update inventories | Chap.II, Section II, Art.8, Paragraph 6 | Enterprise Data Platform inventory relevance is established; maintenance owner is not evidenced; OP-023–029, OP-068. |
| REQ-Art8-11 | Assess legacy and connected systems | Chap.II, Section II, Art.8, Paragraph 7 | Connected-platform relevance is established; entity assessment ownership is not evidenced; OP-023–029, OP-068. |

### Article 9 — Protection and prevention

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art9-01 | Monitor ICT security and functioning | Chap.II, Section II, Art.9, Paragraph 1 | Data offload flow is constrained; OP-006, OP-048, OP-065, OP-081. |
| REQ-Art9-02 | Deploy ICT security controls | Chap.II, Section II, Art.9, Paragraph 1 | Data offload flow is constrained; OP-006, OP-048, OP-065, OP-081. |
| REQ-Art9-03 | Design resilience controls | Chap.II, Section II, Art.9, Paragraph 2 | Data offload flow is constrained; OP-006, OP-048, OP-065, OP-081. |
| REQ-Art9-04 | Design continuity controls | Chap.II, Section II, Art.9, Paragraph 2 | Data offload flow is constrained; OP-006, OP-048, OP-065, OP-081. |
| REQ-Art9-05 | Design availability controls | Chap.II, Section II, Art.9, Paragraph 2 | Enterprise Data Platform is relevant; control ownership is unclear; OP-031–036, OP-088. |
| REQ-Art9-06 | Protect data confidentiality and integrity | Chap.II, Section II, Art.9, Paragraph 2 | Enterprise Data Platform is relevant; control ownership is unclear; OP-031–036, OP-088. |
| REQ-Art9-07 | Secure data transfer | Chap.II, Section II, Art.9, Paragraph 3, Point a | Enterprise Data Platform is relevant; formal transfer-control ownership is unclear; OP-031–036, OP-088. |
| REQ-Art9-08 | Prevent corruption and unauthorised access | Chap.II, Section II, Art.9, Paragraph 3, Point b | Azure AD/internal access supports the duty; externally owned; OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002. |
| REQ-Art9-09 | Prevent availability and integrity loss | Chap.II, Section II, Art.9, Paragraph 3, Point c | Azure AD/internal access supports the duty; externally owned; same evidence as REQ-Art9-08. |
| REQ-Art9-10 | Protect data from management risks | Chap.II, Section II, Art.9, Paragraph 3, Point d | Azure AD/internal access supports the duty; externally owned; same evidence as REQ-Art9-08. |
| REQ-Art9-11 | Document information-security policy | Chap.II, Section II, Art.9, Paragraph 4, Point a | DEV/test readiness is constrained; no policy authorship is claimed; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008. |
| REQ-Art9-12 | Manage and segment networks | Chap.II, Section II, Art.9, Paragraph 4, Point b; Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1 | DEV/test readiness is constrained; no network-control realization is claimed; same evidence as REQ-Art9-11. |
| REQ-Art9-13 | Limit logical and physical access | Chap.II, Section II, Art.9, Paragraph 4, Point c | DEV/test readiness is constrained; no access-control ownership is claimed; same evidence as REQ-Art9-11. |
| REQ-Art9-14 | Use strong authentication and cryptography | Chap.II, Section II, Art.9, Paragraph 4, Point d | DEV/test readiness is constrained; implementation scope is not evidenced; same evidence as REQ-Art9-11. |
| REQ-Art9-15 | Maintain controlled change management | Chap.II, Section II, Art.9, Paragraph 4, Point e | DEV/test readiness is constrained; PR and environment evidence supports relevance, not a full control claim; same evidence as REQ-Art9-11. |
| REQ-Art9-16 | Record changes | Chap.II, Section II, Art.9, Paragraph 4, Point e | Service updates are constrained; OP-038, OP-041–042. |
| REQ-Art9-17 | Test and assess changes | Chap.II, Section II, Art.9, Paragraph 4, Point e | Service updates are constrained; OP-038, OP-041–042. |
| REQ-Art9-18 | Approve, implement and verify changes | Chap.II, Section II, Art.9, Paragraph 4, Point e | Service updates are constrained; OP-038, OP-041–042. |
| REQ-Art9-19 | Document patch and update controls | Chap.II, Section II, Art.9, Paragraph 4, Point f; Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2 | Service updates are constrained; OP-038, OP-041–042. |

### Article 10 — Detection

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art10-01 | Detect anomalies and performance issues | Chap.II, Section II, Art.10, Paragraph 1 | Production monitoring is constrained; OP-014, OP-070, OP-072. |
| REQ-Art10-02 | Identify material single points of failure | Chap.II, Section II, Art.10, Paragraph 1 | Production monitoring is constrained; OP-014, OP-070, OP-072. |
| REQ-Art10-03 | Test detection mechanisms | Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1 | Incident escalation supports the duty; monitoring-team ownership is external; OP-070, OP-072, OP-076. |
| REQ-Art10-04 | Use control layers and alert thresholds | Chap.II, Section II, Art.10, Paragraph 2 | Incident escalation supports the duty; monitoring-team ownership is external; OP-070, OP-072, OP-076. |
| REQ-Art10-05 | Trigger and notify incident responders | Chap.II, Section II, Art.10, Paragraph 2 | Incident escalation supports the duty; monitoring-team ownership is external; OP-070, OP-072, OP-076. |
| REQ-Art10-06 | Resource continuous anomaly monitoring | Chap.II, Section II, Art.10, Paragraph 3 | Incident escalation supports the duty; resourcing ownership is external; OP-070, OP-072, OP-076. |

### Article 11 — Response and recovery

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art11-01 | Maintain ICT business-continuity policy | Chap.II, Section II, Art.11, Paragraph 1 | Critical Enterprise Data Platform makes the duty relevant; policy evidence/owner not captured; OP-060, OP-070–080. |
| REQ-Art11-02 | Ensure critical-function continuity | Chap.II, Section II, Art.11, Paragraph 2, Point a | Critical-function relevance confirmed; continuity implementation/owner not captured; OP-060, OP-070–080. |
| REQ-Art11-03 | Respond to and resolve incidents | Chap.II, Section II, Art.11, Paragraph 2, Point b | Software remediation directly realizes the observed response/resolution part; OP-071, OP-073–078. |
| REQ-Art11-04 | Activate containment and recovery plans | Chap.II, Section II, Art.11, Paragraph 2, Point c | Incident escalation is constrained; plan activation owner and evidence are unclear; OP-060, OP-070–080. |
| REQ-Art11-05 | Estimate disruption impacts and losses | Chap.II, Section II, Art.11, Paragraph 2, Point d | Incident escalation is constrained; assessment ownership/evidence are unclear; OP-060, OP-070–080. |
| REQ-Art11-06 | Provide crisis communications and reporting | Chap.II, Section II, Art.11, Paragraph 2, Point e | Incident escalation is constrained; crisis communication ownership/evidence are unclear; OP-060, OP-070–080. |
| REQ-Art11-07 | Maintain audited response and recovery plans | Chap.II, Section II, Art.11, Paragraph 3 | Incident escalation is constrained; audit/plan owner is unclear; OP-060, OP-070–080. |
| REQ-Art11-08 | Maintain continuity plans | Chap.II, Section II, Art.11, Paragraph 4 | Incident escalation is constrained; continuity plan evidence/owner are unclear; OP-060, OP-070–080. |
| REQ-Art11-09 | Test plans for outsourced critical functions | Chap.II, Section II, Art.11, Paragraph 4 | Incident escalation is constrained; such plan-test evidence/owner are unclear; OP-060, OP-070–080. |
| REQ-Art11-10 | Conduct a business-impact analysis | Chap.II, Section II, Art.11, Paragraph 5 | Incident escalation is constrained; BIA evidence/owner are unclear; OP-060, OP-070–080. |
| REQ-Art11-11 | Assess critical functions | Chap.II, Section II, Art.11, Paragraph 5 | Criticality is operator-confirmed; formal assessment record/owner not captured; OP-062–063, OP-070–080. |
| REQ-Art11-12 | Assess dependencies and information assets | Chap.II, Section II, Art.11, Paragraph 5 | Platform dependency relevance is clear; formal assessment owner not captured; OP-062–063, OP-070–080. |
| REQ-Art11-13 | Align ICT assets and redundancy to BIA | Chap.II, Section II, Art.11, Paragraph 5 | Platform relevance is clear; BIA/redundancy evidence and owner not captured; OP-062–063, OP-070–080. |
| REQ-Art11-14 | Test plans at least annually | Chap.II, Section II, Art.11, Paragraph 6, Point a | Platform development is constrained; annual plan-test evidence/owner not captured; OP-060, OP-068. |
| REQ-Art11-15 | Test after substantive critical-system change | Chap.II, Section II, Art.11, Paragraph 6, Point a | Platform development is constrained; formal test-plan evidence/owner not captured; OP-060, OP-068. |
| REQ-Art11-16 | Test crisis communications | Chap.II, Section II, Art.11, Paragraph 6, Point b | Platform development is constrained; crisis-communication test evidence/owner not captured; OP-060, OP-068. |
| REQ-Art11-17 | Test cyberattack and switchover scenarios | Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1 | Incident escalation is constrained; scenario-test evidence/owner not captured; OP-070–080. |
| REQ-Art11-18 | Review plans from testing and assurance | Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2 | Incident escalation is constrained; review evidence/owner not captured; OP-070–080. |
| REQ-Art11-19 | Operate a crisis-management function | Chap.II, Section II, Art.11, Paragraph 7 | Incident escalation is constrained; crisis-function ownership not captured; OP-070–080. |
| REQ-Art11-20 | Keep disruption-event records | Chap.II, Section II, Art.11, Paragraph 8 | Incident escalation is constrained; record ownership/evidence not captured; OP-070–080. |

### Article 12 — Backup policies and restoration procedures

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art12-01 | Document backup policy | Chap.II, Section II, Art.12, Paragraph 1, Point a | Critical platform recovery is relevant; backup policy evidence/owner not captured; OP-062–063, OP-073, OP-078, OP-080. |
| REQ-Art12-02 | Set backup scope and frequency | Chap.II, Section II, Art.12, Paragraph 1, Point a | Critical platform recovery is relevant; scope/frequency evidence/owner not captured; same evidence as REQ-Art12-01. |
| REQ-Art12-03 | Document restoration and recovery methods | Chap.II, Section II, Art.12, Paragraph 1, Point b | Critical platform recovery is relevant; method evidence/owner not captured; same evidence as REQ-Art12-01. |
| REQ-Art12-04 | Activate backup systems | Chap.II, Section II, Art.12, Paragraph 2 | Critical platform recovery is relevant; activation ownership/evidence not captured; same evidence as REQ-Art12-01. |
| REQ-Art12-05 | Protect security and data qualities during backup | Chap.II, Section II, Art.12, Paragraph 2 | Infrastructure remediation supports the duty; infrastructure ownership is external; OP-027–029, OP-063, OP-074–075, OP-078. |
| REQ-Art12-06 | Periodically test backup and restoration | Chap.II, Section II, Art.12, Paragraph 2 | Infrastructure remediation supports the duty; test ownership is external; same evidence as REQ-Art12-05. |
| REQ-Art12-07 | Segregate and protect restoration systems | Chap.II, Section II, Art.12, Paragraph 3 | Infrastructure remediation supports the duty; infrastructure ownership is external; same evidence as REQ-Art12-05. |
| REQ-Art12-08 | Restore services in a timely way | Chap.II, Section II, Art.12, Paragraph 3 | Infrastructure remediation supports the duty; infrastructure ownership is external; same evidence as REQ-Art12-05. |
| REQ-Art12-09 | Maintain adequate redundant capacity | Chap.II, Section II, Art.12, Paragraph 4 | Platform development is constrained; redundancy owner/evidence not captured; OP-048, OP-065, OP-078, OP-080. |
| REQ-Art12-10 | Set recovery-time objectives | Chap.II, Section II, Art.12, Paragraph 6 | Platform development is constrained; RTO evidence/owner not captured; OP-048, OP-065, OP-078, OP-080. |
| REQ-Art12-11 | Set recovery-point objectives | Chap.II, Section II, Art.12, Paragraph 6 | Platform development is constrained; RPO evidence/owner not captured; OP-048, OP-065, OP-078, OP-080. |
| REQ-Art12-12 | Check and reconcile recovered data | Chap.II, Section II, Art.12, Paragraph 7 | Platform development is constrained; recovery-check evidence/owner not captured; OP-048, OP-065, OP-078, OP-080. |
| REQ-Art12-13 | Check externally reconstructed data | Chap.II, Section II, Art.12, Paragraph 7 | Platform development is constrained; reconstruction-check evidence/owner not captured; OP-048, OP-065, OP-078, OP-080. |

### Article 13 — Learning and evolving

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art13-01 | Gather vulnerability information | Chap.II, Section II, Art.13, Paragraph 1 | Platform development is constrained; OP-014, OP-038, OP-042, OP-048. |
| REQ-Art13-02 | Gather cyber-threat information | Chap.II, Section II, Art.13, Paragraph 1 | Platform development is constrained; OP-014, OP-038, OP-042, OP-048. |
| REQ-Art13-03 | Gather ICT-incident information | Chap.II, Section II, Art.13, Paragraph 1 | Platform development is constrained; OP-014, OP-038, OP-042, OP-048. |
| REQ-Art13-04 | Analyse resilience impacts | Chap.II, Section II, Art.13, Paragraph 1 | Platform development is constrained; OP-014, OP-038, OP-042, OP-048. |
| REQ-Art13-05 | Review disruptive major incidents | Chap.II, Section II, Art.13, Paragraph 2 | Platform development is constrained; formal review ownership/evidence not captured; OP-014, OP-038, OP-042, OP-048. |
| REQ-Art13-06 | Identify causes and ICT improvements | Chap.II, Section II, Art.13, Paragraph 2 | Incident escalation supports the duty; external process ownership; OP-070–076. |
| REQ-Art13-07 | Communicate review changes when requested | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1 | Incident escalation supports the duty; external process ownership; OP-070–076. |
| REQ-Art13-08 | Evaluate procedure and action effectiveness | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2 | Incident escalation supports the duty; external process ownership; OP-070–076. |
| REQ-Art13-09 | Review response to security alerts | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a | Incident escalation supports the duty; external process ownership; OP-070–076. |
| REQ-Art13-10 | Review forensic-analysis quality | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b | Incident escalation supports the duty; external process ownership; OP-070–076. |
| REQ-Art13-11 | Review incident escalation | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c | Enterprise Data Platform is relevant; formal review ownership/evidence unclear; OP-061–063, OP-070–080. |
| REQ-Art13-12 | Review internal and external communications | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d | Enterprise Data Platform is relevant; formal review ownership/evidence unclear; OP-061–063, OP-070–080. |
| REQ-Art13-13 | Incorporate lessons in ICT-risk assessment | Chap.II, Section II, Art.13, Paragraph 3 | Enterprise Data Platform is relevant; formal risk-assessment owner/evidence unclear; OP-061–063, OP-070–080. |
| REQ-Art13-14 | Review ICT-risk-management components | Chap.II, Section II, Art.13, Paragraph 3 | Enterprise Data Platform is relevant; framework review owner/evidence unclear; OP-061–063, OP-070–080. |
| REQ-Art13-15 | Monitor resilience strategy and ICT-risk evolution | Chap.II, Section II, Art.13, Paragraph 4 | Service updates are constrained; OP-038, OP-067, OP-087. |
| REQ-Art13-16 | Report lessons and recommendations to management | Chap.II, Section II, Art.13, Paragraph 5 | Service updates are constrained; management-report ownership not claimed; OP-038, OP-067, OP-087. |
| REQ-Art13-17 | Provide mandatory awareness and resilience training | Chap.II, Section II, Art.13, Paragraph 6 | Service updates are constrained; training provision evidence/owner not captured; OP-038, OP-067, OP-087. |
| REQ-Art13-18 | Monitor relevant technology developments | Chap.II, Section II, Art.13, Paragraph 7 | Service updates are constrained; OP-038, OP-067, OP-087. |

### Article 17 — ICT-related incident management process

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art17-01 | Establish an incident-management process | Chap.III, Art.17, Paragraph 1 | Incident escalation is constrained; OP-070–073. |
| REQ-Art17-02 | Record incidents and significant cyber threats | Chap.III, Art.17, Paragraph 2 | Incident escalation is constrained; OP-070–073. |
| REQ-Art17-03 | Integrate monitoring, handling, follow-up and root-cause treatment | Chap.III, Art.17, Paragraph 2 | Incident escalation is constrained; OP-070–073. |
| REQ-Art17-04 | Use early-warning indicators | Chap.III, Art.17, Paragraph 3, Point a | Incident escalation supports the duty; external monitoring-process ownership; OP-070–072. |
| REQ-Art17-05 | Identify, log, categorise and classify incidents | Chap.III, Art.17, Paragraph 3, Point b | Incident escalation supports the duty; external monitoring-process ownership; OP-070–072. |
| REQ-Art17-06 | Assign incident roles and responsibilities | Chap.III, Art.17, Paragraph 3, Point c | Incident escalation supports the duty; external monitoring-process ownership; OP-070–072. |
| REQ-Art17-07 | Plan communications and escalation | Chap.III, Art.17, Paragraph 3, Point d | Incident escalation supports the duty; external monitoring-process ownership; OP-070–072. |
| REQ-Art17-08 | Report major incidents to management | Chap.III, Art.17, Paragraph 3, Point e | Incident escalation is constrained; management-report ownership/evidence unclear; OP-070–078. |
| REQ-Art17-09 | Mitigate incident impacts | Chap.III, Art.17, Paragraph 3, Point f | Software remediation directly realizes the observed mitigation part; OP-073–078. |
| REQ-Art17-10 | Restore secure services promptly | Chap.III, Art.17, Paragraph 3, Point f | Software remediation directly realizes the observed restoration part; OP-073–078. |

### Article 24 — General requirements for testing

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art24-01 | Establish a resilience-testing programme | Chap.IV, Art.24, Paragraph 1 | Test/DEV readiness is constrained; programme ownership/evidence not captured; OP-008, OP-048, OP-050. |
| REQ-Art24-02 | Identify weaknesses and implement corrections | Chap.IV, Art.24, Paragraph 1 | Test/DEV readiness directly realizes the observed identification/correction part; OP-008, OP-048, OP-050. |
| REQ-Art24-03 | Maintain and review the programme | Chap.IV, Art.24, Paragraph 1 | Test/DEV readiness is constrained; programme governance not evidenced; OP-008, OP-048, OP-059–060. |
| REQ-Art24-04 | Use a range of tests and methods | Chap.IV, Art.24, Paragraph 2 | Test/DEV readiness is constrained; full testing scope not evidenced; OP-008, OP-048, OP-059–060. |
| REQ-Art24-05 | Apply a risk-based testing approach | Chap.IV, Art.24, Paragraph 3 | Test/DEV readiness is constrained; risk-based programme evidence absent; OP-008, OP-048, OP-059–060. |
| REQ-Art24-06 | Use independent testers and avoid conflicts | Chap.IV, Art.24, Paragraph 4 | Pull-request review is constrained; tester independence/owner not evidenced; OP-009, OP-047, OP-064. |
| REQ-Art24-07 | Prioritise and remedy test findings | Chap.IV, Art.24, Paragraph 5 | Test/DEV readiness is constrained; formal prioritisation evidence/owner not captured; OP-008, OP-048, OP-050. |
| REQ-Art24-08 | Test critical-function ICT annually | Chap.IV, Art.24, Paragraph 6 | Platform development is constrained by confirmed critical-function status; annual test evidence/owner not captured; OP-008, OP-048, OP-050. |

### Article 25 — Testing of ICT tools and systems

| Requirement | Binding duty | Direct legal-text ID | AT3 operational link and boundary |
| --- | --- | --- | --- |
| REQ-Art25-01 | Perform vulnerability assessments and scans | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-02 | Perform open-source analyses | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-03 | Perform network-security assessments | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-04 | Perform gap analyses | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-05 | Perform physical-security reviews | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-06 | Use questionnaires and scanning tools | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-07 | Perform feasible source-code reviews | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; PR evidence exists but this formal test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-08 | Perform scenario-based tests | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-09 | Perform compatibility tests | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-10 | Perform performance tests | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-11 | Perform end-to-end tests | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |
| REQ-Art25-12 | Perform penetration tests | Chap.IV, Art.25, Paragraph 1 | Test/DEV readiness is relevant; this test type is not evidenced; OP-008, OP-048, OP-050. |

## Footprint-to-requirement coverage ledger

The following is a bidirectional, evidence-backed ledger. Every COV and REL-COV range expands in the stated sequence, one ordinal per listed requirement: for example, COV-005 and REL-COV-005 map only to REQ-Art8-01. “Unclear” is an evidence/visibility state, not a compliance finding.

| COV / REL-COV IDs | Requirement IDs in ordinal order | Operational unit and evidence | Ownership state | Directed relationship and ArchiMate candidate |
| --- | --- | --- | --- | --- |
| 001–002 | REQ-Art7-01–02 | Framework Maintenance; OP-004, OP-038 | Directly performed | Framework Maintenance realizes part of each requirement; Realization. |
| 003–004 | REQ-Art7-03–04 | Platform Development; OP-001–004, OP-050, OP-060, CON-006 | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 005–007 | REQ-Art8-01–03 | Platform Development; OP-001–003, OP-006, OP-018–019, OP-066, OP-081–082 | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 008–010 | REQ-Art8-04–06 | Service Update; OP-038, OP-041–042, OP-052, CON-001 | Stakeholder-constrained | Requirement legally applies to / constrains Service Update; Association. |
| 011–015 | REQ-Art8-07–11 | Enterprise Data Platform; OP-023–029, OP-068 | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 016–019 | REQ-Art9-01–04 | Data Offload Flow; OP-006, OP-048, OP-065, OP-081 | Stakeholder-constrained | Requirement legally applies to / constrains Data Offload Flow; Association. |
| 020–022 | REQ-Art9-05–07 | Enterprise Data Platform; OP-031–036, OP-088 | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 023–025 | REQ-Art9-08–10 | Azure AD / Internal Service Access; OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | Externally owned | Azure AD / Internal Service Access supports each requirement; Association. |
| 026–030 | REQ-Art9-11–15 | Test and DEV Readiness; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | Stakeholder-constrained | Requirement legally applies to / constrains Test and DEV Readiness; Association. |
| 031–034 | REQ-Art9-16–19 | Service Update; OP-038, OP-041–042 | Stakeholder-constrained | Requirement legally applies to / constrains Service Update; Association. |
| 035–036 | REQ-Art10-01–02 | Production Monitoring; OP-014, OP-070, OP-072 | Stakeholder-constrained | Requirement legally applies to / constrains Production Monitoring; Association. |
| 037–040 | REQ-Art10-03–06 | Incident Escalation; OP-070, OP-072, OP-076 | Externally owned | Incident Escalation supports each requirement; Association. |
| 041–042 | REQ-Art11-01–02 | Enterprise Data Platform; OP-060, OP-070–080; critical-function confirmation | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 043 | REQ-Art11-03 | Software Remediation; OP-071, OP-073–078 | Directly performed | Software Remediation realizes part of the requirement; Realization. |
| 044–050 | REQ-Art11-04–10 | Incident Escalation; OP-060, OP-070–080 | Not evidenced / unclear owner | Requirement legally applies to / constrains Incident Escalation; Association. |
| 051–053 | REQ-Art11-11–13 | Enterprise Data Platform; OP-062–063, OP-070–080 | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 054–056 | REQ-Art11-14–16 | Platform Development; OP-060, OP-068; critical-function confirmation | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 057–060 | REQ-Art11-17–20 | Incident Escalation; OP-070–080 | Not evidenced / unclear owner | Requirement legally applies to / constrains Incident Escalation; Association. |
| 061–064 | REQ-Art12-01–04 | Enterprise Data Platform; OP-062–063, OP-073, OP-078, OP-080 | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 065–068 | REQ-Art12-05–08 | Infrastructure Remediation; OP-027–029, OP-063, OP-074–075, OP-078 | Externally owned | Infrastructure Remediation supports each requirement; Association. |
| 069–073 | REQ-Art12-09–13 | Platform Development; OP-048, OP-065, OP-078, OP-080 | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 074–078 | REQ-Art13-01–05 | Platform Development; OP-014, OP-038, OP-042, OP-048 | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 079–083 | REQ-Art13-06–10 | Incident Escalation; OP-070–076 | Externally owned | Incident Escalation supports each requirement; Association. |
| 084–087 | REQ-Art13-11–14 | Enterprise Data Platform; OP-061–063, OP-070–080 | Not evidenced / unclear owner | Requirement legally applies to / constrains Enterprise Data Platform; Association. |
| 088–091 | REQ-Art13-15–18 | Service Update; OP-038, OP-067, OP-087 | Stakeholder-constrained | Requirement legally applies to / constrains Service Update; Association. |
| 092–094 | REQ-Art17-01–03 | Incident Escalation; OP-070–073 | Stakeholder-constrained | Requirement legally applies to / constrains Incident Escalation; Association. |
| 095–098 | REQ-Art17-04–07 | Incident Escalation; OP-070–072 | Externally owned | Incident Escalation supports each requirement; Association. |
| 099 | REQ-Art17-08 | Incident Escalation; OP-070–078 | Not evidenced / unclear owner | Requirement legally applies to / constrains Incident Escalation; Association. |
| 100–101 | REQ-Art17-09–10 | Software Remediation; OP-073–078 | Directly performed | Software Remediation realizes part of each requirement; Realization. |
| 102 | REQ-Art24-01 | Test and DEV Readiness; OP-008, OP-048, OP-050 | Stakeholder-constrained | Requirement legally applies to / constrains Test and DEV Readiness; Association. |
| 103 | REQ-Art24-02 | Test and DEV Readiness; OP-008, OP-048, OP-050 | Directly performed | Test and DEV Readiness realizes part of the requirement; Realization. |
| 104–106 | REQ-Art24-03–05 | Test and DEV Readiness; OP-008, OP-048, OP-059–060 | Stakeholder-constrained | Requirement legally applies to / constrains Test and DEV Readiness; Association. |
| 107 | REQ-Art24-06 | Pull Request Review; OP-009, OP-047, OP-064 | Not evidenced / unclear owner | Requirement legally applies to / constrains Pull Request Review; Association. |
| 108 | REQ-Art24-07 | Test and DEV Readiness; OP-008, OP-048, OP-050 | Not evidenced / unclear owner | Requirement legally applies to / constrains Test and DEV Readiness; Association. |
| 109 | REQ-Art24-08 | Platform Development; OP-008, OP-048, OP-050; critical-function confirmation | Stakeholder-constrained | Requirement legally applies to / constrains Platform Development; Association. |
| 110–121 | REQ-Art25-01–12 | Test and DEV Readiness; OP-008, OP-048, OP-050 | Not evidenced / unclear owner | Requirement legally applies to / constrains Test and DEV Readiness; Association. |

### Operational-context coverage

The atomic requirement ledger is supplemented by the following footprint evidence, so it is retained without inventing a legal relationship:

- Specifications and mainframe context: OP-005, OP-007.
- Development tool context: OP-015–016, OP-086–087.
- Licence and VPN provisioning: OP-020–022.
- Work allocation, planning, decision-making, and requirement intake: OP-039–046, OP-051, OP-069.
- Cross-project visibility constraint: OP-061 and CON-007.
- Recovery evidence limit: OP-062–063.
- C#/.NET work: OP-067.
- Wider-team scope limitation: OP-089.

**Uncovered register:** empty. Each explicit AT3 operational item is either in the atomic coverage ledger or retained in the operational-context coverage above.

## Evidence gaps and boundaries

The following are material evidence/visibility gaps denoted [Gap]. They are not findings that Employer Bank is non-compliant:

- [Gap] Entity asset inventories, classification records, and formal ICT-risk-assessment framework evidence for Article 8 are not visible to this stakeholder.
- [Gap] Business-continuity policy, BIA, recovery-plan, backup, restoration, RTO/RPO, and redundancy evidence for Articles 11–12 are not visible to this stakeholder.
- [Gap] Formal post-incident review, lessons-learned governance, management reporting, and awareness-training evidence for Article 13 are not visible to this stakeholder.
- [Gap] A formal resilience-testing programme, risk-based approach, tester independence, and annual critical-function testing evidence for Article 24 are not visible to this stakeholder.
- [Gap] The Article 25 test types — vulnerability assessment, open-source analysis, network-security assessment, gap analysis, physical-security review, questionnaire/scanning, source-code review, scenario, compatibility, performance, end-to-end, and penetration testing — are not evidenced in AT3.
- [Gap] ICT contractual-arrangement, register, due-diligence, audit, and termination-right evidence is absent; consequently the approved scope omits Article 28 and its contract-dependent chain.

## Legal-role placement ledger

Employer Bank is a single organisation. “Credit Institution” below is a DORA legal classification, not a second bank or organisation.

| Relationship ID | Source | Relationship | Target | ArchiMate candidate | Evidence and boundary |
| --- | --- | --- | --- | --- | --- |
| REL-ROLE-001 | Employer Bank — Business Actor | assigns | Back-end Developer — Business Role | Assignment — Business Actor to Business Role | AT3 describes a Back-end Developer at a very large Portuguese bank; employer linkage confirmed by operator. |
| REL-ROLE-002 | Employer Bank — Business Actor | is classified as | Credit Institution — Business Actor | Specialization — Business Actor to Business Actor | Operator confirmed the employer is a credit institution; direct DORA anchor Chap.I, Art.2, Paragraph 1, Point a. |

## Validation gates and approvals

| Gate | Result |
| --- | --- |
| 5.1 — consensus set | Approved: Arts. 7–13, 17, 24–25. |
| 5.2 — split candidates | Approved: no force-inclusion of Arts. 5, 6, 14, 18, 19, or 28. |
| 5.3 — legal index | Approved: regenerated DORA CELEX-qualified index and validation completed. |
| 5.4 — legal anchors | Approved: all 79 unique Enacting Terms paths verified. |
| 5.5 — coverage and relationship ledger | Approved: 121 atomic COV/REL-COV mappings, with Realization used only for the six evidence-supported partial realizations. |
| 5.6 — legal-role placement | Approved: Employer Bank and Credit Institution are one entity/classification relationship, not separate organisations. |
| Persistence | Explicitly authorised by operator. |
