# DORA Regulatory Relevance, Coverage, and Legal-Role Report

**Pipeline stage:** Step 5 — approved regulatory relevance analysis  
**Stakeholder:** Infrastructure Engineer / Cloud Database Administrator  
**Employing organization label:** Bank (operator-approved anonymized label)  
**Regulation:** Regulation (EU) 2022/2554 (DORA)  
**CELEX:** `32022R2554`

## Approval status

All Step 5 gates are approved:

- Gate 5.1 — consensus articles and exhaustive requirement register;
- Gate 5.2 — Article 5 omitted after a remaining panel split;
- Gate 5.3 — DORA legal index generation;
- Gate 5.4 — canonical legal-text anchors, including the corrected Article 6 mapping;
- Gate 5.5 — footprint-regulation coverage and relationship ledger;
- Gate 5.6 — stakeholder legal-role placement.

This report describes regulatory relevance and operational impact. It does not assess Bank's compliance.

## Legal Index Provenance

| Field | Recorded value |
|---|---|
| Regulation / CELEX | DORA / `32022R2554` |
| Matrix selector | `DORA` |
| Generated workbook | `TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx` |
| Generation timestamp | `2026-09-30T02:16:35+01:00` |
| Workbook validation | Exact sheets `Recitals` and `Enacting Terms`; expected schemas present. |
| Identity validation | `traceability_lookup.py row-id --row 1` returned law `DORA`, CELEX `32022R2554`, and `Chap.I`. |
| Anchor validation | 114 unique Enacting-Term canonical IDs verified; no recital, amendment, or ambiguous anchor used. |

## Three-perspective consensus

The Literal and Gap/Risk evaluators each reviewed Articles 1–64 one at a time through LexAPI. The Systemic evaluator reviewed Articles 1–48 one at a time through LexAPI; a `402 CREDITS_EXHAUSTED` response occurred at Article 49, after which Articles 49–64 were reviewed individually from the same already retrieved live structured document. All retained articles are Article 25 or earlier; the exhaustion did not change the consensus set.

| Final status | Articles |
|---|---|
| Included unanimously | 6–14, 17–18, 24–25 |
| Omitted after debate | 5, 19, 28 |
| Explicit operator decision | Keep Article 5 omitted. |

Article 5 remained split after cross-examination (Literal and Gap/Risk: include; Systemic: exclude) and is therefore omitted under the strict unanimity rule. Articles 19 and 28 were unanimously excluded after debate.

## Approved Requirement and Anchor Register

Every entry below preserves the approved `REQ-*` identifier and direct, verified Enacting Terms anchor. The short duty text is an unsummarized operational label for the binding provision; it does not replace the legal text in the recorded workbook.

### Article 6 — ICT risk management framework

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art6-01 | Sound, comprehensive, documented ICT-risk framework | Art. 6(1) | Chap.II, Section II, Art.6, Paragraph 1 |
| REQ-Art6-02 | Framework enables rapid, efficient, comprehensive ICT-risk response | Art. 6(1) | Chap.II, Section II, Art.6, Paragraph 1 |
| REQ-Art6-03 | Strategies, policies, procedures, protocols, and tools protect ICT assets | Art. 6(2) | Chap.II, Section II, Art.6, Paragraph 2 |
| REQ-Art6-04 | Protect assets from damage and unauthorised access or use | Art. 6(2) | Chap.II, Section II, Art.6, Paragraph 2 |
| REQ-Art6-05 | Minimise ICT-risk impact through appropriate controls | Art. 6(3) | Chap.II, Section II, Art.6, Paragraph 3 |
| REQ-Art6-06 | Supply complete, current ICT-risk information to authorities on request | Art. 6(3) | Chap.II, Section II, Art.6, Paragraph 3 |
| REQ-Art6-07 | Assign ICT-risk oversight to an independent control function | Art. 6(4) | Chap.II, Section II, Art.6, Paragraph 4 |
| REQ-Art6-08 | Segregate risk management, control, and internal audit functions | Art. 6(4) | Chap.II, Section II, Art.6, Paragraph 4 |
| REQ-Art6-09 | Document and periodically review the framework | Art. 6(5) | Chap.II, Section II, Art.6, Paragraph 5 |
| REQ-Art6-10 | Review after major incidents, tests, audits, or supervisory instruction | Art. 6(5) | Chap.II, Section II, Art.6, Paragraph 5 |
| REQ-Art6-11 | Continuously improve from implementation and monitoring lessons | Art. 6(5) | Chap.II, Section II, Art.6, Paragraph 5 |
| REQ-Art6-12 | Submit framework-review report to authority on request | Art. 6(5) | Chap.II, Section II, Art.6, Paragraph 5 |
| REQ-Art6-13 | Conduct regular independent internal ICT-risk audits | Art. 6(6) | Chap.II, Section II, Art.6, Paragraph 6 |
| REQ-Art6-14 | Ensure auditor ICT skills, expertise, and independence | Art. 6(6) | Chap.II, Section II, Art.6, Paragraph 6 |
| REQ-Art6-15 | Set audit frequency and focus commensurate with ICT risk | Art. 6(6) | Chap.II, Section II, Art.6, Paragraph 6 |
| REQ-Art6-16 | Formally verify and remediate critical audit findings | Art. 6(7) | Chap.II, Section II, Art.6, Paragraph 7 |
| REQ-Art6-17 | Include a digital operational resilience strategy | Art. 6(8) | Chap.II, Section II, Art.6, Paragraph 8 |
| REQ-Art6-18 | Explain framework support for business strategy and objectives | Art. 6(8)(a) | Chap.II, Section II, Art.6, Paragraph 8, Point a |
| REQ-Art6-19 | Establish ICT-risk and disruption-impact tolerances | Art. 6(8)(b) | Chap.II, Section II, Art.6, Paragraph 8, Point b |
| REQ-Art6-20 | Set information-security objectives, KPIs, and KRIs | Art. 6(8)(c) | Chap.II, Section II, Art.6, Paragraph 8, Point c |
| REQ-Art6-21 | Explain ICT reference architecture and required changes | Art. 6(8)(d) | Chap.II, Section II, Art.6, Paragraph 8, Point d |
| REQ-Art6-22 | Outline incident detection, prevention, and protection mechanisms | Art. 6(8)(e) | Chap.II, Section II, Art.6, Paragraph 8, Point e |
| REQ-Art6-23 | Evidence current digital-resilience situation and preventive effectiveness | Art. 6(8)(f) | Chap.II, Section II, Art.6, Paragraph 8, Point f |
| REQ-Art6-24 | Implement digital operational resilience testing | Art. 6(8)(g) | Chap.II, Section II, Art.6, Paragraph 8, Point g |
| REQ-Art6-25 | Outline communication strategy for reportable ICT incidents | Art. 6(8)(h) | Chap.II, Section II, Art.6, Paragraph 8, Point h |
| REQ-Art6-26 | Retain compliance-verification responsibility if verification is outsourced | Art. 6(10) | Chap.II, Section II, Art.6, Paragraph 10 |

### Articles 7 and 8 — ICT systems and identification

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art7-01 | Use and maintain updated ICT systems, protocols, and tools | Art. 7(1) | Chap.II, Section II, Art.7, Paragraph 1 |
| REQ-Art7-02 | Ensure systems are proportionate to operations | Art. 7(1)(a) | Chap.II, Section II, Art.7, Paragraph 1, Point a |
| REQ-Art7-03 | Ensure systems are reliable | Art. 7(1)(b) | Chap.II, Section II, Art.7, Paragraph 1, Point b |
| REQ-Art7-04 | Provide sufficient capacity for data and peak volumes | Art. 7(1)(c) | Chap.II, Section II, Art.7, Paragraph 1, Point c |
| REQ-Art7-05 | Ensure technological resilience under adverse conditions | Art. 7(1)(d) | Chap.II, Section II, Art.7, Paragraph 1, Point d |
| REQ-Art8-01 | Identify, classify, and document ICT functions, roles, assets, and dependencies | Art. 8(1) | Chap.II, Section II, Art.8, Paragraph 1 |
| REQ-Art8-02 | Review classification and documentation at least yearly | Art. 8(1) | Chap.II, Section II, Art.8, Paragraph 1 |
| REQ-Art8-03 | Continuously identify ICT-risk sources | Art. 8(2) | Chap.II, Section II, Art.8, Paragraph 2 |
| REQ-Art8-04 | Assess relevant cyber threats, vulnerabilities, and risk scenarios | Art. 8(2) | Chap.II, Section II, Art.8, Paragraph 2 |
| REQ-Art8-05 | Review ICT-risk scenarios regularly and at least yearly | Art. 8(2) | Chap.II, Section II, Art.8, Paragraph 2 |
| REQ-Art8-06 | Assess risk for each major ICT infrastructure or process change | Art. 8(3) | Chap.II, Section II, Art.8, Paragraph 3 |
| REQ-Art8-07 | Identify all information and ICT assets, including remote/network assets | Art. 8(4) | Chap.II, Section II, Art.8, Paragraph 4 |
| REQ-Art8-08 | Map information and ICT assets considered critical | Art. 8(4) | Chap.II, Section II, Art.8, Paragraph 4 |
| REQ-Art8-09 | Map configurations, links, and interdependencies | Art. 8(4) | Chap.II, Section II, Art.8, Paragraph 4 |
| REQ-Art8-10 | Document provider-dependent processes and critical-function interconnections | Art. 8(5) | Chap.II, Section II, Art.8, Paragraph 5 |
| REQ-Art8-11 | Maintain relevant asset inventories | Art. 8(6) | Chap.II, Section II, Art.8, Paragraph 6 |
| REQ-Art8-12 | Update inventories periodically and after major changes | Art. 8(6) | Chap.II, Section II, Art.8, Paragraph 6 |
| REQ-Art8-13 | Assess legacy systems and technology connections regularly | Art. 8(7) | Chap.II, Section II, Art.8, Paragraph 7 |

### Articles 9 and 10 — Protection and detection

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art9-01 | Continuously monitor and control ICT security and functioning | Art. 9(1) | Chap.II, Section II, Art.9, Paragraph 1 |
| REQ-Art9-02 | Minimise ICT-risk impact with security tools, policies, and procedures | Art. 9(1) | Chap.II, Section II, Art.9, Paragraph 1 |
| REQ-Art9-03 | Design and implement resilient, continuous, available ICT security | Art. 9(2) | Chap.II, Section II, Art.9, Paragraph 2 |
| REQ-Art9-04 | Preserve data availability, authenticity, integrity, and confidentiality | Art. 9(2) | Chap.II, Section II, Art.9, Paragraph 2 |
| REQ-Art9-05 | Use proportionate ICT solutions and processes | Art. 9(3) | Chap.II, Section II, Art.9, Paragraph 3 |
| REQ-Art9-06 | Secure data-transfer means | Art. 9(3)(a) | Chap.II, Section II, Art.9, Paragraph 3, Point a |
| REQ-Art9-07 | Minimise data loss, unauthorised access, and technical flaws | Art. 9(3)(b) | Chap.II, Section II, Art.9, Paragraph 3, Point b |
| REQ-Art9-08 | Prevent loss of availability, integrity, authenticity, and confidentiality | Art. 9(3)(c) | Chap.II, Section II, Art.9, Paragraph 3, Point c |
| REQ-Art9-09 | Protect data from management, processing, and human-error risks | Art. 9(3)(d) | Chap.II, Section II, Art.9, Paragraph 3, Point d |
| REQ-Art9-10 | Develop and document information-security policy | Art. 9(4)(a) | Chap.II, Section II, Art.9, Paragraph 4, Point a |
| REQ-Art9-11 | Establish risk-based network and infrastructure management | Art. 9(4)(b) | Chap.II, Section II, Art.9, Paragraph 4, Point b |
| REQ-Art9-12 | Limit logical/physical access and administer access rights | Art. 9(4)(c) | Chap.II, Section II, Art.9, Paragraph 4, Point c |
| REQ-Art9-13 | Limit access to legitimate, approved functions | Art. 9(4)(c) | Chap.II, Section II, Art.9, Paragraph 4, Point c |
| REQ-Art9-14 | Use strong authentication and protect cryptographic keys | Art. 9(4)(d) | Chap.II, Section II, Art.9, Paragraph 4, Point d |
| REQ-Art9-15 | Base encryption protection on classification and risk assessment | Art. 9(4)(d) | Chap.II, Section II, Art.9, Paragraph 4, Point d |
| REQ-Art9-16 | Document controlled ICT change management | Art. 9(4)(e) | Chap.II, Section II, Art.9, Paragraph 4, Point e |
| REQ-Art9-17 | Record, test, assess, approve, implement, and verify changes | Art. 9(4)(e) | Chap.II, Section II, Art.9, Paragraph 4, Point e |
| REQ-Art9-18 | Obtain management-approved change protocols | Art. 9(4) | Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2 |
| REQ-Art9-19 | Maintain documented patch and update policies | Art. 9(4)(f) | Chap.II, Section II, Art.9, Paragraph 4, Point f |
| REQ-Art9-20 | Permit prompt network severance or segmentation | Art. 9(4) | Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1 |
| REQ-Art10-01 | Detect anomalies, performance issues, and ICT incidents promptly | Art. 10(1) | Chap.II, Section II, Art.10, Paragraph 1 |
| REQ-Art10-02 | Identify potential material single points of failure | Art. 10(1) | Chap.II, Section II, Art.10, Paragraph 1 |
| REQ-Art10-03 | Regularly test detection mechanisms | Art. 10(1) | Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1 |
| REQ-Art10-04 | Enable multiple layers of detection control | Art. 10(2) | Chap.II, Section II, Art.10, Paragraph 2 |
| REQ-Art10-05 | Define alert thresholds and incident-response triggers | Art. 10(2) | Chap.II, Section II, Art.10, Paragraph 2 |
| REQ-Art10-06 | Automatically alert relevant incident-response staff | Art. 10(2) | Chap.II, Section II, Art.10, Paragraph 2 |
| REQ-Art10-07 | Resource monitoring of user activity, anomalies, and cyber-attacks | Art. 10(3) | Chap.II, Section II, Art.10, Paragraph 3 |

### Articles 11 and 12 — Continuity and recovery

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art11-01 | Establish comprehensive ICT business-continuity policy | Art. 11(1) | Chap.II, Section II, Art.11, Paragraph 1 |
| REQ-Art11-02 | Implement policy with documented arrangements, plans, procedures, and mechanisms | Art. 11(2) | Chap.II, Section II, Art.11, Paragraph 2 |
| REQ-Art11-03 | Ensure continuity of critical or important functions | Art. 11(2)(a) | Chap.II, Section II, Art.11, Paragraph 2, Point a |
| REQ-Art11-04 | Respond to and resolve incidents promptly and effectively | Art. 11(2)(b) | Chap.II, Section II, Art.11, Paragraph 2, Point b |
| REQ-Art11-05 | Prioritise resumption and recovery actions | Art. 11(2)(b) | Chap.II, Section II, Art.11, Paragraph 2, Point b |
| REQ-Art11-06 | Activate containment measures and plans without delay | Art. 11(2)(c) | Chap.II, Section II, Art.11, Paragraph 2, Point c |
| REQ-Art11-07 | Maintain tailored response and recovery procedures | Art. 11(2)(c) | Chap.II, Section II, Art.11, Paragraph 2, Point c |
| REQ-Art11-08 | Estimate preliminary incident impacts, damage, and losses | Art. 11(2)(d) | Chap.II, Section II, Art.11, Paragraph 2, Point d |
| REQ-Art11-09 | Implement crisis communications and authority reporting | Art. 11(2)(e) | Chap.II, Section II, Art.11, Paragraph 2, Point e |
| REQ-Art11-10 | Implement ICT response and recovery plans | Art. 11(3) | Chap.II, Section II, Art.11, Paragraph 3 |
| REQ-Art11-11 | Subject response and recovery plans to independent audit | Art. 11(3) | Chap.II, Section II, Art.11, Paragraph 3 |
| REQ-Art11-12 | Maintain and periodically test continuity plans | Art. 11(4) | Chap.II, Section II, Art.11, Paragraph 4 |
| REQ-Art11-13 | Conduct business-impact analysis | Art. 11(5) | Chap.II, Section II, Art.11, Paragraph 5 |
| REQ-Art11-14 | Assess potential severe-disruption impacts | Art. 11(5) | Chap.II, Section II, Art.11, Paragraph 5 |
| REQ-Art11-15 | Consider criticality, dependencies, assets, and interdependencies in BIA | Art. 11(5) | Chap.II, Section II, Art.11, Paragraph 5 |
| REQ-Art11-16 | Align assets, services, and redundancy with BIA | Art. 11(5) | Chap.II, Section II, Art.11, Paragraph 5 |
| REQ-Art11-17 | Test continuity/recovery plans annually and after substantive change | Art. 11(6)(a) | Chap.II, Section II, Art.11, Paragraph 6, Point a |
| REQ-Art11-18 | Test crisis-communication plans | Art. 11(6)(b) | Chap.II, Section II, Art.11, Paragraph 6, Point b |
| REQ-Art11-19 | Test cyberattack, switchover, backup, and redundancy scenarios | Art. 11(6) | Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1 |
| REQ-Art11-20 | Review continuity and recovery plans after tests/audits/reviews | Art. 11(6) | Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2 |
| REQ-Art11-21 | Maintain a crisis-management function | Art. 11(7) | Chap.II, Section II, Art.11, Paragraph 7 |
| REQ-Art11-22 | Keep disruption-event activity records readily accessible | Art. 11(8) | Chap.II, Section II, Art.11, Paragraph 8 |
| REQ-Art11-23 | Estimate and report annual major-incident costs and losses | Art. 11(10) | Chap.II, Section II, Art.11, Paragraph 10 |
| REQ-Art12-01 | Restore ICT systems and data with minimal downtime, disruption, and loss | Art. 12(1) | Chap.II, Section II, Art.12, Paragraph 1 |
| REQ-Art12-02 | Specify backup scope and minimum frequency | Art. 12(1)(a) | Chap.II, Section II, Art.12, Paragraph 1, Point a |
| REQ-Art12-03 | Develop restoration and recovery procedures and methods | Art. 12(1)(b) | Chap.II, Section II, Art.12, Paragraph 1, Point b |
| REQ-Art12-04 | Provide activatable backup systems | Art. 12(2) | Chap.II, Section II, Art.12, Paragraph 2 |
| REQ-Art12-05 | Preserve security and data properties on backup activation | Art. 12(2) | Chap.II, Section II, Art.12, Paragraph 2 |
| REQ-Art12-06 | Periodically test backup, restoration, and recovery | Art. 12(2) | Chap.II, Section II, Art.12, Paragraph 2 |
| REQ-Art12-07 | Use physically and logically segregated restoration systems | Art. 12(3) | Chap.II, Section II, Art.12, Paragraph 3 |
| REQ-Art12-08 | Secure restoration systems against unauthorised access and corruption | Art. 12(3) | Chap.II, Section II, Art.12, Paragraph 3 |
| REQ-Art12-09 | Enable timely restoration using data and system backups | Art. 12(3) | Chap.II, Section II, Art.12, Paragraph 3 |
| REQ-Art12-10 | Maintain adequate redundant ICT capacity | Art. 12(4) | Chap.II, Section II, Art.12, Paragraph 4 |
| REQ-Art12-11 | Microenterprise redundancy assessment | Art. 12(4) | Chap.II, Section II, Art.12, Paragraph 4 |
| REQ-Art12-12 | Set recovery time/point objectives based on criticality and impact | Art. 12(6) | Chap.II, Section II, Art.12, Paragraph 6 |
| REQ-Art12-13 | Meet agreed service levels in extreme scenarios | Art. 12(6) | Chap.II, Section II, Art.12, Paragraph 6 |
| REQ-Art12-14 | Perform recovery integrity checks and reconciliations | Art. 12(7) | Chap.II, Section II, Art.12, Paragraph 7 |
| REQ-Art12-15 | Ensure consistency of data reconstructed from external stakeholders | Art. 12(7) | Chap.II, Section II, Art.12, Paragraph 7 |

### Articles 13 and 14 — Learning and communication

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art13-01 | Gather vulnerability, threat, and incident information and analyse resilience impact | Art. 13(1) | Chap.II, Section II, Art.13, Paragraph 1 |
| REQ-Art13-02 | Conduct post-major-incident reviews | Art. 13(2) | Chap.II, Section II, Art.13, Paragraph 2 |
| REQ-Art13-03 | Identify required improvements to ICT operations or continuity policy | Art. 13(2) | Chap.II, Section II, Art.13, Paragraph 2 |
| REQ-Art13-04 | Communicate review-driven changes to authorities on request | Art. 13(2) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1 |
| REQ-Art13-05 | Determine whether procedures and actions were followed/effective | Art. 13(2) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2 |
| REQ-Art13-06 | Assess response promptness and incident severity assessment | Art. 13(2)(a) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a |
| REQ-Art13-07 | Assess forensic-analysis quality and speed | Art. 13(2)(b) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b |
| REQ-Art13-08 | Assess effectiveness of incident escalation | Art. 13(2)(c) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c |
| REQ-Art13-09 | Assess effectiveness of internal and external communication | Art. 13(2)(d) | Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d |
| REQ-Art13-10 | Incorporate lessons into ICT-risk assessment | Art. 13(3) | Chap.II, Section II, Art.13, Paragraph 3 |
| REQ-Art13-11 | Review ICT-risk-framework components using those lessons | Art. 13(3) | Chap.II, Section II, Art.13, Paragraph 3 |
| REQ-Art13-12 | Monitor resilience-strategy implementation effectiveness | Art. 13(4) | Chap.II, Section II, Art.13, Paragraph 4 |
| REQ-Art13-13 | Map ICT-risk evolution and incident patterns | Art. 13(4) | Chap.II, Section II, Art.13, Paragraph 4 |
| REQ-Art13-14 | Senior ICT staff report findings and recommendations yearly | Art. 13(5) | Chap.II, Section II, Art.13, Paragraph 5 |
| REQ-Art13-15 | Provide compulsory awareness and resilience training | Art. 13(6) | Chap.II, Section II, Art.13, Paragraph 6 |
| REQ-Art13-16 | Include relevant ICT third-party providers in training where appropriate | Art. 13(6) | Chap.II, Section II, Art.13, Paragraph 6 |
| REQ-Art13-17 | Monitor relevant technological developments and current risk-management practices | Art. 13(7) | Chap.II, Section II, Art.13, Paragraph 7 |
| REQ-Art14-01 | Maintain crisis-communication plans | Art. 14(1) | Chap.II, Section II, Art.14, Paragraph 1 |
| REQ-Art14-02 | Enable responsible disclosure of major incidents/vulnerabilities | Art. 14(1) | Chap.II, Section II, Art.14, Paragraph 1 |
| REQ-Art14-03 | Implement internal and external communication policies | Art. 14(2) | Chap.II, Section II, Art.14, Paragraph 2 |
| REQ-Art14-04 | Differentiate ICT-response staff from staff to be informed | Art. 14(2) | Chap.II, Section II, Art.14, Paragraph 2 |
| REQ-Art14-05 | Assign public/media incident-communication responsibility | Art. 14(3) | Chap.II, Section II, Art.14, Paragraph 3 |

### Articles 17, 18, 24, and 25 — Incidents and testing

| Requirement | Binding duty / restriction | Citation | Verified direct legal-text ID |
|---|---|---|---|
| REQ-Art17-01 | Define, establish, and implement incident management | Art. 17(1) | Chap.III, Art.17, Paragraph 1 |
| REQ-Art17-02 | Detect, manage, and notify ICT-related incidents | Art. 17(1) | Chap.III, Art.17, Paragraph 1 |
| REQ-Art17-03 | Record ICT incidents and significant cyber threats | Art. 17(2) | Chap.III, Art.17, Paragraph 2 |
| REQ-Art17-04 | Monitor, handle, and follow up incidents consistently | Art. 17(2) | Chap.III, Art.17, Paragraph 2 |
| REQ-Art17-05 | Identify, document, and address root causes | Art. 17(2) | Chap.III, Art.17, Paragraph 2 |
| REQ-Art17-06 | Maintain early-warning indicators | Art. 17(3)(a) | Chap.III, Art.17, Paragraph 3, Point a |
| REQ-Art17-07 | Identify, track, log, categorise, and classify incidents | Art. 17(3)(b) | Chap.III, Art.17, Paragraph 3, Point b |
| REQ-Art17-08 | Assign roles/responsibilities for incident scenarios | Art. 17(3)(c) | Chap.III, Art.17, Paragraph 3, Point c |
| REQ-Art17-09 | Set communication, notification, and escalation procedures | Art. 17(3)(d) | Chap.III, Art.17, Paragraph 3, Point d |
| REQ-Art17-10 | Report major incidents to senior management/body | Art. 17(3)(e) | Chap.III, Art.17, Paragraph 3, Point e |
| REQ-Art17-11 | Mitigate impact and restore secure services promptly | Art. 17(3)(f) | Chap.III, Art.17, Paragraph 3, Point f |
| REQ-Art18-01 | Classify incidents and determine their impact | Art. 18(1) | Chap.III, Art.18, Paragraph 1 |
| REQ-Art18-02 | Consider affected clients/counterparts | Art. 18(1)(a) | Chap.III, Art.18, Paragraph 1, Point a |
| REQ-Art18-03 | Consider affected transactions | Art. 18(1)(a) | Chap.III, Art.18, Paragraph 1, Point a |
| REQ-Art18-04 | Consider reputational impact | Art. 18(1)(a) | Chap.III, Art.18, Paragraph 1, Point a |
| REQ-Art18-05 | Consider incident duration and downtime | Art. 18(1)(b) | Chap.III, Art.18, Paragraph 1, Point b |
| REQ-Art18-06 | Consider geographical spread | Art. 18(1)(c) | Chap.III, Art.18, Paragraph 1, Point c |
| REQ-Art18-07 | Consider availability, authenticity, integrity, and confidentiality data losses | Art. 18(1)(d) | Chap.III, Art.18, Paragraph 1, Point d |
| REQ-Art18-08 | Consider criticality of affected services and operations | Art. 18(1)(e) | Chap.III, Art.18, Paragraph 1, Point e |
| REQ-Art18-09 | Consider direct and indirect economic impact | Art. 18(1)(f) | Chap.III, Art.18, Paragraph 1, Point f |
| REQ-Art18-10 | Classify significant cyber threats | Art. 18(2) | Chap.III, Art.18, Paragraph 2 |
| REQ-Art24-01 | Establish, maintain, and review resilience-testing programme | Art. 24(1) | Chap.IV, Art.24, Paragraph 1 |
| REQ-Art24-02 | Assess preparedness, identify gaps, and implement corrections | Art. 24(1) | Chap.IV, Art.24, Paragraph 1 |
| REQ-Art24-03 | Include a range of test assessments, methodologies, practices, and tools | Art. 24(2) | Chap.IV, Art.24, Paragraph 2 |
| REQ-Art24-04 | Apply a risk-based testing approach | Art. 24(3) | Chap.IV, Art.24, Paragraph 3 |
| REQ-Art24-05 | Use independent testing parties | Art. 24(4) | Chap.IV, Art.24, Paragraph 4 |
| REQ-Art24-06 | Resource internal testing and avoid conflicts of interest | Art. 24(4) | Chap.IV, Art.24, Paragraph 4 |
| REQ-Art24-07 | Prioritise, classify, remedy, and validate test findings | Art. 24(5) | Chap.IV, Art.24, Paragraph 5 |
| REQ-Art24-08 | Test critical ICT systems/applications at least yearly | Art. 24(6) | Chap.IV, Art.24, Paragraph 6 |
| REQ-Art25-01 | Execute appropriate resilience tests | Art. 25(1) | Chap.IV, Art.25, Paragraph 1 |
| REQ-Art25-02 | Cover compatibility, performance, end-to-end, and penetration testing as appropriate | Art. 25(1) | Chap.IV, Art.25, Paragraph 1 |
| REQ-Art25-03 | Use applicable assessment, scan, review, and scenario test methods | Art. 25(1) | Chap.IV, Art.25, Paragraph 1 |
| REQ-Art25-04 | CSD/CCP vulnerability assessment before deployment/redeployment | Art. 25(2) | Chap.IV, Art.25, Paragraph 2 |
| REQ-Art25-05 | Microenterprise risk-based strategic test planning | Art. 25(3) | Chap.IV, Art.25, Paragraph 3 |

## Footprint-Regulation Coverage Ledger

`Realization` is used only where the stakeholder directly performs the recorded activity. `Association` records a verified legal constraint, external duty, or unresolved ownership; it does not assert that the stakeholder realizes the requirement. Every coverage edge is visible, proposed-to-approved through Gate 5.5, and has the same numeric suffix in its `COV-*` and `REL-COV-*` identifiers.

### ICT-risk framework, systems, identification, protection, and detection

| COV / Relation | Operational endpoint and evidence | Legal endpoint | Evidence-backed effect | Ownership | Stream |
|---|---|---|---|---|---|
| COV-001 / REL-COV-001 | Stakeholder Team accountability (OP-048) | Sound ICT-risk framework (REQ-Art6-01) | Team technology accountability is constrained by the framework. | Stakeholder-constrained | ICT governance |
| COV-002 / REL-COV-002 | Technology maintenance (OP-007) | Rapid ICT-risk response (REQ-Art6-02) | Maintenance work is constrained by the framework response objective. | Stakeholder-constrained | ICT governance |
| COV-003 / REL-COV-003 | Platform responsibility (OP-002, OP-003, OP-004) | Asset-protection controls (REQ-Art6-03) | Administered platforms are the stated ICT assets. | Stakeholder-constrained | ICT governance |
| COV-004 / REL-COV-004 | Access provisioning/Ranger policies (OP-005, OP-009, OP-052, CON-002, CON-003) | Protection from unauthorised access (REQ-Art6-04) | The named access work is constrained by this protection duty. | Stakeholder-constrained | Access control |
| COV-005 / REL-COV-005 | SingleStore recovery (OP-037, OP-054, CON-007) | Minimise ICT-risk impact (REQ-Art6-05) | Recovery directly mitigates stated service-impact incidents. | Directly performed | Incident recovery |
| COV-006 / REL-COV-006 | Post-incident report (OP-043) | Supply authority information (REQ-Art6-06) | Report is sent to support; authority reporting is outside the role. | Externally owned | ICT governance |
| COV-007 / REL-COV-007 | Stakeholder Team accountability (OP-048) | Independent ICT-risk control (REQ-Art6-07) | Control-function ownership is not assigned to the stakeholder. | Externally owned | ICT governance |
| COV-008 / REL-COV-008 | Authorization/Security Teams (OP-044, OP-045) | Segregated control functions (REQ-Art6-08) | Separate approval teams are explicit. | Externally owned | Change governance |
| COV-009 / REL-COV-009 | Change review (OP-050) | Documented framework review (REQ-Art6-09) | Review work is constrained by the framework-review duty. | Stakeholder-constrained | ICT governance |
| COV-010 / REL-COV-010 | Change review/post-incident report (OP-050, OP-043) | Event-triggered review (REQ-Art6-10) | Both facts are inputs to, not evidence of ownership of, framework review. | Stakeholder-constrained | ICT governance |
| COV-011 / REL-COV-011 | Technology maintenance (OP-007) | Continuous framework improvement (REQ-Art6-11) | Improvement work is constrained by the framework-improvement duty. | Stakeholder-constrained | ICT governance |
| COV-012 / REL-COV-012 | Post-incident report (OP-043) | Authority review report (REQ-Art6-12) | Authority reporting is not assigned to the stakeholder. | Externally owned | ICT governance |
| COV-013 / REL-COV-013 | Stakeholder Team accountability (OP-048) | Independent ICT audit (REQ-Art6-13) | Audit ownership is external to the team role. | Externally owned | ICT governance |
| COV-014 / REL-COV-014 | Senior technical role (OP-001) | Auditor skills/independence (REQ-Art6-14) | No auditor role is evidenced. | Externally owned | ICT governance |
| COV-015 / REL-COV-015 | Stakeholder Team accountability (OP-048) | Risk-based audit frequency (REQ-Art6-15) | Audit planning is outside the stated role. | Externally owned | ICT governance |
| COV-016 / REL-COV-016 | Change review (OP-050) | Audit-finding follow-up (REQ-Art6-16) | Review task can be constrained by audit follow-up. | Stakeholder-constrained | ICT governance |
| COV-017 / REL-COV-017 | Stakeholder Team accountability (OP-048) | Resilience strategy (REQ-Art6-17) | Team accountability lies within the strategy's scope. | Stakeholder-constrained | ICT governance |
| COV-018 / REL-COV-018 | Stakeholder Team accountability (OP-048) | Strategy supports business objectives (REQ-Art6-18) | Business-strategy ownership is not assigned to the role. | Stakeholder-constrained | ICT governance |
| COV-019 / REL-COV-019 | Service-outage impact (OP-036, CON-006) | ICT-risk/disruption tolerance (REQ-Art6-19) | Stated outage impact is an input to tolerance setting. | Stakeholder-constrained | ICT governance |
| COV-020 / REL-COV-020 | Datadog monitoring (OP-038) | Security KPIs and KRIs (REQ-Art6-20) | Monitoring provides a constrained operational input. | Stakeholder-constrained | Monitoring |
| COV-021 / REL-COV-021 | GitOps/AKS deployment (OP-015, OP-020, OP-023) | ICT reference architecture (REQ-Art6-21) | Deployment/configuration changes affect the reference architecture. | Stakeholder-constrained | Change governance |
| COV-022 / REL-COV-022 | Datadog alerting and recovery (OP-037, OP-038) | Detect/prevent/protect mechanisms (REQ-Art6-22) | Detection and recovery are directly performed. | Directly performed | Monitoring |
| COV-023 / REL-COV-023 | Post-incident report (OP-043) | Evidence resilience situation (REQ-Art6-23) | Report provides a constrained technical input. | Stakeholder-constrained | Incident recovery |
| COV-024 / REL-COV-024 | Non-production testing (OP-016, OP-017, OP-025) | Resilience testing (REQ-Art6-24) | Testing is directly performed. | Directly performed | Resilience testing |
| COV-025 / REL-COV-025 | Support handoff report (OP-043) | Incident communication strategy (REQ-Art6-25) | Communication-strategy ownership is external. | Externally owned | Incident recovery |
| COV-026 / REL-COV-026 | Provider-supported platforms (OP-002, OP-003, OP-004; operator confirmation) | Retained verification responsibility (REQ-Art6-26) | Providers are confirmed, but whether compliance verification is outsourced is unknown. | Not evidenced / unclear owner | Third-party dependency |
| COV-027 / REL-COV-027 | Technology maintenance (OP-002, OP-003, OP-004, OP-007) | Updated ICT systems/tools (REQ-Art7-01) | Maintenance is directly performed. | Directly performed | Platform operations |
| COV-028 / REL-COV-028 | Platform responsibility (OP-002, OP-003, OP-004) | Proportionate systems/tools (REQ-Art7-02) | System scale/proportionality is not assigned to the role. | Stakeholder-constrained | Platform operations |
| COV-029 / REL-COV-029 | Connectivity validation (OP-019) | Reliable systems/tools (REQ-Art7-03) | Availability/connectivity validation is directly performed. | Directly performed | Platform operations |
| COV-030 / REL-COV-030 | Compute dependency (OP-031, CON-005) | Sufficient ICT capacity (REQ-Art7-04) | Capacity depends on the stated compute team. | Stakeholder-constrained | Platform operations |
| COV-031 / REL-COV-031 | Service-outage impact (OP-036, CON-006) | Technological resilience (REQ-Art7-05) | The incident impact constrains resilience needs. | Stakeholder-constrained | Platform operations |
| COV-032 / REL-COV-032 | Role/asset responsibility (OP-001, OP-002, OP-003, OP-004, OP-048) | Document functions, roles, assets, dependencies (REQ-Art8-01) | Existing asset responsibility is a constrained input. | Stakeholder-constrained | Asset governance |
| COV-033 / REL-COV-033 | Change review (OP-050) | Review classification/documentation (REQ-Art8-02) | Self-review is constrained by the broader duty. | Stakeholder-constrained | Asset governance |
| COV-034 / REL-COV-034 | Team/provider dependencies (OP-031, OP-032, OP-033; provider confirmation) | Identify ICT-risk sources (REQ-Art8-03) | Named dependencies provide a constrained source record. | Stakeholder-constrained | Asset governance |
| COV-035 / REL-COV-035 | Developer issue diagnosis (OP-006) | Assess threats/vulnerabilities (REQ-Art8-04) | Diagnosis work is constrained; threat assessment owner is unstated. | Stakeholder-constrained | Asset governance |
| COV-036 / REL-COV-036 | Team/provider dependencies (OP-031, OP-032, OP-033; provider confirmation) | Review ICT-risk scenarios (REQ-Art8-05) | Named dependencies are a constrained risk-scenario input. | Stakeholder-constrained | Asset governance |
| COV-037 / REL-COV-037 | GitOps migration (OP-014) | Risk assessment for major change (REQ-Art8-06) | Major change is explicit; risk-assessment ownership is unstated. | Stakeholder-constrained | Change governance |
| COV-038 / REL-COV-038 | Platform responsibility (OP-002, OP-003, OP-004) | Identify ICT assets (REQ-Art8-07) | Named administered technologies are asset evidence. | Stakeholder-constrained | Asset governance |
| COV-039 / REL-COV-039 | Platform responsibility (OP-002, OP-003, OP-004) | Map critical ICT assets (REQ-Art8-08) | Criticality mapping owner is unstated. | Stakeholder-constrained | Asset governance |
| COV-040 / REL-COV-040 | Configuration maintenance (OP-020, OP-021, OP-023) | Map configurations/interdependencies (REQ-Art8-09) | Configurations and integration are explicit. | Stakeholder-constrained | Asset governance |
| COV-041 / REL-COV-041 | Provider-supported platforms (OP-002, OP-003, OP-004; operator confirmation) | Document provider dependencies/interconnections (REQ-Art8-10) | Provider use is confirmed; documentation owner is unstated. | Stakeholder-constrained | Third-party dependency |
| COV-042 / REL-COV-042 | Azure DevOps configuration store (OP-021) | Maintain asset inventories (REQ-Art8-11) | Configuration store is constrained by inventory duty. | Stakeholder-constrained | Asset governance |
| COV-043 / REL-COV-043 | Production change opening (OP-028) | Update inventories after change (REQ-Art8-12) | Change work is constrained by update duty. | Stakeholder-constrained | Asset governance |
| COV-044 / REL-COV-044 | Historic deployment/External Secrets connection (OP-014, OP-023, CON-001) | Assess legacy systems and technology connections (REQ-Art8-13) | Historic script and connection are constrained risk-assessment inputs. | Stakeholder-constrained | Asset governance |
| COV-045 / REL-COV-045 | Datadog monitoring (OP-038) | Monitor security/functioning (REQ-Art9-01) | Monitoring is directly performed. | Directly performed | Monitoring |
| COV-046 / REL-COV-046 | SingleStore recovery (OP-037, OP-038) | Minimise impact with security controls (REQ-Art9-02) | Recovery directly mitigates the incident. | Directly performed | Incident recovery |
| COV-047 / REL-COV-047 | Platform responsibility (OP-002, OP-003, OP-004, OP-048) | Resilient/continuous/available ICT security (REQ-Art9-03) | Platform work is constrained by the duty. | Stakeholder-constrained | Security controls |
| COV-048 / REL-COV-048 | Secret handling (OP-022, OP-024) | Data availability/authenticity/integrity/confidentiality (REQ-Art9-04) | Sensitive-data work is constrained by data protection. | Stakeholder-constrained | Security controls |
| COV-049 / REL-COV-049 | Technology maintenance (OP-007) | Appropriate ICT solutions/processes (REQ-Art9-05) | Maintenance is directly performed. | Directly performed | Security controls |
| COV-050 / REL-COV-050 | Support handoff (OP-034) | Secure transfer means (REQ-Art9-06) | Logs/configs are transferred; transfer-security control owner is unstated. | Stakeholder-constrained | Security controls |
| COV-051 / REL-COV-051 | Root-secret use (OP-022, OP-024) | Prevent loss/access/flaws (REQ-Art9-07) | Secret use is constrained by prevention duty. | Stakeholder-constrained | Security controls |
| COV-052 / REL-COV-052 | Service-outage impact (OP-036) | Prevent loss of availability/integrity/confidentiality (REQ-Art9-08) | Outage impact is a constrained input. | Stakeholder-constrained | Security controls |
| COV-053 / REL-COV-053 | Access/maintenance work (OP-005, OP-007) | Protect from admin/processing/human-error risk (REQ-Art9-09) | Work is constrained by the protection duty. | Stakeholder-constrained | Security controls |
| COV-054 / REL-COV-054 | Stakeholder Team accountability (OP-048) | Information-security policy (REQ-Art9-10) | Policy ownership is unstated. | Stakeholder-constrained | Security controls |
| COV-055 / REL-COV-055 | Compute/network dependencies (OP-031, OP-032) | Network/infrastructure management (REQ-Art9-11) | Responsibility rests with dependency teams. | Stakeholder-constrained | Security controls |
| COV-056 / REL-COV-056 | Access provisioning/Ranger automation (OP-005, OP-008, OP-009, OP-052, CON-002, CON-003) | Access-rights policies/administration (REQ-Art9-12) | Access administration is directly performed. | Directly performed | Access control |
| COV-057 / REL-COV-057 | Security Team approval (OP-045) | Access limited to approved functions (REQ-Art9-13) | Approval is externally owned. | Externally owned | Access control |
| COV-058 / REL-COV-058 | Azure Key Vault secrets (OP-022) | Strong authentication/key protection (REQ-Art9-14) | Secret store is constrained by this duty. | Stakeholder-constrained | Security controls |
| COV-059 / REL-COV-059 | Root-secret use (OP-022, OP-024) | Classification/risk-based encryption protection (REQ-Art9-15) | Classification/risk owner is unstated. | Stakeholder-constrained | Security controls |
| COV-060 / REL-COV-060 | Production change recording (OP-027, OP-028) | Document controlled changes (REQ-Art9-16) | Recording is directly performed. | Directly performed | Change governance |
| COV-061 / REL-COV-061 | Production-readiness gate (OP-017, OP-030, OP-050) | Test/assess/approve/implement/verify change (REQ-Art9-17) | Testing/review is performed; approval is external. | Stakeholder-constrained | Change governance |
| COV-062 / REL-COV-062 | Authorization-status workflow (OP-044, OP-046, OP-047, OP-056, CON-009) | Management-approved change protocols (REQ-Art9-18) | Authorization team exists; automation owner is unknown. | Not evidenced / unclear owner | Change governance |
| COV-063 / REL-COV-063 | Technology maintenance (OP-007) | Patch/update policy (REQ-Art9-19) | Updates are performed; policy owner unstated. | Stakeholder-constrained | Change governance |
| COV-064 / REL-COV-064 | Networking dependency (OP-032) | Network severance/segmentation (REQ-Art9-20) | Capability depends on networking team. | Stakeholder-constrained | Security controls |
| COV-065 / REL-COV-065 | Datadog monitoring (OP-038) | Detect anomalies/performance/incidents (REQ-Art10-01) | Detection is directly performed. | Directly performed | Monitoring |
| COV-066 / REL-COV-066 | Monitoring/outage evidence (OP-031, OP-036, OP-038) | Identify material single points of failure (REQ-Art10-02) | Evidence constrains the identification duty. | Stakeholder-constrained | Monitoring |
| COV-067 / REL-COV-067 | Log validation/testing (OP-016, OP-018) | Test detection mechanisms (REQ-Art10-03) | Detection-test scope/owner is unstated. | Stakeholder-constrained | Monitoring |
| COV-068 / REL-COV-068 | Datadog monitoring (OP-038) | Multiple detection-control layers (REQ-Art10-04) | Monitoring is a constrained input. | Stakeholder-constrained | Monitoring |
| COV-069 / REL-COV-069 | Datadog monitoring (OP-038) | Alert thresholds/criteria (REQ-Art10-05) | Threshold ownership is unstated. | Stakeholder-constrained | Monitoring |
| COV-070 / REL-COV-070 | Datadog alerts and phones (OP-038) | Automatic alerting of response staff (REQ-Art10-06) | Automatic alerts are directly evidenced. | Directly performed | Monitoring |
| COV-071 / REL-COV-071 | Datadog monitoring (OP-038) | Resources for monitoring activity/anomalies/incidents (REQ-Art10-07) | Resource allocation is unstated. | Stakeholder-constrained | Monitoring |

### Continuity, recovery, learning, and communication

| COV / Relation | Operational endpoint and evidence | Legal endpoint | Evidence-backed effect | Ownership | Stream |
|---|---|---|---|---|---|
| COV-072 / REL-COV-072 | Stakeholder Team accountability (OP-048) | ICT business-continuity policy (REQ-Art11-01) | Team technology accountability is constrained by policy. | Stakeholder-constrained | Continuity |
| COV-073 / REL-COV-073 | Stakeholder Team accountability (OP-048) | Documented continuity arrangements (REQ-Art11-02) | Plan/procedure ownership is unstated. | Stakeholder-constrained | Continuity |
| COV-074 / REL-COV-074 | Service-outage impact (OP-036, CON-006) | Continuity of critical functions (REQ-Art11-03) | Stated service impact is a continuity input. | Stakeholder-constrained | Continuity |
| COV-075 / REL-COV-075 | SingleStore recovery (OP-037, CON-007) | Prompt incident response/resolution (REQ-Art11-04) | Response and remediation are directly performed. | Directly performed | Incident recovery |
| COV-076 / REL-COV-076 | SingleStore recovery (OP-037) | Resumption/recovery priority (REQ-Art11-05) | Recovery is directly performed. | Directly performed | Incident recovery |
| COV-077 / REL-COV-077 | SingleStore recovery (OP-037) | Containment plans (REQ-Art11-06) | Containment-plan ownership is unstated. | Stakeholder-constrained | Incident recovery |
| COV-078 / REL-COV-078 | Technology-native recovery tools (OP-042) | Tailored recovery procedures (REQ-Art11-07) | Recovery-tool use is directly performed. | Directly performed | Incident recovery |
| COV-079 / REL-COV-079 | Service-outage impact (OP-036) | Estimate impacts/damage/losses (REQ-Art11-08) | Outage evidence is a constrained input. | Stakeholder-constrained | Continuity |
| COV-080 / REL-COV-080 | Post-incident report (OP-043) | Crisis communications/authority reporting (REQ-Art11-09) | Report goes to support; formal reporting is external. | Externally owned | Continuity |
| COV-081 / REL-COV-081 | SingleStore recovery (OP-037) | Response and recovery plans (REQ-Art11-10) | Recovery is constrained by plan ownership. | Stakeholder-constrained | Continuity |
| COV-082 / REL-COV-082 | Change review (OP-050) | Independent audit of recovery plans (REQ-Art11-11) | Independent audit is external. | Externally owned | Continuity |
| COV-083 / REL-COV-083 | Non-production testing (OP-016) | Maintain/test continuity plans (REQ-Art11-12) | Testing is not evidenced as continuity-plan testing. | Stakeholder-constrained | Continuity |
| COV-084 / REL-COV-084 | Service-outage impact (OP-036) | Business-impact analysis (REQ-Art11-13) | Incident impact is a constrained input. | Stakeholder-constrained | Continuity |
| COV-085 / REL-COV-085 | Service-outage impact (OP-036) | Severe-disruption impact assessment (REQ-Art11-14) | Incident impact is a constrained input. | Stakeholder-constrained | Continuity |
| COV-086 / REL-COV-086 | Platform/team/provider dependencies (OP-031, OP-032, OP-033; provider confirmation) | BIA dependencies/interdependencies (REQ-Art11-15) | Dependencies are explicitly stated. | Stakeholder-constrained | Third-party dependency |
| COV-087 / REL-COV-087 | Compute dependency (OP-031) | BIA-aligned redundancy (REQ-Art11-16) | Redundancy design depends on compute team. | Stakeholder-constrained | Continuity |
| COV-088 / REL-COV-088 | Non-production testing (OP-016) | Annual/post-change plan testing (REQ-Art11-17) | Test frequency/scope is unstated. | Stakeholder-constrained | Continuity |
| COV-089 / REL-COV-089 | Support handoff report (OP-043) | Crisis-communication testing (REQ-Art11-18) | Crisis communication testing is external. | Externally owned | Continuity |
| COV-090 / REL-COV-090 | Ranger backup/testing (OP-013, OP-016) | Cyber/switchover/backup scenario tests (REQ-Art11-19) | Backup and testing are stated; scenario scope is unstated. | Stakeholder-constrained | Continuity |
| COV-091 / REL-COV-091 | Change review (OP-050) | Review continuity/recovery plans (REQ-Art11-20) | Review is not identified as plan review. | Stakeholder-constrained | Continuity |
| COV-092 / REL-COV-092 | Incident participants (OP-039, OP-040, OP-041) | Crisis-management function (REQ-Art11-21) | Participants exist; formal function ownership is external. | Externally owned | Continuity |
| COV-093 / REL-COV-093 | Post-incident report (OP-043) | Disruption-event activity records (REQ-Art11-22) | Report provides a constrained record input. | Stakeholder-constrained | Incident recovery |
| COV-094 / REL-COV-094 | Service-outage impact/report (OP-036, OP-043) | Annual costs/losses report (REQ-Art11-23) | Cost/loss calculation and authority reporting are external. | Externally owned | Continuity |
| COV-095 / REL-COV-095 | Ranger backup (OP-013) | Minimal downtime/disruption/loss recovery (REQ-Art12-01) | Backup is a constrained recovery input. | Stakeholder-constrained | Recovery |
| COV-096 / REL-COV-096 | Ranger backup (OP-013) | Backup scope/frequency (REQ-Art12-02) | Backup is directly performed; policy scope/frequency is unstated. | Directly performed | Recovery |
| COV-097 / REL-COV-097 | SingleStore recovery (OP-037) | Restoration/recovery procedures (REQ-Art12-03) | Recovery is directly performed. | Directly performed | Recovery |
| COV-098 / REL-COV-098 | Ranger backup (OP-013) | Activatable backup systems (REQ-Art12-04) | Activation capability is unstated. | Stakeholder-constrained | Recovery |
| COV-099 / REL-COV-099 | Secret handling (OP-022) | Secure backup activation/data protection (REQ-Art12-05) | Secret work is constrained by protection duty. | Stakeholder-constrained | Recovery |
| COV-100 / REL-COV-100 | Non-production testing (OP-016) | Periodic backup/recovery tests (REQ-Art12-06) | Tests are not identified as backup/recovery tests. | Stakeholder-constrained | Recovery |
| COV-101 / REL-COV-101 | Compute dependency (OP-031) | Segregated restoration systems (REQ-Art12-07) | Restoration-environment design is external. | Stakeholder-constrained | Recovery |
| COV-102 / REL-COV-102 | Azure Key Vault secrets (OP-022) | Secure restoration environment (REQ-Art12-08) | Secret handling is constrained by this duty. | Stakeholder-constrained | Recovery |
| COV-103 / REL-COV-103 | SingleStore recovery (OP-037) | Timely backup-based restoration (REQ-Art12-09) | Timely recovery is directly performed. | Directly performed | Recovery |
| COV-104 / REL-COV-104 | Compute dependency (OP-031) | Adequate redundant ICT capacity (REQ-Art12-10) | Capacity depends on compute team. | Stakeholder-constrained | Recovery |
| COV-106 / REL-COV-106 | Service-outage impact (OP-036) | Criticality-based RTO/RPO (REQ-Art12-12) | Outage impact is a constrained input. | Stakeholder-constrained | Recovery |
| COV-107 / REL-COV-107 | Service-outage impact (OP-036) | Extreme-scenario service levels (REQ-Art12-13) | Service levels are not owned by the role. | Stakeholder-constrained | Recovery |
| COV-108 / REL-COV-108 | Database connection testing (OP-025) | Recovery integrity checks/reconciliations (REQ-Art12-14) | Query testing is a constrained integrity input. | Stakeholder-constrained | Recovery |
| COV-109 / REL-COV-109 | Database connection testing (OP-025) | External-data reconstruction consistency (REQ-Art12-15) | External-data reconstruction is not evidenced. | Stakeholder-constrained | Recovery |
| COV-110 / REL-COV-110 | Datadog monitoring/service-outage impact (OP-036, OP-038) | Gather incident information and analyse impact (REQ-Art13-01) | Monitoring and outage evidence are directly available to the role. | Directly performed | Monitoring |
| COV-111 / REL-COV-111 | Post-incident report (OP-043) | Post-major-incident review (REQ-Art13-02) | Report is input; formal review ownership is unstated. | Stakeholder-constrained | Learning |
| COV-112 / REL-COV-112 | Post-incident report and maintenance (OP-007, OP-043) | Identify required improvements after review (REQ-Art13-03) | Evidence is constrained by formal review ownership. | Stakeholder-constrained | Learning |
| COV-113 / REL-COV-113 | Post-incident report (OP-043) | Authority communication of changes (REQ-Art13-04) | Authority communication is external. | Externally owned | Learning |
| COV-114 / REL-COV-114 | Change review (OP-050) | Procedure/action effectiveness review (REQ-Art13-05) | Review is a constrained input. | Stakeholder-constrained | Learning |
| COV-115 / REL-COV-115 | Datadog alerts (OP-038) | Review response promptness/severity (REQ-Art13-06) | Alert evidence is a constrained input. | Stakeholder-constrained | Learning |
| COV-116 / REL-COV-116 | Cause investigation (OP-037) | Review forensic analysis (REQ-Art13-07) | Cause investigation is a constrained input. | Stakeholder-constrained | Learning |
| COV-117 / REL-COV-117 | Incident participants (OP-039, OP-040) | Review escalation effectiveness (REQ-Art13-08) | Escalation participants are explicit. | Stakeholder-constrained | Learning |
| COV-118 / REL-COV-118 | Post-incident report (OP-043) | Review communication effectiveness (REQ-Art13-09) | Support handoff is a constrained communication input. | Stakeholder-constrained | Learning |
| COV-119 / REL-COV-119 | Change review (OP-050) | Incorporate lessons in risk assessment (REQ-Art13-10) | No integration owner is stated. | Stakeholder-constrained | Learning |
| COV-120 / REL-COV-120 | Technology maintenance (OP-007) | Review framework components (REQ-Art13-11) | Maintenance is constrained by framework review. | Stakeholder-constrained | Learning |
| COV-121 / REL-COV-121 | Stakeholder Team accountability (OP-048) | Monitor strategy effectiveness (REQ-Art13-12) | Strategy monitoring is external. | Externally owned | Learning |
| COV-122 / REL-COV-122 | Datadog monitoring (OP-038) | Map risk evolution/incident patterns (REQ-Art13-13) | Metrics are a constrained input. | Stakeholder-constrained | Learning |
| COV-123 / REL-COV-123 | Team-lead participation (OP-039) | Senior ICT report to management (REQ-Art13-14) | Management reporting is external. | Externally owned | Learning |
| COV-124 / REL-COV-124 | Stakeholder role (OP-001) | Compulsory staff resilience training (REQ-Art13-15) | Role is subject to training; training provision owner unstated. | Stakeholder-constrained | Learning |
| COV-125 / REL-COV-125 | Provider-supported platforms (operator confirmation) | Provider training where appropriate (REQ-Art13-16) | Third-party training is externally owned. | Externally owned | Third-party dependency |
| COV-126 / REL-COV-126 | Technology investigation (OP-007, OP-026) | Monitor technology developments (REQ-Art13-17) | Investigation is a constrained input. | Stakeholder-constrained | Learning |
| COV-127 / REL-COV-127 | Post-incident report (OP-043) | Crisis-communication plan (REQ-Art14-01) | Plan ownership is external. | Externally owned | Communication |
| COV-128 / REL-COV-128 | Service-outage impact/report (OP-036, OP-043) | Responsible incident disclosure (REQ-Art14-02) | Disclosure is external. | Externally owned | Communication |
| COV-129 / REL-COV-129 | Post-incident report (OP-043) | Internal/external communication policy (REQ-Art14-03) | Policy ownership is external. | Externally owned | Communication |
| COV-130 / REL-COV-130 | Incident participants (OP-039, OP-040, OP-041) | Differentiate response/informed staff (REQ-Art14-04) | Participants give a constrained staffing input. | Stakeholder-constrained | Communication |
| COV-131 / REL-COV-131 | Post-incident reporting (OP-043) | Public/media communication owner (REQ-Art14-05) | No responsible person is identified. | Not evidenced / unclear owner | Communication |

### Incident management, classification, and resilience testing

| COV / Relation | Operational endpoint and evidence | Legal endpoint | Evidence-backed effect | Ownership | Stream |
|---|---|---|---|---|---|
| COV-132 / REL-COV-132 | SingleStore recovery (OP-037) | Incident-management process (REQ-Art17-01) | Recovery is constrained by process ownership. | Stakeholder-constrained | Incident management |
| COV-133 / REL-COV-133 | Recovery/monitoring (OP-037, OP-038) | Detect, manage, notify incidents (REQ-Art17-02) | Detection/recovery are explicit; notification owner unstated. | Stakeholder-constrained | Incident management |
| COV-134 / REL-COV-134 | ServiceNow incidents/report records (OP-029, OP-043) | Record incidents/cyber threats (REQ-Art17-03) | Records are a constrained input. | Stakeholder-constrained | Incident management |
| COV-135 / REL-COV-135 | Recovery investigation (OP-037) | Integrated incident monitoring/handling/follow-up (REQ-Art17-04) | Activity is constrained by broader process ownership. | Stakeholder-constrained | Incident management |
| COV-136 / REL-COV-136 | Recovery investigation (OP-037) | Identify/document/address root causes (REQ-Art17-05) | Cause investigation and mitigation are directly performed. | Directly performed | Incident management |
| COV-137 / REL-COV-137 | Datadog alerts (OP-038) | Early-warning indicators (REQ-Art17-06) | Early alerts are directly evidenced. | Directly performed | Incident management |
| COV-138 / REL-COV-138 | ServiceNow/report records (OP-029, OP-043) | Track/log/categorise/classify incidents (REQ-Art17-07) | Classification ownership is unstated. | Stakeholder-constrained | Incident management |
| COV-139 / REL-COV-139 | Incident participants (OP-039, OP-040, OP-041) | Incident roles/responsibilities (REQ-Art17-08) | Formal assignment is externally owned. | Externally owned | Incident management |
| COV-140 / REL-COV-140 | Report handoff/escalation (OP-039, OP-040, OP-043) | Communication/escalation procedures (REQ-Art17-09) | Handoffs are a constrained input. | Stakeholder-constrained | Incident management |
| COV-141 / REL-COV-141 | Team-lead participation (OP-039) | Major-incident reporting to management (REQ-Art17-10) | Management reporting is external. | Externally owned | Incident management |
| COV-142 / REL-COV-142 | SingleStore recovery (OP-037) | Mitigate impact/restore secure services (REQ-Art17-11) | Recovery is directly performed. | Directly performed | Incident management |
| COV-143 / REL-COV-143 | Service-outage evidence (OP-036) | Incident classification/impact determination (REQ-Art18-01) | Outage evidence is a constrained input. | Stakeholder-constrained | Incident classification |
| COV-144 / REL-COV-144 | Front-facing outage impact (OP-036) | Affected clients/counterparts criterion (REQ-Art18-02) | Client/counterpart classification is external. | Stakeholder-constrained | Incident classification |
| COV-145 / REL-COV-145 | Front-facing outage impact (OP-036) | Affected-transactions criterion (REQ-Art18-03) | Transaction classification is external. | Stakeholder-constrained | Incident classification |
| COV-146 / REL-COV-146 | Front-facing outage impact (OP-036) | Reputational-impact criterion (REQ-Art18-04) | Reputation assessment is external. | Stakeholder-constrained | Incident classification |
| COV-147 / REL-COV-147 | Service outage (OP-036) | Duration/downtime criterion (REQ-Art18-05) | Service impact is a constrained input. | Stakeholder-constrained | Incident classification |
| COV-148 / REL-COV-148 | Service outage (OP-036) | Geographical-spread criterion (REQ-Art18-06) | Geographical assessment is external. | Stakeholder-constrained | Incident classification |
| COV-149 / REL-COV-149 | Sensitive-data handling (OP-024) | Data-loss criterion (REQ-Art18-07) | Data-loss classification is external. | Stakeholder-constrained | Incident classification |
| COV-150 / REL-COV-150 | Service outage (OP-036) | Critical-service criterion (REQ-Art18-08) | Service impact is a constrained input. | Stakeholder-constrained | Incident classification |
| COV-151 / REL-COV-151 | Service outage (OP-036) | Economic-impact criterion (REQ-Art18-09) | Economic calculation is external. | Stakeholder-constrained | Incident classification |
| COV-152 / REL-COV-152 | Datadog monitoring (OP-038) | Significant-threat classification (REQ-Art18-10) | Threat classification is external. | Stakeholder-constrained | Incident classification |
| COV-153 / REL-COV-153 | Non-production testing (OP-016) | Maintain/review testing programme (REQ-Art24-01) | Programme ownership is unstated. | Stakeholder-constrained | Resilience testing |
| COV-154 / REL-COV-154 | Non-production record-visibility gap (OP-058, CON-011) | Identify resilience weaknesses/gaps (REQ-Art24-02) | The stated visibility gap is a constrained test-governance signal. | Stakeholder-constrained | Resilience testing |
| COV-155 / REL-COV-155 | Non-production testing (OP-016) | Range of test types (REQ-Art24-03) | Testing is directly performed. | Directly performed | Resilience testing |
| COV-156 / REL-COV-156 | Non-production testing (OP-016) | Risk-based test approach (REQ-Art24-04) | Risk approach is not evidenced. | Stakeholder-constrained | Resilience testing |
| COV-157 / REL-COV-157 | DevOps validation test (OP-051) | Independent test parties (REQ-Art24-05) | Independence is not evidenced. | Stakeholder-constrained | Resilience testing |
| COV-158 / REL-COV-158 | DevOps validation test (OP-051) | Internal-test resources/conflict avoidance (REQ-Art24-06) | Resource/conflict controls are not evidenced. | Stakeholder-constrained | Resilience testing |
| COV-159 / REL-COV-159 | Non-production record-visibility gap (OP-058, CON-011) | Remedy/validate test findings (REQ-Art24-07) | Visibility gap is a constrained test-governance signal. | Stakeholder-constrained | Resilience testing |
| COV-160 / REL-COV-160 | Non-production testing (OP-016) | Annual critical-system tests (REQ-Art24-08) | Frequency/criticality scope is not evidenced. | Stakeholder-constrained | Resilience testing |
| COV-161 / REL-COV-161 | Non-production testing (OP-016) | Appropriate test execution (REQ-Art25-01) | Testing is directly performed. | Directly performed | Resilience testing |
| COV-162 / REL-COV-162 | Starburst connectivity validation (OP-019) | Compatibility/performance/end-to-end testing (REQ-Art25-02) | Connectivity validation is directly performed. | Directly performed | Resilience testing |
| COV-163 / REL-COV-163 | Database connection testing (OP-025) | Assessment/scan/review/scenario test methods (REQ-Art25-03) | Test-method selection is constrained by the programme. | Stakeholder-constrained | Resilience testing |

### Conditional provisions resolved outside active stakeholder coverage

| Requirement | Resolution | Evidence |
|---|---|---|
| REQ-Art12-11 | Not active: the microenterprise alternative in Art. 12(4) does not apply. | Operator: Bank is not a microenterprise. |
| REQ-Art25-04 | Not active: CSD/CCP-specific deployment rule is outside Bank's confirmed credit-institution class. | Operator: Bank is a credit institution. |
| REQ-Art25-05 | Not active: microenterprise strategic testing alternative does not apply. | Operator: Bank is not a microenterprise. |

## Operational Context Coverage

These source items have no defensible direct regulatory edge. They remain in role-specific context streams and retain their approved operational relationships; no regulatory relationship is invented from co-occurrence.

| Context ID | Operational source | Named context stream | Evidence |
|---|---|---|---|
| COV-CTX-001 | Kafka colleague assistance (OP-010) | Cross-platform colleague support | OP-010 |
| COV-CTX-002 | Cosmos colleague assistance (OP-011) | Cross-platform colleague support | OP-011 |
| COV-CTX-003 | Databricks colleague assistance (OP-012) | Cross-platform colleague support | OP-012 |
| COV-CTX-004 | LLM log parsing/information search (OP-026) | Investigation tooling | OP-026 |
| COV-CTX-005 | Unknown DevOps-consumed output (OP-035) | Cross-team output visibility | OP-035 |
| COV-CTX-006 | Monotonous daily work (OP-055) | Work-pattern context | OP-055 |
| COV-CTX-007 | Unknown DevOps-output gap (OP-057) | Cross-team output visibility | OP-057 |
| COV-CTX-008 | Monotonous-work concern (CON-008) | Work-pattern context | CON-008 / OP-055 |
| COV-CTX-009 | Unknown DevOps-output concern (CON-010) | Cross-team output visibility | CON-010 / OP-057 |
| COV-CTX-010 | Emergency change and subsequent report (OP-049) | Emergency-change context | OP-049 |
| COV-CTX-011 | Connection dependency blockage (OP-053, CON-004) | Cross-team dependency context | OP-053 / CON-004 |

## Uncovered Register

No unresolved source or active requirement remains. The outsourcing-verification owner is explicitly recorded as `Not evidenced / unclear owner` in COV-026; it is not assigned to the stakeholder. The three conditional records above are not active for Bank based on operator-confirmed legal classification.

## Stakeholder Legal-Role Placement Ledger

| Relationship ID | Source → Target | Meaning | ArchiMate relation | Evidence | Approval |
|---|---|---|---|---|---|
| REL-ROLE-001 | Infrastructure Engineer / Cloud DB Admin → Bank | Works within the employing organization | Association | Operator approved `Bank` as the anonymized employing-organization label. | Approved |
| REL-ROLE-002 | Bank → DORA-regulated financial entity | Is a DORA-regulated credit institution | Specialization | Operator confirmed non-micro credit-institution status; original context confirmed DORA applicability. | Approved |

**Validated element types:** Infrastructure Engineer / Cloud DB Admin — Business Role; Bank — Business Actor; DORA-regulated financial entity — Business Actor class. The stakeholder is not equated with the regulated entity.

## Approval Record

- Requirement register and Article 5 omission: approved by operator.
- Legal-index generation and canonical anchors: approved by operator.
- Corrected Article 6 anchor mapping: approved by operator.
- Coverage and relationship ledger: approved by operator.
- Stakeholder legal-role placement: approved by operator.
