---
name: extract-operational-footprint
description: Extracts a stakeholder's operational footprint from an interview transcript, detailing daily tasks, workflows, dependencies, and pain points.
---

## name: extract_operational_footprint
description: Extracts a stakeholder's operational footprint from an interview transcript, detailing daily tasks, dependencies, pain points, and cross-layer ArchiMate element mappings (Active Structure, Behavior, Passive Structure).

# AI Skill Specification: extract_operational_footprint

## 1. Semantic Metadata

* **Skill Identifier:** `extract_operational_footprint`
* **Short Summary:** Analyzes a stakeholder interview to synthesize their operational footprint, detailing standard workflows and mapping extracted entities directly into ArchiMate structural categories.
* **LLM Routing Description:**
> "Use this tool when acting as an Expert Business Analyst and Organizational Designer to synthesize a stakeholder's operational footprint from an interview transcript. This tool maps real-world answers to architectural dimensions. Do NOT use this tool to generate code, and do NOT use this tool if the interview text or file path is missing."



## 2. Interface Schema (JSON Style)

```json
{
  "name": "extract_operational_footprint",
  "description": "Analyzes an interview transcript to synthesize the stakeholder's operational footprint and ArchiMate categorization.",
  "parameters": {
    "type": "object",
    "properties": {
      "interview_source": {
        "type": "string",
        "description": "The raw interview text or the directory path to the interview file."
      }
    },
    "required": ["interview_source"]
  },
  "returns": {
    "type": "string",
    "description": "A structured markdown report detailing Core Role Context, Tasks, Dependencies, Friction, and ArchiMate cross-layer entity mappings."
  }
}

```

## 3. Core Logic & Execution Flow

1. **Pre-execution Verification (Step 1: Input Verification):**
* Check if the `interview_source` (text or directory path) is provided in the prompt context.
* If missing, **STOP** immediately and output exactly: *"Please provide the directory path to the interview file or paste the interview transcript."* Do not proceed.


2. **Main Processing Path (Step 2: Analysis & Extraction):**
* **Core Context & Operations:** Identify the stakeholder's primary mandate, daily recurring tasks, dependencies (people/systems), approval gates, incident interfaces, assets/data, and operational bottlenecks.
* **Stable source register:** Assign a stable `OP-*` ID to every distinct task, asset/data object, dependency, approval, incident interface, and explicit operational gap. Preserve the interview evidence beside the ID; never collapse separate facts because they are later mapped to one stream.
* **ArchiMate Translation (Cross-Layer Mapping):** Dissect the extracted entities and categorize them strictly into three architectural domains:
* *Active Structure:* Who or what performs the action (Business Actors, Roles, Technology Nodes, Devices).
* *Behavior:* What is being done (Business Processes, Workflows, Events, Triggers).
* *Passive Structure:* What is being acted upon or used (Application Components, System Software, Data Objects).




3. **State & Context Preservation:**
* Read-only analysis. Does not modify external files or states.



## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True - If the transcript is absent, the AI must halt and prompt the operator. Before compiling and saving the final footprint to `3_operational_footprint.md`, you must execute two sequential gating checks using the `question` tool:
  * **Gate 3.1 (Tasks & Mappings):**
    - **Header:** `Confirm Extracted Tasks`
    - **Question:** `"I have extracted the following core tasks and mapped them to their respective ArchiMate layers: [list tasks & layer mappings]. Do you agree with these extracted tasks and layer classifications?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Gate 3.2 (Operational Relationships):**
    * **Header:** `Confirm Operational Relationships`
    * **Question:** Present every proposed `REL-OP-*` using textual source name,
      action/meaning, textual target name, ArchiMate candidate, and exact `OP-*`
      evidence. Ask the operator to approve or correct the atomic relationships.
  * **Gate 3.3 (Gaps & Friction Points):**
    - **Header:** `Confirm Gaps & Friction`
    - **Question:** `"I have identified the following operational friction points and inferred compliance gaps [Gap] from the transcript: [list friction and gaps]. Do you agree with this friction and gap analysis?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Execution Rule:** Resolve Gate 3.1, then relationship Gate 3.2, then gap Gate
    3.3. Proceed only when all three are approved.
* **Deterministic Error Matrix:**

| Input/State Failure | System Error Action | Return Message to LLM |
| --- | --- | --- |
| Missing interview text/path | Halt execution | `"Please provide the directory path to the interview file or paste the interview transcript."` |
| Missing data for a specific section | Proceed | Do not hallucinate; leave the section blank or state *"No entities identified."* |

* **Strict Constraints:**
* Extract *only* what is explicitly stated in the transcript. Do not infer or invent ArchiMate components that the stakeholder did not mention.
* Tag inferred gaps explicitly as `[Gap]` if the stakeholder implies a missing process (e.g., resilience testing unperformed).
* Each `OP-*` item must be individually approved in Gate 3.1 or Gate 3.3 before it can be used in regulatory coverage.
* Invoke `evidence-grounded-relationship-ledger` after fact extraction. Preserve
  explicit subject-action-object statements as `REL-OP-*` rows with distinct named
  endpoints, direction, natural-language meaning, proposed ArchiMate type, exact
  evidence, and approval. A stakeholder saying they develop Offload, ETL, or Query
  services is affirmative relationship evidence, not unrelated catalog membership.
* Co-occurrence and shared stream membership do not establish a relationship. If
  an endpoint or meaning is unclear, halt for clarification rather than leave a
  future view element unconnected.



## 5. Required Output Format

The AI must provide a structured text report using exactly the following markdown format:

### Stakeholder Operational Footprint

**1. Core Role Context:**
[Brief description of the stakeholder's primary objective and scope]

**2. Everyday Tasks:**

* [Task 1]
* [Task 2]

**3. Key Dependencies:**

* [Dependency 1]
* [Dependency 2]

**4. Operational Insights & Friction:**
[Pain points, manual workarounds, bottlenecks, or notable observations]

**5. Operational Source Register:**

| Source ID | Type | Stated Operational Fact | Interview Evidence |
| --- | --- | --- | --- |
| OP-001 | Task / Asset / Dependency / Approval / Incident interface / Gap | [Distinct fact] | [Transcript evidence] |


### ArchiMate Cross-Layer Mapping

*The following operational entities have been extracted directly from the interview answers and mapped into their respective ArchiMate elements.*

**A. Active Structure (Actors, Roles, & Nodes)**

* **Business Actors / Roles:**
* **[Actor/Role Name]:** [Brief description of their extracted responsibility/action]


* **Technology Nodes & Devices:**
* **[Node/Device Name]:** [Brief description of the hardware/platform]



**B. Behavior (Processes & Events)**

* **Business Processes:**
* **[Process Name]:** [Brief description of the workflow or lifecycle]


* **Business Events:**
* **[Event Name]:** [Brief description of what triggers a process]



**C. Passive Structure (Application Components, Systems, & Data)**

* **Application Components & System Software:**
* **[Component/System Name]:** [Brief descrisption of the software, API, or infrastructure service]


* **Data Objects:**
* **[Data Object Name]:** [Brief description of the information or physical data payload]
