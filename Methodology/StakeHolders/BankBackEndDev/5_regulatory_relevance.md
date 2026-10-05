# DORA Regulatory Relevance Analysis

**Stakeholder:** Back-end Developer  
**Employing organisation:** Employer Bank (unnamed; operator-confirmed credit institution)  
**Target regulation:** Regulation (EU) 2022/2554 (DORA)  
**Status:** Approved Step 5 output; this is an evidence-backed relevance and coverage record, not a compliance assessment.

## Legal Index Provenance

| Field | Recorded value |
| --- | --- |
| Regulation / CELEX | DORA / `32022R2554` |
| Matrix selector | `DORA` |
| Generated legal index | `TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx` |
| Generation timestamp | 2026-09-11 21:14:32 +0100 |
| Validation | `row-id --row 1` returned `Chap.I`; workbook schema and law/CELEX identity validated. |
| Anchor resolution | Every approved direct Enacting Terms path was verified using `traceability_lookup.py verify-anchor`. No recital or amendment provision is an anchor. |

## Consensus Result

The three independent DORA evaluators unanimously retained Articles 7–13, 17, 24 and 25 after structured debate. Article 28 was then explicitly added by operator direction because Microsoft provides relevant cloud services and a Microsoft contract exists. The employer is a non-micro credit institution and the platform supports DORA critical or important functions.

| Article | Result | Operational chain |
| --- | --- | --- |
| 7–13 | Included | System maintenance, data flows, access, release controls, monitoring, incident/recovery evidence and platform critical-function impact. |
| 17 | Included | Datadog detection, Monitoring Team escalation, remediation and recovery chain. |
| 24–25 | Included | Developer testing, pull-request validation and critical-function service impact. |
| 28 | Included by operator direction | Microsoft Azure/Cosmos DB/Kubernetes provision, cloud dependency and confirmed contract. |
| 6, 14, 18, 19 | Omitted from stakeholder scope | No recorded framework participation, crisis communication duty, formal incident classification, or competent-authority reporting handoff. |

## Atomic Requirement Register

Each requirement below preserves its approved direct legal-text anchor(s). Repeated anchors mean that the source provision contains several distinct atomic obligations.

### Article 7

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art7-01 | Appropriate ICT systems | Art. 7 | `Chap.II, Section II, Art.7, Paragraph 1, Point a` |
| REQ-Art7-02 | Reliable ICT systems | Art. 7 | `Chap.II, Section II, Art.7, Paragraph 1, Point b` |
| REQ-Art7-03 | Sufficient processing capacity | Art. 7 | `Chap.II, Section II, Art.7, Paragraph 1, Point c` |
| REQ-Art7-04 | Technological resilience | Art. 7 | `Chap.II, Section II, Art.7, Paragraph 1, Point d` |
### Article 8

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art8-01 | Identify and classify functions | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 1` |
| REQ-Art8-02 | Document roles and responsibilities | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 1` |
| REQ-Art8-03 | Document information and ICT assets | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 1` |
| REQ-Art8-04 | Review classification and documentation | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 1` |
| REQ-Art8-05 | Identify ICT risk sources | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 2` |
| REQ-Art8-06 | Assess threats and risk scenarios | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 2` |
| REQ-Art8-07 | Assess major ICT changes | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 3` |
| REQ-Art8-08 | Map assets and interdependencies | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 4` |
| REQ-Art8-09 | Document third-party dependencies | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 5` |
| REQ-Art8-10 | Maintain and update inventories | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 6` |
| REQ-Art8-11 | Assess legacy and connected systems | Art. 8 | `Chap.II, Section II, Art.8, Paragraph 7` |
### Article 9

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art9-01 | Monitor ICT security and functioning | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 1` |
| REQ-Art9-02 | Deploy ICT security controls | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 1` |
| REQ-Art9-03 | Design resilience controls | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 2` |
| REQ-Art9-04 | Design continuity controls | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 2` |
| REQ-Art9-05 | Design availability controls | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 2` |
| REQ-Art9-06 | Protect data confidentiality and integrity | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 2` |
| REQ-Art9-07 | Secure data transfer | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 3, Point a` |
| REQ-Art9-08 | Prevent corruption and unauthorised access | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 3, Point b` |
| REQ-Art9-09 | Prevent availability and integrity loss | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 3, Point c` |
| REQ-Art9-10 | Protect data from management risks | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 3, Point d` |
| REQ-Art9-11 | Document information security policy | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point a` |
| REQ-Art9-12 | Manage and segment networks | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point b`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1` |
| REQ-Art9-13 | Limit logical and physical access | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point c` |
| REQ-Art9-14 | Use strong authentication and cryptography | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point d` |
| REQ-Art9-15 | Maintain controlled change management | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| REQ-Art9-16 | Record changes | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| REQ-Art9-17 | Test and assess changes | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| REQ-Art9-18 | Approve, implement and verify changes | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point e` |
| REQ-Art9-19 | Document patch and update controls | Art. 9 | `Chap.II, Section II, Art.9, Paragraph 4, Point f`<br>`Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2` |
### Article 10

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art10-01 | Detect anomalies and performance issues | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 1` |
| REQ-Art10-02 | Identify material single points of failure | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 1` |
| REQ-Art10-03 | Test detection mechanisms | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1` |
| REQ-Art10-04 | Use control layers and alert thresholds | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 2` |
| REQ-Art10-05 | Trigger and notify incident responders | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 2` |
| REQ-Art10-06 | Resource continuous anomaly monitoring | Art. 10 | `Chap.II, Section II, Art.10, Paragraph 3` |
### Article 11

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art11-01 | Maintain ICT business-continuity policy | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 1` |
| REQ-Art11-02 | Ensure critical-function continuity | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 2, Point a` |
| REQ-Art11-03 | Respond to and resolve incidents | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 2, Point b` |
| REQ-Art11-04 | Activate containment and recovery plans | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 2, Point c` |
| REQ-Art11-05 | Estimate disruption impacts and losses | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 2, Point d` |
| REQ-Art11-06 | Provide crisis communications and reporting | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 2, Point e` |
| REQ-Art11-07 | Maintain audited response and recovery plans | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 3` |
| REQ-Art11-08 | Maintain continuity plans | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 4` |
| REQ-Art11-09 | Test plans for outsourced critical functions | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 4` |
| REQ-Art11-10 | Conduct a business-impact analysis | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 5` |
| REQ-Art11-11 | Assess critical functions | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 5` |
| REQ-Art11-12 | Assess dependencies and information assets | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 5` |
| REQ-Art11-13 | Align ICT assets and redundancy to BIA | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 5` |
| REQ-Art11-14 | Test plans at least annually | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 6, Point a` |
| REQ-Art11-15 | Test after substantive critical-system change | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 6, Point a` |
| REQ-Art11-16 | Test crisis communications | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 6, Point b` |
| REQ-Art11-17 | Test cyberattack and switchover scenarios | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1` |
| REQ-Art11-18 | Review plans from testing and assurance | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2` |
| REQ-Art11-19 | Operate a crisis-management function | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 7` |
| REQ-Art11-20 | Keep disruption-event records | Art. 11 | `Chap.II, Section II, Art.11, Paragraph 8` |
### Article 12

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art12-01 | Document backup policy | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 1, Point a` |
| REQ-Art12-02 | Set backup scope and frequency | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 1, Point a` |
| REQ-Art12-03 | Document restoration and recovery methods | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 1, Point b` |
| REQ-Art12-04 | Activate backup systems | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 2` |
| REQ-Art12-05 | Protect security and data qualities during backup | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 2` |
| REQ-Art12-06 | Periodically test backup and restoration | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 2` |
| REQ-Art12-07 | Segregate and protect restoration systems | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 3` |
| REQ-Art12-08 | Restore services in a timely way | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 3` |
| REQ-Art12-09 | Maintain adequate redundant capacity | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 4` |
| REQ-Art12-10 | Set recovery-time objectives | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 6` |
| REQ-Art12-11 | Set recovery-point objectives | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 6` |
| REQ-Art12-12 | Check and reconcile recovered data | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 7` |
| REQ-Art12-13 | Check externally reconstructed data | Art. 12 | `Chap.II, Section II, Art.12, Paragraph 7` |
### Article 13

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art13-01 | Gather vulnerability information | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 1` |
| REQ-Art13-02 | Gather cyber-threat information | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 1` |
| REQ-Art13-03 | Gather ICT-incident information | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 1` |
| REQ-Art13-04 | Analyse resilience impacts | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 1` |
| REQ-Art13-05 | Review disruptive major incidents | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2` |
| REQ-Art13-06 | Identify causes and ICT improvements | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2` |
| REQ-Art13-07 | Communicate review changes when requested | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1` |
| REQ-Art13-08 | Evaluate procedure and action effectiveness | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2` |
| REQ-Art13-09 | Review response to security alerts | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a` |
| REQ-Art13-10 | Review forensic-analysis quality | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b` |
| REQ-Art13-11 | Review incident escalation | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c` |
| REQ-Art13-12 | Review internal and external communications | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d` |
| REQ-Art13-13 | Incorporate lessons in ICT risk assessment | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 3` |
| REQ-Art13-14 | Review ICT risk-management components | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 3` |
| REQ-Art13-15 | Monitor resilience strategy and ICT-risk evolution | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 4` |
| REQ-Art13-16 | Report lessons and recommendations to management | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 5` |
| REQ-Art13-17 | Provide mandatory awareness and resilience training | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 6` |
| REQ-Art13-18 | Monitor relevant technology developments | Art. 13 | `Chap.II, Section II, Art.13, Paragraph 7` |
### Article 17

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art17-01 | Establish an incident-management process | Art. 17 | `Chap.III, Art.17, Paragraph 1` |
| REQ-Art17-02 | Record incidents and significant cyber threats | Art. 17 | `Chap.III, Art.17, Paragraph 2` |
| REQ-Art17-03 | Integrate monitoring, handling, follow-up and root-cause treatment | Art. 17 | `Chap.III, Art.17, Paragraph 2` |
| REQ-Art17-04 | Use early-warning indicators | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point a` |
| REQ-Art17-05 | Identify, log, categorise and classify incidents | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point b` |
| REQ-Art17-06 | Assign incident roles and responsibilities | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point c` |
| REQ-Art17-07 | Plan communications and escalation | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point d` |
| REQ-Art17-08 | Report major incidents to management | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point e` |
| REQ-Art17-09 | Mitigate incident impacts | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point f` |
| REQ-Art17-10 | Restore secure services promptly | Art. 17 | `Chap.III, Art.17, Paragraph 3, Point f` |
### Article 24

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art24-01 | Establish a resilience-testing programme | Art. 24 | `Chap.IV, Art.24, Paragraph 1` |
| REQ-Art24-02 | Identify weaknesses and implement corrections | Art. 24 | `Chap.IV, Art.24, Paragraph 1` |
| REQ-Art24-03 | Maintain and review the programme | Art. 24 | `Chap.IV, Art.24, Paragraph 1` |
| REQ-Art24-04 | Use a range of tests and methods | Art. 24 | `Chap.IV, Art.24, Paragraph 2` |
| REQ-Art24-05 | Apply a risk-based testing approach | Art. 24 | `Chap.IV, Art.24, Paragraph 3` |
| REQ-Art24-06 | Use independent testers and avoid conflicts | Art. 24 | `Chap.IV, Art.24, Paragraph 4` |
| REQ-Art24-07 | Prioritise and remedy test findings | Art. 24 | `Chap.IV, Art.24, Paragraph 5` |
| REQ-Art24-08 | Test critical-function ICT annually | Art. 24 | `Chap.IV, Art.24, Paragraph 6` |
### Article 25

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art25-01 | Perform vulnerability assessments and scans | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-02 | Perform open-source analyses | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-03 | Perform network-security assessments | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-04 | Perform gap analyses | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-05 | Perform physical-security reviews | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-06 | Use questionnaires and scanning tools | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-07 | Perform feasible source-code reviews | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-08 | Perform scenario-based tests | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-09 | Perform compatibility tests | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-10 | Perform performance tests | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-11 | Perform end-to-end tests | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
| REQ-Art25-12 | Perform penetration tests | Art. 25 | `Chap.IV, Art.25, Paragraph 1` |
### Article 28

| Requirement | Atomic duty | Citation | Direct legal-text IDs |
| --- | --- | --- | --- |
| REQ-Art28-01 | Manage ICT third-party risk within ICT risk management | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 1` |
| REQ-Art28-02 | Retain responsibility for DORA compliance | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 1, Point a` |
| REQ-Art28-03 | Apply proportional third-party risk management | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 1, Point b` |
| REQ-Art28-04 | Assess ICT-related dependencies | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point i` |
| REQ-Art28-05 | Assess contractual critical-function risk | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 1, Point b, Sub-Point ii` |
| REQ-Art28-06 | Maintain third-party risk strategy and policy | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 2` |
| REQ-Art28-07 | Have management review third-party risks | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 2` |
| REQ-Art28-08 | Maintain a third-party contract register | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 3` |
| REQ-Art28-09 | Document and classify contractual arrangements | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 1` |
| REQ-Art28-10 | Report annual arrangement information | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 2` |
| REQ-Art28-11 | Provide the register to competent authorities | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 3` |
| REQ-Art28-12 | Notify planned critical arrangements | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 3, Sub-Paragraph 4` |
| REQ-Art28-13 | Assess whether a service supports a critical function | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 4, Point a` |
| REQ-Art28-14 | Assess supervisory contracting conditions | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 4, Point b` |
| REQ-Art28-15 | Assess contractual and concentration risks | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 4, Point c` |
| REQ-Art28-16 | Perform provider due diligence | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 4, Point d` |
| REQ-Art28-17 | Assess contractual conflicts of interest | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 4, Point e` |
| REQ-Art28-18 | Use providers meeting security standards | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 5` |
| REQ-Art28-19 | Plan risk-based provider audits | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 6` |
| REQ-Art28-20 | Use suitably skilled auditors | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 6, Sub-Paragraph 1` |
| REQ-Art28-21 | Provide contractual termination rights | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 7` |
| REQ-Art28-22 | Terminate for significant breach | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 7, Point a` |
| REQ-Art28-23 | Terminate for material risk changes | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 7, Point b` |
| REQ-Art28-24 | Terminate for provider ICT-risk weaknesses | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 7, Point c` |
| REQ-Art28-25 | Terminate where supervision is impaired | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 7, Point d` |
| REQ-Art28-26 | Maintain critical-function exit strategies | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8` |
| REQ-Art28-27 | Exit without business disruption | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point a` |
| REQ-Art28-28 | Exit without limiting regulatory compliance | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point b` |
| REQ-Art28-29 | Exit without harming client-service continuity | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 1, Point c` |
| REQ-Art28-30 | Document, test and review exit plans | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 2` |
| REQ-Art28-31 | Prepare alternative solutions and transition plans | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 3` |
| REQ-Art28-32 | Maintain exit contingency measures | Art. 28 | `Chap.V, Section I, Art.28, Paragraph 8, Sub-Paragraph 4` |

## Footprint-Regulation Coverage Ledger

Every approved `COV-*` record has one requirement, named operational endpoint, approved legal anchor(s) from the register, effect, ownership state, and stream. This ledger does not infer a missing owner or state that entity controls are implemented.

| Coverage ID | Operational source(s) | REQ / citation | Named endpoint and evidence-backed effect | Ownership state | Stream |
| --- | --- | --- | --- | --- | --- |
| COV-001 | OP-004, OP-038 | REQ-Art7-01 / Art. 7 | Framework Maintenance realizes REQ-Art7-01 | Directly performed | ICT Systems & Asset Governance |
| COV-002 | OP-004, OP-038 | REQ-Art7-02 / Art. 7 | Framework Maintenance realizes REQ-Art7-02 | Directly performed | ICT Systems & Asset Governance |
| COV-003 | OP-050, OP-060, CON-006 | REQ-Art7-03 / Art. 7 | Platform Development is constrained by REQ-Art7-03 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-004 | OP-050, OP-060, CON-006 | REQ-Art7-04 / Art. 7 | Platform Development is constrained by REQ-Art7-04 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-005 | OP-006, OP-018–019, OP-066, OP-081–082 | REQ-Art8-01 / Art. 8 | Platform Development is constrained by REQ-Art8-01 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-006 | OP-006, OP-018–019, OP-066, OP-081–082 | REQ-Art8-02 / Art. 8 | Platform Development is constrained by REQ-Art8-02 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-007 | OP-006, OP-018–019, OP-066, OP-081–082 | REQ-Art8-03 / Art. 8 | Platform Development is constrained by REQ-Art8-03 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-008 | OP-038, OP-041–042, OP-052, CON-001 | REQ-Art8-04 / Art. 8 | Service Update is constrained by REQ-Art8-04 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-009 | OP-038, OP-041–042, OP-052, CON-001 | REQ-Art8-05 / Art. 8 | Service Update is constrained by REQ-Art8-05 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-010 | OP-038, OP-041–042, OP-052, CON-001 | REQ-Art8-06 / Art. 8 | Service Update is constrained by REQ-Art8-06 | Stakeholder-constrained | ICT Systems & Asset Governance |
| COV-011 | OP-023–026, OP-027–029, OP-068 | REQ-Art8-07 / Art. 8 | Enterprise Data Platform is subject to REQ-Art8-07 | Not evidenced / unclear owner | ICT Systems & Asset Governance |
| COV-012 | OP-023–026, OP-027–029, OP-068 | REQ-Art8-08 / Art. 8 | Enterprise Data Platform is subject to REQ-Art8-08 | Not evidenced / unclear owner | ICT Systems & Asset Governance |
| COV-013 | OP-023–026, OP-027–029, OP-068 | REQ-Art8-09 / Art. 8 | Enterprise Data Platform is subject to REQ-Art8-09 | Not evidenced / unclear owner | ICT Systems & Asset Governance |
| COV-014 | OP-023–026, OP-027–029, OP-068 | REQ-Art8-10 / Art. 8 | Enterprise Data Platform is subject to REQ-Art8-10 | Not evidenced / unclear owner | ICT Systems & Asset Governance |
| COV-015 | OP-023–026, OP-027–029, OP-068 | REQ-Art8-11 / Art. 8 | Enterprise Data Platform is subject to REQ-Art8-11 | Not evidenced / unclear owner | ICT Systems & Asset Governance |
| COV-016 | OP-006, OP-048, OP-065, OP-081 | REQ-Art9-01 / Art. 9 | Data Offload Flow is constrained by REQ-Art9-01 | Stakeholder-constrained | Protection & Controlled Change |
| COV-017 | OP-006, OP-048, OP-065, OP-081 | REQ-Art9-02 / Art. 9 | Data Offload Flow is constrained by REQ-Art9-02 | Stakeholder-constrained | Protection & Controlled Change |
| COV-018 | OP-006, OP-048, OP-065, OP-081 | REQ-Art9-03 / Art. 9 | Data Offload Flow is constrained by REQ-Art9-03 | Stakeholder-constrained | Protection & Controlled Change |
| COV-019 | OP-006, OP-048, OP-065, OP-081 | REQ-Art9-04 / Art. 9 | Data Offload Flow is constrained by REQ-Art9-04 | Stakeholder-constrained | Protection & Controlled Change |
| COV-020 | OP-031–036, OP-088 | REQ-Art9-05 / Art. 9 | Enterprise Data Platform is subject to REQ-Art9-05 | Not evidenced / unclear owner | Protection & Controlled Change |
| COV-021 | OP-031–036, OP-088 | REQ-Art9-06 / Art. 9 | Enterprise Data Platform is subject to REQ-Art9-06 | Not evidenced / unclear owner | Protection & Controlled Change |
| COV-022 | OP-031–036, OP-088 | REQ-Art9-07 / Art. 9 | Enterprise Data Platform is subject to REQ-Art9-07 | Not evidenced / unclear owner | Protection & Controlled Change |
| COV-023 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | REQ-Art9-08 / Art. 9 | Azure AD / Internal Service Access realizes part of REQ-Art9-08 | Externally owned | Protection & Controlled Change |
| COV-024 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | REQ-Art9-09 / Art. 9 | Azure AD / Internal Service Access realizes part of REQ-Art9-09 | Externally owned | Protection & Controlled Change |
| COV-025 | OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002 | REQ-Art9-10 / Art. 9 | Azure AD / Internal Service Access realizes part of REQ-Art9-10 | Externally owned | Protection & Controlled Change |
| COV-026 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | REQ-Art9-11 / Art. 9 | Test and DEV Readiness realizes REQ-Art9-11 | Directly performed | Protection & Controlled Change |
| COV-027 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | REQ-Art9-12 / Art. 9 | Test and DEV Readiness realizes REQ-Art9-12 | Directly performed | Protection & Controlled Change |
| COV-028 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | REQ-Art9-13 / Art. 9 | Test and DEV Readiness realizes REQ-Art9-13 | Directly performed | Protection & Controlled Change |
| COV-029 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | REQ-Art9-14 / Art. 9 | Test and DEV Readiness realizes REQ-Art9-14 | Directly performed | Protection & Controlled Change |
| COV-030 | OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008 | REQ-Art9-15 / Art. 9 | Test and DEV Readiness realizes REQ-Art9-15 | Directly performed | Protection & Controlled Change |
| COV-031 | OP-038, OP-041–042 | REQ-Art9-16 / Art. 9 | Service Update is constrained by REQ-Art9-16 | Stakeholder-constrained | Protection & Controlled Change |
| COV-032 | OP-038, OP-041–042 | REQ-Art9-17 / Art. 9 | Service Update is constrained by REQ-Art9-17 | Stakeholder-constrained | Protection & Controlled Change |
| COV-033 | OP-038, OP-041–042 | REQ-Art9-18 / Art. 9 | Service Update is constrained by REQ-Art9-18 | Stakeholder-constrained | Protection & Controlled Change |
| COV-034 | OP-038, OP-041–042 | REQ-Art9-19 / Art. 9 | Service Update is constrained by REQ-Art9-19 | Stakeholder-constrained | Protection & Controlled Change |
| COV-035 | OP-014, OP-070, OP-072 | REQ-Art10-01 / Art. 10 | Production Monitoring is constrained by REQ-Art10-01 | Stakeholder-constrained | Detection & Continuity |
| COV-036 | OP-014, OP-070, OP-072 | REQ-Art10-02 / Art. 10 | Production Monitoring is constrained by REQ-Art10-02 | Stakeholder-constrained | Detection & Continuity |
| COV-037 | OP-070, OP-072, OP-076 | REQ-Art10-03 / Art. 10 | Incident Escalation realizes part of REQ-Art10-03 | Externally owned | Detection & Continuity |
| COV-038 | OP-070, OP-072, OP-076 | REQ-Art10-04 / Art. 10 | Incident Escalation realizes part of REQ-Art10-04 | Externally owned | Detection & Continuity |
| COV-039 | OP-070, OP-072, OP-076 | REQ-Art10-05 / Art. 10 | Incident Escalation realizes part of REQ-Art10-05 | Externally owned | Detection & Continuity |
| COV-040 | OP-070, OP-072, OP-076 | REQ-Art10-06 / Art. 10 | Incident Escalation realizes part of REQ-Art10-06 | Externally owned | Detection & Continuity |
| COV-041 | OP-060, OP-070–080; operator critical-function clarification | REQ-Art11-01 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-01 | Not evidenced / unclear owner | Detection & Continuity |
| COV-042 | OP-060, OP-070–080; operator critical-function clarification | REQ-Art11-02 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-02 | Not evidenced / unclear owner | Detection & Continuity |
| COV-043 | OP-060, OP-070–080; operator critical-function clarification | REQ-Art11-03 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-03 | Not evidenced / unclear owner | Detection & Continuity |
| COV-044 | OP-060, OP-070–080; operator critical-function clarification | REQ-Art11-04 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-04 | Not evidenced / unclear owner | Detection & Continuity |
| COV-045 | OP-071, OP-073–078 | REQ-Art11-05 / Art. 11 | Software Remediation realizes REQ-Art11-05 | Directly performed | Detection & Continuity |
| COV-046 | OP-071, OP-073–078 | REQ-Art11-06 / Art. 11 | Software Remediation realizes REQ-Art11-06 | Directly performed | Detection & Continuity |
| COV-047 | OP-071, OP-073–078 | REQ-Art11-07 / Art. 11 | Software Remediation realizes REQ-Art11-07 | Directly performed | Detection & Continuity |
| COV-048 | OP-060, OP-071, OP-079–080 | REQ-Art11-08 / Art. 11 | Incident Escalation is subject to REQ-Art11-08 | Not evidenced / unclear owner | Detection & Continuity |
| COV-049 | OP-060, OP-071, OP-079–080 | REQ-Art11-09 / Art. 11 | Incident Escalation is subject to REQ-Art11-09 | Not evidenced / unclear owner | Detection & Continuity |
| COV-050 | OP-060, OP-071, OP-079–080 | REQ-Art11-10 / Art. 11 | Incident Escalation is subject to REQ-Art11-10 | Not evidenced / unclear owner | Detection & Continuity |
| COV-051 | OP-062–063, OP-070–080 | REQ-Art11-11 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-11 | Not evidenced / unclear owner | Detection & Continuity |
| COV-052 | OP-062–063, OP-070–080 | REQ-Art11-12 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-12 | Not evidenced / unclear owner | Detection & Continuity |
| COV-053 | OP-062–063, OP-070–080 | REQ-Art11-13 / Art. 11 | Enterprise Data Platform is subject to REQ-Art11-13 | Not evidenced / unclear owner | Detection & Continuity |
| COV-054 | OP-060, OP-068 | REQ-Art11-14 / Art. 11 | Platform Development is constrained by REQ-Art11-14 | Stakeholder-constrained | Detection & Continuity |
| COV-055 | OP-060, OP-068 | REQ-Art11-15 / Art. 11 | Platform Development is constrained by REQ-Art11-15 | Stakeholder-constrained | Detection & Continuity |
| COV-056 | OP-060, OP-068 | REQ-Art11-16 / Art. 11 | Platform Development is constrained by REQ-Art11-16 | Stakeholder-constrained | Detection & Continuity |
| COV-057 | OP-070–080 | REQ-Art11-17 / Art. 11 | Incident Escalation is subject to REQ-Art11-17 | Not evidenced / unclear owner | Detection & Continuity |
| COV-058 | OP-070–080 | REQ-Art11-18 / Art. 11 | Incident Escalation is subject to REQ-Art11-18 | Not evidenced / unclear owner | Detection & Continuity |
| COV-059 | OP-070–080 | REQ-Art11-19 / Art. 11 | Incident Escalation is subject to REQ-Art11-19 | Not evidenced / unclear owner | Detection & Continuity |
| COV-060 | OP-070–080 | REQ-Art11-20 / Art. 11 | Incident Escalation is subject to REQ-Art11-20 | Not evidenced / unclear owner | Detection & Continuity |
| COV-061 | OP-062–063, OP-073, OP-078, OP-080 | REQ-Art12-01 / Art. 12 | Enterprise Data Platform is subject to REQ-Art12-01 | Not evidenced / unclear owner | Detection & Continuity |
| COV-062 | OP-062–063, OP-073, OP-078, OP-080 | REQ-Art12-02 / Art. 12 | Enterprise Data Platform is subject to REQ-Art12-02 | Not evidenced / unclear owner | Detection & Continuity |
| COV-063 | OP-062–063, OP-073, OP-078, OP-080 | REQ-Art12-03 / Art. 12 | Enterprise Data Platform is subject to REQ-Art12-03 | Not evidenced / unclear owner | Detection & Continuity |
| COV-064 | OP-062–063, OP-073, OP-078, OP-080 | REQ-Art12-04 / Art. 12 | Enterprise Data Platform is subject to REQ-Art12-04 | Not evidenced / unclear owner | Detection & Continuity |
| COV-065 | OP-027–029, OP-063, OP-074–075, OP-078 | REQ-Art12-05 / Art. 12 | Infrastructure Remediation realizes part of REQ-Art12-05 | Externally owned | Detection & Continuity |
| COV-066 | OP-027–029, OP-063, OP-074–075, OP-078 | REQ-Art12-06 / Art. 12 | Infrastructure Remediation realizes part of REQ-Art12-06 | Externally owned | Detection & Continuity |
| COV-067 | OP-027–029, OP-063, OP-074–075, OP-078 | REQ-Art12-07 / Art. 12 | Infrastructure Remediation realizes part of REQ-Art12-07 | Externally owned | Detection & Continuity |
| COV-068 | OP-027–029, OP-063, OP-074–075, OP-078 | REQ-Art12-08 / Art. 12 | Infrastructure Remediation realizes part of REQ-Art12-08 | Externally owned | Detection & Continuity |
| COV-069 | OP-048, OP-065, OP-078, OP-080 | REQ-Art12-09 / Art. 12 | Platform Development is constrained by REQ-Art12-09 | Stakeholder-constrained | Detection & Continuity |
| COV-070 | OP-048, OP-065, OP-078, OP-080 | REQ-Art12-10 / Art. 12 | Platform Development is constrained by REQ-Art12-10 | Stakeholder-constrained | Detection & Continuity |
| COV-071 | OP-048, OP-065, OP-078, OP-080 | REQ-Art12-11 / Art. 12 | Platform Development is constrained by REQ-Art12-11 | Stakeholder-constrained | Detection & Continuity |
| COV-072 | OP-048, OP-065, OP-078, OP-080 | REQ-Art12-12 / Art. 12 | Platform Development is constrained by REQ-Art12-12 | Stakeholder-constrained | Detection & Continuity |
| COV-073 | OP-048, OP-065, OP-078, OP-080 | REQ-Art12-13 / Art. 12 | Platform Development is constrained by REQ-Art12-13 | Stakeholder-constrained | Detection & Continuity |
| COV-074 | OP-014, OP-038, OP-042, OP-048 | REQ-Art13-01 / Art. 13 | Platform Development is constrained by REQ-Art13-01 | Stakeholder-constrained | Learning & Incident Management |
| COV-075 | OP-014, OP-038, OP-042, OP-048 | REQ-Art13-02 / Art. 13 | Platform Development is constrained by REQ-Art13-02 | Stakeholder-constrained | Learning & Incident Management |
| COV-076 | OP-014, OP-038, OP-042, OP-048 | REQ-Art13-03 / Art. 13 | Platform Development is constrained by REQ-Art13-03 | Stakeholder-constrained | Learning & Incident Management |
| COV-077 | OP-014, OP-038, OP-042, OP-048 | REQ-Art13-04 / Art. 13 | Platform Development is constrained by REQ-Art13-04 | Stakeholder-constrained | Learning & Incident Management |
| COV-078 | OP-014, OP-038, OP-042, OP-048 | REQ-Art13-05 / Art. 13 | Platform Development is constrained by REQ-Art13-05 | Stakeholder-constrained | Learning & Incident Management |
| COV-079 | OP-070–076 | REQ-Art13-06 / Art. 13 | Incident Escalation realizes part of REQ-Art13-06 | Externally owned | Learning & Incident Management |
| COV-080 | OP-070–076 | REQ-Art13-07 / Art. 13 | Incident Escalation realizes part of REQ-Art13-07 | Externally owned | Learning & Incident Management |
| COV-081 | OP-070–076 | REQ-Art13-08 / Art. 13 | Incident Escalation realizes part of REQ-Art13-08 | Externally owned | Learning & Incident Management |
| COV-082 | OP-070–076 | REQ-Art13-09 / Art. 13 | Incident Escalation realizes part of REQ-Art13-09 | Externally owned | Learning & Incident Management |
| COV-083 | OP-070–076 | REQ-Art13-10 / Art. 13 | Incident Escalation realizes part of REQ-Art13-10 | Externally owned | Learning & Incident Management |
| COV-084 | OP-061–063, OP-070–080 | REQ-Art13-11 / Art. 13 | Enterprise Data Platform is subject to REQ-Art13-11 | Not evidenced / unclear owner | Learning & Incident Management |
| COV-085 | OP-061–063, OP-070–080 | REQ-Art13-12 / Art. 13 | Enterprise Data Platform is subject to REQ-Art13-12 | Not evidenced / unclear owner | Learning & Incident Management |
| COV-086 | OP-061–063, OP-070–080 | REQ-Art13-13 / Art. 13 | Enterprise Data Platform is subject to REQ-Art13-13 | Not evidenced / unclear owner | Learning & Incident Management |
| COV-087 | OP-061–063, OP-070–080 | REQ-Art13-14 / Art. 13 | Enterprise Data Platform is subject to REQ-Art13-14 | Not evidenced / unclear owner | Learning & Incident Management |
| COV-088 | OP-038, OP-067, OP-087 | REQ-Art13-15 / Art. 13 | Service Update is constrained by REQ-Art13-15 | Stakeholder-constrained | Learning & Incident Management |
| COV-089 | OP-038, OP-067, OP-087 | REQ-Art13-16 / Art. 13 | Service Update is constrained by REQ-Art13-16 | Stakeholder-constrained | Learning & Incident Management |
| COV-090 | OP-038, OP-067, OP-087 | REQ-Art13-17 / Art. 13 | Service Update is constrained by REQ-Art13-17 | Stakeholder-constrained | Learning & Incident Management |
| COV-091 | OP-038, OP-067, OP-087 | REQ-Art13-18 / Art. 13 | Service Update is constrained by REQ-Art13-18 | Stakeholder-constrained | Learning & Incident Management |
| COV-092 | OP-070–073 | REQ-Art17-01 / Art. 17 | Incident Escalation is constrained by REQ-Art17-01 | Stakeholder-constrained | Learning & Incident Management |
| COV-093 | OP-070–073 | REQ-Art17-02 / Art. 17 | Incident Escalation is constrained by REQ-Art17-02 | Stakeholder-constrained | Learning & Incident Management |
| COV-094 | OP-070–073 | REQ-Art17-03 / Art. 17 | Incident Escalation is constrained by REQ-Art17-03 | Stakeholder-constrained | Learning & Incident Management |
| COV-095 | OP-070–072 | REQ-Art17-04 / Art. 17 | Incident Escalation realizes part of REQ-Art17-04 | Externally owned | Learning & Incident Management |
| COV-096 | OP-070–072 | REQ-Art17-05 / Art. 17 | Incident Escalation realizes part of REQ-Art17-05 | Externally owned | Learning & Incident Management |
| COV-097 | OP-070–072 | REQ-Art17-06 / Art. 17 | Incident Escalation realizes part of REQ-Art17-06 | Externally owned | Learning & Incident Management |
| COV-098 | OP-070–072 | REQ-Art17-07 / Art. 17 | Incident Escalation realizes part of REQ-Art17-07 | Externally owned | Learning & Incident Management |
| COV-099 | OP-073–078 | REQ-Art17-08 / Art. 17 | Software Remediation realizes REQ-Art17-08 | Directly performed | Learning & Incident Management |
| COV-100 | OP-073–078 | REQ-Art17-09 / Art. 17 | Software Remediation realizes REQ-Art17-09 | Directly performed | Learning & Incident Management |
| COV-101 | OP-073–078 | REQ-Art17-10 / Art. 17 | Software Remediation realizes REQ-Art17-10 | Directly performed | Learning & Incident Management |
| COV-102 | OP-008, OP-048, OP-050 | REQ-Art24-01 / Art. 24 | Test and DEV Readiness realizes REQ-Art24-01 | Directly performed | Resilience Testing |
| COV-103 | OP-008, OP-048, OP-050 | REQ-Art24-02 / Art. 24 | Test and DEV Readiness realizes REQ-Art24-02 | Directly performed | Resilience Testing |
| COV-104 | OP-008, OP-048, OP-059–060 | REQ-Art24-03 / Art. 24 | Test and DEV Readiness is constrained by REQ-Art24-03 | Stakeholder-constrained | Resilience Testing |
| COV-105 | OP-008, OP-048, OP-059–060 | REQ-Art24-04 / Art. 24 | Test and DEV Readiness is constrained by REQ-Art24-04 | Stakeholder-constrained | Resilience Testing |
| COV-106 | OP-008, OP-048, OP-059–060 | REQ-Art24-05 / Art. 24 | Test and DEV Readiness is constrained by REQ-Art24-05 | Stakeholder-constrained | Resilience Testing |
| COV-107 | OP-009, OP-047, OP-064 | REQ-Art24-06 / Art. 24 | Pull Request Review is subject to REQ-Art24-06 | Not evidenced / unclear owner | Resilience Testing |
| COV-108 | OP-009, OP-047, OP-064 | REQ-Art24-07 / Art. 24 | Pull Request Review is subject to REQ-Art24-07 | Not evidenced / unclear owner | Resilience Testing |
| COV-109 | OP-009, OP-047, OP-064 | REQ-Art24-08 / Art. 24 | Pull Request Review is subject to REQ-Art24-08 | Not evidenced / unclear owner | Resilience Testing |
| COV-110 | OP-008, OP-048 | REQ-Art25-01 / Art. 25 | Test and DEV Readiness realizes REQ-Art25-01 | Directly performed | Resilience Testing |
| COV-111 | OP-008, OP-048 | REQ-Art25-02 / Art. 25 | Test and DEV Readiness realizes REQ-Art25-02 | Directly performed | Resilience Testing |
| COV-112 | OP-008, OP-048, OP-050 | REQ-Art25-03 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-03 | Stakeholder-constrained | Resilience Testing |
| COV-113 | OP-008, OP-048, OP-050 | REQ-Art25-04 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-04 | Stakeholder-constrained | Resilience Testing |
| COV-114 | OP-008, OP-048, OP-050 | REQ-Art25-05 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-05 | Stakeholder-constrained | Resilience Testing |
| COV-115 | OP-008, OP-048, OP-050 | REQ-Art25-06 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-06 | Stakeholder-constrained | Resilience Testing |
| COV-116 | OP-008, OP-048, OP-050 | REQ-Art25-07 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-07 | Stakeholder-constrained | Resilience Testing |
| COV-117 | OP-008, OP-048, OP-050 | REQ-Art25-08 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-08 | Stakeholder-constrained | Resilience Testing |
| COV-118 | OP-008, OP-048, OP-050 | REQ-Art25-09 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-09 | Stakeholder-constrained | Resilience Testing |
| COV-119 | OP-008, OP-048, OP-050 | REQ-Art25-10 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-10 | Stakeholder-constrained | Resilience Testing |
| COV-120 | OP-008, OP-048, OP-050 | REQ-Art25-11 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-11 | Stakeholder-constrained | Resilience Testing |
| COV-121 | OP-008, OP-048, OP-050 | REQ-Art25-12 / Art. 25 | Test and DEV Readiness is constrained by REQ-Art25-12 | Stakeholder-constrained | Resilience Testing |
| COV-122 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-01 / Art. 28 | Microsoft Contract is subject to REQ-Art28-01 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-123 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-02 / Art. 28 | Microsoft Contract is subject to REQ-Art28-02 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-124 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-03 / Art. 28 | Microsoft Contract is subject to REQ-Art28-03 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-125 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-04 / Art. 28 | Microsoft Contract is subject to REQ-Art28-04 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-126 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-05 / Art. 28 | Microsoft Contract is subject to REQ-Art28-05 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-127 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-06 / Art. 28 | Microsoft Contract is subject to REQ-Art28-06 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-128 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-07 / Art. 28 | Microsoft Contract is subject to REQ-Art28-07 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-129 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-08 / Art. 28 | Microsoft Contract is subject to REQ-Art28-08 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-130 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-09 / Art. 28 | Microsoft Contract is subject to REQ-Art28-09 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-131 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-10 / Art. 28 | Microsoft Contract is subject to REQ-Art28-10 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-132 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-11 / Art. 28 | Microsoft Contract is subject to REQ-Art28-11 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-133 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-12 / Art. 28 | Microsoft Contract is subject to REQ-Art28-12 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-134 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-13 / Art. 28 | Microsoft Contract is subject to REQ-Art28-13 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-135 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-14 / Art. 28 | Microsoft Contract is subject to REQ-Art28-14 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-136 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-15 / Art. 28 | Microsoft Contract is subject to REQ-Art28-15 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-137 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-16 / Art. 28 | Microsoft Contract is subject to REQ-Art28-16 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-138 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-17 / Art. 28 | Microsoft Contract is subject to REQ-Art28-17 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-139 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-18 / Art. 28 | Microsoft Contract is subject to REQ-Art28-18 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-140 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-19 / Art. 28 | Microsoft Contract is subject to REQ-Art28-19 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-141 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-20 / Art. 28 | Microsoft Contract is subject to REQ-Art28-20 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-142 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-21 / Art. 28 | Microsoft Contract is subject to REQ-Art28-21 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-143 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-22 / Art. 28 | Microsoft Contract is subject to REQ-Art28-22 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-144 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-23 / Art. 28 | Microsoft Contract is subject to REQ-Art28-23 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-145 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-24 / Art. 28 | Microsoft Contract is subject to REQ-Art28-24 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-146 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-25 / Art. 28 | Microsoft Contract is subject to REQ-Art28-25 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-147 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-26 / Art. 28 | Microsoft Contract is subject to REQ-Art28-26 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-148 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-27 / Art. 28 | Microsoft Contract is subject to REQ-Art28-27 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-149 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-28 / Art. 28 | Microsoft Contract is subject to REQ-Art28-28 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-150 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-29 / Art. 28 | Microsoft Contract is subject to REQ-Art28-29 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-151 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-30 / Art. 28 | Microsoft Contract is subject to REQ-Art28-30 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-152 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-31 / Art. 28 | Microsoft Contract is subject to REQ-Art28-31 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |
| COV-153 | OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification | REQ-Art28-32 / Art. 28 | Microsoft Contract is subject to REQ-Art28-32 | Stakeholder-constrained | Microsoft Cloud Third-Party Risk |

## Regulatory Relationship Ledger

Each visible regulatory effect is an approved, directional, two-endpoint relationship. `Realization` is used only for the approved direct or named external behaviour; an externally owned or unclear duty is never represented as a Back-end Developer realization. The `Association` rows specifically mean “the DORA requirement legally applies to/constrains this evidenced endpoint”; they make no implementation claim.

| Relationship ID | Source | Meaning | Target | Candidate ArchiMate relation | Evidence | Ownership | Approval |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REL-COV-001 | Framework Maintenance | realizes | REQ-Art7-01 | Realization | COV-001; OP-004, OP-038; REQ-Art7-01 | Directly performed | approved |
| REL-COV-002 | Framework Maintenance | realizes | REQ-Art7-02 | Realization | COV-002; OP-004, OP-038; REQ-Art7-02 | Directly performed | approved |
| REL-COV-003 | REQ-Art7-03 | legally applies to / constrains | Platform Development | Association | COV-003; OP-050, OP-060, CON-006; REQ-Art7-03 | Stakeholder-constrained | approved |
| REL-COV-004 | REQ-Art7-04 | legally applies to / constrains | Platform Development | Association | COV-004; OP-050, OP-060, CON-006; REQ-Art7-04 | Stakeholder-constrained | approved |
| REL-COV-005 | REQ-Art8-01 | legally applies to / constrains | Platform Development | Association | COV-005; OP-006, OP-018–019, OP-066, OP-081–082; REQ-Art8-01 | Stakeholder-constrained | approved |
| REL-COV-006 | REQ-Art8-02 | legally applies to / constrains | Platform Development | Association | COV-006; OP-006, OP-018–019, OP-066, OP-081–082; REQ-Art8-02 | Stakeholder-constrained | approved |
| REL-COV-007 | REQ-Art8-03 | legally applies to / constrains | Platform Development | Association | COV-007; OP-006, OP-018–019, OP-066, OP-081–082; REQ-Art8-03 | Stakeholder-constrained | approved |
| REL-COV-008 | REQ-Art8-04 | legally applies to / constrains | Service Update | Association | COV-008; OP-038, OP-041–042, OP-052, CON-001; REQ-Art8-04 | Stakeholder-constrained | approved |
| REL-COV-009 | REQ-Art8-05 | legally applies to / constrains | Service Update | Association | COV-009; OP-038, OP-041–042, OP-052, CON-001; REQ-Art8-05 | Stakeholder-constrained | approved |
| REL-COV-010 | REQ-Art8-06 | legally applies to / constrains | Service Update | Association | COV-010; OP-038, OP-041–042, OP-052, CON-001; REQ-Art8-06 | Stakeholder-constrained | approved |
| REL-COV-011 | REQ-Art8-07 | legally applies to / constrains | Enterprise Data Platform | Association | COV-011; OP-023–026, OP-027–029, OP-068; REQ-Art8-07 | Not evidenced / unclear owner | approved |
| REL-COV-012 | REQ-Art8-08 | legally applies to / constrains | Enterprise Data Platform | Association | COV-012; OP-023–026, OP-027–029, OP-068; REQ-Art8-08 | Not evidenced / unclear owner | approved |
| REL-COV-013 | REQ-Art8-09 | legally applies to / constrains | Enterprise Data Platform | Association | COV-013; OP-023–026, OP-027–029, OP-068; REQ-Art8-09 | Not evidenced / unclear owner | approved |
| REL-COV-014 | REQ-Art8-10 | legally applies to / constrains | Enterprise Data Platform | Association | COV-014; OP-023–026, OP-027–029, OP-068; REQ-Art8-10 | Not evidenced / unclear owner | approved |
| REL-COV-015 | REQ-Art8-11 | legally applies to / constrains | Enterprise Data Platform | Association | COV-015; OP-023–026, OP-027–029, OP-068; REQ-Art8-11 | Not evidenced / unclear owner | approved |
| REL-COV-016 | REQ-Art9-01 | legally applies to / constrains | Data Offload Flow | Association | COV-016; OP-006, OP-048, OP-065, OP-081; REQ-Art9-01 | Stakeholder-constrained | approved |
| REL-COV-017 | REQ-Art9-02 | legally applies to / constrains | Data Offload Flow | Association | COV-017; OP-006, OP-048, OP-065, OP-081; REQ-Art9-02 | Stakeholder-constrained | approved |
| REL-COV-018 | REQ-Art9-03 | legally applies to / constrains | Data Offload Flow | Association | COV-018; OP-006, OP-048, OP-065, OP-081; REQ-Art9-03 | Stakeholder-constrained | approved |
| REL-COV-019 | REQ-Art9-04 | legally applies to / constrains | Data Offload Flow | Association | COV-019; OP-006, OP-048, OP-065, OP-081; REQ-Art9-04 | Stakeholder-constrained | approved |
| REL-COV-020 | REQ-Art9-05 | legally applies to / constrains | Enterprise Data Platform | Association | COV-020; OP-031–036, OP-088; REQ-Art9-05 | Not evidenced / unclear owner | approved |
| REL-COV-021 | REQ-Art9-06 | legally applies to / constrains | Enterprise Data Platform | Association | COV-021; OP-031–036, OP-088; REQ-Art9-06 | Not evidenced / unclear owner | approved |
| REL-COV-022 | REQ-Art9-07 | legally applies to / constrains | Enterprise Data Platform | Association | COV-022; OP-031–036, OP-088; REQ-Art9-07 | Not evidenced / unclear owner | approved |
| REL-COV-023 | Azure AD / Internal Service Access | supports | REQ-Art9-08 | Association | COV-023; OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002; REQ-Art9-08 | Externally owned | approved |
| REL-COV-024 | Azure AD / Internal Service Access | supports | REQ-Art9-09 | Association | COV-024; OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002; REQ-Art9-09 | Externally owned | approved |
| REL-COV-025 | Azure AD / Internal Service Access | supports | REQ-Art9-10 | Association | COV-025; OP-017, OP-020, OP-037, OP-053–054, OP-057, CON-002; REQ-Art9-10 | Externally owned | approved |
| REL-COV-026 | Test and DEV Readiness | realizes | REQ-Art9-11 | Realization | COV-026; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008; REQ-Art9-11 | Directly performed | approved |
| REL-COV-027 | Test and DEV Readiness | realizes | REQ-Art9-12 | Realization | COV-027; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008; REQ-Art9-12 | Directly performed | approved |
| REL-COV-028 | Test and DEV Readiness | realizes | REQ-Art9-13 | Realization | COV-028; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008; REQ-Art9-13 | Directly performed | approved |
| REL-COV-029 | Test and DEV Readiness | realizes | REQ-Art9-14 | Realization | COV-029; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008; REQ-Art9-14 | Directly performed | approved |
| REL-COV-030 | Test and DEV Readiness | realizes | REQ-Art9-15 | Realization | COV-030; OP-008–013, OP-047, OP-064, OP-082, OP-084–085, CON-008; REQ-Art9-15 | Directly performed | approved |
| REL-COV-031 | REQ-Art9-16 | legally applies to / constrains | Service Update | Association | COV-031; OP-038, OP-041–042; REQ-Art9-16 | Stakeholder-constrained | approved |
| REL-COV-032 | REQ-Art9-17 | legally applies to / constrains | Service Update | Association | COV-032; OP-038, OP-041–042; REQ-Art9-17 | Stakeholder-constrained | approved |
| REL-COV-033 | REQ-Art9-18 | legally applies to / constrains | Service Update | Association | COV-033; OP-038, OP-041–042; REQ-Art9-18 | Stakeholder-constrained | approved |
| REL-COV-034 | REQ-Art9-19 | legally applies to / constrains | Service Update | Association | COV-034; OP-038, OP-041–042; REQ-Art9-19 | Stakeholder-constrained | approved |
| REL-COV-035 | REQ-Art10-01 | legally applies to / constrains | Production Monitoring | Association | COV-035; OP-014, OP-070, OP-072; REQ-Art10-01 | Stakeholder-constrained | approved |
| REL-COV-036 | REQ-Art10-02 | legally applies to / constrains | Production Monitoring | Association | COV-036; OP-014, OP-070, OP-072; REQ-Art10-02 | Stakeholder-constrained | approved |
| REL-COV-037 | Incident Escalation | supports | REQ-Art10-03 | Association | COV-037; OP-070, OP-072, OP-076; REQ-Art10-03 | Externally owned | approved |
| REL-COV-038 | Incident Escalation | supports | REQ-Art10-04 | Association | COV-038; OP-070, OP-072, OP-076; REQ-Art10-04 | Externally owned | approved |
| REL-COV-039 | Incident Escalation | supports | REQ-Art10-05 | Association | COV-039; OP-070, OP-072, OP-076; REQ-Art10-05 | Externally owned | approved |
| REL-COV-040 | Incident Escalation | supports | REQ-Art10-06 | Association | COV-040; OP-070, OP-072, OP-076; REQ-Art10-06 | Externally owned | approved |
| REL-COV-041 | REQ-Art11-01 | legally applies to / constrains | Enterprise Data Platform | Association | COV-041; OP-060, OP-070–080; operator critical-function clarification; REQ-Art11-01 | Not evidenced / unclear owner | approved |
| REL-COV-042 | REQ-Art11-02 | legally applies to / constrains | Enterprise Data Platform | Association | COV-042; OP-060, OP-070–080; operator critical-function clarification; REQ-Art11-02 | Not evidenced / unclear owner | approved |
| REL-COV-043 | REQ-Art11-03 | legally applies to / constrains | Enterprise Data Platform | Association | COV-043; OP-060, OP-070–080; operator critical-function clarification; REQ-Art11-03 | Not evidenced / unclear owner | approved |
| REL-COV-044 | REQ-Art11-04 | legally applies to / constrains | Enterprise Data Platform | Association | COV-044; OP-060, OP-070–080; operator critical-function clarification; REQ-Art11-04 | Not evidenced / unclear owner | approved |
| REL-COV-045 | Software Remediation | realizes | REQ-Art11-05 | Realization | COV-045; OP-071, OP-073–078; REQ-Art11-05 | Directly performed | approved |
| REL-COV-046 | Software Remediation | realizes | REQ-Art11-06 | Realization | COV-046; OP-071, OP-073–078; REQ-Art11-06 | Directly performed | approved |
| REL-COV-047 | Software Remediation | realizes | REQ-Art11-07 | Realization | COV-047; OP-071, OP-073–078; REQ-Art11-07 | Directly performed | approved |
| REL-COV-048 | REQ-Art11-08 | legally applies to / constrains | Incident Escalation | Association | COV-048; OP-060, OP-071, OP-079–080; REQ-Art11-08 | Not evidenced / unclear owner | approved |
| REL-COV-049 | REQ-Art11-09 | legally applies to / constrains | Incident Escalation | Association | COV-049; OP-060, OP-071, OP-079–080; REQ-Art11-09 | Not evidenced / unclear owner | approved |
| REL-COV-050 | REQ-Art11-10 | legally applies to / constrains | Incident Escalation | Association | COV-050; OP-060, OP-071, OP-079–080; REQ-Art11-10 | Not evidenced / unclear owner | approved |
| REL-COV-051 | REQ-Art11-11 | legally applies to / constrains | Enterprise Data Platform | Association | COV-051; OP-062–063, OP-070–080; REQ-Art11-11 | Not evidenced / unclear owner | approved |
| REL-COV-052 | REQ-Art11-12 | legally applies to / constrains | Enterprise Data Platform | Association | COV-052; OP-062–063, OP-070–080; REQ-Art11-12 | Not evidenced / unclear owner | approved |
| REL-COV-053 | REQ-Art11-13 | legally applies to / constrains | Enterprise Data Platform | Association | COV-053; OP-062–063, OP-070–080; REQ-Art11-13 | Not evidenced / unclear owner | approved |
| REL-COV-054 | REQ-Art11-14 | legally applies to / constrains | Platform Development | Association | COV-054; OP-060, OP-068; REQ-Art11-14 | Stakeholder-constrained | approved |
| REL-COV-055 | REQ-Art11-15 | legally applies to / constrains | Platform Development | Association | COV-055; OP-060, OP-068; REQ-Art11-15 | Stakeholder-constrained | approved |
| REL-COV-056 | REQ-Art11-16 | legally applies to / constrains | Platform Development | Association | COV-056; OP-060, OP-068; REQ-Art11-16 | Stakeholder-constrained | approved |
| REL-COV-057 | REQ-Art11-17 | legally applies to / constrains | Incident Escalation | Association | COV-057; OP-070–080; REQ-Art11-17 | Not evidenced / unclear owner | approved |
| REL-COV-058 | REQ-Art11-18 | legally applies to / constrains | Incident Escalation | Association | COV-058; OP-070–080; REQ-Art11-18 | Not evidenced / unclear owner | approved |
| REL-COV-059 | REQ-Art11-19 | legally applies to / constrains | Incident Escalation | Association | COV-059; OP-070–080; REQ-Art11-19 | Not evidenced / unclear owner | approved |
| REL-COV-060 | REQ-Art11-20 | legally applies to / constrains | Incident Escalation | Association | COV-060; OP-070–080; REQ-Art11-20 | Not evidenced / unclear owner | approved |
| REL-COV-061 | REQ-Art12-01 | legally applies to / constrains | Enterprise Data Platform | Association | COV-061; OP-062–063, OP-073, OP-078, OP-080; REQ-Art12-01 | Not evidenced / unclear owner | approved |
| REL-COV-062 | REQ-Art12-02 | legally applies to / constrains | Enterprise Data Platform | Association | COV-062; OP-062–063, OP-073, OP-078, OP-080; REQ-Art12-02 | Not evidenced / unclear owner | approved |
| REL-COV-063 | REQ-Art12-03 | legally applies to / constrains | Enterprise Data Platform | Association | COV-063; OP-062–063, OP-073, OP-078, OP-080; REQ-Art12-03 | Not evidenced / unclear owner | approved |
| REL-COV-064 | REQ-Art12-04 | legally applies to / constrains | Enterprise Data Platform | Association | COV-064; OP-062–063, OP-073, OP-078, OP-080; REQ-Art12-04 | Not evidenced / unclear owner | approved |
| REL-COV-065 | Infrastructure Remediation | supports | REQ-Art12-05 | Association | COV-065; OP-027–029, OP-063, OP-074–075, OP-078; REQ-Art12-05 | Externally owned | approved |
| REL-COV-066 | Infrastructure Remediation | supports | REQ-Art12-06 | Association | COV-066; OP-027–029, OP-063, OP-074–075, OP-078; REQ-Art12-06 | Externally owned | approved |
| REL-COV-067 | Infrastructure Remediation | supports | REQ-Art12-07 | Association | COV-067; OP-027–029, OP-063, OP-074–075, OP-078; REQ-Art12-07 | Externally owned | approved |
| REL-COV-068 | Infrastructure Remediation | supports | REQ-Art12-08 | Association | COV-068; OP-027–029, OP-063, OP-074–075, OP-078; REQ-Art12-08 | Externally owned | approved |
| REL-COV-069 | REQ-Art12-09 | legally applies to / constrains | Platform Development | Association | COV-069; OP-048, OP-065, OP-078, OP-080; REQ-Art12-09 | Stakeholder-constrained | approved |
| REL-COV-070 | REQ-Art12-10 | legally applies to / constrains | Platform Development | Association | COV-070; OP-048, OP-065, OP-078, OP-080; REQ-Art12-10 | Stakeholder-constrained | approved |
| REL-COV-071 | REQ-Art12-11 | legally applies to / constrains | Platform Development | Association | COV-071; OP-048, OP-065, OP-078, OP-080; REQ-Art12-11 | Stakeholder-constrained | approved |
| REL-COV-072 | REQ-Art12-12 | legally applies to / constrains | Platform Development | Association | COV-072; OP-048, OP-065, OP-078, OP-080; REQ-Art12-12 | Stakeholder-constrained | approved |
| REL-COV-073 | REQ-Art12-13 | legally applies to / constrains | Platform Development | Association | COV-073; OP-048, OP-065, OP-078, OP-080; REQ-Art12-13 | Stakeholder-constrained | approved |
| REL-COV-074 | REQ-Art13-01 | legally applies to / constrains | Platform Development | Association | COV-074; OP-014, OP-038, OP-042, OP-048; REQ-Art13-01 | Stakeholder-constrained | approved |
| REL-COV-075 | REQ-Art13-02 | legally applies to / constrains | Platform Development | Association | COV-075; OP-014, OP-038, OP-042, OP-048; REQ-Art13-02 | Stakeholder-constrained | approved |
| REL-COV-076 | REQ-Art13-03 | legally applies to / constrains | Platform Development | Association | COV-076; OP-014, OP-038, OP-042, OP-048; REQ-Art13-03 | Stakeholder-constrained | approved |
| REL-COV-077 | REQ-Art13-04 | legally applies to / constrains | Platform Development | Association | COV-077; OP-014, OP-038, OP-042, OP-048; REQ-Art13-04 | Stakeholder-constrained | approved |
| REL-COV-078 | REQ-Art13-05 | legally applies to / constrains | Platform Development | Association | COV-078; OP-014, OP-038, OP-042, OP-048; REQ-Art13-05 | Stakeholder-constrained | approved |
| REL-COV-079 | Incident Escalation | supports | REQ-Art13-06 | Association | COV-079; OP-070–076; REQ-Art13-06 | Externally owned | approved |
| REL-COV-080 | Incident Escalation | supports | REQ-Art13-07 | Association | COV-080; OP-070–076; REQ-Art13-07 | Externally owned | approved |
| REL-COV-081 | Incident Escalation | supports | REQ-Art13-08 | Association | COV-081; OP-070–076; REQ-Art13-08 | Externally owned | approved |
| REL-COV-082 | Incident Escalation | supports | REQ-Art13-09 | Association | COV-082; OP-070–076; REQ-Art13-09 | Externally owned | approved |
| REL-COV-083 | Incident Escalation | supports | REQ-Art13-10 | Association | COV-083; OP-070–076; REQ-Art13-10 | Externally owned | approved |
| REL-COV-084 | REQ-Art13-11 | legally applies to / constrains | Enterprise Data Platform | Association | COV-084; OP-061–063, OP-070–080; REQ-Art13-11 | Not evidenced / unclear owner | approved |
| REL-COV-085 | REQ-Art13-12 | legally applies to / constrains | Enterprise Data Platform | Association | COV-085; OP-061–063, OP-070–080; REQ-Art13-12 | Not evidenced / unclear owner | approved |
| REL-COV-086 | REQ-Art13-13 | legally applies to / constrains | Enterprise Data Platform | Association | COV-086; OP-061–063, OP-070–080; REQ-Art13-13 | Not evidenced / unclear owner | approved |
| REL-COV-087 | REQ-Art13-14 | legally applies to / constrains | Enterprise Data Platform | Association | COV-087; OP-061–063, OP-070–080; REQ-Art13-14 | Not evidenced / unclear owner | approved |
| REL-COV-088 | REQ-Art13-15 | legally applies to / constrains | Service Update | Association | COV-088; OP-038, OP-067, OP-087; REQ-Art13-15 | Stakeholder-constrained | approved |
| REL-COV-089 | REQ-Art13-16 | legally applies to / constrains | Service Update | Association | COV-089; OP-038, OP-067, OP-087; REQ-Art13-16 | Stakeholder-constrained | approved |
| REL-COV-090 | REQ-Art13-17 | legally applies to / constrains | Service Update | Association | COV-090; OP-038, OP-067, OP-087; REQ-Art13-17 | Stakeholder-constrained | approved |
| REL-COV-091 | REQ-Art13-18 | legally applies to / constrains | Service Update | Association | COV-091; OP-038, OP-067, OP-087; REQ-Art13-18 | Stakeholder-constrained | approved |
| REL-COV-092 | REQ-Art17-01 | legally applies to / constrains | Incident Escalation | Association | COV-092; OP-070–073; REQ-Art17-01 | Stakeholder-constrained | approved |
| REL-COV-093 | REQ-Art17-02 | legally applies to / constrains | Incident Escalation | Association | COV-093; OP-070–073; REQ-Art17-02 | Stakeholder-constrained | approved |
| REL-COV-094 | REQ-Art17-03 | legally applies to / constrains | Incident Escalation | Association | COV-094; OP-070–073; REQ-Art17-03 | Stakeholder-constrained | approved |
| REL-COV-095 | Incident Escalation | supports | REQ-Art17-04 | Association | COV-095; OP-070–072; REQ-Art17-04 | Externally owned | approved |
| REL-COV-096 | Incident Escalation | supports | REQ-Art17-05 | Association | COV-096; OP-070–072; REQ-Art17-05 | Externally owned | approved |
| REL-COV-097 | Incident Escalation | supports | REQ-Art17-06 | Association | COV-097; OP-070–072; REQ-Art17-06 | Externally owned | approved |
| REL-COV-098 | Incident Escalation | supports | REQ-Art17-07 | Association | COV-098; OP-070–072; REQ-Art17-07 | Externally owned | approved |
| REL-COV-099 | Software Remediation | realizes | REQ-Art17-08 | Realization | COV-099; OP-073–078; REQ-Art17-08 | Directly performed | approved |
| REL-COV-100 | Software Remediation | realizes | REQ-Art17-09 | Realization | COV-100; OP-073–078; REQ-Art17-09 | Directly performed | approved |
| REL-COV-101 | Software Remediation | realizes | REQ-Art17-10 | Realization | COV-101; OP-073–078; REQ-Art17-10 | Directly performed | approved |
| REL-COV-102 | Test and DEV Readiness | realizes | REQ-Art24-01 | Realization | COV-102; OP-008, OP-048, OP-050; REQ-Art24-01 | Directly performed | approved |
| REL-COV-103 | Test and DEV Readiness | realizes | REQ-Art24-02 | Realization | COV-103; OP-008, OP-048, OP-050; REQ-Art24-02 | Directly performed | approved |
| REL-COV-104 | REQ-Art24-03 | legally applies to / constrains | Test and DEV Readiness | Association | COV-104; OP-008, OP-048, OP-059–060; REQ-Art24-03 | Stakeholder-constrained | approved |
| REL-COV-105 | REQ-Art24-04 | legally applies to / constrains | Test and DEV Readiness | Association | COV-105; OP-008, OP-048, OP-059–060; REQ-Art24-04 | Stakeholder-constrained | approved |
| REL-COV-106 | REQ-Art24-05 | legally applies to / constrains | Test and DEV Readiness | Association | COV-106; OP-008, OP-048, OP-059–060; REQ-Art24-05 | Stakeholder-constrained | approved |
| REL-COV-107 | REQ-Art24-06 | legally applies to / constrains | Pull Request Review | Association | COV-107; OP-009, OP-047, OP-064; REQ-Art24-06 | Not evidenced / unclear owner | approved |
| REL-COV-108 | REQ-Art24-07 | legally applies to / constrains | Pull Request Review | Association | COV-108; OP-009, OP-047, OP-064; REQ-Art24-07 | Not evidenced / unclear owner | approved |
| REL-COV-109 | REQ-Art24-08 | legally applies to / constrains | Pull Request Review | Association | COV-109; OP-009, OP-047, OP-064; REQ-Art24-08 | Not evidenced / unclear owner | approved |
| REL-COV-110 | Test and DEV Readiness | realizes | REQ-Art25-01 | Realization | COV-110; OP-008, OP-048; REQ-Art25-01 | Directly performed | approved |
| REL-COV-111 | Test and DEV Readiness | realizes | REQ-Art25-02 | Realization | COV-111; OP-008, OP-048; REQ-Art25-02 | Directly performed | approved |
| REL-COV-112 | REQ-Art25-03 | legally applies to / constrains | Test and DEV Readiness | Association | COV-112; OP-008, OP-048, OP-050; REQ-Art25-03 | Stakeholder-constrained | approved |
| REL-COV-113 | REQ-Art25-04 | legally applies to / constrains | Test and DEV Readiness | Association | COV-113; OP-008, OP-048, OP-050; REQ-Art25-04 | Stakeholder-constrained | approved |
| REL-COV-114 | REQ-Art25-05 | legally applies to / constrains | Test and DEV Readiness | Association | COV-114; OP-008, OP-048, OP-050; REQ-Art25-05 | Stakeholder-constrained | approved |
| REL-COV-115 | REQ-Art25-06 | legally applies to / constrains | Test and DEV Readiness | Association | COV-115; OP-008, OP-048, OP-050; REQ-Art25-06 | Stakeholder-constrained | approved |
| REL-COV-116 | REQ-Art25-07 | legally applies to / constrains | Test and DEV Readiness | Association | COV-116; OP-008, OP-048, OP-050; REQ-Art25-07 | Stakeholder-constrained | approved |
| REL-COV-117 | REQ-Art25-08 | legally applies to / constrains | Test and DEV Readiness | Association | COV-117; OP-008, OP-048, OP-050; REQ-Art25-08 | Stakeholder-constrained | approved |
| REL-COV-118 | REQ-Art25-09 | legally applies to / constrains | Test and DEV Readiness | Association | COV-118; OP-008, OP-048, OP-050; REQ-Art25-09 | Stakeholder-constrained | approved |
| REL-COV-119 | REQ-Art25-10 | legally applies to / constrains | Test and DEV Readiness | Association | COV-119; OP-008, OP-048, OP-050; REQ-Art25-10 | Stakeholder-constrained | approved |
| REL-COV-120 | REQ-Art25-11 | legally applies to / constrains | Test and DEV Readiness | Association | COV-120; OP-008, OP-048, OP-050; REQ-Art25-11 | Stakeholder-constrained | approved |
| REL-COV-121 | REQ-Art25-12 | legally applies to / constrains | Test and DEV Readiness | Association | COV-121; OP-008, OP-048, OP-050; REQ-Art25-12 | Stakeholder-constrained | approved |
| REL-COV-122 | REQ-Art28-01 | legally applies to / constrains | Microsoft Contract | Association | COV-122; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-01 | Stakeholder-constrained | approved |
| REL-COV-123 | REQ-Art28-02 | legally applies to / constrains | Microsoft Contract | Association | COV-123; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-02 | Stakeholder-constrained | approved |
| REL-COV-124 | REQ-Art28-03 | legally applies to / constrains | Microsoft Contract | Association | COV-124; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-03 | Stakeholder-constrained | approved |
| REL-COV-125 | REQ-Art28-04 | legally applies to / constrains | Microsoft Contract | Association | COV-125; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-04 | Stakeholder-constrained | approved |
| REL-COV-126 | REQ-Art28-05 | legally applies to / constrains | Microsoft Contract | Association | COV-126; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-05 | Stakeholder-constrained | approved |
| REL-COV-127 | REQ-Art28-06 | legally applies to / constrains | Microsoft Contract | Association | COV-127; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-06 | Stakeholder-constrained | approved |
| REL-COV-128 | REQ-Art28-07 | legally applies to / constrains | Microsoft Contract | Association | COV-128; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-07 | Stakeholder-constrained | approved |
| REL-COV-129 | REQ-Art28-08 | legally applies to / constrains | Microsoft Contract | Association | COV-129; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-08 | Stakeholder-constrained | approved |
| REL-COV-130 | REQ-Art28-09 | legally applies to / constrains | Microsoft Contract | Association | COV-130; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-09 | Stakeholder-constrained | approved |
| REL-COV-131 | REQ-Art28-10 | legally applies to / constrains | Microsoft Contract | Association | COV-131; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-10 | Stakeholder-constrained | approved |
| REL-COV-132 | REQ-Art28-11 | legally applies to / constrains | Microsoft Contract | Association | COV-132; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-11 | Stakeholder-constrained | approved |
| REL-COV-133 | REQ-Art28-12 | legally applies to / constrains | Microsoft Contract | Association | COV-133; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-12 | Stakeholder-constrained | approved |
| REL-COV-134 | REQ-Art28-13 | legally applies to / constrains | Microsoft Contract | Association | COV-134; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-13 | Stakeholder-constrained | approved |
| REL-COV-135 | REQ-Art28-14 | legally applies to / constrains | Microsoft Contract | Association | COV-135; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-14 | Stakeholder-constrained | approved |
| REL-COV-136 | REQ-Art28-15 | legally applies to / constrains | Microsoft Contract | Association | COV-136; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-15 | Stakeholder-constrained | approved |
| REL-COV-137 | REQ-Art28-16 | legally applies to / constrains | Microsoft Contract | Association | COV-137; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-16 | Stakeholder-constrained | approved |
| REL-COV-138 | REQ-Art28-17 | legally applies to / constrains | Microsoft Contract | Association | COV-138; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-17 | Stakeholder-constrained | approved |
| REL-COV-139 | REQ-Art28-18 | legally applies to / constrains | Microsoft Contract | Association | COV-139; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-18 | Stakeholder-constrained | approved |
| REL-COV-140 | REQ-Art28-19 | legally applies to / constrains | Microsoft Contract | Association | COV-140; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-19 | Stakeholder-constrained | approved |
| REL-COV-141 | REQ-Art28-20 | legally applies to / constrains | Microsoft Contract | Association | COV-141; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-20 | Stakeholder-constrained | approved |
| REL-COV-142 | REQ-Art28-21 | legally applies to / constrains | Microsoft Contract | Association | COV-142; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-21 | Stakeholder-constrained | approved |
| REL-COV-143 | REQ-Art28-22 | legally applies to / constrains | Microsoft Contract | Association | COV-143; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-22 | Stakeholder-constrained | approved |
| REL-COV-144 | REQ-Art28-23 | legally applies to / constrains | Microsoft Contract | Association | COV-144; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-23 | Stakeholder-constrained | approved |
| REL-COV-145 | REQ-Art28-24 | legally applies to / constrains | Microsoft Contract | Association | COV-145; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-24 | Stakeholder-constrained | approved |
| REL-COV-146 | REQ-Art28-25 | legally applies to / constrains | Microsoft Contract | Association | COV-146; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-25 | Stakeholder-constrained | approved |
| REL-COV-147 | REQ-Art28-26 | legally applies to / constrains | Microsoft Contract | Association | COV-147; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-26 | Stakeholder-constrained | approved |
| REL-COV-148 | REQ-Art28-27 | legally applies to / constrains | Microsoft Contract | Association | COV-148; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-27 | Stakeholder-constrained | approved |
| REL-COV-149 | REQ-Art28-28 | legally applies to / constrains | Microsoft Contract | Association | COV-149; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-28 | Stakeholder-constrained | approved |
| REL-COV-150 | REQ-Art28-29 | legally applies to / constrains | Microsoft Contract | Association | COV-150; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-29 | Stakeholder-constrained | approved |
| REL-COV-151 | REQ-Art28-30 | legally applies to / constrains | Microsoft Contract | Association | COV-151; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-30 | Stakeholder-constrained | approved |
| REL-COV-152 | REQ-Art28-31 | legally applies to / constrains | Microsoft Contract | Association | COV-152; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-31 | Stakeholder-constrained | approved |
| REL-COV-153 | REQ-Art28-32 | legally applies to / constrains | Microsoft Contract | Association | COV-153; OP-023–026, OP-068, OP-060; operator Microsoft-contract clarification; REQ-Art28-32 | Stakeholder-constrained | approved |

## Operational Context Coverage

These source records have no defensible DORA effect in the approved scope. They remain represented as role-specific operational context rather than being converted into inferred obligations.

| Context ID | Operational source | Named context stream | Evidence treatment |
| --- | --- | --- | --- |
| CTX-001 | OP-005 | Specification and Mainframe dependency | Context only |
| CTX-002 | OP-007 | Source-system context | Context only |
| CTX-003–004 | OP-015–016 | Development-tool context | Context only |
| CTX-005–007 | OP-020–022 | Licence and VPN provisioning | Context only |
| CTX-008–010 | OP-027–029 | Infrastructure provisioning context | Context only |
| CTX-011–012 | OP-039–040 | Work allocation and planning | Context only |
| CTX-013–016 | OP-043–046 | Decision and requirement intake | Context only |
| CTX-017 | OP-051 | Demand context | Context only |
| CTX-018 | OP-061 / CON-007 | Cross-project visibility gap | Context only; retained as an approved visibility limitation |
| CTX-019–020 | OP-062–063 | Recovery-evidence limitations | Context only; no missing control inferred |
| CTX-021 | OP-067 | C#/.NET technology context | Context only |
| CTX-022 | OP-069 | Management and architect collaboration | Context only |
| CTX-023–024 | OP-086–087 | IDE and mandatory-tool context | Context only |
| CTX-025 | OP-089 | Wider-team visibility limitation | Context only |

**Uncovered register:** empty. The 71 remaining approved source records have a `COV-*` entry above; the 26 listed here have explicit context coverage.

## Stakeholder Legal-Role Placement

| Relationship ID | Source | Meaning | Target | Candidate relation | Evidence | Approval |
| --- | --- | --- | --- | --- | --- | --- |
| REL-ROLE-001 | Employer Bank | assigns the stakeholder role | Back-end Developer | Assignment — Business Actor → Business Role | Approved stakeholder role and operator confirmation of employer | approved |
| REL-ROLE-002 | Employer Bank | is a specific instance of | Credit Institution | Specialization — Business Actor → Business Actor | Operator confirmation; `Chap.I, Art.2, Paragraph 1, Point a` verified in the DORA legal index | approved |

The regulated entity is the Employer Bank / Credit Institution, not the individual Back-end Developer.

## Step 6 Connectivity Clarification Ledger

These relationships were added after Gate 6.2 solely to connect already approved
coverage endpoints to the stakeholder anchor. They do not add a legal duty,
change an ownership state, or assert implementation. The operator approved each
relationship as supported by the cited existing evidence.

| Relationship ID | Source | Meaning | Target | Candidate ArchiMate relation | Evidence | Approval |
| --- | --- | --- | --- | --- | --- | --- |
| REL-OP-090 | Back-end Developer | performs | Framework Maintenance | Assignment | OP-004 | approved |
| REL-OP-091 | Framework Maintenance | maintains | Internal Framework | Association | OP-004 | approved |
| REL-OP-092 | Azure AD / Internal Service Access | restricts | Back-end Developer | Association | OP-017, OP-037, CON-002 | approved |
| REL-OP-093 | Back-end Developer | develops for | Enterprise Data Platform | Association | OP-001–003 | approved |
| REL-OP-094 | Employer Bank | is party to | Microsoft Contract | Association | Operator-confirmed Microsoft provider and contract | approved |

## Validation Record

* **Gate 5.1 — Confirm Requirements:** Approved. Articles 7–13, 17, 24 and 25 retained with atomic requirement decomposition.
* **Gate 5.2 — Confirm Article 28:** Approved by explicit operator direction. Microsoft is the relevant cloud provider and a contract exists.
* **Gate 5.3 — Confirm Legal Index:** Approved. The DORA CELEX-qualified legal index was regenerated and validated.
* **Gate 5.4 — Confirm Legal Anchors:** Approved. Direct Enacting Terms paths were verified; no recital/amendment anchors were retained.
* **Gate 5.5 — Confirm Coverage Resolution:** Approved. COV-001–153 and REL-COV-001–153 are approved; operational context and uncovered register resolved.
* **Gate 5.6 — Confirm Stakeholder Legal Role:** Approved. REL-ROLE-001–002 are approved.
* **Step 6 connectivity clarification:** Approved. REL-OP-090–094 append existing evidence-backed paths without changing the approved coverage or ownership ledger.
* **Step 6 relationship-type correction:** Approved. REL-COV-023–025, REL-COV-037–040, REL-COV-065–068, REL-COV-079–083, and REL-COV-095–098 changed from externally owned Realization to externally owned Association; endpoints, evidence, direct legal-text IDs, and ownership states are unchanged.
