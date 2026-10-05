---
name: viewpoint-scope-definer
description: This skill activates when a user needs to define the scope and boundaries of an ArchiMate viewpoint based on a stakeholder's operational footprint and a pre-compiled list of relevant legislative articles. It outputs the boundary of representation, justifications, specific viewpoint inclusions (what and why), and the detailed legislative focus.
---

# AI Skill Specification: viewpoint-scope-definer

## 1. Semantic Metadata

* **Skill Identifier:** `viewpoint-scope-definer`
* **Short Summary:** Determines the exact scope and architectural boundaries of a regulatory viewpoint by analyzing a stakeholder's operational footprint alongside their applicable legislative articles.
* **LLM Routing Description:**
  > "Use this tool to define the scope of a regulatory ArchiMate viewpoint. It requires two pre-existing inputs: a file detailing the stakeholder's operational footprint, and a file containing the specific legislative articles relevant to them. The tool decides what should be represented, where the boundary of responsibility lies, what architectural elements to include (and why), and which legislative parts require detailed focus. Do NOT use this tool to fetch legislation or conduct initial interviews."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "viewpoint-scope-definer",
  "description": "Defines the scope, boundaries, and required inclusions of an ArchiMate viewpoint based on operational and legislative inputs.",
  "parameters": {
    "type": "object",
    "properties": {
      "operational_footprint_file": {
        "type": "string",
        "description": "The file path or content containing the stakeholder's raw operational footprint (assets, processes, dependencies, etc.)."
      },
      "relevant_articles_file": {
        "type": "string",
        "description": "The file path or content containing the specific legislative articles that have already been deemed relevant to this stakeholder."
      },
      "stakeholder_classification_file": {
        "type": "string",
        "description": "Approved Step 4 classification and distinct CON-* concern records."
      },
      "coverage_ledger": {
        "type": "string",
        "description": "Approved Step 5 Footprint-Regulation Coverage Ledger with no unresolved items and direct legal-text IDs for each legal REQ-*."
      },
      "relationship_ledger": {
        "type": "string",
        "description": "Approved REL-OP-*, REL-COV-*, REL-ROLE-*, and REL-COMP-* relationships with exact endpoints and evidence."
      },
      "regulation_overview_baseline": {
        "type": "string",
        "description": "Path to the immutable, selected-technology View 0 baseline for the complete regulation."
      }
    },
    "required": ["operational_footprint_file", "relevant_articles_file", "stakeholder_classification_file", "coverage_ledger", "relationship_ledger", "regulation_overview_baseline"]
  },
  "returns": {
    "type": "object",
    "description": "A markdown-formatted scoping document detailing the viewpoint's boundary, justification, inclusions, and legislative focus."
  }
}

```

## 3. Core Logic & Execution Flow

### A. Theoretical Foundation (Scope & Boundary Definition)

When executing this skill, the AI acts as an **Architecture Scoping Strategist**. Its goal is to synthesize two existing datasets (operational reality and applicable law) to define the *limits* of the viewpoint. It must answer: *Where does this stakeholder's concern begin and end?* If a law mandates data encryption, but the stakeholder only handles physical shipping, the scope must strictly reflect their physical domain, leaving cryptography to the IT stakeholder's viewpoint.

### B. Execution Step-by-Step

1. **Input Ingestion:** Read and analyze the `operational_footprint_file`, `stakeholder_classification_file`, `relevant_articles_file`, approved `coverage_ledger`, and immutable regulation overview baseline. Specifically parse `OP-*`, `CON-*`, the unsummarized `REQ-*` requirements, approved direct legal-text IDs, ownership states, and unresolved register. Halt if the ledger is missing, unresolved, or a legal requirement lacks IDs. Use the baseline only to identify regulation-wide duties outside the stakeholder boundary; do not modify it or use it as compliance evidence.
2. **Boundary Delineation:** Define the boundary around the approved Coverage Ledger: direct work, constraints on that work, externally owned duties with recorded operational effects, and role-specific operational context. Do not extend it to entity-wide obligations without a recorded operational chain.
3. **Legislation-Agnostic Scoping Rules:**
   * **RULE A: FUNCTIONAL DOMAIN COHESION:** Statutory requirements addressing the same functional domain (e.g. *Testing & Verification*, *Third-Party Risk*, *Incident Telemetry*, *Change & Access Governance*) MUST be unified into coherent, domain-aligned scope streams, regardless of which specific regulation or article numbers they stem from. Articles or statutory provisions governing the same domain MUST NOT be artificially split into unrelated scopes.
   * **RULE B: MULTIDIMENSIONAL PERSPECTIVE DISAMBIGUATION:** When defining operational streams and scope inclusions, the scoping strategist MUST categorize and disambiguate requirements using three universal architectural perspectives:
     - **Governance Perspective (`[Governance]`):** High-level policy frameworks, executive/board oversight, regulatory accountability, risk appetites, and organizational mandates (Drivers, Principles, Roles, Risk Frameworks).
     - **Administrative & Process Management Perspective (`[Administrative]`):** Procedural workflows, change request authorizations, approval sign-off gates, segregation of duties, access request approvals, vendor contract registers, and documentation management (Business Processes, Change Requests, Sign-offs).
     - **Technical & Operational Assurance Perspective (`[Technical]`):** Execution-level tools, automated and manual quality/security verification mechanisms, codebase integrity checks, vulnerability assessments & scans, static/dynamic software analysis, performance testing, source code peer reviews, runtime telemetry, and infrastructure deployment controls (Application Components, Automated Pipelines, Test Suites, Artifacts, Telemetry Monitors).
   * **RULE C: GRANULAR STATUTORY REQUIREMENT SCOPING:** Scoping MUST NOT stop at the article level. For each relevant article, the scoping document must explicitly identify:
     - Which specific granular statutory requirements (`REQ-*`) are `Directly performed`, `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner`.
     - Which source-backed external responsibility must remain visible as a role, approval, or dependency rather than a stakeholder realization.
4. **Inclusion Mapping (What & Why):** Assign every approved `OP-*` and `CON-*` to a named requirement family, visible external role/dependency, or a dedicated role-specific operational-context stream. Tag each by perspective and provide an architectural reason. A routine fact with no legal edge remains mandatory operational-context coverage.
5. **Node-and-Relationship View Ledger:** For every cohesive stream, define exact
   node membership plus every approved `REL-*` relationship needed by that graph.
   Carry family containment, coverage, legal IDs, traceability, and ownership
   unchanged. Coverage or stream membership is not a relationship, and relation
   count is unlimited.
6. **Connectivity partitioning:** Invoke `connected-view-validator`. Every node has
   degree at least one, every candidate includes the stakeholder, and each has one
   weakly connected component. Split multi-island candidates into semantically
   named views. Halt for operator evidence or exclusion clarification when a
   component lacks an approved stakeholder path. More than 30 roots is an advisory
   readability warning, not an omission rule.
7. **Legislative Focus Extraction:** Identify which specific parts of the provided legislation represent the heaviest burden or highest risk for this specific footprint, designating them for "greater detail" in the final view.
8. **Output Generation:** Format the findings into the strict Markdown format specified below.

## 4. Safety, Boundaries & Error Interception

* **Zero Assumption Rule:** The LLM must rely *only* on the provided files. It must not hallucinate extra operational duties or invent new legal articles not present in the inputs.
* **Coverage Interception:** If any `OP-*`, `CON-*`, or in-scope `REQ-*` is absent from the ledger assignment, halt and return it to `Confirm Coverage Resolution`; never quietly omit it or invent an owner.
* **Legal-anchor preservation:** Do not resolve, alter, or omit legal-text IDs in scoping. A legal Requirement/Constraint without carried direct IDs is invalid and must return to Step 5.
* **Interactive Validation Gates:** Before compiling and saving the final scope to `6_viewpoint_scope.md`, execute three sequential gating checks using the `question` tool:
  * **Gate 6.1 (Boundary & Legislative Focus):**
    - **Header:** `Confirm Scope Boundary`
    - **Question:** `"The viewpoint boundary is defined as: [boundary] and primary legislative focus is: [focus]. Do you agree with this viewpoint boundary and primary legislative focus?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Gate 6.2 (Inclusions & Streams):**
    - **Header:** `Confirm Inclusions & Streams`
    - **Question:** `"I have grouped the viewpoint inclusions into [N] core functional streams/views, tagged by perspective: [list streams & inclusions]. Do you agree with these specific inclusions and thematic streams?"`
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Gate 6.3 (Connectivity & Splits):**
    - **Header:** `Confirm Connectivity & Splits`
    - **Question:** Present textual node and relationship names, stakeholder paths,
      component counts, proposed semantic split names, and any 30-root warnings.
    - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
  * **Execution Rule:** Resolve Gates 6.1, 6.2, and 6.3 in order. Proceed only when all are approved.
* **Missing Context Interception:** If the footprint file and the articles file have zero logical intersection (e.g., the footprint is about HR, but the articles are strictly about IT server redundancies), the LLM must **HALT** and ask the user to clarify the mismatch before generating the scope.
* **No Diagramming:** This skill defines the *scope* and *boundary* of the viewpoint. It must not attempt to draw PlantUML, Mermaid, or generate the actual ArchiMate diagram.

## 5. Required Output Format

The LLM must output the result strictly in the following format.

### Output Template

**Viewpoint Scope Definition: [Stakeholder Role]**

| Scope Dimension | Definition |
| --- | --- |
| **Operational Source** | [Name/Path of the operational footprint file] |
| **Legislative Source** | [Name/Path of the relevant articles file] |
| **Viewpoint Boundary** | [Clear definition of the limits of what is represented. What is explicitly *in* scope and what is explicitly *out* of scope for this specific stakeholder?] |
| **Scope Justification** | [Detailed explanation of *why* this boundary was chosen based on the intersection of their daily operations and the legal mandates.] |

---

### Viewpoint Inclusions (What & Why)

* **[Element/Concept 1 to Include - e.g., Third-Party Cloud Providers]**
* *Why:* [Justification linking the footprint to the legal requirement, e.g., "Article 15 mandates oversight of all external data hosts."]


* **[Element/Concept 2 to Include - e.g., Data Backup Processes]**
* *Why:* [Justification...]
*(Repeat for all major required inclusions)*



---

### Detailed Legislative Focus

* **Primary Legislative Focus:** [Which specific article or clause requires the most granular representation?]
* **Detail Rationale:** [Explanation of why this specific part of the full legislation needs greater detail (e.g., due to high compliance risk, complex operational impact, or heavy reliance on specific assets).]

---

### Requirement-Family Ledger

| Family Parent | Nested Child Requirements | Coverage IDs / Ownership States | Legal Text IDs / Source / Operational Traceability | Visible External Links |
| --- | --- | --- | --- | --- |
| [Meaningful parent] | [Target-qualified children] | [COV-* and approved state] | [Article clauses and/or operational elements] | [Role, cross-family, direct-realization links only] |
