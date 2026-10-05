---
name: engineer-viewpoint-interview-recipe

description: This skill activates when a user needs to design a customized questionnaire, interview script, or elicitation guide for a specific project stakeholder to define an ArchiMate viewpoint. Do NOT use this tool if the user is asking to build/draw a viewpoint diagram directly, or if the user is a non-architect seeking basic ArchiMate training.
---

# AI Skill Specification: engineer_viewpoint_interview_recipe

## 1. Semantic Metadata
* **Skill Identifier:** `engineer_viewpoint_interview_recipe`
* **Short Summary:** Assists Enterprise Architects in designing tailored, stakeholder-centric interview guides that deterministically extract the structural dimensions of an ArchiMate viewpoint without exposing technical modeling jargon.
* **LLM Routing Description:**
  > "Use this tool when an Enterprise Architect (EA) needs to design a customized questionnaire, interview script, or elicitation guide for a specific project stakeholder to define an ArchiMate viewpoint. Do NOT use this tool if the user is asking to build/draw a viewpoint diagram directly, or if the user is a non-architect seeking basic ArchiMate training."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "engineer_viewpoint_interview_recipe",
  "description": "Formulates a contextualized stakeholder interview script and translation matrix to define an ArchiMate viewpoint.",
  "parameters": {
    "type": "object",
    "properties": {
      "target_stakeholder_profile": {
        "type": "string",
        "description": "The specific persona, role, and mission of the stakeholder being interviewed (e.g., 'CISO responsible for DORA compliance' or 'Product Manager of a mobile app')."
      },
      "project_context_type": {
        "type": "string",
        "enum": ["small_tech_project", "large_scale_business_mapping", "regulatory_compliance_mapping", "custom"],
        "description": "The scale and nature of the initiative, which dictates the adaptation rules of the questions."
      },
      "project_context_description": {
        "type": "string",
        "description": "A description of the project, including its boundaries, critical deadlines, or strategic drivers (e.g., 'Migrating customer profiles to a centralized DB' or 'Implementing DORA digital operational resilience rules')."
      },
      "known_concerns_or_hypotheses": {
        "type": "string",
        "description": "Any pre-identified pain points, risks, or topics the EA wants to ensure are covered during the interview."
      }
    },
    "required": ["target_stakeholder_profile", "project_context_type", "project_context_description"]
  },
  "returns": {
    "type": "object",
    "description": "A structured, complete interview recipe including the contextualized questionnaire, mapping rules to ArchiMate dimensions, and fallback options."
  }
}
```

## 3. Core Logic & Execution Flow

### A. Theoretical Foundation (What is a Viewpoint?)
When executing this skill, the AI must act as an expert Enterprise Architecture Consultant. It must understand the core definitions of **ISO/IEC 42010** and the **ArchiMate Specification**:
*   **Architecture View (The Instance):** The actual diagram or work product (e.g., the schematic of the specific payment system).
*   **Architecture Viewpoint (The Schema):** The specification of the ru\s, conventions, layers, and aspects used to construct that view.
*   **Analogies to keep in mind:**
    1.  *The Camera Filter:* The architecture model is reality; the viewpoint is the filter isolating specific wavelengths (e.g., thermal tracking) while blurring out irrelevant data.
    2.  *The Structural Blueprint:* Different engineers (electrical, structural, HVAC) look at the same physical building but require different blueprint templates (viewpoints) to isolate their concerns.

### B. Core Adaptation Rules (Contextual Tuning)
The AI must adapt the wording, metaphors, and focus of the interview questions based on the `project_context_type`:

1.  **Small Tech Project:**
    *   *Tone:* Action-oriented, lightweight, pragmatic.
    *   *Metaphors:* Plumbing, gears, engine parts, road trips.
    *   *Focus:* Deep dive into Technology and Application layers; focus on immediate technical dependencies, performance bottlenecks, and resource allocation.
2.  **Large Scale Business Mapping:**
    *   *Tone:* Strategic, capability-focused, value-driven.
    *   *Metaphors:* Organisms, cities, symphony orchestras, maps.
    *   *Focus:* Strategy and Business layers; focus on business capabilities, value streams, organizational silos, and horizontal cooperation.
3.  **Regulatory & Compliance Mapping (e.g., DORA, GDPR):**
    *   *Tone:* Rigorous, risk-averse, precise, traceable.
    *   *Metaphors:* Guardrails, check-points, shields, audits, safety nets.
    *   *Focus:* Motivation (Drivers, Requirements, Constraints) and Application/Technology layers; focus on traceability, data flows, operational boundaries, incident recovery paths, and accountability.

### C. The 7-Step Elicitation Framework & Question Templates
The AI must customize the standard question set from `Questions.md` to match the selected context and persona:

| Step | ArchiMate Dimension | Core Question Template (to be Contextualized) | Transition/Translation Key for the EA |
| :--- | :--- | :--- | :--- |
| **1** | **Define Persona** | *"Beyond your job title, what is your specific 'mission' or mandate regarding this project?"* | Identifies the **Motivation** elements (Drivers, Goals) and primary actor boundaries. |
| **2** | **Select Concerns** | *"If you had to explain the biggest risk or critical success factor for this project in a 30-second elevator ride, what would it be? And does this primarily involve people/processes, software/data, or technology/infrastructure? (This helps us understand the architectural domain of your concern.)"* | Maps to **Pain Points/Drivers**; implicitly guides **Layer/Aspect** deduction based on focus (e.g., "people/processes" -> Business Layer, Active Structure Aspect). |
| **3** | **Identify Objects** | *"When you think about the core subject of our discussion, what are the 'moving parts' you genuinely care about (e.g., specific departments, critical software systems, or physical infrastructure components)?"* | Whitelists specific **ArchiMate elements** and begins to clarify **Layer**. |
| **4** | **Determine Representation** | *"Do you prefer a high-level 'map' of connections, a 'step-by-step' story, or a 'traffic light' heat map of what is broken? How detailed does this need to be—an overview, how things link together, or specific technical configurations? (This will define the level of granularity.)"* | Determines the **Notation/Visual Style** and implicitly guides **Abstraction Level**. |
| **5** | **Define Layer & Aspect** | **Layer:** *"Are we primarily focusing on how people interact (Business), how software functions (Application), or how physical systems operate (Technology)? Does your concern stem from strategic goals, business processes, or detailed implementation? (Choose the primary area of focus.)"*<br>**Aspect:** *"Are you primarily interested in 'Who or what' performs actions (e.g., departments, systems), 'What' actions or processes occur (e.g., workflows, functions), or 'What' information/data is involved in these actions? (Choose the main perspective.)"* | Directly maps to **Layer** and **Aspect** based on explicit choice and keywords from previous questions. |
| **6** | **Determine Purpose** | *"After looking at this view, what is the *next* critical action you need to take? Do you need to understand a concept, give instructions to build something, or make a key decision (e.g., sign off on a budget, approve a change, assess compliance)? (Your action will guide the viewpoint's depth and breadth.)"* | Maps to Standard **Purpose** (Informing/Designing/Deciding); implicitly guides **Abstraction Level** (e.g., "sign off" often implies Overview/Coherence). |
| **7** | **Abstraction Level** | *"If this architecture were a Google Map, do you need to see individual house numbers (Detail), city street layouts (Coherence), or the highway system (Overview)?"* | Maps to Abstraction Level:<br>• **Detail:** Tech specs / Builders<br>• **Coherence:** Interaction / Coordinators<br>• **Overview:** High-level capabilities / Funders |

### D. Step-by-Step EAs Elicitation Path (How the Agent must work)
1.  **Ingest Inputs:** Read `target_stakeholder_profile`, `project_context_type`, and `project_context_description`.
2.  **Generate a Highly Detailed, Tailored Interview Guide:** Apply the contextual adaptation rules to completely customize the 7 steps.
3.  **Produce Fallback Scenarios:** Provide secondary questions in case the stakeholder is non-responsive or overly technical.
4.  **Produce the Translation Key:** Generate a specific ArchiMate translation guide for the EA to decipher the stakeholder's eventual answers.

### E. Deduction Logic for Viewpoint Fields

The LLM will analyze responses to the interview questions, particularly those from Steps 2, 4, 5, and 6, to deduce the appropriate ArchiMate Layer, Aspect, and Abstraction Level. This deduction will leverage keyword analysis and the `project_context_type`.

**1. Deducing ArchiMate Layer:**
    *   **Motivation/Strategy Layer:** Inferred if keywords like "goals, drivers, mandates, strategic objectives, why we do things" are prominent, especially from Step 2 and 5 answers.
    *   **Business Layer:** Inferred if keywords like "people, processes, organizational workflows, departments, activities" are prominent, especially from Step 2 and 5 answers.
    *   **Application Layer:** Inferred if keywords like "software, systems, data, integrations, applications" are prominent, especially from Step 2 and 5 answers.
    *   **Technology Layer:** Inferred if keywords like "hardware, infrastructure, servers, networks, configurations, physical systems" are prominent, especially from Step 2 and 5 answers.
    *   **Contextual Weighting:** For `regulatory_compliance_mapping`, higher weighting will be given to Motivation, Business, and Application Layers, especially concerning data flows and accountability. For `small_tech_project`, more weight on Application and Technology Layers.

**2. Deducing ArchiMate Aspect:**
    *   **Active Structure Aspect:** Inferred if keywords like "who does, actors, systems, teams, responsible parties, what performs actions" are prominent, especially from Step 5 answers.
    *   **Behavior Aspect:** Inferred if keywords like "actions, processes, activities, sequence, how it gets done, workflows, functions" are prominent, especially from Step 5 answers.
    *   **Passive Structure Aspect:** Inferred if keywords like "information, data, artifacts, what is involved, data affected" are prominent, especially from Step 5 answers.

**3. Deducing Abstraction Level:**
    *   **Overview Level:** Inferred if keywords like "broad overview, big picture, high-level summaries, KPIs, strategic impact, sign off on budget" are prominent, especially from Step 4 and 6 answers, and often associated with "Informing" or "Deciding" purposes.
    *   **Coherence Level:** Inferred if keywords like "how parts connect, mid-level view, interactions, flows, linking together, process maps" are prominent, especially from Step 4 and 6 answers, and can be associated with all purposes.
    *   **Detail Level:** Inferred if keywords like "fine-grained detail, specifics, individual instances, configurations, drill-down, instructions to build" are prominent, especially from Step 4 and 6 answers, and often associated with "Designing" purposes.
    *   **Contextual Weighting:** For `regulatory_compliance_mapping`, "Coherence" and "Detail" for traceability are often prioritized. For "Designing" purposes, "Detail" is more likely.

## 4. Safety, Boundaries & Error Interception
*   **No Technical Jargon Leakage:** Under no circumstances should the generated interview script include ArchiMate words like *Metamodel*, *Active Structure Aspect*, *Realization Relationship*, or *Decomposition*.
*   **Context Mismatch Prevention:** If the `project_context_type` is `regulatory_compliance_mapping` but the EA describes a context focused solely on infrastructure racking, output a warning advising them that the motivation/compliance layers should be prioritized.
*   **Loop Prevention Rule:** "If this tool fails to produce custom-tailored metaphors twice consecutively, revert to standard templates and explicitly prompt the user for human guidance."

## 5. Reference Interview Recipes (Few-Shot Examples)

### Example 1: Large-Scale Business Mapping (e.g., E-Commerce Transformation)
*   **Context:** Digital Transformation of a traditional retail chain.
*   **Stakeholder:** VP of Retail Operations.
*   **Generated Interview Script:**
    1.  *Persona Mission:* "Beyond your VP title, what is your primary mandate for this transformation?" (Targeting: Business Actors & Strategy Goals).
    2.  *Risk/Concern:* "If this rollout fails, what operational metric will crash first? Is it order processing delay or customer service complaints?" (Targeting: Business Processes/Services bottlenecks).
    3.  *Objects of Interest:* "When tracking an order, do you care about the software databases, the warehouse staff steps, or the physical delivery trucks?" (Targeting: Whitelisting elements).
    4.  *Representation:* "Would you prefer to see a map of our current operational capabilities, or a step-by-step swimlane diagram of how an order moves across departments?" (Targeting: Capability Maps or Process Diagrams).
    5.  *Abstraction:* "Do you need to see the individual keys entered by a clerk, the flow of information between departments, or the 30,000-foot view of retail operations?" (Targeting: Coherence level).

### Example 2: Regulatory Compliance Mapping (e.g., DORA Resilience)
*   **Context:** Aligning critical ICT services with DORA (Digital Operational Resilience Act) requirements.
*   **Stakeholder:** ICT Risk Officer.
*   **Generated Interview Script:**
    1.  *Persona Mission:* "What specific regulatory article of DORA are you tasked with certifying compliance for in this audit?" (Targeting: Motivation Requirements).
    2.  *Risk/Concern:* "In the event of a severe cyber-incident, what is the biggest threat to our operational resilience? Is it failing to report the breach on time, or losing transaction data?" (Targeting: Business Continuity & Risk).
    3.  *Objects of Interest:* "Which critical ICT systems, data processing nodes, and third-party vendors must be mapped to prove compliance?" (Targeting: Application Components & Technology Nodes).
    4.  *Representation:* "Do you require a compliance compliance-matrix (table) mapping services to regulations, or a visual flow chart showing redundancy and failover paths?" (Targeting: Matrix or Functional Flow).
    5.  *Abstraction:* "Do we need to show the exact IP configurations and firewall rules (Detail), the interactions between ICT systems and third-party vendors (Coherence), or our overall digital resilience posture for the board (Overview)?" (Targeting: Coherence level).
