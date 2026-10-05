### Stakeholder Operational Footprint

**Interview source:** `Methodology/StakeHolders/BankBackEndDev_2/2_interview.md`  
**Stakeholder:** Back-end Developer  
**Operational area:** Internal Enterprise Data Platform

**1. Core Role Context:**

The stakeholder develops offloads, ETLs, and query services for an internal data platform. They also maintain and extend the team's internal framework. The described work makes data available to other teams and services in the bank. The stakeholder performs the technical implementation, testing, pull-request creation, release coordination, and post-deployment monitoring; functional personnel prepare specifications.

**2. Everyday Tasks:**

* Develop offloads, ETLs, and query services.
* Maintain services, update versions, and extend the team's internal framework.
* Read documentation and specifications; implement code; check data sinks and duplicate filtering; and test code.
* Create an offload from a specification, including transformations, sanitisation, and a stated destination.
* Test data mapping, naming, validation, and error handling before creating a pull request.
* Obtain technical pull-request validation; open QUA and PROD change requests; and trigger authorised deployment steps.
* Monitor a PROD deployment in Datadog for about two hours.
* Discuss a development plan with the Team Manager and Solution Architect when blocked by permissions or implementation decisions.
* Update a service for a full dependency change or version update.
* Participate in incident escalation and, where the responsible team owns the software error, remediate it through normal code changes.

**3. Key Dependencies:**

* Functional personnel prepare the specification in a wiki after contacting the Mainframe.
* Read permission, write permission, and a sufficiently complete specification are prerequisites for a microservice to run.
* The Team Manager and Solution Architect allocate work and provide planning support.
* The Infrastructure Team provides functional pods, Kubernetes environments, and pipelines for deployment.
* The workflow uses DBeaver, RedPanda, VPN, Azure DevOps, Azure Portal, Datadog, Azure AD, databases, Kafka, Cosmos DB, SingleStore, Azure FileSystem, Kubernetes clusters, and C#/.NET.
* The Bank provides Rider licences and VPN. Microsoft provides Azure Portal, Azure, Cosmos DB, and Kubernetes clusters.
* Internal consumer teams use platform data and, by operator clarification, own that data.

**4. Operational Insights & Friction:**

* External dependencies make the work difficult.
* Missing read or write permission blocks the work.
* Development cannot begin without a specification; a poorly made specification can prevent a microservice from running.
* Infrastructure-team availability is required for deployment.
* A platform outage can affect the team, other teams, and potentially customers.
* **[Gap] Cross-project visibility:** the stakeholder has context only for their smaller project and cannot track all concurrent work across the wider team. This is a viewpoint visibility limitation, not a claim that a control is absent.
* The interview did not establish an outage workaround or the Infrastructure Team's remediation method. These are evidence limitations, not gaps.
* Approval is an explicit prerequisite: nothing can happen without it.

**5. Operational Source Register:**

| Source ID | Type | Stated Operational Fact | Interview Evidence |
| --- | --- | --- | --- |
| OP-001 | Task / application component | The stakeholder develops offloads. | Lines 20, 70 |
| OP-002 | Task / application component | The stakeholder develops ETLs. | Lines 20, 70 |
| OP-003 | Task / application component | The stakeholder develops query services. | Lines 20, 70 |
| OP-004 | Task / application component | The stakeholder maintains and adds features to the internal framework. | Lines 23, 26 |
| OP-005 | Dependency / process | Functional personnel write a specification in a wiki after contacting the Mainframe. | Line 144 |
| OP-006 | Task / data | The stakeholder creates an offload from a specification, streams data from a source to a sink, and applies stated transformations and sanitisation. | Line 78 |
| OP-007 | Dependency / node | The Mainframe is the data source for the described offload. | Line 114 |
| OP-008 | Task / approval | After tests pass and the offload works in DEV, the stakeholder creates a pull request. | Line 78 |
| OP-009 | Approval / role | A technically knowledgeable person not involved in development checks and validates the pull request. | Line 84 |
| OP-010 | Event / application component | Pull-request approval triggers the Azure pipeline. | Line 84 |
| OP-011 | Task / approval | The stakeholder opens QUA and PROD change requests and uses accepted requests to trigger pipeline steps. | Line 84 |
| OP-012 | Approval | The Team Manager approves QUA change requests and sends PROD for Board approval. | Line 87 |
| OP-013 | Task / approval | The Team Manager or Solution Architect presses PROD deployment using the PROD change code. | Line 84 |
| OP-014 | Task / application component | The stakeholder monitors the PROD deployment in Datadog for about two hours. | Line 84 |
| OP-015 | Task / application component | The stakeholder uses DBeaver to check and query databases. | Lines 176, 218 |
| OP-016 | Task / application component | The stakeholder uses RedPanda to inspect Kafka. | Lines 176, 218 |
| OP-017 | Task / technology service | The stakeholder uses VPN to access necessary internal services. | Lines 176, 218 |
| OP-018 | Task / application component | The stakeholder uses Azure DevOps for repositories, pipelines, and pull requests. | Lines 176, 218 |
| OP-019 | Task / application component | The stakeholder uses Azure Portal for Kubernetes clusters and Cosmos DB. | Lines 176, 218 |
| OP-020 | Dependency / approval | The Team Manager arranges service access and software licences for the stakeholder. | Line 185 |
| OP-021 | Dependency / business actor | The Bank provides Rider licences. | Line 221 |
| OP-022 | Dependency / technology service | The Bank provides VPN. | Line 221 |
| OP-023 | Dependency / business actor | Microsoft provides Azure Portal. | Line 221 |
| OP-024 | Dependency / business actor | Microsoft provides Azure. | Line 221 |
| OP-025 | Dependency / application component | Microsoft provides Cosmos DB. | Line 221 |
| OP-026 | Dependency / node | Microsoft provides Kubernetes clusters. | Line 221 |
| OP-027 | Dependency / active structure | The Infrastructure Team provides functional pods. | Line 283 |
| OP-028 | Dependency / node | The Infrastructure Team provides Kubernetes environments. | Line 283 |
| OP-029 | Dependency / application component | The Infrastructure Team provides deployment pipelines. | Line 283 |
| OP-030 | Consumer / application component | The platform's microservices make data available to internal teams. | Lines 35–44, 259 |
| OP-031 | Access | Development teams can access databases. | Line 233 |
| OP-032 | Access | Development teams can access Cosmos DB. | Line 233 |
| OP-033 | Access | C# applications can access databases. | Line 233; operator clarification that “solutions” means C# applications |
| OP-034 | Access | C# applications can access Cosmos DB. | Line 233; operator clarification |
| OP-035 | Access | In PROD, only C# applications access data. | Line 233; operator clarification |
| OP-036 | Ownership | Consuming teams own the data. | Operator clarification |
| OP-037 | Access / application component | Azure AD decides service-access permissions; teams contact the platform team to use the platform. | Line 382 |
| OP-038 | Task / event | A full dependency change or version update results in the relevant service being updated. | Line 271 |
| OP-039 | Dependency / role | The Team Manager assigns work tasks. | Lines 238, 279 |
| OP-040 | Dependency / role | The Team Manager and Solution Architect help formulate a development plan when the stakeholder is blocked. | Line 244 |
| OP-041 | Decision / role | The Team Manager has the final word on platform changes; the Team Manager and/or Solution Architect decide whether a change can go live. | Lines 361, 373, 391 |
| OP-042 | Decision criterion | Performance, good practices, and availability guide change decisions. | Line 367 |
| OP-043 | Task / role | The stakeholder contributes suggestions when new requirements arise. | Line 370 |
| OP-044 | Decision / role | The Team Manager decides final architecture with the Solution Architect and decides functional requirements. | Line 403 |
| OP-045 | Event | A decision triggers development. | Line 409 |
| OP-046 | Decision recipient | The stakeholder receives the decision. | Line 412 |
| OP-047 | Approval constraint | Nothing can happen without approval. | Line 415 |
| OP-048 | Task | The stakeholder reads documentation and specifications, programs, checks the database sink and duplicate filtering, and tests code. | Line 61 |
| OP-049 | Output | The stakeholder produces microservices that make data available to other teams. | Lines 35, 70 |
| OP-050 | Completion criterion | Completion includes data in databases, Kafka events, passing unit tests, approved pull requests, completed deployments, non-erroring pods, and no Datadog problem metrics. | Line 47 |
| OP-051 | Dependency | Other teams or management usually request developments. | Line 158 |
| OP-052 | Friction | External dependencies make work difficult. | Line 53 |
| OP-053 | Permission | Read permission is required for the described work. | Line 129 |
| OP-054 | Permission | Write permission is required for the described work. | Line 129 |
| OP-055 | Dependency | A well-made specification is required to get a microservice running. | Line 129 |
| OP-056 | Friction | External dependencies make work difficult. | Line 53 |
| OP-057 | Friction | Missing read or write permission blocks work. | Lines 53, 129 |
| OP-058 | Friction | A sufficiently complete specification is required before development can begin. | Lines 129, 250 |
| OP-059 | Operational dependency | Deployment cannot occur without Infrastructure Team availability. | Line 295 |
| OP-060 | Operational impact | A platform outage can affect the team, other teams, and potentially customers. | Lines 306, 312 |
| OP-061 | [Gap] | The stakeholder has context only for the smaller project and cannot track all concurrent work across the wider team. | Line 117 |
| OP-062 | Evidence limitation | No outage workaround was identified by the stakeholder. | Line 330 |
| OP-063 | Evidence limitation | The stakeholder does not know the Infrastructure Team's remediation method. | Line 350 |
| OP-064 | Governance constraint | Approval is required before work can proceed. | Line 415 |
| OP-065 | Task / data | The stakeholder transforms, sanitises, or combines information before placing it in the platform. | Line 197 |
| OP-066 | Application component | The stakeholder interacts with Kafka, other teams' query services, SingleStore, Cosmos DB, and Azure FileSystem. | Line 203 |
| OP-067 | System software | C#/.NET supports the work. | Line 206 |
| OP-068 | Dependency | SingleStore and Kafka are cloud-hosted; no provider relationship beyond that statement is evidenced. | Line 265 |
| OP-069 | Role / process | The Team Manager manages and delegates work; the Solution Architect designs with the Manager and assists developers. | Lines 279–280 |
| OP-070 | Incident interface | Datadog alarms are picked up and escalated by the Monitoring Team. | Line 300 |
| OP-071 | Incident interface | The Manager, the developer responsible for the latest change, and, when relevant, the Infrastructure Team become involved in an incident. | Line 309 |
| OP-072 | Incident interface | The stakeholder or Monitoring Team can identify a failure; the Monitoring Team detects failures. | Lines 324, 344 |
| OP-073 | Incident task | Recovery proceeds through contact and escalation until the responsible party can fix the issue. | Line 315 |
| OP-074 | Incident event | Software errors and transient infrastructure problems cause failures. | Line 341 |
| OP-075 | Incident ownership | The team that developed the software handles software errors; the Infrastructure Team handles infrastructure problems. | Line 347 |
| OP-076 | Incident task | The teams use Datadog to understand what went wrong. | Line 350 |
| OP-077 | Incident output | Remediation produces a fix. | Line 353 |
| OP-078 | Recovery criterion | Recovery is indicated by stopped error logs or pods that stop crashing. | Line 356 |
| OP-079 | Operational constraint | Work not depending on the platform can continue during an outage. | Line 327 |
| OP-080 | Recovery outcome | After recovery, the platform's data is available again. | Line 333 |
| OP-081 | Data / specification | The specification identifies source location, data types, names, transformations, sanitisation, and the destination. | Line 78 |
| OP-082 | Environment | The reported environments are DEV, INT, QUA, and PROD. | Lines 47, 84 |
| OP-083 | Technology node | Kubernetes pods must run without errors as a completion criterion. | Line 47 |
| OP-084 | Data / approval | The stakeholder uses QUA and PROD change codes for deployment steps. | Line 84 |
| OP-085 | Application component | Azure Pipelines executes approved pipeline steps. | Line 84 |
| OP-086 | Asset | Rider or Visual Studio is the stakeholder's IDE; the interview does not identify which is used for a given task. | Line 176 |
| OP-087 | Asset | The listed tools are mandatory, except that AI is not essential. | Line 188 |
| OP-088 | Access policy | In PROD, access to data is restricted to C# applications. | Line 233; operator clarification |
| OP-089 | Operational scope | The described development was isolated; the stakeholder lacks context for all simultaneous work in the team. | Lines 117, 123 |

## Operational Relationship Ledger

All relationships below were approved in Gate 3.2. Each has `visibility: visible` and `approval: approved`.

| Relationship ID | Source | Meaning | Target | Candidate ArchiMate relation | Evidence |
| --- | --- | --- | --- | --- | --- |
| REL-OP-001 | Back-end Developer | performs | Platform Development | Assignment | OP-001–003 |
| REL-OP-002 | Back-end Developer | develops | Offload Service | Association | OP-001 |
| REL-OP-003 | Back-end Developer | develops | ETL Service | Association | OP-002 |
| REL-OP-004 | Back-end Developer | develops | Query Service | Association | OP-003 |
| REL-OP-005 | Back-end Developer | maintains and enhances | Internal Framework | Association | OP-004 |
| REL-OP-006 | Internal Framework | serves | Platform Development | Serving | OP-004 |
| REL-OP-007 | Functional Personnel | performs | Specification Preparation | Assignment | OP-005 |
| REL-OP-008 | Specification Preparation | writes | Offload Specification | Access/write | OP-005 |
| REL-OP-009 | Platform Development | reads | Offload Specification | Access/read | OP-006 |
| REL-OP-010 | Offload Service | performs | Data Offload Flow | Assignment | OP-006 |
| REL-OP-011 | Data Offload Flow | reads | Source Data | Access/read | OP-006 |
| REL-OP-012 | Data Offload Flow | writes | Destination Data | Access/write | OP-006 |
| REL-OP-013 | Mainframe | supplies | Source Data | Association | OP-007 |
| REL-OP-014 | Back-end Developer | performs | Test and DEV Readiness | Assignment | OP-008 |
| REL-OP-015 | Test Passed | triggers | Pull Request Creation | Triggering | OP-008 |
| REL-OP-016 | Back-end Developer | performs | Pull Request Creation | Assignment | OP-008 |
| REL-OP-017 | Pull Request Creation | writes | Pull Request | Access/write | OP-008 |
| REL-OP-018 | Technical Reviewer | performs | Pull Request Review | Assignment | OP-009 |
| REL-OP-019 | Pull Request Review | reads | Pull Request | Access/read | OP-009 |
| REL-OP-020 | Pull Request Approval | triggers | Pipeline Execution | Triggering | OP-010 |
| REL-OP-021 | Back-end Developer | performs | Release Coordination | Assignment | OP-011 |
| REL-OP-022 | Release Coordination | writes | QUA Change Request | Access/write | OP-011 |
| REL-OP-023 | Release Coordination | writes | PROD Change Request | Access/write | OP-011 |
| REL-OP-024 | Team Manager | performs | QUA Change Approval | Assignment | OP-012 |
| REL-OP-025 | QUA Change Approval | triggers | Pipeline Execution | Triggering | OP-011 |
| REL-OP-026 | Board | performs | PROD Approval | Assignment | OP-012 |
| REL-OP-027 | PROD Approval | triggers | PROD Deployment | Triggering | OP-012 |
| REL-OP-028 | Team Manager | performs | PROD Deployment | Assignment; alternative performer | OP-013 |
| REL-OP-029 | Solution Architect | performs | PROD Deployment | Assignment; alternative performer | OP-013 |
| REL-OP-030 | PROD Deployment | reads | PROD Change Code | Access/read | OP-013, OP-084 |
| REL-OP-031 | Back-end Developer | performs | Production Monitoring | Assignment | OP-014 |
| REL-OP-032 | Datadog | serves | Production Monitoring | Serving | OP-014 |
| REL-OP-033 | Back-end Developer | performs | Database Querying | Assignment | OP-015 |
| REL-OP-034 | DBeaver | serves | Database Querying | Serving | OP-015 |
| REL-OP-035 | Database Querying | reads | Databases | Access/read | OP-015 |
| REL-OP-036 | Back-end Developer | performs | Kafka Inspection | Assignment | OP-016 |
| REL-OP-037 | RedPanda | serves | Kafka Inspection | Serving | OP-016 |
| REL-OP-038 | Kafka Inspection | reads | Kafka Topics | Access/read | OP-016 |
| REL-OP-039 | Back-end Developer | performs | Internal Service Access | Assignment | OP-017 |
| REL-OP-040 | VPN | serves | Internal Service Access | Serving | OP-017 |
| REL-OP-041 | Back-end Developer | performs | Repository and Release Work | Assignment | OP-018 |
| REL-OP-042 | Azure DevOps | serves | Repository and Release Work | Serving | OP-018 |
| REL-OP-043 | Back-end Developer | performs | Platform Administration | Assignment | OP-019 |
| REL-OP-044 | Azure Portal | serves | Platform Administration | Serving | OP-019 |
| REL-OP-045 | Team Manager | performs | Access and Licence Provisioning | Assignment | OP-020 |
| REL-OP-046 | Access and Licence Provisioning | triggers | Internal Service Access | Triggering | OP-020 |
| REL-OP-047 | The Bank | provides | Rider Licence | Association | OP-021 |
| REL-OP-048 | The Bank | provides | VPN | Association | OP-022 |
| REL-OP-049 | Microsoft | provides | Azure Portal | Association | OP-023 |
| REL-OP-050 | Microsoft | provides | Azure | Association | OP-024 |
| REL-OP-051 | Microsoft | provides | Cosmos DB | Association | OP-025 |
| REL-OP-052 | Microsoft | provides | Kubernetes Clusters | Association | OP-026 |
| REL-OP-053 | Infrastructure Team | performs | Infrastructure Provisioning | Assignment | OP-027–029 |
| REL-OP-054 | Kubernetes Clusters | serve | PROD Deployment | Serving | OP-028 |
| REL-OP-055 | Azure Pipelines | serve | PROD Deployment | Serving | OP-029, OP-085 |
| REL-OP-056 | Enterprise Data Platform | serves | Internal Consumer Teams | Serving | OP-030 |
| REL-OP-057 | Development Teams | access | Databases | Access/read | OP-031 |
| REL-OP-058 | Development Teams | access | Cosmos DB | Access/read | OP-032 |
| REL-OP-059 | C# Applications | access | Databases | Access/read | OP-033 |
| REL-OP-060 | C# Applications | access | Cosmos DB | Access/read | OP-034 |
| REL-OP-061 | C# Applications | access | Production Data | Access/read | OP-035 |
| REL-OP-062 | Internal Consumer Teams | own | Consumer Data | Association | OP-036 |
| REL-OP-063 | Internal Consumer Teams | perform | Platform Access Request | Assignment | OP-037 |
| REL-OP-064 | Azure AD | serves | Platform Access Request | Serving | OP-037 |
| REL-OP-065 | Dependency Change | triggers | Service Update | Triggering | OP-038 |
| REL-OP-066 | Back-end Developer | performs | Service Update | Assignment | OP-038 |
| REL-OP-067 | Team Manager | performs | Work Allocation | Assignment | OP-039 |
| REL-OP-068 | Work Allocation | triggers | Platform Development | Triggering | OP-039 |
| REL-OP-069 | Team Manager | performs | Development Planning | Assignment | OP-040 |
| REL-OP-070 | Solution Architect | performs | Development Planning | Assignment | OP-040 |
| REL-OP-071 | Back-end Developer | performs | Development Planning | Assignment | OP-040 |
| REL-OP-072 | Team Manager | performs | Change Decision | Assignment | OP-041, OP-044 |
| REL-OP-073 | Solution Architect | performs | Change Decision | Assignment | OP-044 |
| REL-OP-074 | Change Decision | triggers | Platform Development | Triggering | OP-045 |
| REL-OP-075 | Team Manager | performs | Functional Requirement Decision | Assignment | OP-044 |
| REL-OP-076 | Team Manager | performs | Go-Live Authorisation | Assignment | OP-041 |
| REL-OP-077 | Solution Architect | performs | Go-Live Authorisation | Assignment | OP-041 |
| REL-OP-078 | Go-Live Authorisation | triggers | PROD Deployment | Triggering | OP-041 |
| REL-OP-079 | Datadog Alarm | triggers | Incident Escalation | Triggering | OP-070 |
| REL-OP-080 | Monitoring Team | performs | Incident Escalation | Assignment | OP-070 |
| REL-OP-081 | Incident Escalation | triggers | Software Remediation | Triggering | OP-071, OP-073 |
| REL-OP-082 | Incident Escalation | triggers | Infrastructure Remediation | Triggering | OP-071, OP-073 |
| REL-OP-083 | Responsible Development Team | performs | Software Remediation | Assignment | OP-075 |
| REL-OP-084 | Infrastructure Team | performs | Infrastructure Remediation | Assignment | OP-075 |
| REL-OP-085 | Datadog | serves | Software Remediation | Serving | OP-076 |
| REL-OP-086 | Datadog | serves | Infrastructure Remediation | Serving | OP-076 |
| REL-OP-087 | Software Error | triggers | Software Remediation | Triggering | OP-074 |
| REL-OP-088 | Infrastructure Problem | triggers | Infrastructure Remediation | Triggering | OP-074 |
| REL-OP-089 | Software Remediation | writes | Software Fix | Access/write | OP-077 |

### ArchiMate Cross-Layer Mapping

*The following operational entities are extracted from the approved interview facts and operator clarifications. They are candidate mappings, not a view layout.*

**A. Active Structure (Actors, Roles, & Nodes)**

* **Business Actors / Roles:**
  * **Back-end Developer:** develops, maintains, tests, releases, monitors, plans, and remediates described platform work.
  * **Functional Personnel:** prepare and record specifications.
  * **Technical Reviewer:** validates pull requests.
  * **Team Manager:** allocates work, approves QUA changes, manages access and licences, and makes final decisions.
  * **Solution Architect:** contributes to architecture decisions, planning, and can deploy PROD.
  * **Board:** approves PROD release.
  * **Infrastructure Team:** provides infrastructure and remediates infrastructure problems.
  * **Monitoring Team:** receives Datadog alarms and escalates incidents.
  * **Internal Consumer Teams:** consume platform data and own that data.
  * **Development Teams:** access databases and Cosmos DB.
  * **Microsoft** and **The Bank:** named providers.
  * **Responsible Development Team:** repairs software errors in the service it developed.
* **Technology Nodes & Devices:**
  * **Mainframe:** stated offload data source.
  * **Kubernetes Clusters:** stated deployment environment.
  * **Pods:** runtime-health completion indicator.

**B. Behavior (Processes & Events)**

* **Business Processes:**
  * **Platform Development; Framework Maintenance; Specification Preparation; Test and DEV Readiness; Pull Request Creation; Pull Request Review; Release Coordination; QUA Change Approval; PROD Approval; PROD Deployment; Production Monitoring; Database Querying; Kafka Inspection; Internal Service Access; Repository and Release Work; Platform Administration; Access and Licence Provisioning; Infrastructure Provisioning; Platform Access Request; Service Update; Work Allocation; Development Planning; Change Decision; Functional Requirement Decision; Go-Live Authorisation; Incident Escalation; Software Remediation; Infrastructure Remediation.**
* **Business Events:**
  * **Test Passed; Pull Request Approval; QUA Change Approval; PROD Approval; Change Decision; Go-Live Authorisation.**
* **Application Processes and Events:**
  * **Data Offload Flow; Pipeline Execution.**
  * **Datadog Alarm; Software Error; Infrastructure Problem.**

**C. Passive Structure (Application Components, Systems, & Data)**

* **Application Components & System Software:**
  * **Enterprise Data Platform; Offload Service; ETL Service; Query Service; Internal Framework; DBeaver; RedPanda; Azure DevOps; Azure Portal; Azure AD; Datadog; Azure Pipelines; Cosmos DB; Kafka; SingleStore; Azure FileSystem; C#/.NET.**
* **Technology Services:**
  * **VPN; Azure.**
* **Data Objects and Artifacts:**
  * **Offload Specification; Source Data; Destination Data; Databases; Kafka Topics; Pull Request; QUA Change Request; PROD Change Request; PROD Change Code; Production Data; Consumer Data; Rider Licence; Software Fix.**

## Validation Record

* **Gate 3.1 — Confirm Extracted Tasks:** Approved with the clarification that “solutions” means C# applications and consuming teams own the data.
* **Gate 3.2 — Confirm Operational Relationships:** All `REL-OP-001` through `REL-OP-089` approved.
* **Gate 3.3 — Confirm Gaps & Friction:** Approved. Only `OP-061` is an explicit `[Gap]`; `OP-062` and `OP-063` are evidence limitations, not gaps.
