---
name: regulation-blind-operational-discovery
description: This skill activates when a user needs to interview a stakeholder who has little to no knowledge of a specific regulation to deeply extract their operational footprint. It generates a structured interview guide using very short, non-leading questions, nudges, alternative angles, and true fallback questions, each followed by a designated response line. Do NOT use this tool to define or build an ArchiMate viewpoint.
---

# AI Skill Specification: regulation_blind_operational_discovery

## 1. Semantic Metadata

* **Skill Identifier:** `regulation_blind_operational_discovery`
* **Short Summary:** Assists Enterprise Architects (EAs) in designing a jargon-free, short-question interview script to extract a highly detailed operational footprint from a regulation-naive stakeholder. This sets the factual groundwork for future regulatory mapping.
* **LLM Routing Description:**
> "Use this tool when an Enterprise Architect needs to interview a business or IT stakeholder who knows NOTHING or VERY LITTLE about a specific regulation (like DORA or eIDAS). The goal is to discover their operational footprint (processes, tools, data, dependencies) without guiding their answers. Do NOT use this tool if the user is asking to build or define an ArchiMate viewpoint directly."



## 2. Interface Schema (JSON Style)

```json
{
  "name": "regulation_blind_operational_discovery",
  "description": "Formulates a jargon-free, non-leading interview script to extract an operational footprint from a regulation-naive stakeholder.",
  "parameters": {
    "type": "object",
    "properties": {
      "target_stakeholder_profile": {
        "type": "string",
        "description": "The specific persona and role of the stakeholder being interviewed (e.g., 'Head of Customer Onboarding' or 'Lead Cloud Engineer')."
      },
      "operational_domain": {
        "type": "string",
        "description": "The specific business area or project context being investigated (e.g., 'Payment processing pipeline' or 'Warehouse inventory management')."
      },
      "hidden_regulatory_context": {
        "type": "string",
        "description": "The target regulation the EA is secretly investigating (e.g., 'DORA', 'NIS2'). The LLM uses this to subtly focus the operational topics, but MUST NOT mention it in the questions."
      }
    },
    "required": ["target_stakeholder_profile", "operational_domain", "hidden_regulatory_context"]
  },
  "returns": {
    "type": "object",
    "description": "A structured interview guide consisting exclusively of short, open-ended, non-leading questions, nudges, fallback questions, and alternative angle questions. Each generated question is followed by an empty 'R:' line for responses."
  }
}

```

## 3. Core Logic & Execution Flow

### A. Theoretical Foundation (Extracting Raw Reality)

When executing this skill, the AI must act as an expert Enterprise Architecture Consultant conducting pure discovery.

* **The Objective:** To capture the underlying architecture model, which is the raw, unrestricted reality of the stakeholder's daily operations.
* **The Rule of Silence:** The stakeholder must never be exposed to technical modeling jargon or regulatory terminology.
* **The Anti-Leading Mandate:** Questions must be incredibly brief. Over-explaining a question gives the stakeholder the "expected" answer. The LLM must generate questions that force the stakeholder to fill the silence with their operational reality.

### B. The 6-Step Operational Extraction Framework

The AI must customize these structural steps based on the `target_stakeholder_profile` and the `hidden_regulatory_context`. **All generated questions MUST be strictly short (ideally under 15 words) and entirely open-ended.**

| Step | Discovery Target | Standard Short-Question Template (To be Contextualized) | Intent for Later Mapping |
| --- | --- | --- | --- |
| **1** | **Core Mission** | *"What are your main daily responsibilities?"* or *"Describe your primary objective."* | Establishes the primary business value and top-level capabilities. |
| **2** | **Workflow & Processes** | *"How do you achieve this, step-by-step?"* or *"What triggers this workflow?"* | Extracts the sequential business processes and actions. |
| **3** | **Critical Assets** | *"What tools are strictly required?"* or *"What data do you use?"* | Uncovers the software components, systems, and passive data objects. |
| **4** | **External Dependencies** | *"Who outside your team helps you?"* or *"What external vendors are involved?"* | Identifies third-party risks, external roles, and integrations. |
| **5** | **Failure & Resilience** | *"What happens if this tool fails?"* or *"How do you recover from a crash?"* | Extracts disaster recovery paths, physical nodes, and single points of failure. |
| **6** | **Governance & Ownership** | *"Who approves changes here?"* or *"Who owns this data?"* | Identifies the active structure actors, roles, and decision-makers. |

For every named activity or asset, include short, non-leading follow-ups that
elicit relationship facts: `What do you do with it?`, `What does it connect to?`,
`Who performs that step?`, `What does it produce?`, and `What uses the result?`.
Keep one-concrete-change questioning for large platforms; never ask for a vague
walkthrough of all concurrent platform change.

### C. Step-by-Step Elicitation Path (How the Agent must work)

1. **Ingest Inputs:** Read `target_stakeholder_profile`, `operational_domain`, and `hidden_regulatory_context`.
2. **Validation & No-Guessing Check:** The AI must NEVER guess. If the provided inputs are too vague, ambiguous, or incomplete to generate a highly targeted script, the LLM must halt execution and prompt the operator for specific clarifying details.
3. **Adopt the Persona:** Act purely as an inquisitive, non-technical investigator.
4. **Draft the Script:** Generate the 6-step interview guide. Ensure every single primary question follows the strict "Short & Non-Leading" mandate.
5. **Mandatory Response Lines:** After *every single question* (including primary questions, nudges, fallbacks, and alternative angles), you must insert a new line starting with `R:` to reserve space for the user's response.
6. **Provide Follow-Up Prompts, Fallbacks, and Alternative Angles:**
7. **Interactive Validation Gate:** Before compiling and saving the final interview guide to `2_interview.md`, you MUST invoke the `question` tool to show the operator the drafted core themes and questions and obtain explicit approval:
   * **Header:** `Confirm Interview Guide`
   * **Question:** `"I have designed the 6-step interview guide for [Stakeholder Profile] under [Operational Domain]. Here are the proposed core themes and key questions: [list them]. Do you agree with this interview structure?"`
   * **Options:** `Yes (Recommended)`, `No` (with custom answer support)

* **Nudges:** 2-3 short prompts (e.g., *"And then?"*, *"What else?"*, *"Why?"*) to keep the stakeholder talking if they pause.
* **Fallback Questions (for the primary question):** Direct rephrasings of the *exact same primary question* in simpler or different words (used if the stakeholder misunderstands the initial short prompt).
* **Alternative Angles:** At least 4 different questions regarding the *same subject* to uncover hidden aspects, edge cases, or details not captured by the primary question. These remain non-leading but shift the perspective.
* **Alternative Angle Fallbacks:** Each alternative angle must have its own direct fallback rephrasing.

## 4. Safety, Boundaries & Error Interception

* **Strict No-Guessing Rule:** If the operator provides insufficient or unclear context regarding the stakeholder's profile, operational domain, or the hidden regulatory context, the LLM must explicitly halt and ask the operator clarifying questions. Do not fabricate, assume, or guess context.
* **MANDATORY CONSTRAINT - Short Questions:** If a generated question exceeds 15-20 words, the LLM must rewrite it to be shorter. Do not use compound questions (e.g., do not ask "What tools do you use and who approves them?"). Break them up.
* **MANDATORY CONSTRAINT - Response Lines:** Every question must be immediately followed by a line that reads exactly `R:`.
* **Zero-Regulation Rule:** The generated interview script must completely hide the regulatory context. No legal articles, compliance acronyms, or audit terminology whatsoever.
* **No ArchiMate Jargon Leakage:** Under no circumstances should the generated interview script include ArchiMate words.
* **No Viewpoint Creation:** Do not output any matrix, translation key, or mapping guide. This skill stops the moment the operational data is extracted.

## 5. Reference Interview Recipes (Few-Shot Examples)

### Example 1: DORA (Hidden Context: Third-Party ICT Risk)

* **Profile:** E-Commerce Logistics Manager
* **Domain:** Order Dispatch

**Generated Interview Script:**

1. **Core Mission:** "What are your main daily responsibilities?"
R:

* *Nudge 1:* "What else?"
R:
* *Nudge 2:* "Can you elaborate?"
R:
* *Primary Fallback:* "What does your role entail on a daily basis?"
R:
* *Alternative Angle 1:* "What defines a successful day for your department?"
R:
* *Fallback 1:* "How do you know you had a good day?"
R:
* *Alternative Angle 2:* "What is your primary metric?"
R:
* *Fallback 2:* "How is your performance measured here?"
R:
* *Alternative Angle 3:* "What takes up most of your time?"
R:
* *Fallback 3:* "Where do you spend the majority of your hours?"
R:
* *Alternative Angle 4:* "What is your team's main deliverable?"
R:
* *Fallback 4:* "What exactly does your team produce?"
R:

2. **Workflow:** "Walk me through a standard dispatch."
R:

* *Nudge 1:* "What happens next?"
R:
* *Nudge 2:* "And then?"
R:
* *Primary Fallback:* "Can you explain the dispatch process from start to finish?"
R:
* *Alternative Angle 1:* "What is the very first step you take when an order arrives?"
R:
* *Fallback 1:* "How does the dispatch process start?"
R:
* *Alternative Angle 2:* "Are there any manual steps in this process?"
R:
* *Fallback 2:* "Do you have to do anything by hand?"
R:
* *Alternative Angle 3:* "What triggers this entire workflow?"
R:
* *Fallback 3:* "What event starts this whole chain?"
R:
* *Alternative Angle 4:* "Where does your part of the process end?"
R:
* *Fallback 4:* "When is your specific job considered finished?"
R:

3. **Critical Assets:** "What specific software do you use?"
R:

* *Nudge 1:* "Where is that data stored?"
R:
* *Nudge 2:* "Any spreadsheets?"
R:
* *Primary Fallback:* "Which computer programs do you need to do your job?"
R:
* *Alternative Angle 1:* "If your computer was wiped, what applications must be reinstalled?"
R:
* *Fallback 1:* "What programs are absolutely essential to reinstall?"
R:
* *Alternative Angle 2:* "Do you use any physical hardware or scanners?"
R:
* *Fallback 2:* "Are there any physical devices you rely on?"
R:
* *Alternative Angle 3:* "Where is the order data physically stored?"
R:
* *Fallback 3:* "Which system holds the actual order information?"
R:
* *Alternative Angle 4:* "Are there any critical spreadsheets you maintain?"
R:
* *Fallback 4:* "Do you rely on Excel files to track anything?"
R:

4. **External Dependencies:** "Which external companies are involved?"
R:

* *Nudge 1:* "Are there any cloud tools?"
R:
* *Nudge 2:* "Who physically ships it?"
R:
* *Primary Fallback:* "Do you work with any outside vendors for this?"
R:
* *Alternative Angle 1:* "Could you do this entire job without any outside help?"
R:
* *Fallback 1:* "Are you fully independent of other organizations?"
R:
* *Alternative Angle 2:* "What third-party platforms integrate with your system?"
R:
* *Fallback 2:* "Which outside software connects to yours?"
R:
* *Alternative Angle 3:* "Who physically ships the product?"
R:
* *Fallback 3:* "Which company handles the physical delivery?"
R:
* *Alternative Angle 4:* "Do you rely on any external cloud providers?"
R:
* *Fallback 4:* "Is any of your data hosted by outside cloud companies?"
R:

5. **Failure Mechanics:** "What happens if the routing software crashes?"
R:

* *Nudge 1:* "How long until operations stop?"
R:
* *Nudge 2:* "Who do you call first?"
R:
* *Primary Fallback:* "If the routing system goes down, what is the impact?"
R:
* *Alternative Angle 1:* "What is your manual workaround when the internet is entirely down?"
R:
* *Fallback 1:* "How do you work if you lose internet access?"
R:
* *Alternative Angle 2:* "How long can operations run without this system?"
R:
* *Fallback 2:* "What is the maximum downtime you can survive?"
R:
* *Alternative Angle 3:* "Who is the very first person you call during an outage?"
R:
* *Fallback 3:* "Who do you contact when the system breaks?"
R:
* *Alternative Angle 4:* "Where are the backup files located?"
R:
* *Fallback 4:* "How do you access historical data if the main system fails?"
R:

6. **Governance:** "Who signs the contracts for these vendors?"
R:

* *Nudge 1:* "Who approves the budget?"
R:
* *Nudge 2:* "Who audits them?"
R:
* *Primary Fallback:* "Who is responsible for agreeing to vendor terms?"
R:
* *Alternative Angle 1:* "If you need to purchase a new logistics tool tomorrow, who has to say yes?"
R:
* *Fallback 1:* "Who approves new software purchases?"
R:
* *Alternative Angle 2:* "Who audits these external vendors?"
R:
* *Fallback 2:* "Who checks that the vendors are doing their job safely?"
R:
* *Alternative Angle 3:* "Who owns the budget for your department's tools?"
R:
* *Fallback 3:* "Who pays for the software you use?"
R:
* *Alternative Angle 4:* "Who is responsible for updating the dispatch procedures?"
R:
* *Fallback 4:* "Who holds the authority to change how you work?"
R:

### Example 2: eIDAS (Hidden Context: Digital Identity Verification)

* **Profile:** Customer Support Lead
* **Domain:** User Account Recovery

**Generated Interview Script:**

1. **Core Mission:** "What is your team's main function?"
R:

* *Nudge 1:* "Any other tasks?"
R:
* *Nudge 2:* "Who do you report to?"
R:
* *Primary Fallback:* "What is the primary purpose of your team?"
R:
* *Alternative Angle 1:* "What core service do you provide to the rest of the business?"
R:
* *Fallback 1:* "How does your team help the wider company?"
R:
* *Alternative Angle 2:* "What is your primary daily outcome?"
R:
* *Fallback 2:* "What must you achieve by the end of the day?"
R:
* *Alternative Angle 3:* "Who are your main internal clients?"
R:
* *Fallback 3:* "Which other departments rely on your work?"
R:
* *Alternative Angle 4:* "What is the biggest challenge in your role?"
R:
* *Fallback 4:* "What part of your job is the hardest?"
R:

2. **Workflow:** "Walk me through a standard customer interaction."
R:

* *Nudge 1:* "How do they prove who they are?"
R:
* *Nudge 2:* "What is the exact next step?"
R:
* *Primary Fallback:* "Can you describe a typical interaction with a user?"
R:
* *Alternative Angle 1:* "Describe a typical support ticket from opening to closing."
R:
* *Fallback 1:* "How does a ticket move from start to finish?"
R:
* *Alternative Angle 2:* "How are edge cases or exceptions handled?"
R:
* *Fallback 2:* "What do you do when a request doesn't fit the standard process?"
R:
* *Alternative Angle 3:* "What is the exact next step after verifying an ID?"
R:
* *Fallback 3:* "Once identity is confirmed, what happens immediately after?"
R:
* *Alternative Angle 4:* "How long does a standard verification take?"
R:
* *Fallback 4:* "What is the average time spent on one user?"
R:

3. **Critical Assets:** "Where do you view their information?"
R:

* *Nudge 1:* "What database holds this?"
R:
* *Nudge 2:* "Any other screens open?"
R:
* *Primary Fallback:* "In which system do you look at customer data?"
R:
* *Alternative Angle 1:* "What specific systems must be running for you to verify someone?"
R:
* *Fallback 1:* "Which tools are mandatory for the verification step?"
R:
* *Alternative Angle 2:* "Where are these documents permanently stored?"
R:
* *Fallback 2:* "Which database holds the long-term records?"
R:
* *Alternative Angle 3:* "What kind of data do you extract from the IDs?"
R:
* *Fallback 3:* "Which specific fields do you copy from the documents?"
R:
* *Alternative Angle 4:* "Do you use a CRM or a custom dashboard?"
R:
* *Fallback 4:* "What type of software interface do you look at?"
R:

4. **External Dependencies:** "Do any external services connect to your tools?"
R:

* *Nudge 1:* "Any government portals?"
R:
* *Nudge 2:* "Third-party APIs?"
R:
* *Primary Fallback:* "Are there outside systems linked to your software?"
R:
* *Alternative Angle 1:* "Is all the identity verification done entirely in-house?"
R:
* *Fallback 1:* "Do we handle all verifications without outside help?"
R:
* *Alternative Angle 2:* "Do you rely on external databases for background checks?"
R:
* *Fallback 2:* "Do you query any government or private registries?"
R:
* *Alternative Angle 3:* "Who developed the scanning software?"
R:
* *Fallback 3:* "Was the ID scanner built internally or bought?"
R:
* *Alternative Angle 4:* "Are there any third-party APIs involved?"
R:
* *Fallback 4:* "Does the system talk to outside software automatically?"
R:

5. **Failure Mechanics:** "What happens if a fake document is submitted?"
R:

* *Nudge 1:* "How do you detect that?"
R:
* *Nudge 2:* "Then what?"
R:
* *Primary Fallback:* "How is a forged document handled if received?"
R:
* *Alternative Angle 1:* "Walk me through the exact steps when a verification looks suspicious."
R:
* *Fallback 1:* "What is the protocol for suspected fraud?"
R:
* *Alternative Angle 2:* "Who is notified when fraud is detected?"
R:
* *Fallback 2:* "Who gets the alert when an ID is fake?"
R:
* *Alternative Angle 3:* "What happens if the verification API goes down?"
R:
* *Fallback 3:* "If the external checker fails, what do you do?"
R:
* *Alternative Angle 4:* "Can a user bypass the automated check manually?"
R:
* *Fallback 4:* "Is there a manual override for failed automated checks?"
R:

6. **Governance:** "Who owns the privacy policy for this data?"
R:

* *Nudge 1:* "Who updates it?"
R:
* *Nudge 2:* "Who is responsible for breaches?"
R:
* *Primary Fallback:* "Who is in charge of the data privacy rules here?"
R:
* *Alternative Angle 1:* "Who takes the ultimate blame if this customer data leaks?"
R:
* *Fallback 1:* "Who is held accountable for data breaches here?"
R:
* *Alternative Angle 2:* "Who updates the verification procedures?"
R:
* *Fallback 2:* "Who writes the rules for how you check IDs?"
R:
* *Alternative Angle 3:* "Who audits your team's compliance with these rules?"
R:
* *Fallback 3:* "Who checks your work to ensure procedures are followed?"
R:
* *Alternative Angle 4:* "Who approves access requests to this database?"
R:
* *Fallback 4:* "Who decides which employees can see these IDs?"
R:
