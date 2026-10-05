---
name: extract-stakeholder-class-and-concerns
description: Analyzes a stakeholder's operational footprint report to classify their organizational level and extract an exhaustive, unsummarized list of every explicitly stated concern or friction point.
---

# AI Skill Specification: extract_stakeholder_class_and_concerns

## 1. Semantic Metadata

* **Skill Identifier:** `extract_stakeholder_class_and_concerns`
* **Short Summary:** Evaluates an operational footprint document to determine the stakeholder's hierarchical class (e.g., Junior, Senior, Management) and compiles a comprehensive, non-summarized list of all operational concerns.
* **LLM Routing Description:**
> "Use this tool to process an existing 'Stakeholder Operational Footprint' report. It determines the stakeholder's seniority/class based on their described duties (e.g., approvals, reviews, core tasks) and extracts an exhaustive, itemized list of every single pain point, gap, or concern mentioned. Do NOT use this tool to summarize concerns; every individual concern must be listed explicitly."



## 2. Interface Schema (JSON Style)

```json
{
  "name": "extract_stakeholder_class_and_concerns",
  "description": "Classifies stakeholder seniority and extracts an exhaustive list of operational concerns from a footprint report.",
  "parameters": {
    "type": "object",
    "properties": {
      "operational_footprint_report": {
        "type": "string",
        "description": "The generated markdown report containing the stakeholder's core role context, everyday tasks, dependencies, and operational friction."
      }
    },
    "required": ["operational_footprint_report"]
  },
  "returns": {
    "type": "string",
    "description": "A structured markdown output detailing the Stakeholder Class Justification and an exhaustive, itemized list of all concerns."
  }
}

```

## 3. Core Logic & Execution Flow

1. **Pre-execution Verification (Input Verification):**
* Verify the `operational_footprint_report` is provided and contains readable text.
* If the input is missing, vague, or incomplete, **STOP** execution and output: *"Please provide the complete Operational Footprint report for analysis. If specific tasks or pain points are missing from the report, please clarify them before proceeding."*


2. **Main Processing Path (Classification & Extraction):**
* **Class Assessment:** Analyze the "Everyday Tasks," "Core Role Context," and "Dependencies" to determine the stakeholder's class.
* *Junior/Execution Level:* Focuses on isolated tasks, requires approvals, relies heavily on senior guidance.
* *Senior/Architect Level:* Dictates standards, reviews work (e.g., Pull Requests), vets external tools, handles complex system integrations.
* *Management/Governance Level:* Owns final approvals, manages budgets, assumes accountability for deployments/failures.


* **Exhaustive Concern Extraction:** Scan the "Operational Insights & Friction" and "Dependencies" sections. Extract **every single** bottleneck, missing process (e.g., `[Gap]`), manual workaround, and failure point. Assign each distinct concern a stable `CON-*` ID and retain its originating `OP-*` ID where one exists.


3. **State & Context Preservation:**
* This is a read-only parsing operation. It transforms existing analytical text into a strict classification and exhaustive list.



## 4. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** True - If the provided report lacks sufficient detail to definitively classify the stakeholder, the AI must halt and ask the operator for clarifying details regarding the stakeholder's approval authority or autonomy. Before compiling and saving the classification to `4_stakeholder_classification.md`, you must execute two sequential gating checks using the `question` tool:
  * **Gate 4.1 (Seniority Classification):**
    - **Header:** `Confirm Seniority Class`
    - **Question:** `"I have assessed the stakeholder's profile and daily tasks. I propose the following classification: Assigned Class: [Seniority], Justification: [Justification]. Do you agree with this seniority classification and justification?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Gate 4.2 (Exhaustive Concern List):**
    - **Header:** `Confirm Concern List`
    - **Question:** `"I have compiled the exhaustive, unsummarized list of [N] concerns and bottlenecks: [Brief list]. Do you agree with this concern list? (Note: No concerns have been grouped or summarized, preserving raw fidelity)."`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Execution Rule:** Ensure Gate 4.1 is resolved first, then Gate 4.2. Proceed only when both are approved.
* **Deterministic Error Matrix:**

| Input/State Failure | System Error Action | Return Message to LLM |
| --- | --- | --- |
| Missing footprint report | Halt execution | `"Please provide the complete Operational Footprint report for analysis."` |
| Ambiguous seniority (tasks conflict) | Halt execution | `"Stakeholder tasks show overlapping Junior and Management duties. Please clarify their direct reporting structure or approval authority."` |
| No concerns found in text | Proceed with notation | `"No explicit concerns or friction points were identified in the provided report."` |

* **Strict Constraints:**
* **NO SUMMARIZATION:** You must not group, synthesize, or summarize the concerns. If the stakeholder mentions 14 distinct friction points, the output must contain exactly 14 bullet points.
* **NO ASSUMPTIONS:** Do not invent concerns based on the stakeholder's class. Extract only what is present in the source text.
* **SOURCE FIDELITY:** A concern remains a separate `CON-*` record even when it shares a source, legal requirement, or eventual stream with another concern.



## 5. Required Output Format

The AI must provide a structured text report using exactly the following markdown format:

### Stakeholder Classification & Concern Audit

**1. Stakeholder Class & Justification:**

* **Assigned Class:** [e.g., Senior Programmer, Management, Junior Developer, Compliance Officer]
* **Justification:** [1-2 sentences strictly citing the specific tasks or approval authorities from the report that led to this classification.]

**2. Exhaustive List of Concerns:**
*(Note: This is a direct, unsummarized extraction of all identified friction points, gaps, and operational bottlenecks.)*

* **CON-001 / OP-001 — Concern 1:** [Exact detail of the pain point or gap]
* **Concern 2:** [Exact detail of the pain point or gap]
* **Concern 3:** [Exact detail of the pain point or gap]
*(Continue until every single concern is listed)*
