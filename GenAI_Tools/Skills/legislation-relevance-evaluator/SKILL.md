---
name: legislation-relevance-evaluator
description: This skill activates when a user needs to evaluate a stakeholder's pre-prepared operational footprint against a specific regulation. It enforces the use of the LexAPI MCP server to fetch regulatory articles one by one, evaluates their relevance, constructs a thematic chapter and sub-article screening table, and outputs a consolidated list of applicable articles with concise 3-part operational justifications and an exhaustive, unsummarized bulleted listing of every statutory requirement, restriction, and obligation.
---

# AI Skill Specification: legislation-relevance-evaluator

## 1. Semantic Metadata
* **Skill Identifier:** `legislation-relevance-evaluator`
* **Short Summary:** Evaluates a stakeholder's operational footprint against target regulations by fetching articles individually via the LexAPI MCP server, constructing a granular chapter & thematic sub-block screening matrix, and outputting a consolidated list of relevant mandates accompanied by concise 3-part operational justifications and an exhaustive, unsummarized listing of every requirement/restriction/obligation imposed by each article.
* **LLM Routing Description:**
  > "Use this tool to determine which specific articles of a given regulation apply to a stakeholder. The tool requires a pre-existing operational footprint file. The LLM MUST use the LexAPI MCP server to fetch regulatory articles exactly one at a time, evaluate each against the footprint, construct a legislative screening matrix table broken down by thematic sub-article ranges, and output the final list of relevant articles accompanied by concise 3-part operational justifications and an exhaustive, unsummarized bulleted listing of every single requirement, restriction, and obligation present in each article text. Do NOT summarize requirements. Do NOT use this tool to define or build an ArchiMate viewpoint."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "legislation-relevance-evaluator",
  "description": "Evaluates a stakeholder's operational footprint against all articles of a target regulation using factual LexAPI data, outputting a thematic sub-article range screening matrix alongside detailed article mappings with concise 3-part operational justifications and an exhaustive, unsummarized listing of all requirements and restrictions.",
  "parameters": {
    "type": "object",
    "properties": {
      "operational_footprint_file": {
        "type": "string",
        "description": "The file path or content containing the stakeholder's raw operational footprint (e.g., mission, workflow, assets, dependencies)."
      },
      "target_regulation": {
        "type": "string",
        "description": "The specific regulation (e.g., 'DORA', 'NIS2') that the operational footprint must be evaluated against."
      },
      "legal_index_workbook": {
        "type": "string",
        "description": "Matching `<REGULATION>-CELEX:<CELEX>.xlsx` index for the target law. Its Enacting Terms canonical paths are the only permitted legal-text IDs."
      }
    },
    "required": ["operational_footprint_file", "target_regulation", "legal_index_workbook"]
  },
  "returns": {
    "type": "object",
    "description": "A markdown-formatted report containing a granular thematic screening table followed by a detailed list of regulatory articles deemed relevant, including concise justifications and exhaustive, unsummarized requirement/restriction bullet lists."
  }
}
```

## 3. Core Logic & Execution Flow

### A. Theoretical Foundation (Compliance Evaluation)

When executing this skill, the AI acts as a **Regulatory Compliance Analyst**. Its goal is to bridge two distinct domains:

1. **The Operational Reality:** The raw physical and logical assets, tasks, dependencies, and friction points identified in the footprint file.
2. **The Regulatory Mandate:** The strict legal requirements fetched from LexAPI.

### B. Execution Step-by-Step

1. **Footprint Ingestion & Entity Extraction:** Parse the `operational_footprint_file`. Identify critical business processes, software applications, data objects, external vendors, and actors mentioned by the stakeholder.

2. **Mandatory LexAPI Fact-Finding (Iterative):**
   * The LLM **MUST** query the LexAPI MCP Server using the `target_regulation`.
   * **CRITICAL CONSTRAINT:** The LLM must fetch and process the regulation strictly **1 article at a time**.

3. **Granular Thematic Screening & Sub-Block Categorization:**
   * Group the regulation's articles by Chapter / Section.
   * **Sub-Block Partitioning Rule:** Within any given Chapter or Section, the LLM **MUST** subdivide the articles into distinct **thematic sub-article ranges** based on operational topics (e.g. separating governance/board duties from day-to-day technical operations, crisis communications, or vendor contracting within the same chapter).
   * Evaluate each thematic sub-article range independently against the stakeholder's role, class, and operational footprint.
   * Mark each sub-block status explicitly as:
     * **INCLUDED (Arts X–Y):** Contains a specific mandate with a recorded operational chain to the stakeholder's task, asset, dependency, approval, incident interface, or concern. Direct execution is not required.
     * **EXCLUDED (Arts A–B):** Governs topics out of scope for this stakeholder role (e.g. board governance, ESA regulatory reporting, legal procurement contracts, red-team operations).
     * **CONTEXTUAL BASELINE:** Definitions or general scope provisions that provide context but contain no direct operational requirements.
   * Provide a concise, clear justification for the evaluation status of each thematic sub-article block.

4. **Detailed Article-Level Relevance Deduction, Concise Justification & Exhaustive Requirements Listing:**
   * For each article within an **INCLUDED** sub-block, cross-reference its exact provisions against stable `OP-*` and `CON-*` source records. Retain requirements that affect the footprint even where an identified external role owns the control; entity-wide applicability alone is never enough.
   * **EXHAUSTIVE UNCONFLATED REQUIREMENTS RULE (MANDATORY):** Instead of pasting a bulk text extract or summarizing provisions, the evaluator **MUST parse and list every single requirement, restriction, prohibition, condition, and obligation imposed by the text of that article as an individual bullet point without any summarization**. Every sub-paragraph and clause that imposes a duty must have its own clear bullet point identifying what is required or restricted.
   * **CONCISE 3-PART JUSTIFICATION RULE:** Keep the relevance justification concise, precise, and high-density (avoiding repetitive filler words while preserving semantic completeness):
     1. **Operational Anchor:** Concisely name specific physical/logical assets, daily tasks, platforms, or tools from the footprint (e.g. C# ETLs, Azure Pipelines, Datadog, K8s pods).
     2. **Legal Bridge:** Concisely explain *how* the article's requirements apply to those anchored operational items.
     3. **Operational Reality & Gap Annotation:** Concisely describe the current operational handling or explicitly tag missing statutory controls, unperformed tasks, or lack of visibility as `[Gap]`.
   * **MANDATORY STATUTORY GAP LOGGING (`[Gap]`):** If the stakeholder entity is non-exempt (e.g. non-microenterprise) and an applicable statutory article contains mandatory controls or testing demands that are absent from the stakeholder's operational footprint (e.g., missing automated vulnerability scans, static/dynamic code analysis, performance testing, or resilience checks), the evaluator MUST explicitly log these missing requirements as statutory operational gaps (`[Gap]`) in the justification and gap summary, rather than omitting the article or ignoring the unperformed statutory requirements.

5. **Resolve canonical legal-text IDs before coverage approval.** After the in-scope `REQ-*` list is fixed, invoke `legal-text-anchor-resolver` for every requirement. It must match the exact duty to one or more Enacting Terms canonical paths and verify each through `tools/traceability_lookup.py verify-anchor`. Store the ordered direct IDs alongside the ordinary legal citation. Never infer an ID from an Article citation; reject recital, amendment, ambiguous, missing, or unmatched anchors.

6. **Compilation & Strict Quality Check:**
   * Verify that NO article in Section 2 is missing a `Relevance Justification` or the unsummarized requirement list.
   * Verify that justifications are concise yet substantive.
   * Verify that NO requirement is lumped or summarized away; every obligation present in the statutory text must appear.

7. **Output Generation:** Format the compiled findings into the strict Markdown format specified below.

## 4. Safety, Boundaries & Error Interception

* **Zero Guessing Rule:** The LLM must NEVER hallucinate or assume what a regulation states. If the LexAPI search returns zero results or ambiguous text, the LLM must **HALT** and prompt the operator for clarification.
* **One-by-One Mandate:** The LLM must strictly fetch articles one at a time. Fetching multiple articles at once is a violation of this skill's core execution flow.
* **Zero Summarization of Requirements (Hard Intercept):** It is strictly forbidden to summarize or compress the requirements/restrictions of an article into a single generic statement. Every distinct requirement and restriction must be explicitly bulleted.
* **Concise Justification Mandate:** Keep justifications punchy and direct, eliminating verbose narrative bloat while preserving all 3 mandatory components (Anchor, Bridge, Reality/Gap).
* **Mandatory Granular Screening Table:** The LLM MUST include the **Legislative Structure & Screening Table** broken down into thematic sub-article ranges at the beginning of the report.
* **Incomplete Footprint Rule:** If the `operational_footprint_file` lacks sufficient detail to confidently map to the regulatory articles found, the LLM must point out this gap (`[Gap]`) to the operator instead of inventing concepts.
* **Scope Constraint:** The final output must focus purely on legislative relevance. Do not generate any ArchiMate viewpoints, metamodels, or diagrammatic mapping instructions.
* **Canonical Anchor Rule:** Do not approve or pass a legal `REQ-*` downstream without one or more verified direct legal-text IDs. Present `Confirm Legal Text IDs` after resolution and before coverage approval.

## 5. Required Output Format

The LLM must output the result strictly in the following format.

### Output Template

**Regulatory Relevance Report: [Stakeholder Role] - [Regulation]**

* **Operational Footprint Source:** [File Name/Path]
* **Target Regulation:** [Regulation Name / CELEX Number]

---

### 1. Legislative Structure & Screening Table

| Legislative Chapter / Section | Article Range | Operational Scope | Evaluated Status | Inclusion / Exclusion Justification |
| :--- | :--- | :--- | :--- | :--- |
| **[Chapter I: General Provisions]** | Arts [1–4] | [Definitions, scope, and proportionality principle] | **CONTEXTUAL BASELINE** | [General framework definitions; provides regulatory context but contains no direct operational requirements.] |
| ... | ... | ... | ... | ... |

---

### 2. Relevant Articles (Detailed Mapping)

* **Article [X]: [Title of Article]**
  * **Concise Relevance Justification:**
    * **(a) Operational Anchor:** [Specific physical/logical assets, tools, tasks, or dependencies cited directly from footprint, e.g., C# ETLs on EDP, K8s pods, Datadog]
    * **(b) Legal Bridge:** [Concise explanation of how Article X requirements apply to those operational assets/tasks]
    * **(c) Operational Reality & Ownership Annotation:** [Concise description of current handling plus `Directly performed`, `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner`; use `[Gap]` only for a stated missing control or visibility limit]
  * **Statutory Requirements & Restrictions (Unsummarized Listing):**
    * `[REQ-ArtX-01]` [Exact unsummarized statutory requirement / obligation from paragraph 1]
      * **Legal text IDs:** `[Exact Enacting Terms canonical path]`
    * `[REQ-ArtX-02]` [Exact unsummarized statutory requirement / restriction from paragraph 2]
    * `[REQ-ArtX-03]` [Exact unsummarized statutory requirement / prohibition / condition from paragraph 3]
    * *(List every single requirement, restriction, or obligation without omission or summarization)*
