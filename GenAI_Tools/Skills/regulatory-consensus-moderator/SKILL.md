---
name: regulatory-consensus-moderator
description: Orchestrates a 3-agent parallel regulatory search and consensus debate protocol (Literal Evaluator 4a, Systemic Evaluator 4b, Gap Evaluator 4c) to produce a unanimously agreed set of applicable legislative articles (4a ∩ 4b ∩ 4c).
---

# AI Skill Specification: regulatory-consensus-moderator

## 1. Semantic Metadata
* **Skill Identifier:** `regulatory-consensus-moderator`
* **Short Summary:** Facilitates a 3-agent parallel regulatory assessment (Literal, Systemic, Gap), conducts multi-turn peer debate and cross-defense, and computes the strict unanimous intersection of applicable legislative articles with combined 3-part operational justifications.
* **LLM Routing Description:**
  > "Use this tool to orchestrate a 3-agent regulatory evaluation and debate protocol. It triggers Literal (4a), Systemic (4b), and Gap (4c) evaluator subagents concurrently using LexAPI, conducts multi-turn peer confrontation over task IDs, filters for strict unanimous intersection (4a ∩ 4b ∩ 4c), and synthesizes a final consensus report for operator validation."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "regulatory-consensus-moderator",
  "description": "Orchestrates 3 parallel evaluator agents (Literal 4a, Systemic 4b, Gap 4c), manages cross-defense and debate rounds, and compiles the unanimous consensus regulatory relevance report.",
  "parameters": {
    "type": "object",
    "properties": {
      "operational_footprint_file": {
        "type": "string",
        "description": "Path to the stakeholder's operational footprint file."
      },
      "stakeholder_classification_file": {
        "type": "string",
        "description": "Path to the stakeholder classification and concerns file."
      },
      "target_regulation": {
        "type": "string",
        "description": "The target EU regulation (e.g., 'DORA', 'NIS2', 'eIDAS')."
      }
    },
    "required": ["operational_footprint_file", "target_regulation"]
  },
  "returns": {
    "type": "object",
    "description": "Consolidated Markdown report containing initial agent proposals, debate summary, unanimous article intersection table, and combined 3-part operational justifications."
  }
}
```

## 3. Core Logic & Execution Flow

### Phase 1: Parallel Multi-Perspective Evaluation
The moderator triggers 3 specialized subagents concurrently:
1. **Agent 4a (`4a-eu-legislation-literal-evaluator`):** Evaluates articles through strict textual keyword matching, explicit legal mandates, and direct operational duties.
2. **Agent 4b (`4b-eu-legislation-systemic-evaluator`):** Evaluates articles through systemic architecture, cross-system dependencies, structural workflows, and governance controls.
3. **Agent 4c (`4c-eu-legislation-gap-evaluator`):** Evaluates articles through friction points, operational gaps `[Gap]`, incident response, and vulnerability handling.

Each agent independently queries LexAPI (1 article at a time) using the `legislation-relevance-evaluator` skill and returns its candidate screening matrix and article list.

### Phase 2: Initial Proposal Matrix & Discrepancy Identification
The moderator compiles the initial evaluations into a comparison matrix:
* **Unanimous Inclusions ($4a = 4b = 4c = \text{INCLUDED}$):** Articles agreed upon by all 3 agents in Phase 1.
* **Disputed Articles:** Articles included by 1 or 2 agents but excluded by others.
* **Unanimous Exclusions:** Articles excluded by all 3 agents.

### Phase 3: Peer Confrontation & Cross-Defense (Debate Round)
The moderator re-invokes each evaluator agent via its `task_id`, presenting the disputed articles and peer arguments:

```
[Moderator Prompt to Agent 4a via task_id]:
"Peer Evaluation Summary:
- Agent 4b (Systemic) proposed INCLUSION of Article 9 (Protection & Prevention) based on K8s infrastructure monitoring.
- Agent 4c (Gap) proposed INCLUSION of Article 9 based on missing automated patch management [Gap].
- You (Agent 4a) EXCLUDED Article 9 citing lack of direct SDLC developer mandates.

Debate Task:
1. Re-evaluate Article 9 against 4b and 4c's operational arguments.
2. Formally defend your exclusion OR accept peer inclusion with updated justification.
3. Respond to peer challenges for any articles you uniquely included."
```

Each agent performs a cross-defense turn, providing counter-arguments or revising its stance.

### Phase 4: Strict Unanimous Agreement Filter ($4a \cap 4b \cap 4c$)
After debate, the moderator calculates the final consensus:
* **STRICT INTERSECTION RULE:** An article is **INCLUDED** in the final regulatory relevance report **IF AND ONLY IF** all 3 agents explicitly agree to include it after deliberation.
* If any single agent maintains a valid, unrefuted exclusion stance grounded in the footprint, the article MUST be omitted from the final active list and recorded in the Disputed / Omitted Candidates section with justification.

### Phase 5: Synthesis of Combined Concise 3-Part Operational Justifications & Granular Requirements
For each unanimously agreed article, the moderator synthesizes:
1. **Concise Operational Justification:**
   - **Operational Anchor:** Combines physical/logical assets from 4a (direct code/tools), 4b (architectural dependencies), and 4c (friction/gap assets) in a concise, direct listing.
   - **Legal Bridge:** Concise synthesized legal mapping explaining how the requirements apply.
   - **Operational Reality & Gap Annotation:** Combined operational reality and explicit `[Gap]` tags across perspectives.
2. **Exhaustive Statutory Requirements & Restrictions (Unsummarized):**
   - Compiles every single requirement, restriction, prohibition, condition, and obligation identified in that article across the evaluations.
   - **Zero Summarization Rule:** Maintains the unsummarized, bulleted list of each specific statutory requirement, ensuring every mandatory clause is discrete, addressable, and ready to be mapped as an element in subsequent steps.

### Phase 6: Legal-Index Generation, Legal-Text IDs, Coverage Ledger, Human-in-the-Loop Review & Persistence
After the unanimous article and requirement intersection is formed and Gates 5.1 and 5.2 are approved, present Gate 5.3, `Confirm Legal Index`. It must state the selected regulation, CELEX, TraceabilityMatrixCreator selector, expected `<REGULATION>-CELEX:<CELEX>.xlsx` path, and that any same-name workbook will be regenerated. On approval, run `(cd TraceabilityMatrixCreator/TraceabilityMatrixCreator.App && dotnet run --project ../TraceabilityMatrixCreator -- <selector>)` from the repository root and regenerate the workbook in `TraceabilityMatrixCreator/OutputDirectory`. Validate the exact filename, `Recitals` and `Enacting Terms` schema, and returned law/CELEX identity using `tools/traceability_lookup.py row-id --row 1`. Record regulation, CELEX, selector, generated path, generation timestamp, and the successful validation result as Legal Index Provenance in the Step 5 report. Do not resolve anchors until validation succeeds.

Invoke `legal-text-anchor-resolver` with only the generated workbook from Legal Index Provenance. Match every approved atomic `REQ-*` to exact binding Enacting Terms text and verify every canonical path through `tools/traceability_lookup.py verify-anchor`. Persist each requirement's ordered direct IDs beside its citation; reject recitals, amendment provisions, missing, ambiguous, or citation-only inferred anchors. Then invoke `stakeholder-footprint-coverage` and `evidence-grounded-relationship-ledger`. Build endpoint-specific `REL-COV-*` representation edges in addition to coverage rows; shared stream membership is not a relationship. A legal requirement remains stakeholder-relevant when it has a recorded operational chain, whether it is directly performed, constrains the stakeholder, is externally owned, or has unclear ownership. Keep non-regulatory source items in a named role-specific operational-context stream. Do not persist while the uncovered register has unresolved entries or a visible coverage edge lacks exact endpoints.

After coverage resolution invoke `stakeholder-legal-role-mapper`. Keep the
stakeholder, employing organization, and law-defined entity group distinct and
build only evidence-backed `REL-ROLE-*` edges. Never infer organization
applicability or classify an employee as the regulated entity.

The moderator presents the draft report to the operator for review. Before compiling the final consensus report and saving to `5_regulatory_relevance.md`, execute these sequential gates:
The moderator presents the draft report to the operator for review. Before compiling the final consensus report and saving to `5_regulatory_relevance.md`, you must execute two sequential gating checks using the `question` tool:
* **Gate 5.1 (Agreed Articles):**
  - **Header:** `Confirm Agreed Articles`
  - **Question:** `"I have moderated the 3-agent panel. The following [N] articles have achieved strict unanimous agreement: [list articles], each with concise justifications and exhaustive unsummarized requirements. Do you agree with including these articles and their requirements?"`
  - **Options:** `Yes (Recommended)`, `No` (with custom feedback)
* **Gate 5.2 (Omitted Candidates):**
  - **Header:** `Confirm Omitted Articles`
  - **Question:** `"These [M] articles were split decisions (no unanimous consensus) and have been omitted: [list omitted articles]. Would you like to force-include any of these omitted candidate articles?"`
  - **Options:** `No, keep them omitted (Recommended)`, `Yes, force-include ALL of them`, `Yes, select individual articles` (with custom feedback)
* **Gate 5.3 (Legal Index):**
  - **Header:** `Confirm Legal Index`
  - **Question:** `"Generate the legal index for [regulation] (CELEX [CELEX]) using selector [selector] at [output path]? An existing workbook at that path will be regenerated."`
  - **Options:** `Generate index (Recommended)`, `Abort`
* **Gate 5.4 (Legal Text IDs):**
  - **Header:** `Confirm Legal Text IDs`
  - **Question:** `"Each approved REQ-* has these verified direct Enacting Terms canonical IDs: [requirement-to-ID mapping]. Do you approve this legal-text traceability mapping?"`
  - **Options:** `Approve IDs (Recommended)`, `Revise mapping` (with custom feedback)
* **Gate 5.5 (Coverage Resolution):**
  - **Header:** `Confirm Coverage Resolution`
  - **Question:** `"The Footprint-Regulation Coverage Ledger maps all OP-* and CON-* records to a named stream/context and every in-scope REQ-* to a recorded operational chain. The uncovered register is: [items]. Resolve every listed item before continuing."`
  - **Options:** `Approve complete coverage (Recommended)`, `Revise coverage` (with custom feedback)
* **Gate 5.6 (Stakeholder Legal Role):**
  - **Header:** `Confirm Stakeholder Legal Role`
  - **Question:** Present textual stakeholder, organization, and legal-role names,
    relationship meanings, evidence, and proposed ArchiMate tuples before their
    `REL-ROLE-*` identifiers. Ask the operator to approve or correct the chain.
* **Execution Rule:** Resolve Gates 5.1 through 5.5 in order, then Gate 5.6.
  Proceed to write only after endpoint-specific coverage relationships and the
  legal-role chain are approved.

## 4. Required Output Format

```markdown
# Regulatory Relevance Consensus Report: [Stakeholder Role] - [Regulation]

* **Operational Footprint Source:** [Path]
* **Target Regulation:** [Regulation Name / CELEX]
* **Evaluation Panel:** 3-Agent Panel (4a Literal, 4b Systemic, 4c Gap)

## Legal Index Provenance

* **Regulation:** [Regulation]
* **CELEX:** [CELEX]
* **Selector:** [TraceabilityMatrixCreator selector]
* **Generated Workbook:** [Path]
* **Generation Timestamp:** [ISO 8601 timestamp]
* **Validation:** [Successful `row-id --row 1` result including law and CELEX]

---

## 1. Panel Debate & Consensus Summary

| Article / Range | Agent 4a (Literal) | Agent 4b (Systemic) | Agent 4c (Gap) | Post-Debate Consensus | Key Resolution / Debate Summary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Arts 1–4** | Baseline | Baseline | Baseline | **BASELINE** | Definitions & general provisions. |
| **Arts 7–10** | Included | Included | Included | **UNANIMOUS INCLUSION** | All 3 agents agreed on ICT risk protection & logging. |
| **Art 14** | Excluded | Included | Included | **OMITTED (No Consensus)** | 4a maintained textual exclusion; 2/3 majority insufficient for inclusion. |

---

## 2. Legislative Structure & Final Screening Matrix

| Legislative Chapter / Section | Article Range | Operational Scope | Evaluated Status | Consensus Inclusion / Exclusion Justification |
| :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... |

---

## 3. Unanimously Agreed Relevant Articles (Detailed Mapping)

* **Article [X]: [Title of Article]**
  * **Concise Consensus 3-Part Justification:**
    * **(a) Operational Anchor:** [Combined assets, tools, and workflows anchored in footprint]
    * **(b) Legal Bridge:** [Synthesized legal mapping across textual, systemic, and risk perspectives]
    * **(c) Operational Reality & Gap Annotation:** [Combined operational reality and explicit `[Gap]` tags]
  * **Statutory Requirements & Restrictions (Unsummarized Listing):**
    * `[REQ-ArtX-01]` [Exact unsummarized statutory obligation / restriction]
      * **Legal text IDs:** [Verified canonical Enacting Terms path(s)]
    * `[REQ-ArtX-02]` [Exact unsummarized statutory obligation / restriction]
    * `[REQ-ArtX-03]` [Exact unsummarized statutory obligation / restriction]

---

## 4. Omitted / Disputed Candidate Articles (No Unanimous Consensus)

* **Article [Y]: [Title]**
  * **Status:** Omitted (2/3 Split)
  * **Divergence Reason:** [Summary of why unanimous agreement was not reached]
```
