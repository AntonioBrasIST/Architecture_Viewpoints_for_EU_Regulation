# Operational Footprint Interview

## 1. Core Responsibilities

**What do you look after each day?**
R: I'm responsible for starburst, openmetadata and singlestore technoligies. Everyday I need to give access to users that require it, understand issues that developers have connecting/using these technologies and trying to improve this tech layer either with updates or other configs.

- What else needs your attention?
  R:
- Which part takes most time?
  R: Access control, although I already automated part of it with a python script unfortunatly it can still take a lot of time. Starburst uses ranger for the acess control so it has a few moving parts regarding the policies
- What are your regular responsibilities?
  R:
- Which results are you responsible for?
  R:
- What outcomes must your work achieve?
  R:Make sure these tech stack works smoothly and that the devs and apps have their necessary access
- What work cannot wait?
  R:problems with singlestore tech usually are a fix ASAP. a lot of apps have their BDs there so problems with that can lead to a lost of service
- What must be handled quickly?
  R:starburst problems are ususally less urgent since it has less users. Some alerts in datadog regarding my teams tech stack can also be less urgent. it all depends on what is breaking and how it is breaking
- What changes from day to day?
  R:not much, its a very monotonous work. 
- What varies in your daily work?
  R:
- What do others depend on you for?
  R:
- What do colleagues need from you?
  R:my team is responsible for a variaty of technologies, some multi tech problems I'll need to be involved. Some of my colegues might need extra hands on their side like on kafka, cosmos, databricks etc and I'll help them

## 2. Workflows and Changes

**Describe one recent production change.**
R:My most recent change was a upgrade to the starburst deployment. we had a script to deploy it but thats not the most correct and efficient way to do it. So I changed and tested a migration to a gitops deployment so that flux in the target AKS could deploy the changes made.

- What happened first?
  R: the first thing we did was backuping the data in the starburst tech stack, more specifically from ranger. so we wouldnt lose all the access and policies and users accessess
- What happened next?
  R:we then activated flux to be able to deploy our starburst configs with gitops
- Tell me about one change you recently made.
  R:
- What starts that work?
  R:normally this types of changes (updates and upgrades) start by a period of testing in non productive envs. and we only go fowards after some time to make sure everything is stable and the users havent reported any issues. this is to minimize the chances of breaking production
- What triggers the change?
  R:in this situation it was a necessity so we can later have a easier way to deploy this technology in DR situation. 
- Who performs each step?
  R:in this step I had one por memeber of my team helping out to make sure we were not forgeting anything since it was a big change, but that being said most of the time its a 1 man job
- Who does the work?
  R:
- What do you use during the change?
  R:mostly the command line so we can do kubectl commands and check logs and validate other things as we go along. in my day command line with kubectl is my most used tool
- Which tools support the work?
  R:
- What happens after completion?
  R:always validate if everything is working, and in this case one of the things we could do was making a simple query in starburst to check if it was up and connecting to the DBs
- What follows the finished change?
  R:

## 3. Systems, Data, and Outputs

**Which tools do you use daily?**
R:kubectl, vscode, git are my main ones since I'm responsible to the techstack at the data layer most of the time I'm "playing around" at the config level of those technologies and these toolds are very important. also some python for automations. and recently LLMs that help me parse logs and search info online

- What do you do with each?
  R:
- What connects to them?
  R:kubectl is to connect to the aks, the git and vscode it to change the yaml configs of the technologies
- Which tools are essential to your work?
  R:
- What information do you read?
  R:at the table level almost nothing as it is not needed but I read and use root level passwords of diferent techologies with PII data. considering my job I have acess to a lot of confidential data. That being said most of the time I dont need to read any of the tables data. and the few queries I do is to test connection so its a simple select * from table limit 10;
- What information do you need to see?
  R:passwords and another secrets in the azure key vaults. its is necessary a lot of times to be able to correct issues
- What information do you change?
  R:I do not change any info, even though I have the access the nature of my job does not require and I can never change info unless specifically told with a change made by a devops teams that has been previously aproved 
- What information do you update?
  R:
- Where do you keep configuration details?
  R:the configs are kept on azure devops except passwords those are in a azure keyvault. AKS also has secrets but its through a resource type called external secret that connects it to the keyvault, so the source is still that keyvault 
- Where are those details recorded?
  R:all changes in PRD are recorded in a change openned in service now. those changes can be openned by myself if its un update or something I want to change to improve or by other teams if they need me to do some change in production. in non productive envs things asked by other teams are with service now incidents and I can test things without having to record it in an official matter. 
- What does your work produce?
  R:
- What results or records do you create?
  R:

## 4. Dependencies and Handoffs

**Who do you rely on to complete work?**
R: A lot of times I rely to a team that is responsible for the layer bellow us, they are responsible for the AKS and other more compute things, as well as the networking team. I also talk a lot with support teams of the technologies we use.

- What do they provide?
  R:from just normal support to correction to the compute infrastructure 
- What do you send them?
  R:mostly logs and sometimes configs
- Who helps you finish a task?
  R:
- What comes from outside your team?
  R:
- What do other teams provide?
  R:
- Which outside services do you use?
  R:
- What external services support your work?
  R:
- Who uses the result of your work?
  R:the result of my work is used by the devops teams
- Who needs what you produce?
  R:
- What work stops without another team?
  R:connection issues most of the times require another team so those task ended stopped there. and the same for the compute team. if its a task that does not require them it usually I can go from start to finish by myself of with the support team of the technologies I'm having an issue
- Which work depends on others?
  R:

## 5. Failures, Recovery, and On-Call Work

**Tell me about a recent production issue.**
R:singlestore stopped working. that made it so the front facing app stoppde working and a myriad of other services

- What stopped working?
  R:
- What did you do first?
  R:the first thig was trying to restart singlestore and then ficure out what cause it so we can mitigate it
- Describe a recent problem in production.
  R:
- How did you notice it?
  R:we have datadog looking a large quantity of metrics and what that happends a lot of alerts start ringing as well as phones
- How was the problem detected?
  R:
- Who joined the response?
  R:singlestore problems normally my team lead joins and later even other devops leads so we can understand the problem. and in extreme cases even the support team
- Who helped resolve it?
  R:
- What did you use to recover?
  R:the tech native toolds
- Which tools supported recovery?
  R:
- What happens after the service returns?
  R:we always create a report to send to support. so they can correct if something is broken and they can also advise on config changes so it gets more resillient
- What do you do once it works again?
  R:

## 6. Authority, Ownership, and Review

**Who authorizes a production change?**
R:we have a team responsible for authorizations, for access control all the requests go through a security team

- How is approval recorded?
  R:the service now change request system keeps track of the aprovals as well as the change request status
- Who decides when a change may proceed?
  R:is automated and configured when the request is being opened
- Who owns each system you support?
  R:
- Who is accountable for that system?
  R:my team is accountable for those technologies we configure.
- Who decides access permissions?
  R:the teams themselves decide what they need, but it passes through security team for the aproval
- Who approves access?
  R:
- How are urgent changes handled?
  R:critical changes that affect service are made as needed. reports are written after to keep track
- What happens when time is limited?
  R:
- Who checks a completed change?
  R:we self check and review. sometimes we also ask some devop teams for a small test
- Who reviews the result afterward?
  R:
