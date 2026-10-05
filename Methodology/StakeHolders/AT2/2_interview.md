# Back-end Developer Operational Interview Guide

**Interviewee:** Back-end Developer at a very large Portuguese bank  
**Operational area:** Internal Enterprise Data Platform  
**Platform purpose:** Makes data available to other bank services

## Interviewer instructions

- Ask each primary question first.
- Use nudges only when the interviewee pauses.
- Use a primary fallback only when the primary question is unclear.
- Use alternative angles to uncover missing detail.
- Keep one concrete platform change in focus throughout Sections 2–6.
- Repeat the relationship probes for every activity, tool, data item, service, and participant named.
- Record the interviewee's words on the `R:` lines without interpretation.

## 1. Everyday purpose

**Primary:** What do you do for the data platform?
R: I develop microservices that, together, make the enterprise data platform take shape. These may be offloads, ETLs or queryServices. 

**Nudge 1:** What else?
R: I also help maintaining and addin new features to our team's internal frameworks, which are used accross multiple microservices.

**Nudge 2:** Where do you spend most of your time?
R: Either coding, or mainting services / updating versions

**Nudge 3:** What happens regularly?
R:

**Primary fallback:** How would you describe your everyday work here?
R: Variate. I am blessed by not having to do the same thing every day or week. The challenges posed to me vary with frequency.

**Alternative angle 1:** What outcome does your work produce?
R: Microservices that produce data available to other teams. 

**Angle 1 fallback:** What results come from your work?
R: Data availability for other teams in the bank to use in their apps/services.

**Alternative angle 2:** Who uses what you produce?
R: Uff, lot's of people/teams. If we are talking data/query services. The framework is just ours. I think only one other team uses it. But data wise, Most of the bank fetches something from us.

**Angle 2 fallback:** Which teams rely on your work?
R: Credit, some campaigns, marketing, just to name a few.

**Alternative angle 3:** How do you know your work is finished?
R: Things work. Data shows in the databases. Events appear in kafka. Unit tests pass. Pull requests are approved, deployment to every environment is complete ( DEV, INT, QUA, PROD), Deploy is successfull, pods are up and running without errors, and no metrics in datadog accuse problems.

**Angle 3 fallback:** What tells you a task is complete?
R:

**Alternative angle 4:** What makes your work difficult?
R: Either external dependencies, or permissions.

**Angle 4 fallback:** Which parts are hardest?
R:

### Repeat for every named responsibility

- What do you do during it?
R:I read documentation and specs, program, check everything is OK during database sink, duplicate filtration and test code.

- Who performs each step?
R: I perform every step, except for spec writing

- What does it use?
R:

- What does it produce?
R:a Microservice, that may be an offload, an ETL or a QueryService

- What uses the result?
R:Either us, to feed into other services, or other teams

## 2. One concrete platform change

**Primary:** Walk me through one platform change you personally handled.
R: Well, during the creation of an offload, I get handled a spec of where data is, datatypes, names, everything I need to know. The spec includes the transformations and sanitizations that must target said data, and the destination for the data post treatment. This includes field names, datatypes, and so on . I then create an offload using our internal framework, respecting the spec, and data is streamed from the data source to the data sink. Unit tests are made to confirm correct data mapping, naming, validations and error handling. When all tests pass, and the offload is working in the DEV environment with full error absence, I create a pull request to a release.

**Nudge 1:** What happened first?
R: 

**Nudge 2:** What happened next?
R: I "poke" someone not involved in the development, but with the context and tecnhical knowledge necessary to check and validate my pull request. Once that "approve" button is pressed, the Azure pipeline gets triggered. Then I must open 2 change requests, one for the Quality Environment, and another for the Production Environment. When they are accepted, I use them to trigger pipeline steps. Int I can just press the button. QUA I need the change code. And Prod must be pressed by either the team Manager or the team's Solution Architect with the PROD change code I have. Afterwards, I monitor the Prod deployment using datadog for about 2 hours.

**Nudge 3:** Who else was involved?
R: Well, the team manager must approve the change requests for QUA, and Send the PROD environment up to board approval.

**Primary fallback:** Tell me how one change you worked on unfolded.
R:

**Alternative angle 1:** Where did your involvement begin?
R:

**Angle 1 fallback:** What was your first part?
R:

**Alternative angle 2:** What ended your involvement?
R: The solution was deployed and working, without triggering alarms.

**Angle 2 fallback:** What was your last part?
R:

**Alternative angle 3:** Which parts were you responsible for?
R: The actual technical bits, coding and getting the service up and running. The spec gets handled by functional personel.

**Angle 3 fallback:** What work belonged to you?
R:

**Alternative angle 4:** Who was responsible for the remaining parts?
R:

**Angle 4 fallback:** Who owned work outside your part?
R: The data source (mainframe), who I was offloading data from.

**Alternative angle 5:** What else was changing at the same time?
R:Uff, I don't know. It's a big team, more than 20 people. I can't keep track of what everybody is doing. We are organized into smaller projects, and only have the context of said small projects.

**Angle 5 fallback:** Which changes happened alongside this one?
R:

**Alternative angle 6:** How was this change coordinated with the others?
R:There was no need to be. It was an isolated development

**Angle 6 fallback:** How did people keep the changes aligned?
R:

**Alternative angle 7:** What did your part depend on?
R: Permissions to read and write. The spec being well made. Without that, it's not possible to get a microservice up and running

**Angle 7 fallback:** What had to be ready for your work?
R:

**Alternative angle 8:** What conflicts, if any, appeared with other changes?
R:

**Angle 8 fallback:** Where, if anywhere, did changes get in each other's way?
R:

**Alternative angle 9:** How did work move between people?
R:

**Angle 9 fallback:** How did one person's work reach the next?
R: Well, I'm the last person in that line. But the functional staff that contact the mainframe to estabilish a spec writes said spec in a wiki. That wiki get's passed on to me, and then I get to work.

**Alternative angle 10:** What showed the whole change was complete?
R:

**Angle 10 fallback:** How was the change known to be finished?
R:

### Repeat for every named step

- Who performed that step?
R:I specified who does what in the responses

- What triggered that step?
R:Usually developments are triggered by requests from other teams or management

THESE ARE ANSWERED IN THE THE RESPONSES{
- What did that step use?
R:

- What did that step produce?
R:

- What used that result?
R:

- What did that step connect to?
R:
}
## 3. Tools and information

**Primary:** What do you need to perform your work?
R: Well, I need My IDE, be it Visual Studio or Rider. I need DBeaver, to check and query Databases. RedPanda, to look at kafka. VPN to access necessary internal services. Azure Devops and Azure portal access, so I can actually get in touch with repos, pipelines, pull requests, k8s clusters and cosmosDB.

**Nudge 1:** What else?
R:

**Nudge 2:** Which item matters most?
R:

**Nudge 3:** How do you obtain it?
R:Software you just download. Accesses to services and Licences for software, I "poke" the team manager, and he get's them assigned to me. 

**Primary fallback:** What could you not work without?
R:Without all of this, well, I couldn't. I could easily work without AI for example. But the listed tools are mandatory.

**Alternative angle 1:** What information do you receive?
R:

**Angle 1 fallback:** What data comes into your work?
R:

**Alternative angle 2:** What information do you produce?
R: I don't produce information. I take information from places, and either just put it in the platform sanitized, transformed or combined.

**Angle 2 fallback:** What data comes out of your work?
R:

**Alternative angle 3:** Which systems do you interact with?
R: Kafka, Other query Services from other teams, Databases (SingleStore, CosmosDB) and Azure FileSystem

**Angle 3 fallback:** What software supports your work?
R: C# Dotnet.

**Alternative angle 4:** Where is important information kept?
R:

**Angle 4 fallback:** How do you find the information you need?
R:


### Repeat for every named tool or information item

- What do you do with it?
R:Program in Rider, Query DBs with DBEaver, Look at kafka topics with Redpanda, connecto to the bank using the VPN, AzureDEVOPS for managing repos, pipelines and pull requests. Azure portal for k8s clusters and cosmos DB

- What provides it?
R: The bank provides Rider licences and VPN. DBeaver and RedPanda are openSource. Microsoft provides the portal and azure, as well as cosmos and k8s.

- What does it connect to?
R:

- What does it produce?
R:

- What uses its result?
R:

- Who can access it?
R: Databases and cosmos can be accessed by development teams and solutions. In prod, only solutions can access data.

## 4. People and services you rely on

**Primary:** Who or what does your work depend on?
R:Mostly the team manager and the solution architect. They hand down the work tasks I perform.

**Nudge 1:** What else?
R:

**Nudge 2:** How do they help?
R: Besides assigning me work, if I get stuck, be it due to permissions or deciding on how to tackle an issue, I can discuss it with them to formulate a development plan to tackel the issue.

**Nudge 3:** How does that affect your work?
R:

**Primary fallback:** What must be available before you can proceed?
R:A spec. Pipelines, Permissions and so on can all be handled paralelly to the development process. The only thing necessary is a spec to begin development. 

**Alternative angle 1:** Which teams must contribute?
R: The Infrastructure Team.

**Angle 1 fallback:** Who inside the bank supports this work?
R:

**Alternative angle 2:** What services connect to the platform?
R: Mostly any other service from another internal team that needs to consume our data.

**Angle 2 fallback:** Which systems exchange information with the platform?
R:

**Alternative angle 3:** What support comes from outside the bank?
R: Everything Microsoft related, Singlestore and Kafka are in the cloud as well.

**Angle 3 fallback:** Which outside organizations support the platform?
R:

**Alternative angle 4:** What happens when a dependency changes?
R: If it's a full change as in, we now use something else, the service in question is updated. If it's a version update, the service get's updated.

**Angle 4 fallback:** How does another system's change affect your work?
R:

### Repeat for every named person, team, organization, or service

- What did they do?
R:Team manager manages, and delegates responsibilities/work tasks. Solution Architect designs along with the manager, and provides technical assistance to other Devs.
InfraStructure team provides assistance with anything infra related, be it pods, k8s, pipelines.

- What did they provide?
R: Information and answers. THe infra team provides functional pods, k8s environmets and pipelines to deploy the software.

- What did you provide them?
R: Informations and questions

- What did they connect to?
R:

- Who contacted them?
R: I contact the infra team and the architect. The manager contacts me.

- What happened if they were unavailable?
R:The infra team cannot be unavailable, otherwise there can be no deployment.

## 5. Failures and recovery

**Primary:** What happens when the platform stops working?
R: Alarm's go off everywhere in Datadog,  the monitoring team picks them up and escalates the issue.

**Nudge 1:** What happens first?
R:

**Nudge 2:** Who notices?
R: Depending on the services that stopped working within the platform either just the team, other teams, or worst case scenario, the customers. 

**Nudge 3:** Who gets involved?
R:The magener and the developer who made the most recent change on the broken service. If it's an infra problem, the infra team is also involved. 

**Primary fallback:** What do you do when the platform is unavailable?
R: It must be fixed. The platform cannot be down.

**Alternative angle 1:** How is service restored?
R: By contacting and escalating the issue until it reaches whomever needs to be reached to get it fixed.

**Angle 1 fallback:** How do you get the platform working again?
R:

**Alternative angle 2:** How do you learn something has failed?
R:

**Angle 2 fallback:** What tells you there is a problem?
R: Either I see it if it happens shortly after a Production deployment, or the monitoring team.

**Alternative angle 3:** What work continues while it is unavailable?
R: All the work not depending on it. Other team's applications that don't need the platform.

**Angle 3 fallback:** What can still be done while it is down?
R:No clue

**Alternative angle 4:** What happens after service returns?
R: Our data is readily available again

**Angle 4 fallback:** How do you return to normal work?
R:

### Repeat for every named failure or recovery action

- What caused it?
R: Errors in software, or some transient problem in infrastructure.

- What detected it?
R: monitoring team

- Who handled it?
R: the team that developed it in case of software error, or the infra team in case of infra problems

- What did they use?
R: if it's software, it gets fixed like normal code. I dont know that the infra team uses. We all use datadog to know what went wrong.

- What did their action produce?
R: a fix

- What showed recovery was complete?
R: either error logs stopped happening (software), or the pods came up and stopped crashing.

## 6. Decisions and ownership

**Primary:** Who decides how platform changes are made?
R: The team manager has the last word. everyone on the team is free to make sujestions though.

**Nudge 1:** Who else is involved?
R:

**Nudge 2:** What guides that decision?
R: Performance, good practices and availabilty

**Nudge 3:** Where do you contribute?
R: with sugestions when new requirements come up-

**Primary fallback:** Who has the final say on a platform change?
R: the team manager

**Alternative angle 1:** Who owns the platform's data?
R: The teams requiring said data to be available

**Angle 1 fallback:** Who is responsible for that data?
R: Us

**Alternative angle 2:** How is access decided?
R: Service access permissions must be decided using Azure AD. When a team must use the platform, they contact us so they can actually use it. 

**Angle 2 fallback:** Who decides who can use the platform?
R:

**Alternative angle 3:** Who accepts a release?
R: Tecnically, first the pull request reviewer, then the team manager, then the board

**Angle 3 fallback:** Who decides a change can go live?
R: The team manager and/or the solution Architect

**Alternative angle 4:** How are responsibilities divided?
R:

**Angle 4 fallback:** Who handles each part of the work?
R:


### Repeat for every named decision, approval, or owner

- What did they decide?
R:The team manager is also a very technically informed individual. He decides both the final architecture (in conjunction with the architec) and functional requirements.

- What evidence did they use?
R:Logic, requirements and good practices

- What did their decision trigger?
R:Development

- Who received the decision?
R:Me

- What happened without approval?
R:Nothing can happen without approval

## Validation record

- **Gate:** Confirm Interview Guide
- **Status:** Approved by the operator
- **Approved structure:** Everyday purpose; one concrete platform change; tools and information; people and services; failures and recovery; decisions and ownership.
