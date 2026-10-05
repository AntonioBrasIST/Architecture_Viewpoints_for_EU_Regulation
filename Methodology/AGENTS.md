# Intended Workflow Overview

The following pipeline is designed to be executed sequentially, but **operator interaction is strictly necessary in-between each step**. The agents do not run autonomously from start to finish; the operator acts as the bridge, reviewer, validator, and executor between each phase.

**Core Principle: Zero Assumptions**
Under no circumstances should any agent in this pipeline guess, hallucinate, or make assumptions to fill in missing information. If any agent determines that the context provided by the operator or the previous step is lacking, ambiguous, or incomplete, the desired and expected behavior is for the agent to halt execution and immediately prompt the operator with specific, clarifying questions.

**Human-in-the-Loop (HITL) Validation & Gating Rule**
At every single step of this pipeline, the executing agent MUST use the interactive `question` tool to present all major decisions, drafts, and proposed outputs to the human operator for validation. No file-writing actions or pipeline transitions may occur without the operator's explicit approval (via 'Yes', 'No', or entering custom feedback in the 'Type your own answer' field). Every decision, naming of Views, layout of slide diagrams, and structural composition of ArchiMate containers has an explicit question gate assigned to it.

**Evidence-Backed Relationship and Connected-View Rule**
Every modeled relationship MUST have a stable `REL-OP-*`, `REL-COV-*`, `REL-ROLE-*`, or `REL-COMP-*` identifier, named endpoints, direction, ArchiMate type, evidence references, and operator-approved status. Coverage or common membership in a stream never substitutes for a relationship. Every semantic element placed in a view MUST participate in at least one approved relationship, and every view MUST form exactly one weakly connected component when relationship direction is ignored. Semantic Composition/Aggregation counts when it is communicated by approved visual nesting. Every view, including the regulation Overview, MUST contain the stakeholder anchor and an evidence-backed path from that anchor to all other elements. If no such path is defensible, halt for operator clarification; never invent a bridge or place an isolated box.

There is no relationship-count limit. More than 30 root elements is an advisory readability condition: present the complete graph and an optional thematic split at the applicable layout gate, but never omit a node or relationship automatically. A split view must independently satisfy the same stakeholder, evidence, degree, and single-component rules.

---

### Pipeline Steps

| **Step** | **Agent** | **Skills** | **Output File Path** |
| :--- | :--- | :--- | :--- |
| **1. Prompt Optimization** | `0-prompt-maker` | `prompt-maker` | `StakeHolders/<Stakeholder>/1_optimized_prompt.md` |
| **2. Produce Interview** | `1-interview-designer` | `regulation-blind-operational-discovery` | `StakeHolders/<Stakeholder>/2_interview.md` |
| **Intermediary Manual Step** | *Operator* | *Manual Elicitation & Recording Responses* | Updates `StakeHolders/<Stakeholder>/2_interview.md` |
| **3. Context Discovery** | `2-operational-footprint-extractor` | `extract-operational-footprint`, `evidence-grounded-relationship-ledger` | `StakeHolders/<Stakeholder>/3_operational_footprint.md` |
| **4. Stakeholder & Concern ID** | `3-stakeholder-classifier` | `extract-stakeholder-class-and-concerns` | `StakeHolders/<Stakeholder>/4_stakeholder_classification.md` |
| **5. Regulatory Relevance Analysis** | `4-eu-legislation-identifier` panel (`4a`, `4b`, `4c`, `4d`) | `legislation-relevance-evaluator`, `regulatory-consensus-moderator`, `TraceabilityMatrixCreator`, `legal-text-anchor-resolver`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `stakeholder-legal-role-mapper` | `StakeHolders/<Stakeholder>/5_regulatory_relevance.md`; legal index in `TraceabilityMatrixCreator/OutputDirectory/` |
| **Technology Selection Gate** | *Operator* | *Choose exactly one model technology* | Selected XML, LikeC4, or pyArchimate path |
| **5a. Contextualized Regulation Overview Baseline** | `4e-a-archimate-overview-modeler`, `4e-b-likec4-overview-modeler`, or `4e-c-pyarchimate-overview-modeler` | `regulation-overview-designer`, `legal-text-anchor-resolver`, `stakeholder-legal-role-mapper`, `regulatory-view-structure`, `connected-view-validator`, plus selected native-model skills | `StakeHolders/<Stakeholder>/Views/0_<law-slug>_regulation_overview.archimate`, `.c4`, or `.py` + `.archimate` |
| **6. Viewpoint Scope & Justification**| `5-stakeholder-viewpoint-scoper` | `viewpoint-scope-definer`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | `StakeHolders/<Stakeholder>/6_viewpoint_scope.md` |
| **7. Viewpoint Generation** | `6-viewpoint-materializer` | `viewpoint-creator`, `viewpoint-materializer`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | `StakeHolders/<Stakeholder>/7_viewpoint.md` and `7_view_graph.json` |
| **8. Textual View Explanation** | `7-view-narrative-explainer` | `view-narrative-explainer`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | `StakeHolders/<Stakeholder>/Views/1_view_explanation.md` |
| **9. Markdown Slide Diagrams** | `8-informal-diagram-designer` | `informal-markdown-diagram-designer`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | `StakeHolders/<Stakeholder>/Views/2_slide_diagrams.md` |
| **10a. ArchiMate XML Generation** | `9a-archimate-model-generator` | `archimate-xml-generator`, `archimate-symbol-validator`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | `StakeHolders/<Stakeholder>/Views/3_view_model.archimate` |
| **10b. LikeC4 Model Generation** | `9b-likec4-model-generator` | `likec4-dsl`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator`, `likec4` MCP Server | `StakeHolders/<Stakeholder>/Views/3_view_model.c4` |
| **10c. pyArchimate Script Generation** | `9c-pyarchimate-model-generator` | `pyarchimate-syntax-reference`, `archimate-symbol-validator`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator`, `pyarchimate-model-generator` | `StakeHolders/<Stakeholder>/Views/3_view_model_pyarchimate.py` and `3_view_model_pyarchimate.archimate` |
| **11. Cross-Artifact Reconciliation** | `10-view-cross-artifact-reconciler` | `view-cross-artifact-reconciler`, `legal-text-anchor-resolver`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `regulatory-view-structure`, `connected-view-validator` | Audit Report & synchronized updates to `Views/` |
| **12. Conditional Gap-Free Derivation** | `11a-gap-free-archimate-views`, `11b-gap-free-likec4-views`, or `11c-gap-free-pyarchimate-views` | `artifact-gap-detector`, `gap-free-view-duplicator`, `connected-view-validator`, plus selected native-model validation skills | Only affected-unit derivatives; `Views/5_gap_free_manifest.md` only when at least one GAP is found |

---

### View Artifact Destination Rule

Every pipeline view artifact, including View 0, MUST be written directly to `StakeHolders/<Stakeholder>/Views/`. Do not create or write to `Views/Regulations/`, law-specific subdirectories, or other nested view-output folders. For multi-law View 0 baselines, include the law slug in the filename: `0_<law-slug>_regulation_overview.*`.

---

## 0. Prompt Maker Agent (`0-prompt-maker`)

**Description:**
This agent is an expert prompt engineering assistant. Its sole purpose is to convert any user input into an optimized, high-performing prompt designed for subsequent pipeline steps. It does not perform regulatory research or execute complex logic; it acts as an input sanitizer and enhancer.

**Tools & Skills:**
* `prompt-maker`

**Responsibilities:**
* Receive the operator's initial, rough request.
* Structure the request to clearly define the target stakeholder profile, operational domain, and regulatory context.
* **Never assume user intent; immediately ask the operator clarifying questions if the initial request lacks necessary context or is too vague.**
* Present the optimized prompt to the operator for review.
* **Mandatory Validation Gate:** Call the `question` tool (Header: `Confirm Optimized Prompt`) to show the operator the full optimized draft and ask if they agree, with options Yes, No, or custom feedback.
* Save the finalized prompt as `1_optimized_prompt.md` inside `StakeHolders/<Stakeholder>/` only after validation is approved.

---

## 1. Interview Design Agent (`1-interview-designer`)

**Description:**
This agent is the elicitation architect. It takes the optimized prompt and prepares highly targeted, jargon-free interview scripts designed to extract raw operational footprints without exposing the stakeholder to regulatory context or architectural modeling jargon.

**Tools & Skills:**
* `regulation-blind-operational-discovery`

**Responsibilities:**
* Receive the optimized prompt from the operator.
* **Halt and question the operator if the provided prompt lacks sufficient detail for the stakeholder profile, domain, or context.**
* Execute the `regulation-blind-operational_discovery` skill to output a structured 6-step interview guide with questions, nudges, alternative angles, and fallbacks.
* Elicit concrete actor-action-target facts with short questions such as what the stakeholder builds, changes, uses, reads, writes, receives, produces, or connects. Ask what the stakeholder does with each named asset. Do not suggest an answer or expose modeling terminology.
* Do not map to ArchiMate or cite regulations.
* Present the draft interview guide to the operator for review.
* **Mandatory Validation Gate:** Call the `question` tool (Header: `Confirm Interview Guide`) to present the 6 core questions and themes to the operator for approval, with options Yes, No, or custom feedback.
* Save the finalized interview guide as `2_interview.md` inside `StakeHolders/<Stakeholder>/` only after validation is approved.

---

## Intermediary Step: Manual Elicitation (Operator-driven)

**Description:**
The operator conducts the interview with the stakeholder (offline or via communication channels), capturing their actual operational responses. The operator then updates the `2_interview.md` file to include these raw answers (e.g., matching questions with responses) or prepares a transcript, which will serve as the input for the next step.

---

## 2. Operational Footprint Extractor Agent (`2-operational-footprint-extractor`)

**Description:**
This agent analyzes stakeholder interview transcripts (completed during the manual elicitation phase) and accurately extracts critical context regarding their day-to-day operations, processes, and structural responsibilities.

**Tools & Skills:**
* `extract-operational-footprint`
* `evidence-grounded-relationship-ledger`

**Responsibilities:**
* Ingest the completed interview guide containing the stakeholder's raw answers.
* **Halt execution and prompt the operator for clarification if the interview transcript is vague or missing.**
* Use the `extract-operational-footprint` skill to process the interview data into Core Role Context, Tasks, Assets/Data, Dependencies, Approval Gates, Incident Interfaces, Friction, and ArchiMate cross-layer mappings (Active Structure, Behavior, Passive Structure).
* Assign a stable `OP-*` source ID and transcript evidence to every distinct task, asset/data object, dependency, approval, incident interface, and explicit gap. Do not merge source facts because they later belong to one stream.
* Invoke `evidence-grounded-relationship-ledger`. Preserve explicit subject-action-object statements as atomic relationship records with stable `REL-OP-*` IDs, textual endpoints, direction, natural-language meaning, proposed ArchiMate type, exact `OP-*` evidence, and approval status. A statement that a developer builds named components is relationship evidence, not a set of unrelated asset mentions.
* Extract strictly what is explicitly stated in the transcript; do not add external assumptions or hallucinated components. Tag inferred gaps as `[Gap]`.
* Present the operational footprint report to the operator for review.
* **Mandatory Validation Gates:** Sequentially trigger Gate 3.1 (Header: `Confirm Extracted Tasks`), Gate 3.2 (Header: `Confirm Operational Relationships`), and Gate 3.3 (Header: `Confirm Gaps & Friction`). Present textual endpoint names before identifiers. Do not save until facts, relationships, and gaps are separately approved.
* Save the finalized report as `3_operational_footprint.md` inside `StakeHolders/<Stakeholder>/` only after validation is approved.

---

## 3. Stakeholder Classifier Agent (`3-stakeholder-classifier`)

**Description:**
This agent processes the operational footprint data to accurately determine the stakeholder's organizational seniority/class and generate a comprehensive list of their core concerns.

**Tools & Skills:**
* `extract-stakeholder-class-and-concerns`

**Responsibilities:**
* Ingest the operational footprint report.
* **Halt and ask the operator for clarifying details if the report lacks sufficient detail to definitively classify the stakeholder (e.g. overlapping duties).**
* Use the `extract-stakeholder-class-and-concerns` skill to assess seniority level (Junior, Senior, Management) and extract an exhaustive, unsummarized, itemized list of all friction points, gaps, or bottlenecks. Give every distinct concern a `CON-*` ID and retain its originating `OP-*` ID where known.
* **Ensure zero grouping or summarization of concerns; if 14 distinct friction points exist, list exactly 14 bullet points.**
* Present the Stakeholder Classification & Concern Audit to the operator for review.
* **Mandatory Validation Gates:** Sequentially trigger Gate 4.1 (Header: `Confirm Seniority Class`) and Gate 4.2 (Header: `Confirm Concern List`) using the `question` tool to validate classification and the unsummarized concern list.
* Save the finalized audit as `4_stakeholder_classification.md` inside `StakeHolders/<Stakeholder>/` only after validation is approved.

---

## 4. EU Legislation Identifier & 3-Agent Consensus Debate Panel (`4-eu-legislation-identifier`)

**Description:**
This step executes a 3-agent parallel regulatory search and consensus debate protocol to evaluate a stakeholder's operational footprint against target EU legislation (e.g., DORA, NIS2, eIDAS) using the LexAPI MCP server. Three evaluator agents analyze the footprint concurrently from distinct analytical perspectives (Literal, Systemic, Gap/Risk), confront each other with their candidate selections, defend or revise their positions in multi-turn debate rounds, and filter for strict unanimous article agreement ($4a \cap 4b \cap 4c$).

**Panel Agents & Skills:**
* `4a-eu-legislation-literal-evaluator` (Literal & explicit statutory lens)
* `4b-eu-legislation-systemic-evaluator` (Architectural & cross-system dependency lens)
* `4c-eu-legislation-gap-evaluator` (Operational friction & risk gap lens)
* `4d-regulatory-consensus-moderator` (Debate orchestrator & consensus synthesizer)
* **Skills & Tools:** LexAPI MCP Server, `legislation-relevance-evaluator`, `regulatory-consensus-moderator`, `TraceabilityMatrixCreator`, `legal-text-anchor-resolver`, `stakeholder-footprint-coverage`, `evidence-grounded-relationship-ledger`, `stakeholder-legal-role-mapper`

**Debate Protocol Workflow:**
1. **Parallel Execution:** Evaluator subagents `4a`, `4b`, and `4c` launch concurrently. Each agent queries LexAPI article-by-article (1 article at a time), systematically decomposes articles into an **exhaustive, unsummarized, bulleted listing of every single requirement, restriction, prohibition, condition, and obligation**, logs missing mandatory statutory controls for non-exempt entities as statutory gaps (`[Gap]`), and builds an independent screening matrix and candidate article list with **concise 3-part operational justifications** (Operational Anchor, Legal Bridge, Operational Reality & Ownership). A requirement is included when it has a recorded chain to an `OP-*` or `CON-*` fact; direct execution is not required.
2. **Proposal Matrix Compilation:** The Moderator (`4d`) aggregates the initial screening tables, identifying unanimous inclusions ($4a = 4b = 4c = \text{INCLUDED}$), split decisions, and unanimous exclusions.
3. **Multi-Turn Peer Confrontation:** The Moderator re-invokes `4a`, `4b`, and `4c` via their session `task_id`s, presenting peer proposals and challenges. Each agent must defend its inclusions/exclusions or accept peer reasoning.
4. **Strict Unanimous Agreement Filter ($4a \cap 4b \cap 4c$):** Only articles where **ALL THREE** agents explicitly agree after debate are retained in the active relevant articles section. Split decisions without consensus are recorded as omitted candidates.
5. **Synthesis of Combined Concise Justifications & Unsummarized Requirements:** The Moderator synthesizes the concise operational anchors, legal bridges, and ownership/gap annotations from all 3 perspectives, and compiles the complete unsummarized bulleted listing of all requirements and restrictions for every agreed article.
6. **Legal-Index Generation:** After Gates 5.1 and 5.2 fix every in-scope `REQ-*`, present Gate 5.3 (Header: `Confirm Legal Index`) with the selected regulation, CELEX, accepted matrix selector, expected `<REGULATION>-CELEX:<CELEX>.xlsx` path, and notice that a same-name workbook will be regenerated. On approval, run `TraceabilityMatrixCreator` from the repository root with `(cd TraceabilityMatrixCreator/TraceabilityMatrixCreator.App && dotnet run --project ../TraceabilityMatrixCreator -- <selector>)`. Always regenerate the workbook in `TraceabilityMatrixCreator/OutputDirectory/`. Validate its exact filename, `Recitals` and `Enacting Terms` schema, and returned law/CELEX identity through `tools/traceability_lookup.py row-id --row 1`. Record the regulation, CELEX, selector, generated path, generation timestamp, and successful validation result as **Legal Index Provenance** in the Step 5 report. Do not resolve anchors until this validation succeeds.
7. **Canonical Legal-Text Anchors:** Invoke `legal-text-anchor-resolver` using only the generated workbook recorded in Legal Index Provenance. Its law label and CELEX must match the selected regulation. Resolve each duty to exact Enacting Terms canonical path(s), verify every ID through `tools/traceability_lookup.py verify-anchor`, and store those direct IDs alongside its citation. Never infer an ID from a citation. Recitals and amendment provisions are out of scope and must be rejected.
8. **Footprint-Regulation Coverage:** After anchor resolution, invoke `stakeholder-footprint-coverage` to produce a bidirectional Coverage Ledger. Every edge records exact named operational and legal endpoints, `OP-*`/`CON-*`, `REQ-*`, citation, approved direct legal-text IDs, evidence-backed effect, named stream, and exactly one ownership state: `Directly performed`, `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner`. Invoke `evidence-grounded-relationship-ledger` to assign `REL-COV-*` IDs and a valid effect relation to each visible coverage edge. Coverage or stream membership alone is not a relationship. Include external duties only when the recorded operational-chain test passes; entity-wide applicability alone is insufficient.
9. **Stakeholder Legal-Role Placement:** Invoke `stakeholder-legal-role-mapper` to distinguish the stakeholder role, employing organization, and law-defined entity group. Record only evidence supplied by the source artifacts or operator. Assign `REL-ROLE-*` IDs to the approved chain and validate its ArchiMate semantics. Never classify the individual stakeholder as the regulated entity merely because their organization qualifies.
10. **Operator Review:** The final Consensus Report is presented to the operator for review.
11. **Mandatory Validation Gates:** Sequentially trigger Gates 5.1 through 5.5 as before, then Gate 5.6 (Header: `Confirm Stakeholder Legal Role`). Gate 5.5 (Header: `Confirm Coverage Resolution`) presents endpoint-specific Coverage and Regulatory Relationship Ledgers. Gate 5.6 presents textual names and relationship meanings first, with identifiers secondarily. Persistence and transition are forbidden until every edge, role placement, ID, and uncovered item is resolved.
12. **Persistence:** Save the report to `5_regulatory_relevance.md` inside `StakeHolders/<Stakeholder>/` only after explicit operator authorization.

---

## 5. Stakeholder Viewpoint Scoper Agent (`5-stakeholder-viewpoint-scoper`)

**Description:**
This agent is a Viewpoint Scoping Agent. It synthesizes a stakeholder's operational context, classification, concerns, and relevant legislative articles and their granular statutory requirements to define a precise, justified architectural scope and boundary.

**Tools & Skills:**
* `viewpoint-scope-definer`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`

**Responsibilities:**
* Ingest the operational footprint, stakeholder classification, relevant legislative articles with their granular statutory requirements and approved direct legal-text IDs, and the approved Footprint-Regulation Coverage Ledger.
* Ingest the selected immutable contextualized regulation overview baseline. Distinguish its immutable legal core and approved stakeholder/legal-role chain from the narrower stakeholder operational boundary; do not alter either.
* Define the strict boundary from the approved ledger: direct work, operational constraints, externally owned duties with a recorded impact, and a role-specific operational-context stream. Do not include entity-wide duties without a recorded operational chain.
* **Enforce Functional Domain Cohesion (Rule A):** Unify all statutory requirements addressing the same operational domain (e.g. *Testing & Verification*, *Third-Party Risk*, *Telemetry & Monitoring*, *Change Governance*) into coherent streams regardless of article origin.
* **Enforce Multidimensional Perspective Disambiguation (Rule B):** Categorize and disambiguate scope elements across three universal perspectives (`[Governance]`, `[Administrative]`, `[Technical]`).
* **Enforce Granular Requirement Boundary Scoping (Rule C):** Explicitly classify every included statutory requirement as `Directly performed`, `Stakeholder-constrained`, `Externally owned`, or `Not evidenced / unclear owner`. Only the first can be a stakeholder realization; external ownership must remain an evidence-backed role, process, approval, or dependency.
* Carry each legal child's approved direct legal-text IDs unchanged into the scope and assign every family parent only the ordered, deduplicated child-ID roll-up. Halt and return to Step 5 if IDs are missing or altered; do not match legal text in Step 6.
* **Ensure the scope focuses strictly on the regulatory parts that directly affect the stakeholder, explicitly stating that it does not encompass the full legislation.**
* Produce a node-and-relationship graph for each thematic stream. Every relationship references an approved `REL-*`; every node participates in one; every candidate view contains the stakeholder and exactly one weakly connected component. Split multi-island candidates into semantically named views. If a component lacks an approved stakeholder path, halt for evidence or exclusion clarification rather than placing it.
* Treat more than 30 root elements as a readability warning and optional split proposal. Never suppress relationships to meet a count.
* Present the Viewpoint Scope Definition to the operator for review.
* **Mandatory Validation Gates:** Sequentially trigger Gate 6.1 (Header: `Confirm Scope Boundary`), Gate 6.2 (Header: `Confirm Inclusions & Streams`), and Gate 6.3 (Header: `Confirm Connectivity & Splits`). Gate 6.3 shows textual element and relationship names, component counts, any split proposal, unresolved stakeholder paths, and root warnings.
* Save the finalized scope as `6_viewpoint_scope.md` inside `StakeHolders/<Stakeholder>/` only after validation is approved.

---

## 6. Viewpoint Materializer Agent (`6-viewpoint-materializer`)

**Description:**
This agent is a Viewpoint Materialization Agent. It takes the architectural scope and justifications generated for a stakeholder and translates them into a formalized, concrete ArchiMate Viewpoint specification.

**Tools & Skills:**
* `viewpoint-creator`
* `viewpoint-materializer`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`
* `archimate-symbol-validator`

**Responsibilities:**
* Ingest the viewpoint scoping document and the selected immutable contextualized regulation overview baseline. Preserve its legal core and approved stakeholder/legal-role chain in View 0; materialize the remaining stakeholder-specific views beneath it.
* Use the `viewpoint-creator`, `viewpoint-materializer`, `regulatory-view-structure`, and `archimate-symbol-validator` skills to define the formal ArchiMate Viewpoint parameters (Purpose, Stakeholders, Concerns, Allowed Concepts, Allowed Relations, and Additional Info/Visual Rules), ensuring domain cohesion, perspective disambiguation (`[Governance]`, `[Administrative]`, `[Technical]`), and 100% accurate ArchiMate element types and symbols.
* **Title Purity & Readability Rule:** Element names MUST NOT contain notation brackets (e.g., `[Right Arrow]`, `[Folded Page]`, `[UML Box]`), `[Gap]`, or long explanatory disclaimers. Names SHOULD normally be $\le 25$ characters for readability. When an approved legal or control title exceeds that recommendation, the operator must explicitly decide whether retaining the exact title is required for legal/control inclusion; record that decision and use the approved title. Gaps must be classified strictly via concept types or tags.
* **Requirement-Family Realization Metamodel Enforcement:** Model each coherent control domain as a meaningful parent requirement or constraint; model every granular statutory requirement/restriction as a target-qualified child `archimate:Requirement` or `archimate:Constraint` composed by that family. Carry `COV-*` IDs, ownership state, and verified direct legal-text IDs in documentation; every parent carries the ordered, deduplicated child-ID roll-up. Connect operational footprint elements through `Realization` only when the ledger says `Directly performed`; otherwise show the evidence-backed external role, approval, or dependency without a false stakeholder realization. Preserve Article citations and legal IDs in documentation, not as visible model nodes, titles, or labels.
* **Relationship and Connectivity Enforcement:** Materialize the complete approved relationship catalog. Semantic-only links are permitted only for Composition/Aggregation communicated by matching nesting. No element may be isolated; every view must include the stakeholder and exactly one weakly connected component. There is no relationship-count limit.
* Emit `7_view_graph.json` beside `7_viewpoint.md` with schema version `1.0`, the stakeholder anchor, 30-root warning threshold, node catalog, evidence-backed relationship catalog, and exact per-view node/relationship membership. Validate it using `tools/view_graph_validator.py` before persistence.
* **Ensure strict metamodel compliance using only official, standard ArchiMate elements and relationships.**
* Present the draft ArchiMate Viewpoint specification to the operator for review.
* **Mandatory Validation Gates:** First call `Confirm Metamodel Scope`, then Gate 7.2 `Confirm View Graph` showing every view's stakeholder path, relationship list, component result, and root warning. Save neither artifact until both are approved.
* Save the finalized viewpoint as `7_viewpoint.md` and its validated graph as `7_view_graph.json` inside `StakeHolders/<Stakeholder>/`.

---

## 7. View Narrative Explainer Agent (`7-view-narrative-explainer`)

**Description:**
This agent generates a dual-purpose textual explanation guide that articulates both how target EU legislation affects a stakeholder's daily operations and a complete textual walkthrough of the corresponding visual ArchiMate view.

**Tools & Skills:**
* `view-narrative-explainer`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`

**Responsibilities:**
* Ingest `7_view_graph.json` and the selected immutable contextualized regulation overview baseline in addition to the Viewpoint specification, operational footprint, and regulatory relevance report. Start with the approved Overview including the stakeholder-to-legal-role path.
* Generate a dual-purpose textual explanation covering executive context, thematic operational streams, layer-by-layer ArchiMate walkthroughs, and a comprehensive traceability table linking:
  $$\text{Coverage ID} \longrightarrow \text{OP/CON Source} \longrightarrow \text{Parent Family or Context Stream} \longrightarrow \text{REQ} \longrightarrow \text{Ownership State} \longrightarrow \text{Representing Element or External Role}$$
* Ensure legislative agnosticism and frame operational gaps (`[Gap]`) non-judgmentally as potential operational or visibility limitations from this stakeholder's viewpoint.
* Preserve citations as readable legal references, but do not reproduce canonical legal-text IDs in this narrative; IDs are documentation-only fields in the formal model and ledger.
* For every view, explain the stakeholder path and every approved `REL-*` relationship in the graph manifest. Do not create, omit, redirect, or reinterpret relationships in prose.
* Present the draft explanation to the operator for review.
* **Mandatory Validation Gates (Sequential Loops):**
  - **Loop 8.1 (View Naming & Definition Loop):** Loop through each proposed View/Stream individually using the `question` tool (Header: `Confirm View Name`) to approve its name and scope.
  - **Loop 8.2 (Detailed Walkthrough Loop):** Once names are locked, loop through each approved view's detailed narrative description individually using the `question` tool (Header: `Confirm View Description`) to obtain operator approval.
* Save the finalized document as `1_view_explanation.md` inside `StakeHolders/<Stakeholder>/Views/` only after all validation loops are approved.

---

## 8. Informal Diagram Designer Agent (`8-informal-diagram-designer`)

**Description:**
This agent translates the Viewpoint specification and textual explanation guide into a presentation slide deck of sketched, informal markdown diagrams (ASCII / box-drawing / Mermaid) illustrating every regulatory impact dimension and showing how operational activities realize granular requirements.

**Tools & Skills:**
* `informal-markdown-diagram-designer`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`
* `archimate-symbol-validator`

**Responsibilities:**
* Ingest the selected immutable contextualized regulation overview baseline, `7_viewpoint.md`, `7_view_graph.json`, and `Views/1_view_explanation.md`. Render the approved stakeholder-aware View 0 as Slide 0.
* Render every approved graph relationship regardless of count. Composition/Aggregation may remain line-free only when matching nesting communicates it.
* Structure the output as a slide deck covering 100% of the approved Coverage Ledger: operational footprint, operational-context work, regulatory mandates, itemized statutory requirements, friction points, and potential gaps. Label each slide with its `COV-*` membership and avoid stakeholder realization for non-direct ownership states.
* Clearly sketch the realization links from stakeholder tasks, review gates, and infrastructure systems up to the granular statutory requirements (`REQ-*`).
* Every semantic box or callout must participate in an approved relationship or attached annotation connector. Every slide must contain the stakeholder and exactly one weakly connected component. Run the connected-view validation before presenting each slide gate.
* Do not render canonical legal-text IDs in slide titles, boxes, labels, callouts, or relationship labels.
* Present the draft slide deck to the operator for review.
* **Mandatory Validation Gate (Slide-by-Slide Gating Loop):** Loop through each planned slide individually and present it to the operator using the `question` tool (Header: `Confirm Slide [N] Diagram`).
* Save the finalized slide deck as `2_slide_diagrams.md` inside `StakeHolders/<Stakeholder>/Views/` only after validation is approved.

---

**Technology Selection Gate (Operator Choice Rule):**
Immediately after completing Step 5 (Regulatory Relevance Analysis) and before Step 5a, the pipeline MUST explicitly force the operator to select exactly one target model generation technology via the interactive `question` tool. The selection controls both the immutable regulation overview baseline and the later final model:
* **Option 10a (ArchiMate XML):** Execute Step 10a (`9a-archimate-model-generator`) to output `3_view_model.archimate`.
* **Option 10b (LikeC4 DSL):** Execute Step 10b (`9b-likec4-model-generator`) to output `3_view_model.c4`.
* **Option 10c (pyArchimate Script):** Execute Step 10c (`9c-pyarchimate-model-generator`) to save `3_view_model_pyarchimate.py`, then run it to output `3_view_model_pyarchimate.archimate`.

## 5a. Contextualized Regulation Overview Baseline Agents (`4e-a` / `4e-b` / `4e-c`)

**Description:**
This stage creates the first immutable stakeholder-aware model view for one selected law. Its legal requirement-family core remains regulation-wide and compliance-neutral; its only stakeholder-specific addition is the approved stakeholder–organization–legal-role chain.

**Tools & Skills:**
* `regulation-overview-designer`
* `legal-text-anchor-resolver`
* `stakeholder-legal-role-mapper`
* `regulatory-view-structure`
* `connected-view-validator`
* The selected native-model generation and validation skills

**Responsibilities:**
* Use `regulation-overview-designer` and the selected native-model skill. Retrieve the current consolidated binding text one Article at a time and verify every binding annex. Use the generated legal index recorded in Step 5 Legal Index Provenance for canonical IDs; do not regenerate or substitute the workbook. Record CELEX/ELI, retrieval date, and in-force status in documentation.
* Verify every binding Article and annex, excluding recitals and amendments, but represent only the approved high-level requirement-family map in View 0. Do not create Article, annex, generic legal-heading, or hidden catalog-only nodes. Keep source citations and canonical legal-text IDs in documentation on the visible family parents and children.
* Decompose each meaningful legal-control domain into target-qualified child requirements, semantically compose children under their parent, visually nest them, and retain every source-backed legal role/family relationship. Add the Gate 5.6-approved stakeholder role, organization actor, legal-role group, and `REL-ROLE-*` chain. Do not add other operational elements, gaps, compliance status, or realization state.
* Require every element to participate in an approved relationship and the complete Overview to form one weakly connected component containing the stakeholder. Split only if the source-backed graph genuinely has multiple components, and apply the stakeholder-path rule to every resulting view. More than 30 roots triggers readability review, never edge suppression.
* Run four mandatory gates before persistence: `Confirm Legal Source Completeness`, `Confirm Obligation Domain`, `Confirm Requirement Family` for every parent/child decomposition including direct IDs and parent roll-ups, and `Confirm Overview Map` for the final grouped canvas. Stop if any binding text is unavailable.
* Preserve the approved legal-core fingerprint and approved stakeholder/legal-role-chain fingerprint unchanged. Every later stage consumes and reproduces both without changing the baseline.

---

## 9. ArchiMate XML Model Generator Agent (`9a-archimate-model-generator` / Step 10a)

**Description:**
This agent converts the formalized Viewpoint specification, explanation narrative, and slide diagrams into a fully compliant, well-formed ArchiMate 3.x XML model file (`.archimate`) for Archi, explicitly modeling requirement families, nested controls, and operational realization links.

**Tools & Skills:**
* `archimate-xml-generator`
* `archimate-symbol-validator`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`

**Responsibilities:**
* Ingest the selected immutable contextualized XML overview baseline alongside `7_viewpoint.md`, `7_view_graph.json`, the narrative, and slides; reproduce its legal core and stakeholder/legal-role chain unchanged.
* **Title Purity & Readability Rule:** Every element `name` in the XML model MUST NOT contain notation brackets (e.g. `[Right Arrow]`, `[UML Box]`, `[Folded Page]`), `[Gap]`, or long explanatory disclaimers. Names SHOULD normally be $\le 25$ characters for readability. When an approved legal or control title exceeds that recommendation, the operator must explicitly decide whether retaining the exact title is required for legal/control inclusion; record that decision and use the approved title. Place disclaimers in `<documentation>`.
* Instantiate meaningful parent-family and granular child requirement elements (`archimate:Requirement` / `archimate:Constraint`) and operational elements. View 0 contains no Article, annex, legal-heading, or hidden catalog-only nodes; citations remain in documentation.
* Formulate `archimate:CompositionRelationship` from each family to its child controls. Create `archimate:RealizationRelationship` only for `Directly performed` coverage; document `COV-*` IDs and model other ownership states as the stated role, approval, or dependency.
* Construct standard 9-folder ArchiMate XML models with professional EA composition patterns, valid UUIDs, coordinates, styles, bi-directional connection bindings, and orthogonal routing. Serialize only approved legal-text IDs in `<documentation>`: `Legal text IDs:` for legal children and `Legal text IDs (child roll-up):` for family parents; never match law text here or put IDs in names/visible labels.
* Use `7_view_graph.json` as the exact node-and-relationship authority. Render every approved relationship; no relationship-count limit or density-safe subset is permitted. A Composition/Aggregation canvas line may be omitted only when matching visual nesting exists. Reject isolated nodes, multiple components, or a missing stakeholder. More than 30 roots is structurally permissible but blocks persistence until readability approval is recorded.
* Present the generated XML or summary to the operator for review.
* **Mandatory Validation Gate (Family-by-Family Layout Loop):** Loop through each planned requirement family individually using the `question` tool (Header: `Confirm Requirement Family`) with an actual layout preview.
* Save the finalized model as `3_view_model.archimate` inside `StakeHolders/<Stakeholder>/Views/` only after validation is approved.

---

## 10. LikeC4 Model Generator Agent (`9b-likec4-model-generator` / Step 10b)

**Description:**
This agent performs the architectural model generation task outputting a valid LikeC4 DSL model file (`.c4`), modeling requirement families, nested controls, and realization relationships.

**Tools & Skills:**
* `likec4-dsl`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`
* `likec4` MCP Server tools

**Responsibilities:**
* Ingest the selected immutable contextualized LikeC4 overview baseline alongside `7_viewpoint.md`, `7_view_graph.json`, the narrative, and slides; reproduce its legal core and stakeholder/legal-role chain unchanged.
* **Title Purity & Readability Rule:** Every element title in LikeC4 MUST NOT contain notation brackets (`[Right Arrow]`, `[3D Cube]`, `[badge]`, etc.), `[Gap]`, or long disclaimers. Titles SHOULD normally be $\le 25$ characters for readability. When an approved legal or control title exceeds that recommendation, the operator must explicitly decide whether retaining the exact title is required for legal/control inclusion; record that decision and use the approved title. Classify gaps strictly using `#gap` and put disclaimers in `description`.
* Construct LikeC4 from the exact graph manifest. Include every approved relationship regardless of count; suppress only Composition/Aggregation arrows communicated by matching nesting. Preserve evidence, ownership, and legal IDs in descriptions. Reject isolated nodes, multiple components, a missing stakeholder, and any relation absent from or missing from the manifest. More than 30 roots triggers readability approval only.
* Use `likec4-dsl` and LikeC4 MCP server tools to verify syntax and rendering.
* **Mandatory Validation Gate (Family-by-Family / View Layout Loop):** Present family and scoped-view layout previews to the operator using the `question` tool (Header: `Confirm Requirement Family`).
* Save the finalized model as `3_view_model.c4` inside `StakeHolders/<Stakeholder>/Views/` only after validation is approved.

---

## 10c. pyArchimate Script Model Generator Agent (`9c-pyarchimate-model-generator` / Step 10c)

**Description:**
This agent converts the formalized Viewpoint specification, explanation narrative, and slide diagrams into a reproducible pyArchimate Python script, then executes it to create an Archi-compatible `.archimate` model archive with requirement-family containment and measured root packing.

**Tools & Skills:**
* `pyarchimate-syntax-reference`
* `archimate-symbol-validator`
* `pyarchimate-model-generator`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`

**Responsibilities:**
* Ingest the selected immutable contextualized pyArchimate overview archive alongside `7_viewpoint.md`, `7_view_graph.json`, the narrative, and slides; reproduce its legal core and stakeholder/legal-role chain unchanged.
* Use the skills in the listed order. The installed pyArchimate API is authoritative; do not use unsupported calls such as `relate`, `create_view`, `save`, `view.add_all()`, or `export_svg`.
* Generate `3_view_model_pyarchimate.py` from the exact graph manifest. Use `Model.add_child()` and `parent_node.add()` for approved containment, and add every other approved relationship and connection regardless of count. Retain evidence/ownership metadata, reject missing IDs and non-direct stakeholder realization, and never omit an edge to improve density. More than 30 roots triggers readability approval only.
* Validate every relationship with `check_valid_relationship(..., raise_flg=True)` before creation. After round-trip, project the archive back to the graph contract and reject relationship mismatch, isolated nodes, multiple components, missing stakeholder anchors, or native integrity failures.
* **Title Purity & Readability Rule:** Every element name MUST contain no notation brackets or `[Gap]` prefix, and explanations belong in documentation. Names SHOULD normally be $\le 25$ characters for readability. When an approved legal or control title exceeds that recommendation, the operator must explicitly decide whether retaining the exact title is required for legal/control inclusion; record that decision and use the approved title.
* **Mandatory Validation Gate (Thematic-View Loop):** Present every planned thematic view, its purpose, included elements, and relationship connections through the `question` tool (Header: `Confirm Thematic View`). Save and execute only after all views are approved.
* Save `3_view_model_pyarchimate.py`, execute it, and save `3_view_model_pyarchimate.archimate` inside `StakeHolders/<Stakeholder>/Views/`. Do not create SVG output or overwrite 10a/10b artifacts.

---

## 11. View Cross-Artifact Reconciler Agent (`10-view-cross-artifact-reconciler`)

**Description:**
This agent performs a rigorous cross-audit across the selected immutable contextualized overview baseline, `7_viewpoint.md`, `7_view_graph.json`, narrative, slides, and the selected final model. It verifies the immutable legal core and stakeholder-role chain plus exact graph traceability and native integrity.

**Tools & Skills:**
* `view-cross-artifact-reconciler`
* `legal-text-anchor-resolver`
* `stakeholder-footprint-coverage`
* `evidence-grounded-relationship-ledger`
* `regulatory-view-structure`
* `connected-view-validator`

**Responsibilities:**
* Cross-audit every `REL-*`, node, and per-view membership against `7_view_graph.json`. Reject missing or extra edges, evidence drift, endpoint/type/direction changes, false non-direct Realizations, isolated nodes, multiple weak components, or missing stakeholder anchors in the viewpoint, narrative, slides, or model. Verify semantic-only Composition/Aggregation has matching nesting. Preserve existing legal-ID, family, title, source-hash, and native-integrity checks. More than 30 roots is reported as an advisory item requiring operator confirmation; relationship count is never an error.
* Compile a structured Discrepancy Audit & Recommendation Report.
* **Mandatory Validation Gate:** Call the `question` tool (Header: `Confirm Reconciliation`) to present choices to the operator ('Apply Recommended Fixes' or 'Abort and Keep Files').
* Execute synchronized updates upon operator authorization.

---

## 12. Gap-Free View Duplication Agents (`11a` / `11b` / `11c`)

**Description:**
This post-reconciliation stage conditionally produces affected-unit-only derivatives for readers who need GAP content removed. It never modifies the selected model, contextualized overview baseline, source narrative, source slides, Coverage Ledger, graph manifest, or reconciliation outputs.

**Tools & Skills:**
* `artifact-gap-detector`
* `gap-free-view-duplicator`
* `connected-view-validator`
* The selected technology's native validation tools: `archimate-symbol-validator` and `archimate-xml-generator`; `likec4-dsl` and LikeC4 tools; or `pyarchimate-syntax-reference` and `archimate-symbol-validator`.

**Inputs:**
* The reconciled selected final model and its recorded source revision/hash.
* `Views/1_view_explanation.md`, `Views/2_slide_diagrams.md`, the approved Coverage Ledger, and model identifiers needed to trace structural GAP content.
* The selected immutable View 0 baseline and reconciliation evidence, used to identify content that must not be cloned.

**Responsibilities:**
* Invoke `artifact-gap-detector` to inspect narrative sections, slides, and model views independently. Identify GAPs structurally only: approved `GAP-*` records, ArchiMate `Gap` elements, LikeC4 `gap`/`#gap` elements, and relationships attached to them. Ordinary prose such as “gap” or “absence” is not classification.
* Feed the normalized inventory to `tools/gap_derivative_plan.py`. Skip every clean unit and every clean artifact type. Derivatives contain only affected sections, slides, or model views; clean units remain available only in the unchanged source artifact.
* If all units are clean, present `Confirm Gap-Free Transformation` with the clean result, then finish without writing a derivative or manifest. If any unit is affected, write only the corresponding artifact-type outputs and `Views/5_gap_free_manifest.md`, recording source hashes, affected/skipped units, structural GAP IDs, removals, and output paths.
* Remove only registry-traceable GAP-specific elements, attached relationships, cards, callouts, rows, and prose from affected units. Preserve all surviving content and native geometry/declarative layout exactly; do not reflow or compact.
* Omit a family, narrative section, slide section, or copied view only when it becomes empty because of structural GAP removal. List every omission in the batch report.
* Before writing, present one `Confirm Gap-Free Transformation` review with the per-unit scan, affected-only transformations, clean-unit skips, source hashes, connectivity outcome, and conditional output paths.
* Re-run `connected-view-validator` after removal. If surviving content is isolated, has multiple components, or lacks its stakeholder path, stop and return the discrepancy to Step 11; do not invent a bridge, silently remove content, or write a derivative.
* Validate zero surviving structural GAP content or attached edges, zero dangling references, exact retained native layout, unchanged source hashes, and native syntax/round-trip integrity. Existing canonical outputs remain immutable without a new approval cycle.
