---
name: viewpoint-creator

description: This skill activates when a user wants to design, build, or specify a new Viewpoint or interview to produce a viewpoint from. It contains the necessary theoretical foundations of what a skill point is.
---

# LLM Skill: ArchiMate Viewpoint Definition and Engineering

## 1. Skill Overview & Objective
This document serves as a comprehensive operational skill definition and reference framework for a Large Language Model (LLM). Its objective is to equip the LLM with an expert-level understanding of **ArchiMate Viewpoints**, their theoretical foundations (aligned with ISO/IEC 42010 and The Open Group ArchiMate Specification), their operational utility, structural anatomy, and the step-by-step methodology required to architect custom viewpoints. 

When executing this skill, the LLM must act as an expert Enterprise Architecture Consultant, guiding practitioners through the discovery, structuring, definition, and validation of views and viewpoints.

---

## 2. Core Definition: What is a Viewpoint?

In Enterprise Architecture (EA) and the ArchiMate language, a fundamental distinction is made between a **View** and a **Viewpoint**, adopting definitions established by the **ISO/IEC 42010** standard:

* **Architecture View (The Instance):** A work product that expresses the architecture of a system from the perspective of specific system concerns. It is the actual artifact or diagram produced (e.g., a specific diagram showing how the "Online Banking Application" runs on "Cloud Server Cluster X").
* **Architecture Viewpoint (The Schema/Specification):** A specification of the conventions for constructing, interpreting, and using an architecture view to frame specific concerns. It defines the "blueprint", "lens", or "template" from which views are generated.

### The Analytical Analogies
1.  **The Camera Filter:** The underlying architecture model is the raw, unrestricted reality. A *Viewpoint* is a camera filter that isolates specific wavebands (e.g., infrared for thermal tracking) and blurs out irrelevant colors. The *View* is the resulting photograph.
2.  **The Structural Blueprint:** A civil engineer, an electrical engineer, and an interior designer look at the same physical building, but each requires a different drawing type. The rules governing what goes into an electrical drawing (wires, panels, loads) represent the *Viewpoint*; the actual schematic for a specific floor is the *View*.

**Key Axiom:** A viewpoint defines the *how* and *what* of a view. It prescribes the concepts, models, analysis techniques, and visualizations that the resulting view must provide.

---

## 3. The Usefulness of Viewpoints

Without viewpoints, an architecture model becomes an impenetrable, monolithic repository of data. Viewpoints are the primary mechanism for transforming raw modeling data into actionable business and technical insight. Their core utility includes:

### A. Cognitive Load and Complexity Management
Modern enterprises are too intricate to be modeled or visualized in a single diagram. Viewpoints allow architects to abstract away non-essential information, breaking down the architecture description into smaller, isolated, and intellectually manageable pieces.

### B. Stakeholder Alignment & Communication
Different stakeholders have completely distinct domains of interest, vocabularies, and technical competencies. Viewpoints act as a semantic translation layer:
* **Executives** need high-level strategic alignment (Drivers, Goals, Capabilities).
* **Operations Managers** need process flows and organizational structures (Roles, Actors, Processes).
* **Engineers & Developers** need concrete system logic and physical deployment maps (Components, Nodes, Interfaces).

### C. Enhanced Governance and Target-Driven Purpose
The ArchiMate standard categorizes the utility of viewpoints based on the decision-making cycle into three distinct types of **Purpose**:
1.  **Informing Viewpoints:** Used to drive broad understanding, achieve consensus, or obtain organizational commitment. They target a wide, frequently non-technical audience, requiring simplified and visually intuitive notation.
2.  **Deciding Viewpoints:** Specifically tailored to support management-level decision-making, choice validation, and risk evaluation. They often highlight gap analyses, scenario comparisons, and cost-benefit trade-offs.
3.  **Designing Viewpoints:** Built to support subject matter experts (SMEs) during the architectural design process from initial abstract concepts down to granular implementation specifications. They enforce technical correctness and architectural rigor.

---

## 4. What a Viewpoint is Made Up Of (The Anatomy)

According to the official ArchiMate specification, a viewpoint definition is highly structured and must be documented using a precise set of metadata attributes. When defining or configuring a viewpoint, it must contain the following components:

| Attribute / Component | Description |
| :--- | :--- |
| **Name** | A clear, descriptive title reflecting its architectural scope (e.g., *Application Cooperation Viewpoint*). |
| **Stakeholders** | The primary target audience whose interests are being represented (e.g., Chief Information Security Officer, Infrastructure Managers). |
| **Concerns** | The precise problems, risks, or performance criteria addressed by the viewpoint (e.g., data security boundaries, system scalability, cost minimization). |
| **Purpose** | Classified into one of the three standard categories: **Informing**, **Deciding**, or **Designing**. |
| **Content / Scope** | Specifies the depth and breadth across the ArchiMate framework. It determines if the view spans a *Single Layer* or *Multiple Layers*, and if it targets a *Single Aspect* (Structural, Behavioral, Passive) or *Multiple Aspects*. |
| **Allowed Concepts** | A strict, white-listed subset of elements selected from the ArchiMate metamodel (e.g., Business Process, Application Service, Node). Elements outside this list are forbidden in the view. |
| **Allowed Relationships** | The specific semantic links permitted to connect the allowed concepts (e.g., Triggering, Composition, Assignment, Realization). |
| **Representation & Notation** | The visual language, iconography, graphical style, and color-coding rules used to map concepts onto a viewport (e.g., standard boxes, matrices, nesting rules, or custom profile shapes). |

### Viewpoint Classification Matrix (The Core Framework Dimensions)
The ArchiMate standard structures viewpoints along a multi-dimensional matrix defined by:
* **Layers Covered:** Motivation, Strategy, Business, Application, Technology, Physical, Implementation & Migration.
* **Aspects Covered:** Active Structure (Who does it?), Behavior (How is it done?), Passive Structure (What is it done to?).
* **Structural Focus Categories:**
    * *Composition:* Internal breakdown and aggregation of domain elements.
    * *Support:* Vertical tracing (how a lower layer supports an upper layer).
    * *Cooperation:* Peer-to-peer horizontal communication and coordination.
    * *Realization:* Tracing how logical concepts are physically materialized.

---

## 5. How a Viewpoint is Built (The Viewpoint Mechanism)

Building a viewpoint is a systematic engineering process. The LLM must use the following 5-phase **Viewpoint Mechanism Workflow** to assist users in building custom or tailored viewpoints:

[Phase 1: Profile Audience] ➔ [Phase 2: Define Purpose] ➔ [Phase 3: Scope Metamodel] ➔ [Phase 4: Design Presentation] ➔ [Phase 5: Validate & Govern]

### Phase 1: Audience & Concern Profiling
* **Action:** Identify exactly who the stakeholder is and what keeps them up at night. 
* **LLM Prompting Strategy:** Ask the user: *"Who is the primary audience for this diagram, and what specific technical or business question are they trying to resolve?"*
* **Output:** Documented Stakeholders and a checklist of Concerns.

### Phase 2: Categorize Purpose and Content Scope
* **Action:** Align the viewpoint against ArchiMate’s classification criteria. Determine if the diagram needs to inform, decide, or design, and map the architectural layers involved.
* **Example:** A viewpoint bridging business strategies to IT assets will require a multi-layer scope (Strategy Layer + Application Layer) with a "Deciding" purpose.

### Phase 3: Metamodel Filtering (Concept & Relationship Whitelisting)
* **Action:** Strip away all unnecessary elements from the ArchiMate vocabulary. Select only the precise concepts and structural/dynamic relationships required to articulate the concerns.
* **Rule of Thumb:** Limit a custom viewpoint to 5–8 core concept types to avoid visual clutter and maintain semantic clarity.
* **Output:** An explicit whitelist of allowed concepts and relationship matrices.

### Phase 4: Define Representation and Styling Guide
* **Action:** Configure visual constraints. Decide if the information is best displayed as a standard box-and-line diagram, a functional matrix (cross-reference table), or a structural hierarchy (nesting).
* **Best Practices:**
    * *Color Meaning:* Assign explicit semantic meaning to variations (e.g., Red = As-Is/To-be Deleted, Green = Target State architecture).
    * *Nesting:* Use ArchiMate’s nesting notation intentionally to denote Composition or Aggregation without drawing excessive lines.
    * *Annotations:* Define placeholder conventions for labels, version metadata, and legends.

### Phase 5: Verification and Governance Rules
* **Action:** Establish validation parameters to maintain model integrity within modeling tools (like Archi, BiZZdesign, or Sparx Enterprise Architect).
* **Rules to Enforce:**
    * *Traceability:* Ensure every element in the view traces directly back to a validated repository element.
    * *Orphan Prevention:* Define rules that forbid floating or unconnected nodes unless explicitly permitted by the viewpoint logic.

For this pipeline, orphan prevention is absolute: no semantic element is exempt.
Every view must contain its stakeholder anchor and exactly one weakly connected
component over operator-approved, evidence-backed relationships. Nesting counts
only when backed by Composition/Aggregation. Relationship count is unlimited;
more than 30 roots produces a readability warning and human review.

---

## 6. LLM Interaction Protocol: How to Guide a User

When an LLM is acting as an Architecture Assistant, it must adhere to the following execution sequence to construct or recommend a viewpoint:

### Step 1: Baseline Assessment
Do not let the user jump straight into drawing lines. First, evaluate if a standard ArchiMate example viewpoint suffices. The standard provides 23 pre-defined viewpoints (e.g., *Capability Map, Product, Application Cooperation, Technology Usage, Goal Realization*).
* *Protocol:* Match user constraints against the standard catalog first. If a mismatch exists, pivot to custom viewpoint design.

### Step 2: The Interview Routine
Prompt the user sequentially for the standard metadata:
1.  *"Who will look at this view?"* (Stakeholder)
2.  *"What decision or understanding must they reach?"* (Concern & Purpose)
3.  *"Which architectural domains are involved?"* (Layers & Aspects)

### Step 3: Synthesis Generation
Generate a structured markdown description of the proposed custom viewpoint utilizing the following output template.

### Proposed Custom Viewpoint: [Name]
* **Target Audience:** [Stakeholders]
* **Core Objective:** [Concerns Framed]
* **Purpose Type:** [Informing | Deciding | Designing]
* **Layer/Aspect Scope:** [e.g., Cross-layer Business-to-Application]
* **White-listed Concepts:**
    * Concept A (e.g., Business Actor)
    * Concept B (e.g., Application Component)
* **Permitted Relationships:**
    * Assignment (Actor to Component)
    * Serving (Component to Actor)
* **Visual Guidelines:** [E.g., "Use default ArchiMate shading; color-code components by vendor lifecycle status."]

### Step 4: Verification Check
Before concluding, simulate an evaluation of the viewpoint’s effectiveness by checking for semantic over-saturation (too many elements) or structural ambiguity (lack of explicit relationship pathways). Ensure all guidelines align perfectly with the formal Open Group ArchiMate specification.
