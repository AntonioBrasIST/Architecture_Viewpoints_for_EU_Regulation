# Regulatory Relevance Consensus Report: Back-end Developer — DORA

* Operational footprint source: Methodology/StakeHolders/AT2/3_operational_footprint.md
* Stakeholder classification source: Methodology/StakeHolders/AT2/4_stakeholder_classification.md
* Target regulation: Regulation (EU) 2022/2554 (DORA), CELEX 32022R2554
* Evaluation panel: 3-Agent Panel (4a Literal, 4b Systemic, 4c Gap)
* Applicability fact: AT2 is an approved migrated copy. The Bank is a non-exempt, non-micro DORA financial entity, as confirmed by the operator.

## Legal Index Provenance

* Regulation: DORA
* CELEX: 32022R2554
* Selector: DORA
* Generated workbook: TraceabilityMatrixCreator/OutputDirectory/DORA-CELEX:32022R2554.xlsx
* Generation timestamp: 2026-09-29T00:41:31+01:00
* Validation: row-id --row 1 returned law DORA, CELEX 32022R2554, and Enacting Terms row ID Chap.I. The required Recitals and Enacting Terms sheets and headers were validated.
* Anchor verification: 126 selected Enacting Terms paths passed verify-anchor. No recital, amendment, missing, or ambiguous source was accepted.

## 1. Panel Debate and Consensus Summary

| Article / range | Final status | Resolution |
| :--- | :--- | :--- |
| Arts. 1–4 | Contextual baseline | Subject matter, scope, definitions, and proportionality. |
| Art. 5 | Excluded | AT2 does not identify DORA's legally defined management body. |
| Arts. 6–14 | Unanimous inclusion | Direct chain to platform delivery, change, access, monitoring, incidents, recovery, and communication. |
| Arts. 15–16 | Excluded | ESA technical-standard duty and simplified-framework provision. |
| Arts. 17–19 | Unanimous inclusion | Direct alarm, escalation, remediation, recovery, and incident-information chain. |
| Arts. 20–23 | Excluded | Authority mechanics or specialised conditions lack an AT2 operational chain. |
| Arts. 24–25 | Unanimous inclusion | Code testing and release-readiness link to the mandatory non-micro testing programme. |
| Arts. 26–27 | Excluded | No TLPT designation or specialised tester evidence. |
| Art. 28 | Omitted — no consensus | Technical provider dependency is evidenced; contractual ICT-service evidence is not. |
| Arts. 29–30 | Excluded | No relevant ICT-service contract, assessment, or contract terms are evidenced. |
| Arts. 31–64 | Excluded / baseline | Critical-provider, authority, legislative, amendment, or application provisions. |

## 2. Relevant Articles: Operational Mapping

| Article | Operational anchor | Legal bridge | Ownership and evidence gap |
| :--- | :--- | :--- | :--- |
| 6 | C#/.NET services, Azure DevOps, Kubernetes, data stores, Datadog, service changes, incident work (OP-001–004, OP-018–019, OP-038, OP-066–078) | The Bank's ICT-risk framework governs these assets and activities. | Not evidenced / unclear owner. [Gap—evidence] No framework, control function, audit, review, or audit-remediation evidence. |
| 7 | C#/.NET, Kafka, Cosmos DB, SingleStore, Azure, pipelines, Kubernetes | These are ICT systems/tools used to process data and provide services. | Stakeholder-constrained. [Gap—evidence] No capacity or stressed-condition resilience-test evidence. |
| 8 | Services, pipelines, cloud platforms, data stores, dependencies, visibility limit (OP-061, OP-066–068, OP-089) | Assets and dependencies must be classified, mapped, and risk assessed. | Not evidenced / unclear owner. [Gap] Cross-project visibility prevents complete dependency evidence. |
| 9 | Data transformation, Azure AD, pull requests, approvals, deployments, updates | Governs security, access, data handling, and change control. | Mixed direct/constrained/external. [Gap—evidence] Formal security, authentication, patch, and enterprise change-policy evidence is absent. |
| 10 | Datadog monitoring and Monitoring Team escalation | Forms the alert-to-response detection chain. | Developer monitors; Monitoring Team escalates. [Gap—evidence] No formal thresholds, automated alerts, or regular detection tests. |
| 11 | Outage impact, escalation, software/infrastructure remediation, restored data | Constrains continuity, response, impact, recovery, testing, and crisis management. | Stakeholder-constrained. [Gap—evidence] No BIA, continuity plan, crisis function, or test evidence; OP-062 identifies no known workaround. |
| 12 | Database/Kafka data flows and restored platform availability | Governs backup, restoration, recovery, and integrity. | Not evidenced / unclear owner. [Gap—evidence] No backup, restoration-test, recovery-objective, or reconciliation evidence. |
| 13 | Datadog investigation, fixes, dependency updates, recovery | Incident evidence must feed learning and risk improvements. | Stakeholder-constrained. [Gap—evidence] No formal review, learning, or training evidence. |
| 14 | Outage/customer impact and incident escalation | The incident chain must connect to crisis communication. | Not evidenced / unclear owner. [Gap—evidence] No crisis plan, policy, or designated communicator. |
| 17 | Datadog Alarm → Monitoring Team → remediation → recovery | Direct ICT-incident-management chain. | Stakeholder-constrained. [Gap—evidence] No logging, classification, root-cause, or formal follow-up evidence. |
| 18 | Outage impact, causes, diagnosis, recovery, consumers, data flow | These are inputs to statutory incident classification. | Not evidenced / unclear owner. [Gap—evidence] No classification process or Article 18 criteria evidence. |
| 19 | Detection, escalation, diagnosis, remediation, recovery, customer impact | These are reporting inputs, not evidence that the developer reports. | Not evidenced / unclear owner. [Gap—evidence] No reporting route, owner, template, client-notification process, or report sequence. |
| 24 | Unit/code testing, validation, pull-request review, release readiness | Development testing belongs within the mandatory resilience-testing programme. | Stakeholder-constrained. [Gap—evidence] No comprehensive programme, independent testing, or annual critical-system testing evidence. |
| 25 | Test/DEV readiness, data mapping, unit tests, review, release gate | Specifies proportionate test types for the resilience-testing programme. | Direct code testing contribution. [Gap—evidence] No risk-based test-selection rationale beyond described tests. |

## 3. Statutory Requirement Catalogue and Verified Direct IDs

### Article 6 — ICT risk-management framework

* [REQ-Art6-01] Maintain a sound, comprehensive, documented ICT risk-management framework.
* [REQ-Art6-02] Ensure it enables quick, efficient, comprehensive ICT-risk treatment and high resilience.
* [REQ-Art6-03] Include strategies, policies, procedures, protocols, and tools.
* [REQ-Art6-04] Protect information and ICT assets including software, hardware, and servers.
* [REQ-Art6-05] Protect physical components and infrastructure from damage and unauthorised access or use.
* [REQ-Art6-06] Minimise ICT-risk impact with suitable controls.
* [REQ-Art6-07] Provide current ICT-risk/framework information to the competent authority on request.
* [REQ-Art6-08] Assign ICT-risk management and oversight to an independent control function.
* [REQ-Art6-09] Segregate ICT-risk management, control, and internal audit functions.
* [REQ-Art6-10] Document and review the framework annually and after statutory review triggers.
* [REQ-Art6-11] Continuously improve the framework from implementation and monitoring lessons.
* [REQ-Art6-12] Submit the framework-review report to the competent authority on request.
* [REQ-Art6-13] Subject the framework to regular internal audit.
* [REQ-Art6-14] Ensure ICT auditors have knowledge, skills, expertise, and independence.
* [REQ-Art6-15] Set ICT-audit frequency and focus proportionately to ICT risk.
* [REQ-Art6-16] Establish formal follow-up for internal-audit conclusions.
* [REQ-Art6-17] Verify and remediate critical ICT-audit findings promptly.
* [REQ-Art6-18] Include a digital operational-resilience strategy.
* [REQ-Art6-19] Explain support for business strategy and objectives.
* [REQ-Art6-20] Set ICT-risk tolerance and analyse ICT-disruption impact tolerance.
* [REQ-Art6-21] Set information-security objectives, KPIs, and key-risk metrics.
* [REQ-Art6-22] Explain the ICT reference architecture and necessary changes.
* [REQ-Art6-23] Describe incident detection, prevention, and protection mechanisms.
* [REQ-Art6-24] Evidence resilience through incident information and preventive-control effectiveness.
* [REQ-Art6-25] Implement Chapter IV digital operational-resilience testing.
* [REQ-Art6-26] Outline the Article 14 communication strategy.
* [REQ-Art6-27] Where compliance verification is outsourced, retain responsibility for it.

Verified direct legal-text IDs:

* REQ-Art6-01–02 → Chap.II, Section II, Art.6, Paragraph 1.
* REQ-Art6-03–05 → Chap.II, Section II, Art.6, Paragraph 2.
* REQ-Art6-06–07 → Chap.II, Section II, Art.6, Paragraph 3.
* REQ-Art6-08–09 → Chap.II, Section II, Art.6, Paragraph 4.
* REQ-Art6-10–12 → Chap.II, Section II, Art.6, Paragraph 5.
* REQ-Art6-13–15 → Chap.II, Section II, Art.6, Paragraph 6.
* REQ-Art6-16–17 → Chap.II, Section II, Art.6, Paragraph 7.
* REQ-Art6-18 → Chap.II, Section II, Art.6, Paragraph 8.
* REQ-Art6-19 → Chap.II, Section II, Art.6, Paragraph 8, Point a.
* REQ-Art6-20 → Chap.II, Section II, Art.6, Paragraph 8, Point b.
* REQ-Art6-21 → Chap.II, Section II, Art.6, Paragraph 8, Point c.
* REQ-Art6-22 → Chap.II, Section II, Art.6, Paragraph 8, Point d.
* REQ-Art6-23 → Chap.II, Section II, Art.6, Paragraph 8, Point e.
* REQ-Art6-24 → Chap.II, Section II, Art.6, Paragraph 8, Point f.
* REQ-Art6-25 → Chap.II, Section II, Art.6, Paragraph 8, Point g.
* REQ-Art6-26 → Chap.II, Section II, Art.6, Paragraph 8, Point h.
* REQ-Art6-27 → Chap.II, Section II, Art.6, Paragraph 10.

### Article 7 — ICT systems, protocols and tools

* [REQ-Art7-01] Use and maintain updated ICT systems, protocols, and tools.
* [REQ-Art7-02] Make them appropriate to the magnitude of operations.
* [REQ-Art7-03] Ensure they are reliable.
* [REQ-Art7-04] Ensure sufficient data-processing and service capacity, including peak demand and new technology.
* [REQ-Art7-05] Ensure technological resilience under stressed or other adverse conditions.

Verified direct legal-text IDs:

* REQ-Art7-01 → Chap.II, Section II, Art.7, Paragraph 1.
* REQ-Art7-02 → Chap.II, Section II, Art.7, Paragraph 1, Point a.
* REQ-Art7-03 → Chap.II, Section II, Art.7, Paragraph 1, Point b.
* REQ-Art7-04 → Chap.II, Section II, Art.7, Paragraph 1, Point c.
* REQ-Art7-05 → Chap.II, Section II, Art.7, Paragraph 1, Point d.

### Article 8 — Identification

* [REQ-Art8-01] Identify, classify, and document ICT-supported business functions, roles, and responsibilities.
* [REQ-Art8-02] Identify, classify, and document supporting information/ICT assets and dependencies.
* [REQ-Art8-03] Review classifications and documentation at least yearly.
* [REQ-Art8-04] Continuously identify ICT-risk sources.
* [REQ-Art8-05] Assess relevant cyber threats and ICT vulnerabilities.
* [REQ-Art8-06] Review relevant risk scenarios regularly and at least yearly.
* [REQ-Art8-07] Risk-assess every major relevant infrastructure, process, or procedure change.
* [REQ-Art8-08] Identify all information and ICT assets.
* [REQ-Art8-09] Map assets considered critical.
* [REQ-Art8-10] Map configurations, links, and interdependencies.
* [REQ-Art8-11] Identify and document processes dependent on ICT third-party providers.
* [REQ-Art8-12] Identify provider interconnections supporting critical/important functions.
* [REQ-Art8-13] Maintain and update relevant inventories.
* [REQ-Art8-14] Assess legacy ICT-system risk regularly and before/after technology connections.

Verified direct legal-text IDs:

* REQ-Art8-01–03 → Chap.II, Section II, Art.8, Paragraph 1.
* REQ-Art8-04–06 → Chap.II, Section II, Art.8, Paragraph 2.
* REQ-Art8-07 → Chap.II, Section II, Art.8, Paragraph 3.
* REQ-Art8-08–10 → Chap.II, Section II, Art.8, Paragraph 4.
* REQ-Art8-11–12 → Chap.II, Section II, Art.8, Paragraph 5.
* REQ-Art8-13 → Chap.II, Section II, Art.8, Paragraph 6.
* REQ-Art8-14 → Chap.II, Section II, Art.8, Paragraph 7.

### Article 9 — Protection and prevention

* [REQ-Art9-01] Continuously monitor and control ICT-system/tool security and functioning.
* [REQ-Art9-02] Minimise ICT-risk impact using security tools, policies, and procedures.
* [REQ-Art9-03] Design, procure, and implement ICT-security controls for resilience, continuity, and availability.
* [REQ-Art9-04] Maintain data availability, authenticity, integrity, and confidentiality.
* [REQ-Art9-05] Use ICT solutions and processes proportionate to risk.
* [REQ-Art9-06] Secure data-transfer means.
* [REQ-Art9-07] Minimise data corruption, loss, unauthorised access, and technical flaws.
* [REQ-Art9-08] Prevent unavailability, impaired authenticity/integrity, confidentiality breaches, and data loss.
* [REQ-Art9-09] Protect data from management, administration, processing, and human-error risks.
* [REQ-Art9-10] Develop and document an information-security policy.
* [REQ-Art9-11] Establish risk-based network and infrastructure management.
* [REQ-Art9-12] Limit physical/logical access to approved functions and activities.
* [REQ-Art9-13] Establish access-right policies, procedures, and administration controls.
* [REQ-Art9-14] Implement strong authentication and cryptographic-key protection.
* [REQ-Art9-15] Maintain documented, risk-based ICT change-management controls.
* [REQ-Art9-16] Record, test, assess, approve, implement, and verify ICT changes under control.
* [REQ-Art9-17] Maintain documented patch and update policies.
* [REQ-Art9-18] Enable prompt severance or segmentation of network connections to limit contagion.
* [REQ-Art9-19] Obtain appropriate management approval and use specific change-management protocols.

Verified direct legal-text IDs:

* REQ-Art9-01–02 → Chap.II, Section II, Art.9, Paragraph 1.
* REQ-Art9-03–04 → Chap.II, Section II, Art.9, Paragraph 2.
* REQ-Art9-05 → Chap.II, Section II, Art.9, Paragraph 3.
* REQ-Art9-06 → Chap.II, Section II, Art.9, Paragraph 3, Point a.
* REQ-Art9-07 → Chap.II, Section II, Art.9, Paragraph 3, Point b.
* REQ-Art9-08 → Chap.II, Section II, Art.9, Paragraph 3, Point c.
* REQ-Art9-09 → Chap.II, Section II, Art.9, Paragraph 3, Point d.
* REQ-Art9-10 → Chap.II, Section II, Art.9, Paragraph 4.
* REQ-Art9-11 → Chap.II, Section II, Art.9, Paragraph 4, Point a.
* REQ-Art9-12 → Chap.II, Section II, Art.9, Paragraph 4, Point b.
* REQ-Art9-13 → Chap.II, Section II, Art.9, Paragraph 4, Point c.
* REQ-Art9-14 → Chap.II, Section II, Art.9, Paragraph 4, Point d.
* REQ-Art9-15–16 → Chap.II, Section II, Art.9, Paragraph 4, Point e.
* REQ-Art9-17 → Chap.II, Section II, Art.9, Paragraph 4, Point f.
* REQ-Art9-18 → Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 1.
* REQ-Art9-19 → Chap.II, Section II, Art.9, Paragraph 4, Sub-Paragraph 2.

### Article 10 — Detection

* [REQ-Art10-01] Promptly detect anomalous activity, performance issues, ICT incidents, and material single points of failure.
* [REQ-Art10-02] Regularly test detection mechanisms.
* [REQ-Art10-03] Provide layered controls, thresholds, triggers, and automatic alerts.
* [REQ-Art10-04] Resource monitoring of user activity, anomalies, incidents, and cyber-attacks.
* [REQ-Art10-05] If a data reporting service provider, check trade reports and request retransmission for omissions/errors.

Verified direct legal-text IDs:

* REQ-Art10-01 → Chap.II, Section II, Art.10, Paragraph 1.
* REQ-Art10-02 → Chap.II, Section II, Art.10, Paragraph 1, Sub-Paragraph 1.
* REQ-Art10-03 → Chap.II, Section II, Art.10, Paragraph 2.
* REQ-Art10-04 → Chap.II, Section II, Art.10, Paragraph 3.
* REQ-Art10-05 → Chap.II, Section II, Art.10, Paragraph 4.

### Article 11 — Response and recovery

* [REQ-Art11-01] Establish an ICT business-continuity policy.
* [REQ-Art11-02] Implement documented continuity arrangements, plans, procedures, and mechanisms.
* [REQ-Art11-03] Ensure critical/important-function continuity.
* [REQ-Art11-04] Resolve ICT incidents quickly, limit damage, and prioritise recovery.
* [REQ-Art11-05] Activate containment and tailored response/recovery procedures without delay.
* [REQ-Art11-06] Estimate preliminary incident impacts, damages, and losses.
* [REQ-Art11-07] Communicate updated information and report as Article 19 requires.
* [REQ-Art11-08] Implement audited ICT response and recovery plans.
* [REQ-Art11-09] Maintain and periodically test continuity plans, including outsourced/contracted critical functions.
* [REQ-Art11-10] Conduct a business-impact analysis for severe disruptions.
* [REQ-Art11-11] Use appropriate quantitative/qualitative criteria, data, and scenarios.
* [REQ-Art11-12] Consider functions, processes, provider dependencies, assets, and interdependencies.
* [REQ-Art11-13] Align ICT assets/services with the BIA, including critical-component redundancy.
* [REQ-Art11-14] Test continuity and response/recovery plans yearly and after relevant changes.
* [REQ-Art11-15] Test crisis-communication plans.
* [REQ-Art11-16] Test cyber-attack and switchover scenarios.
* [REQ-Art11-17] Review plans using test, audit, and supervisory-review results.
* [REQ-Art11-18] Maintain a crisis-management function and internal/external crisis procedures.
* [REQ-Art11-19] Keep accessible records before/during activated disruption events.
* [REQ-Art11-20] Provide annual major-incident cost/loss estimates on request.

Verified direct legal-text IDs:

* REQ-Art11-01 → Chap.II, Section II, Art.11, Paragraph 1.
* REQ-Art11-02 → Chap.II, Section II, Art.11, Paragraph 2.
* REQ-Art11-03 → Chap.II, Section II, Art.11, Paragraph 2, Point a.
* REQ-Art11-04 → Chap.II, Section II, Art.11, Paragraph 2, Point b.
* REQ-Art11-05 → Chap.II, Section II, Art.11, Paragraph 2, Point c.
* REQ-Art11-06 → Chap.II, Section II, Art.11, Paragraph 2, Point d.
* REQ-Art11-07 → Chap.II, Section II, Art.11, Paragraph 2, Point e.
* REQ-Art11-08 → Chap.II, Section II, Art.11, Paragraph 3.
* REQ-Art11-09 → Chap.II, Section II, Art.11, Paragraph 4.
* REQ-Art11-10–13 → Chap.II, Section II, Art.11, Paragraph 5.
* REQ-Art11-14 → Chap.II, Section II, Art.11, Paragraph 6; Chap.II, Section II, Art.11, Paragraph 6, Point a.
* REQ-Art11-15 → Chap.II, Section II, Art.11, Paragraph 6, Point b.
* REQ-Art11-16 → Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 1.
* REQ-Art11-17 → Chap.II, Section II, Art.11, Paragraph 6, Sub-Paragraph 2.
* REQ-Art11-18 → Chap.II, Section II, Art.11, Paragraph 7.
* REQ-Art11-19 → Chap.II, Section II, Art.11, Paragraph 8.
* REQ-Art11-20 → Chap.II, Section II, Art.11, Paragraph 10.

### Article 12 — Backup, restoration and recovery

* [REQ-Art12-01] Document backup scope and frequency by criticality/confidentiality.
* [REQ-Art12-02] Document restoration and recovery procedures and methods.
* [REQ-Art12-03] Establish activatable backup systems.
* [REQ-Art12-04] Ensure backup activation preserves security and data availability, authenticity, integrity, and confidentiality.
* [REQ-Art12-05] Periodically test backup, restoration, and recovery procedures.
* [REQ-Art12-06] Use source-system-segregated ICT systems for own-system data restoration.
* [REQ-Art12-07] Protect restoration systems from unauthorised access and corruption.
* [REQ-Art12-08] Enable timely restoration using data and system backups.
* [REQ-Art12-09] Maintain adequate redundant ICT capacity and resources.
* [REQ-Art12-10] Set recovery-time/recovery-point objectives by criticality and market-efficiency impact.
* [REQ-Art12-11] Meet agreed service levels in extreme scenarios.
* [REQ-Art12-12] Perform recovery checks and reconciliations to preserve data integrity.

Verified direct legal-text IDs:

* REQ-Art12-01 → Chap.II, Section II, Art.12, Paragraph 1, Point a.
* REQ-Art12-02 → Chap.II, Section II, Art.12, Paragraph 1, Point b.
* REQ-Art12-03–05 → Chap.II, Section II, Art.12, Paragraph 2.
* REQ-Art12-06–08 → Chap.II, Section II, Art.12, Paragraph 3.
* REQ-Art12-09 → Chap.II, Section II, Art.12, Paragraph 4.
* REQ-Art12-10–11 → Chap.II, Section II, Art.12, Paragraph 6.
* REQ-Art12-12 → Chap.II, Section II, Art.12, Paragraph 7.

### Article 13 — Learning and evolving

* [REQ-Art13-01] Maintain capability/staff to gather vulnerability, threat, and incident information.
* [REQ-Art13-02] Analyse its resilience impact.
* [REQ-Art13-03] Conduct post-major-incident reviews.
* [REQ-Art13-04] Analyse disruption causes and identify ICT/continuity improvements.
* [REQ-Art13-05] Communicate implemented post-review changes to the authority on request.
* [REQ-Art13-06] Determine whether procedures were followed and actions effective.
* [REQ-Art13-07] Review alert response and severity/impact determination.
* [REQ-Art13-08] Review forensic-analysis quality and speed where appropriate.
* [REQ-Art13-09] Review incident-escalation effectiveness.
* [REQ-Art13-10] Review internal/external communication effectiveness.
* [REQ-Art13-11] Continuously incorporate lessons into ICT-risk assessment.
* [REQ-Art13-12] Use findings to review the ICT risk-management framework.
* [REQ-Art13-13] Monitor resilience-strategy effectiveness.
* [REQ-Art13-14] Map ICT-risk evolution and analyse incident patterns.
* [REQ-Art13-15] Have senior ICT staff report yearly findings/recommendations to the management body.
* [REQ-Art13-16] Make security-awareness and resilience training compulsory and role appropriate.
* [REQ-Art13-17] Monitor technological developments and keep ICT-risk processes current.

Verified direct legal-text IDs:

* REQ-Art13-01–02 → Chap.II, Section II, Art.13, Paragraph 1.
* REQ-Art13-03–04 → Chap.II, Section II, Art.13, Paragraph 2.
* REQ-Art13-05 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 1.
* REQ-Art13-06 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2.
* REQ-Art13-07 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point a.
* REQ-Art13-08 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point b.
* REQ-Art13-09 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point c.
* REQ-Art13-10 → Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2, Point d.
* REQ-Art13-11–12 → Chap.II, Section II, Art.13, Paragraph 3.
* REQ-Art13-13–14 → Chap.II, Section II, Art.13, Paragraph 4.
* REQ-Art13-15 → Chap.II, Section II, Art.13, Paragraph 5.
* REQ-Art13-16 → Chap.II, Section II, Art.13, Paragraph 6.
* REQ-Art13-17 → Chap.II, Section II, Art.13, Paragraph 7.

### Article 14 — Communication

* [REQ-Art14-01] Establish crisis-communication plans for responsible incident/vulnerability disclosure.
* [REQ-Art14-02] Implement internal-staff and external-stakeholder communication policies.
* [REQ-Art14-03] Task at least one person with incident-communication and public/media responsibilities.

Verified direct legal-text IDs:

* REQ-Art14-01 → Chap.II, Section II, Art.14, Paragraph 1.
* REQ-Art14-02 → Chap.II, Section II, Art.14, Paragraph 2.
* REQ-Art14-03 → Chap.II, Section II, Art.14, Paragraph 3.

### Article 17 — ICT-related incident-management process

* [REQ-Art17-01] Define, establish, and implement an incident-management process.
* [REQ-Art17-02] Record all ICT incidents and significant cyber threats.
* [REQ-Art17-03] Establish integrated monitoring, handling, and follow-up.
* [REQ-Art17-04] Identify, document, and address root causes to prevent recurrence.
* [REQ-Art17-05] Establish early-warning indicators.
* [REQ-Art17-06] Identify, track, log, categorise, and classify incidents.
* [REQ-Art17-07] Assign roles/responsibilities for incident types and scenarios.
* [REQ-Art17-08] Plan communication, notification, and internal escalation.
* [REQ-Art17-09] Report major incidents to senior management and inform the management body.
* [REQ-Art17-10] Establish response procedures that mitigate impact and restore secure services promptly.

Verified direct legal-text IDs:

* REQ-Art17-01 → Chap.III, Art.17, Paragraph 1.
* REQ-Art17-02–04 → Chap.III, Art.17, Paragraph 2.
* REQ-Art17-05 → Chap.III, Art.17, Paragraph 3, Point a.
* REQ-Art17-06 → Chap.III, Art.17, Paragraph 3, Point b.
* REQ-Art17-07 → Chap.III, Art.17, Paragraph 3, Point c.
* REQ-Art17-08 → Chap.III, Art.17, Paragraph 3, Point d.
* REQ-Art17-09 → Chap.III, Art.17, Paragraph 3, Point e.
* REQ-Art17-10 → Chap.III, Art.17, Paragraph 3, Point f.

### Article 18 — Classification

* [REQ-Art18-01] Classify ICT incidents and determine their impact.
* [REQ-Art18-02] Use affected-client/counterparty, transactions, and reputational impact.
* [REQ-Art18-03] Use duration and service downtime.
* [REQ-Art18-04] Use geographical spread.
* [REQ-Art18-05] Use data loss affecting availability, authenticity, integrity, or confidentiality.
* [REQ-Art18-06] Use affected-service, transaction, and operation criticality.
* [REQ-Art18-07] Use direct and indirect economic cost/loss.
* [REQ-Art18-08] Classify significant cyber threats using statutory criteria.

Verified direct legal-text IDs:

* REQ-Art18-01 → Chap.III, Art.18, Paragraph 1.
* REQ-Art18-02 → Chap.III, Art.18, Paragraph 1, Point a.
* REQ-Art18-03 → Chap.III, Art.18, Paragraph 1, Point b.
* REQ-Art18-04 → Chap.III, Art.18, Paragraph 1, Point c.
* REQ-Art18-05 → Chap.III, Art.18, Paragraph 1, Point d.
* REQ-Art18-06 → Chap.III, Art.18, Paragraph 1, Point e.
* REQ-Art18-07 → Chap.III, Art.18, Paragraph 1, Point f.
* REQ-Art18-08 → Chap.III, Art.18, Paragraph 2.

### Article 19 — Major-incident reporting

* [REQ-Art19-01] Report major ICT incidents to the relevant competent authority.
* [REQ-Art19-02] Collect/analyse information and prepare/submit initial notifications and reports using Article 20 templates.
* [REQ-Art19-03] Use alternative notification means when technical impossibility prevents template submission.
* [REQ-Art19-04] Include information needed to assess significance and cross-border impact.
* [REQ-Art19-05] Significant-cyber-threat notification is voluntary.
* [REQ-Art19-06] Inform affected clients without undue delay and describe mitigation measures.
* [REQ-Art19-07] Where applicable, inform potentially affected clients of appropriate protection measures.
* [REQ-Art19-08] Submit the initial notification within prescribed time.
* [REQ-Art19-09] Submit an intermediate report and relevant updates.
* [REQ-Art19-10] Submit a final report after root-cause analysis and actual-impact figures.
* [REQ-Art19-11] Retain responsibility where reporting is outsourced.

Verified direct legal-text IDs:

* REQ-Art19-01 → Chap.III, Art.19, Paragraph 1.
* REQ-Art19-02–03 → Chap.III, Art.19, Paragraph 1, Sub-Paragraph 3.
* REQ-Art19-04 → Chap.III, Art.19, Paragraph 1, Sub-Paragraph 4.
* REQ-Art19-05 → Chap.III, Art.19, Paragraph 2.
* REQ-Art19-06 → Chap.III, Art.19, Paragraph 3.
* REQ-Art19-07 → Chap.III, Art.19, Paragraph 3, Sub-Paragraph 1.
* REQ-Art19-08 → Chap.III, Art.19, Paragraph 4, Point a.
* REQ-Art19-09 → Chap.III, Art.19, Paragraph 4, Point b.
* REQ-Art19-10 → Chap.III, Art.19, Paragraph 4, Point c.
* REQ-Art19-11 → Chap.III, Art.19, Paragraph 5.

### Article 24 — Digital operational-resilience testing

* [REQ-Art24-01] Establish, maintain, and review a comprehensive resilience-testing programme.
* [REQ-Art24-02] Include assessments, tests, methodologies, practices, and tools under Articles 25–26.
* [REQ-Art24-03] Use a risk-based approach reflecting risk, exposure, and criticality.
* [REQ-Art24-04] Use independent internal/external testers.
* [REQ-Art24-05] Resource internal testing and avoid conflicts of interest.
* [REQ-Art24-06] Prioritise, classify, and remedy test findings.
* [REQ-Art24-07] Validate that identified weaknesses, deficiencies, and gaps are addressed.
* [REQ-Art24-08] Test every ICT system/application supporting critical or important functions at least yearly.

Verified direct legal-text IDs:

* REQ-Art24-01 → Chap.IV, Art.24, Paragraph 1.
* REQ-Art24-02 → Chap.IV, Art.24, Paragraph 2.
* REQ-Art24-03 → Chap.IV, Art.24, Paragraph 3.
* REQ-Art24-04–05 → Chap.IV, Art.24, Paragraph 4.
* REQ-Art24-06–07 → Chap.IV, Art.24, Paragraph 5.
* REQ-Art24-08 → Chap.IV, Art.24, Paragraph 6.

### Article 25 — Testing of ICT tools and systems

* [REQ-Art25-01] Provide Article 4-proportionate ICT tests in the resilience-testing programme.
* [REQ-Art25-02] Select appropriate vulnerability, open-source, network-security, gap, physical-security, source-code, scenario, compatibility, performance, end-to-end, and penetration tests.
* [REQ-Art25-03] If the Bank is a CSD or CCP, assess vulnerabilities before relevant deployment/redeployment.
* [REQ-Art25-04] The microenterprise-specific strategic testing condition is inapplicable because the Bank is non-micro.

Verified direct legal-text IDs:

* REQ-Art25-01–02 → Chap.IV, Art.25, Paragraph 1.
* REQ-Art25-03 → Chap.IV, Art.25, Paragraph 2.
* REQ-Art25-04 → Chap.IV, Art.25, Paragraph 3.

## 4. Conditional Requirements Outside Stakeholder Coverage

* REQ-Art6-27: no evidence that ICT-risk compliance verification has been outsourced.
* REQ-Art10-05: no evidence that the Bank is a data reporting service provider.
* REQ-Art25-03: no evidence that the Bank is a central securities depository or central counterparty.
* REQ-Art25-04: inapplicable because the Bank is confirmed non-micro.

These direct legal sources are retained for statutory completeness but are not unresolved coverage items and are not stakeholder realizations.

## 5. Footprint-Regulation Coverage and Relationship Ledger

| Coverage / relationship | Source → legal endpoint | Covered REQ range | Effect / ownership |
|---|---|---|---|
| COV-001 / REL-COV-001 | Platform Development → ICT risk-framework core | Art. 6, REQ-01–07 | Operates under; Not evidenced / unclear owner |
| COV-002 / REL-COV-002 | Change and release work → framework governance/audit/remediation | Art. 6, REQ-08–17 | Is governed by; Externally owned |
| COV-003 / REL-COV-003 | Monitoring and incident work → resilience strategy controls | Art. 6, REQ-18–26 | Provides operational input to; Not evidenced / unclear owner |
| COV-004 / REL-COV-004 | Platform Development → reliable ICT systems/capacity | Art. 7, REQ-01–05 | Uses and maintains; Stakeholder-constrained |
| COV-005 / REL-COV-005 | Enterprise Data Platform → asset/dependency classification | Art. 8, REQ-01–14 | Requires identification of; Not evidenced / unclear owner |
| COV-006 / REL-COV-006 | Production Monitoring → security/function monitoring | Art. 9, REQ-01–02 | Realizes monitoring of; Directly performed |
| COV-007 / REL-COV-007 | Data-platform work → secure data handling | Art. 9, REQ-03–09 | Is constrained by; Stakeholder-constrained |
| COV-008 / REL-COV-008 | Access and approval controls → security/access policy | Art. 9, REQ-10–14 | Constrains; Externally owned |
| COV-009 / REL-COV-009 | Test/release work → controlled change and patch controls | Art. 9, REQ-15–19 | Is constrained by; Stakeholder-constrained |
| COV-010 / REL-COV-010 | Production Monitoring → detection capability | Art. 10, REQ-01 and REQ-04 | Realizes monitoring of; Directly performed |
| COV-011 / REL-COV-011 | Monitoring Team → detection testing/thresholds/alerting | Art. 10, REQ-02–03 | Supports; Externally owned |
| COV-012 / REL-COV-012 | Incident response chain → continuity and recovery controls | Art. 11, REQ-01–20 | Is constrained by; Stakeholder-constrained |
| COV-013 / REL-COV-013 | Platform data recovery → backup/restoration/integrity controls | Art. 12, REQ-01–12 | Depends on; Not evidenced / unclear owner |
| COV-014 / REL-COV-014 | Software remediation → learning and improvement | Art. 13, REQ-01–17 | Provides evidence to; Stakeholder-constrained |
| COV-015 / REL-COV-015 | Incident escalation → crisis communications | Art. 14, REQ-01–03 | Triggers; Not evidenced / unclear owner |
| COV-016 / REL-COV-016 | Incident escalation → incident-management process | Art. 17, REQ-01–10 | Is governed by; Stakeholder-constrained |
| COV-017 / REL-COV-017 | Incident facts → incident classification | Art. 18, REQ-01–08 | Supplies classification input to; Not evidenced / unclear owner |
| COV-018 / REL-COV-018 | Incident information → major-incident reporting | Art. 19, REQ-01–11 | Supplies reporting input to; Not evidenced / unclear owner |
| COV-019 / REL-COV-019 | Test/DEV Readiness → resilience-testing programme | Art. 24, REQ-01–08 | Contributes to; Stakeholder-constrained |
| COV-020 / REL-COV-020 | Test/DEV Readiness → ICT test selection/execution | Art. 25, REQ-01–02 | Realizes code-testing contribution to; Directly performed |

Evidence includes OP-008–014, OP-038, OP-048–050, OP-059–080, OP-065–068, OP-081–085, and REL-OP-079–089. The direct legal-text IDs for every REQ range are listed in Section 3.

## 6. Operational Context Coverage

| Context stream | Operational source IDs |
|---|---|
| Platform delivery and data lifecycle | OP-001–008, OP-048–050, OP-065–067, OP-081–083 |
| Change and release governance | OP-009–013, OP-038–047, OP-064, OP-084–085 |
| Monitoring and incident recovery | OP-014, OP-060, OP-062–063, OP-070–080 |
| Platform operations and access | OP-015–020, OP-053–054, OP-086–088 |
| Provider and infrastructure dependencies | OP-021–029, OP-052, OP-059, OP-068 |
| Consumer service and data ownership | OP-030–037, OP-049, OP-051 |
| Specifications, decisions, and work allocation | OP-039–047, OP-069 |
| Constraints and visibility limits | OP-055–058, OP-061, OP-089 |
| Concerns retained by origin | CON-001–008 |

## 7. Uncovered Register

No unresolved in-scope legal requirement or operational source remains. OP-062 and OP-063 remain evidence limitations, not findings that the Bank lacks a control.

## 8. Stakeholder Legal-Role Placement Ledger

| Relationship ID | Source | Meaning | Target | ArchiMate relationship | Evidence | Approval |
|---|---|---|---|---|---|---|
| REL-ROLE-001 | The Bank (Business Actor) | assigns the role of | Back-end Developer (Business Role) | Assignment | Approved AT2 migration; stakeholder context says the developer works at the Bank. | Gate 5.6 approved |
| REL-ROLE-002 | The Bank (Business Actor) | fulfils the law-defined role of | DORA Financial Entity (Business Role) | Assignment | Operator-confirmed non-exempt, non-micro DORA status; Chap.I, Art.2, Paragraph 1 verified through verify-anchor. | Gate 5.6 approved |

The Back-end Developer is not a DORA Financial Entity and is not represented as one.

## Validation Record

* Gate 5.1 — Confirm Agreed Articles: approved. Arts. 6–14, 17–19, and 24–25 retained.
* Gate 5.2 — Confirm Omitted Articles: approved. Art. 28 kept omitted; Arts. 29–30 excluded.
* Gate 5.3 — Confirm Legal Index: approved. DORA index regenerated with selector DORA.
* Gate 5.4 — Confirm Legal Text IDs: approved. 126 direct Enacting Terms paths verified; the REQ-Art6-10 correction was approved before persistence.
* Gate 5.5 — Confirm Coverage Resolution: approved. Every in-scope REQ, OP, and CON record has coverage or a named context assignment.
* Gate 5.6 — Confirm Stakeholder Legal Role: approved. The legal-role chain is limited to The Bank, Back-end Developer, and DORA Financial Entity.
