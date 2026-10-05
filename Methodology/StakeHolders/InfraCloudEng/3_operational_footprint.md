# Stakeholder Operational Footprint

**Pipeline stage:** Step 3 — approved operational facts, relationships, friction, and gaps  
**Stakeholder:** Infrastructure Engineer / Cloud Database Administrator  
**Context:** Internal infrastructure, cloud platform, and production databases at a DORA-regulated financial entity. The regulatory context is operator-provided and is not an interview-derived operational fact.

## 1. Core Role Context

The stakeholder administers Starburst, OpenMetadata, and SingleStore within the data technology layer. Their stated work includes granting access, investigating developer connection and usage issues, maintaining technology through updates and configuration changes, testing production changes, and participating in production/on-call incident response. The stakeholder's team is accountable for the technologies it configures.

## 2. Everyday Tasks

- Provision required user access, including Starburst access control through Ranger policies.
- Investigate developers' connection and technology-usage issues.
- Maintain the data technology layer through updates and configuration changes.
- Partly automate access-control work with Python.
- Assist colleagues with Kafka, Cosmos, and Databricks issues.
- Back up Ranger data, migrate Starburst deployment to GitOps, and validate deployments.
- Test updates in non-production environments before production deployment.
- Use `kubectl`, Git, VS Code, Python, and LLM tools for administration, configuration, validation, and investigation.
- Retrieve passwords and secrets where necessary to correct issues; avoid table-data changes unless an approved DevOps change instructs one.
- Record production changes in ServiceNow, support non-production testing through incidents, and perform change reviews.
- Respond to SingleStore incidents by restarting, investigating, mitigating, and reporting to technology support.

## 3. Key Dependencies

- AKS/compute team for underlying compute support and correction.
- Networking team for connection issues.
- Technology support teams for issue correction and extreme SingleStore incidents.
- Security team for access-request approval.
- Authorization team for production-change authorization.
- DevOps teams for collaborative change validation and as consumers of an unspecified work result.
- Azure DevOps, Azure Key Vault, AKS External Secrets, ServiceNow, Datadog, Ranger, and Flux.

## 4. Operational Insights & Friction

- **OP-052 — Friction:** Access provisioning remains time-consuming despite partial Python automation because Starburst access control has multiple Ranger policy components.
- **OP-053 — Friction:** Connection and compute-related tasks stop while the responsible team resolves the dependency.
- **OP-054 — Friction:** SingleStore failures can halt front-facing applications and other services, requiring urgent remediation.
- **OP-055 — Friction:** The stakeholder describes daily work as monotonous.
- **OP-056 — [Gap]:** The source does not identify the system or team that automatically assigns a production-change authorization status.
- **OP-057 — [Gap]:** The concrete output used by DevOps teams is unknown.
- **OP-058 — [Gap]:** Non-production work requested by other teams can be tested through ServiceNow incidents without an official change record.

These are operational observations and visibility limitations only; they do not assert control failure or regulatory non-compliance.

## 5. Operational Source Register

| Source ID | Type | Stated Operational Fact | Interview Evidence | Approval |
|---|---|---|---|---|
| OP-001 | Role context | The stakeholder acts as an Infrastructure Engineer and Cloud Database Administrator. | Operator-approved Step 1 context. | Approved |
| OP-002 | Asset responsibility | The stakeholder is responsible for Starburst. | “I'm responsible for starburst.” | Approved |
| OP-003 | Asset responsibility | The stakeholder is responsible for OpenMetadata. | “I'm responsible for ... openmetadata.” | Approved |
| OP-004 | Asset responsibility | The stakeholder is responsible for SingleStore. | “I'm responsible for ... singlestore technologies.” | Approved |
| OP-005 | Task | Grants required user access. | “Everyday I need to give access to users that require it.” | Approved |
| OP-006 | Task | Investigates developers' connection and usage issues. | “understand issues that developers have connecting/using these technologies.” | Approved |
| OP-007 | Task | Improves the technology layer through updates and configurations. | “trying to improve this tech layer either with updates or other configs.” | Approved |
| OP-008 | Task | Partly automates access control with Python. | “I already automated part of it with a python script.” | Approved |
| OP-009 | Asset / access control | Starburst access control uses Ranger policies. | “Starburst uses ranger for the acess control ... policies.” | Approved |
| OP-010 | Task | Assists colleagues with Kafka issues. | “extra hands ... on kafka ... I'll help them.” | Approved |
| OP-011 | Task | Assists colleagues with Cosmos issues. | “extra hands ... on ... cosmos ... I'll help them.” | Approved |
| OP-012 | Task | Assists colleagues with Databricks issues. | “extra hands ... on ... databricks ... I'll help them.” | Approved |
| OP-013 | Task | Backs up Ranger data before a Starburst change. | “backuping the data ... from ranger.” | Approved |
| OP-014 | Task | Migrates Starburst deployment from a script to GitOps deployment. | “changed and tested a migration to a gitops deployment.” | Approved |
| OP-015 | Task / technology | Activates Flux in target AKS to deploy Starburst configurations. | “activated flux ... deploy our starburst configs with gitops.” | Approved |
| OP-016 | Task | Tests updates and upgrades in non-production environments. | “start by a period of testing in non productive envs.” | Approved |
| OP-017 | Approval gate | Proceeds to production only after stability testing and no reported user issues. | “we only go fowards ... everything is stable and the users havent reported any issues.” | Approved |
| OP-018 | Task / tool | Uses `kubectl` commands to check logs and validate changes. | “kubectl commands and check logs and validate.” | Approved |
| OP-019 | Task | Validates Starburst availability and database connectivity with a query. | “simple query in starburst to check if it was up and connecting to the DBs.” | Approved |
| OP-020 | Task / configuration | Uses Git and VS Code to change YAML configurations. | “git and vscode ... change the yaml configs.” | Approved |
| OP-021 | Configuration store | Technology configurations are kept in Azure DevOps. | “the configs are kept on azure devops.” | Approved |
| OP-022 | Sensitive data | Passwords are kept in Azure Key Vault. | “passwords those are in a azure keyvault.” | Approved |
| OP-023 | Technology integration | AKS External Secrets connects to Azure Key Vault. | “external secret that connects it to the keyvault.” | Approved |
| OP-024 | Sensitive data / task | Uses root passwords and secrets to correct issues while normally avoiding table-data reads. | “read and use root level passwords ... most of the time I dont need to read any of the tables data.” | Approved |
| OP-025 | Task | Runs limited queries to test database connections. | “the few queries I do is to test connection.” | Approved |
| OP-026 | Tool use | Uses LLMs to parse logs and search for information online. | “LLMs that help me parse logs and search info online.” | Approved |
| OP-027 | Change record | Records production changes in ServiceNow change requests. | “all changes in PRD are recorded in a change openned in service now.” | Approved |
| OP-028 | Task | Opens changes for updates or improvements; other teams can request production changes. | “changes can be openned by myself ... or by other teams.” | Approved |
| OP-029 | Incident record / task | Uses ServiceNow incidents for other teams' non-production requests and testing. | “in non productive envs things asked by other teams are with service now incidents.” | Approved |
| OP-030 | Approval constraint | Does not alter information without an approved DevOps change. | “can never change info unless specifically told with a change made by a devops teams that has been previously aproved.” | Approved |
| OP-031 | Dependency | Relies on the AKS/compute team for underlying compute support and correction. | “team ... responsible for the AKS and other more compute things.” | Approved |
| OP-032 | Dependency | Relies on the networking team. | “as well as the networking team.” | Approved |
| OP-033 | Dependency | Engages technology support teams for support and correction. | “talk a lot with support teams of the technologies we use.” | Approved |
| OP-034 | Technical handoff | Sends logs and sometimes configurations to support or dependent teams. | “mostly logs and sometimes configs.” | Approved |
| OP-035 | Operational output | DevOps teams use the result of the stakeholder's work. The exact output is unknown. | “the result of my work is used by the devops teams”; operator clarification: “unknown.” | Approved |
| OP-036 | Incident interface | SingleStore outages can stop front-facing applications and other services. | “front facing app stoppde working and a myriad of other services.” | Approved |
| OP-037 | Incident task | Restarts SingleStore, investigates cause, and mitigates outages. | “trying to restart singlestore and then ficure out what cause it so we can mitigate it.” | Approved |
| OP-038 | Monitoring interface | Detects issues through Datadog metrics, alerts, and phones. | “datadog looking a large quantity of metrics ... alerts start ringing as well as phones.” | Approved |
| OP-039 | Incident interface | The team lead joins normal SingleStore incident response. | “my team lead joins.” | Approved |
| OP-040 | Incident interface | Other DevOps leads join SingleStore incident response. | “later even other devops leads.” | Approved |
| OP-041 | Incident interface | Technology support joins extreme SingleStore incidents. | “in extreme cases even the support team.” | Approved |
| OP-042 | Recovery tool | Uses technology-native tools during recovery. | “the tech native toolds.” | Approved |
| OP-043 | Incident report | Produces a post-incident report for technology support. | “always create a report to send to support.” | Approved |
| OP-044 | Approval dependency | A dedicated authorization team authorizes production changes. | “we have a team responsible for authorizations.” | Approved |
| OP-045 | Approval dependency | Access requests pass through the security team for approval. | “all the requests go through a security team.” | Approved |
| OP-046 | Approval record | ServiceNow tracks approvals and change-request status. | “service now change request system keeps track of the aprovals ... status.” | Approved |
| OP-047 | Approval mechanism | An authorization status is automatically configured when a request opens; responsible system or team is not identified. | “is automated and configured when the request is being opened”; operator clarification: “an authorization status.” | Approved |
| OP-048 | Team accountability | The stakeholder's team is accountable for configured technologies. | “my team is accountable for those technologies we configure.” | Approved |
| OP-049 | Emergency change | Implements critical service-affecting changes as needed and writes reports afterward. | “critical changes that affect service are made as needed. reports are written after.” | Approved |
| OP-050 | Review | Self-checks and reviews completed changes. | “we self check and review.” | Approved |
| OP-051 | Collaborative validation | Sometimes asks DevOps teams to perform a small test. | “sometimes we also ask some devop teams for a small test.” | Approved |
| OP-052 | Friction | Access provisioning remains time-consuming despite partial automation and Ranger policy complexity. | “it can still take a lot of time”; “a few moving parts regarding the policies.” | Approved |
| OP-053 | Friction | Connection and compute-related tasks stop while awaiting another team. | “those task ended stopped there.” | Approved |
| OP-054 | Friction | SingleStore failure has high service impact and requires urgent remediation. | “problems with ... singlestore ... can lead to a lost of service.” | Approved |
| OP-055 | Friction | Daily work is described as monotonous. | “its a very monotonous work.” | Approved |
| OP-056 | Gap | The owner or system responsible for automated authorization-status assignment is not identified. | OP-047; no named owner or system in operator clarification. | Approved |
| OP-057 | Gap | The concrete output consumed by DevOps teams is unknown. | OP-035; operator clarification: “unknown.” | Approved |
| OP-058 | Gap | Non-production work can be tested without an official change record. | “test things without having to record it in an official matter.” | Approved |

## 6. Operational Relationship Ledger

All entries are source-backed, approved, and visible candidates. Association is used only for an explicit direct link where the evidence does not identify a more specific ArchiMate relation.

| Relationship ID | Source → Target | Meaning | Candidate ArchiMate Relation | Evidence | Approval |
|---|---|---|---|---|---|
| REL-OP-001 | Infrastructure Engineer / Cloud DB Admin → Starburst Administration | administers | Assignment | OP-001, OP-002 | Approved |
| REL-OP-002 | Starburst Administration → Starburst | administers | Association | OP-002 | Approved |
| REL-OP-003 | Infrastructure Engineer / Cloud DB Admin → OpenMetadata Administration | administers | Assignment | OP-001, OP-003 | Approved |
| REL-OP-004 | OpenMetadata Administration → OpenMetadata | administers | Association | OP-003 | Approved |
| REL-OP-005 | Infrastructure Engineer / Cloud DB Admin → SingleStore Administration | administers | Assignment | OP-001, OP-004 | Approved |
| REL-OP-006 | SingleStore Administration → SingleStore | administers | Association | OP-004 | Approved |
| REL-OP-007 | Infrastructure Engineer / Cloud DB Admin → Access Provisioning | grants access | Assignment | OP-005 | Approved |
| REL-OP-008 | Infrastructure Engineer / Cloud DB Admin → Developer Issue Diagnosis | investigates connection and usage issues | Assignment | OP-006 | Approved |
| REL-OP-009 | Infrastructure Engineer / Cloud DB Admin → Technology Maintenance | updates and reconfigures technology | Assignment | OP-007 | Approved |
| REL-OP-010 | Infrastructure Engineer / Cloud DB Admin → Access Automation | automates access-control work with Python | Assignment | OP-008 | Approved |
| REL-OP-011 | Ranger → Starburst | provides access-control policy capability | Serving | OP-009 | Approved |
| REL-OP-012 | Infrastructure Engineer / Cloud DB Admin → Colleague Assistance | assists colleagues | Assignment | OP-010, OP-011, OP-012 | Approved |
| REL-OP-013 | Colleague Assistance → Kafka | supports work involving Kafka | Association | OP-010 | Approved |
| REL-OP-014 | Colleague Assistance → Cosmos | supports work involving Cosmos | Association | OP-011 | Approved |
| REL-OP-015 | Colleague Assistance → Databricks | supports work involving Databricks | Association | OP-012 | Approved |
| REL-OP-016 | Infrastructure Engineer / Cloud DB Admin → Ranger Backup | backs up Ranger data before change | Assignment | OP-013 | Approved |
| REL-OP-017 | Infrastructure Engineer / Cloud DB Admin → Starburst GitOps Migration | migrates deployment approach | Assignment | OP-014 | Approved |
| REL-OP-018 | Flux → Starburst Configuration Deployment | deploys Starburst configurations to target AKS | Serving | OP-015 | Approved |
| REL-OP-019 | Infrastructure Engineer / Cloud DB Admin → Non-production Testing | tests changes before production | Assignment | OP-016 | Approved |
| REL-OP-020 | Non-production Testing → Production Readiness Decision | establishes the condition to proceed | Triggering | OP-017 | Approved |
| REL-OP-021 | Infrastructure Engineer / Cloud DB Admin → Change Validation | validates completed changes | Assignment | OP-018, OP-019 | Approved |
| REL-OP-022 | Change Validation → Starburst | checks service availability and database connection | Association | OP-019 | Approved |
| REL-OP-023 | Infrastructure Engineer / Cloud DB Admin → YAML Configuration Maintenance | changes YAML configurations | Assignment | OP-020 | Approved |
| REL-OP-024 | YAML Configuration Maintenance → YAML Configuration | reads and changes configuration | Access | OP-020 | Approved |
| REL-OP-025 | YAML Configuration → Azure DevOps | is stored in | Association | OP-021 | Approved |
| REL-OP-026 | Infrastructure Engineer / Cloud DB Admin → Secret Retrieval | retrieves credentials to correct issues | Assignment | OP-024 | Approved |
| REL-OP-027 | Secret Retrieval → Azure Key Vault Secrets | accesses passwords and secrets | Access | OP-022, OP-024 | Approved |
| REL-OP-028 | Azure Key Vault → AKS External Secrets | supplies secrets through the stated connection | Serving | OP-023 | Approved |
| REL-OP-029 | Infrastructure Engineer / Cloud DB Admin → Database Connection Testing | performs limited connection tests | Assignment | OP-025 | Approved |
| REL-OP-030 | Database Connection Testing → Database Table Data | reads limited data through test queries | Access | OP-025 | Approved |
| REL-OP-031 | Infrastructure Engineer / Cloud DB Admin → Log Investigation | investigates logs and external information | Assignment | OP-026 | Approved |
| REL-OP-032 | Log Investigation → LLM Tools | uses LLMs to parse logs and search information | Association | OP-026 | Approved |
| REL-OP-033 | Infrastructure Engineer / Cloud DB Admin → Production Change Recording | records production changes | Assignment | OP-027 | Approved |
| REL-OP-034 | Production Change Recording → ServiceNow Change Request | creates and updates the record | Access | OP-027 | Approved |
| REL-OP-035 | Infrastructure Engineer / Cloud DB Admin → Non-production Support Testing | tests non-production requests | Assignment | OP-029 | Approved |
| REL-OP-036 | Non-production Support Testing → ServiceNow Incident | uses the incident record for requested work | Access | OP-029 | Approved |
| REL-OP-037 | Approved DevOps Change → Information Change | authorizes the otherwise prohibited information change | Triggering | OP-030 | Approved |
| REL-OP-038 | AKS/Compute Team → Infrastructure Issue Resolution | provides compute-layer support and correction | Serving | OP-031 | Approved |
| REL-OP-039 | Networking Team → Connection Issue Resolution | provides support for connection issues | Serving | OP-032 | Approved |
| REL-OP-040 | Technology Support Team → Issue Correction | provides support and correction | Serving | OP-033 | Approved |
| REL-OP-041 | Infrastructure Engineer / Cloud DB Admin → Support Handoff | provides technical evidence to support teams | Assignment | OP-034 | Approved |
| REL-OP-042 | Infrastructure Engineer / Cloud DB Admin → Technology Support Team | sends logs | Flow | OP-034 | Approved |
| REL-OP-043 | Infrastructure Engineer / Cloud DB Admin → Technology Support Team | sends configurations | Flow | OP-034 | Approved |
| REL-OP-044 | SingleStore Outage → SingleStore Recovery | initiates incident recovery | Triggering | OP-036 | Approved |
| REL-OP-045 | Infrastructure Engineer / Cloud DB Admin → SingleStore Recovery | restarts, investigates, and mitigates | Assignment | OP-037 | Approved |
| REL-OP-046 | Datadog Alert → SingleStore Recovery | initiates the response | Triggering | OP-038 | Approved |
| REL-OP-047 | Team Lead → SingleStore Incident Response | participates in response | Assignment | OP-039 | Approved |
| REL-OP-048 | DevOps Leads → SingleStore Incident Response | participates in response | Assignment | OP-040 | Approved |
| REL-OP-049 | Technology Support Team → SingleStore Incident Response | participates in extreme cases | Assignment | OP-041 | Approved |
| REL-OP-050 | Infrastructure Engineer / Cloud DB Admin → Post-Incident Reporting | creates the support report | Assignment | OP-043 | Approved |
| REL-OP-051 | Post-Incident Reporting → Technology Support Team | transfers the report | Flow | OP-043 | Approved |
| REL-OP-052 | Authorization Team → Production Change Authorization | performs authorization | Assignment | OP-044 | Approved |
| REL-OP-053 | Security Team → Access Request Approval | performs access approval | Assignment | OP-045 | Approved |
| REL-OP-054 | Production Change Authorization → ServiceNow Change Request | records approval status | Access | OP-046 | Approved |
| REL-OP-055 | Stakeholder Team → Technology Maintenance | configures accountable technologies | Assignment | OP-048 | Approved |
| REL-OP-056 | Critical Service Impact → Emergency Change | initiates urgent change handling | Triggering | OP-049 | Approved |
| REL-OP-057 | Infrastructure Engineer / Cloud DB Admin → Emergency Change | implements required critical changes | Assignment | OP-049 | Approved |
| REL-OP-058 | Emergency Change → Change Report | writes the change report after emergency action | Access (Write) | OP-049 | Approved |
| REL-OP-059 | Infrastructure Engineer / Cloud DB Admin → Change Review | self-checks and reviews completed changes | Assignment | OP-050 | Approved |
| REL-OP-060 | DevOps Team → Collaborative Validation Test | performs requested validation testing | Assignment | OP-051 | Approved |

No `REL-OP-*` relationship is created for the unknown DevOps work output (OP-057) or for the unidentified automation/owner of the authorization-status assignment (OP-056).

### ArchiMate Cross-Layer Mapping

The following mapping is a source-backed candidate catalog for later validation; it is not a persisted view or model.

#### A. Active Structure

**Business actors and roles**

- **Infrastructure Engineer / Cloud DB Admin:** Performs the approved administration, access, maintenance, change, and incident tasks.
- **Stakeholder Team:** Accountable for configured technologies.
- **AKS/Compute Team:** Provides underlying compute support and correction.
- **Networking Team:** Supports connection-related issues.
- **Technology Support Team:** Provides correction support and participates in extreme incidents.
- **Authorization Team:** Performs production-change authorization.
- **Security Team:** Performs access-request approval.
- **DevOps Team / DevOps Leads:** Performs validation testing and participates in incident response.
- **Team Lead:** Participates in SingleStore incident response.

**Technology active structure**

- **AKS:** Target environment for Flux-based deployment and source of External Secrets.
- **Ranger:** Technology used for Starburst access-control policies.
- **Flux:** Technology used to deploy Starburst configurations through GitOps.
- **Starburst, OpenMetadata, SingleStore:** Technologies within the stakeholder's stated responsibility.
- **Azure DevOps, Azure Key Vault, ServiceNow, Datadog, LLM Tools:** Named operational systems and tools.

#### B. Behavior

- **Access Provisioning and Access Automation:** Grants user access; includes partial Python automation.
- **Developer Issue Diagnosis and Technology Maintenance:** Investigates use and connection issues; applies updates and configurations.
- **Starburst GitOps Migration, Ranger Backup, Non-production Testing, and Change Validation:** Performs controlled change work and validation.
- **YAML Configuration Maintenance and Secret Retrieval:** Maintains configurations and retrieves credentials needed for issue correction.
- **Production Change Recording, Non-production Support Testing, and Change Review:** Records, tests, and reviews changes.
- **SingleStore Recovery and Post-Incident Reporting:** Responds to outages and reports to technology support.
- **Production Change Authorization and Access Request Approval:** Implements the stated approval processes.
- **Emergency Change and Collaborative Validation Test:** Handles service-affecting changes and requested DevOps testing.

#### C. Passive Structure

- **Ranger Policies, YAML Configuration, Azure Key Vault Secrets, Database Table Data:** Access-control, configuration, credential, and data assets.
- **ServiceNow Change Request and ServiceNow Incident:** Change and incident records.
- **Logs, Configurations, Post-Incident Report, and Change Report:** Evidence and records exchanged during support, incident, and change work.
- **Authorization Status:** Automatically configured on request opening; its responsible automation or owner is not evidenced.

## 7. Unresolved Items

- **OP-056:** The named system or team responsible for automatically assigning the authorization status is not evidenced.
- **OP-057:** The concrete operational output used by DevOps teams is unknown.

These items may not be represented as source-backed relationships unless clarified by the operator in a later approved update.
