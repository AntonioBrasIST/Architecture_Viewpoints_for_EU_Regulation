---
name: archimate-symbol-validator
description: Validates and enforces 100% correct ArchiMate element selection, layer/aspect classification, and visual symbol/notation representation across viewpoint specifications, narrative guides, slide diagrams, and XML models.
---

# AI Skill Specification: archimate-symbol-validator

## 1. Semantic Metadata
* **Skill Identifier:** `archimate-symbol-validator`
* **Short Summary:** Enforces accurate ArchiMate element selection, visual symbol mapping, and concept definition compliance across all pipeline view generation steps.
* **LLM Routing Description:**
  > "Use this tool to validate or select ArchiMate metamodel concepts and visual symbols. It ensures that every architectural element (Active Structure, Behavior, Passive Structure) is mapped to its correct official ArchiMate element name, visual icon, and layer color. Do NOT use this tool to fetch EU legislation or perform interview transcripts parsing."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "archimate-symbol-validator",
  "description": "Enforces 100% accurate ArchiMate element selection, layer/aspect classification, and visual symbol/notation representation.",
  "parameters": {
    "type": "object",
    "properties": {
      "candidate_elements": {
        "type": "array",
        "description": "List of candidate architectural elements or concepts to be validated against the ArchiMate metamodel and symbol rules.",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string", "description": "The candidate element name" },
            "layer": { "type": "string", "enum": ["Business", "Application", "Technology"] },
            "aspect": { "type": "string", "enum": ["Active Structure", "Behavior", "Passive Structure"] },
            "proposed_archimate_type": { "type": "string", "description": "Proposed ArchiMate concept (e.g. ApplicationComponent, Node, Artifact)" }
          },
          "required": ["name", "proposed_archimate_type"]
        }
      }
    },
    "required": ["candidate_elements"]
  },
  "returns": {
    "type": "object",
    "description": "A validated symbol audit report listing approved elements, corrected mappings, official visual icons, and visual layout notation rules."
  }
}
```

## 3. Core Logic & Execution Flow

### A. Core Metamodel Elements & Symbol Mapping Tables

#### 1. Business Layer (`#FFFACD` / Yellow-Lemon)

| Aspect | ArchiMate Concept | Primary Visual Icon | Alternate Symbol / Notation |
| :--- | :--- | :--- | :--- |
| **Active Structure** | Business Actor | Person figure | Stick figure |
| | Business Role | Position badge | Cylinder shape |
| | Business Collaboration | Intersecting rings | Overlapping circles |
| | Business Interface | Lollipop / Ball-and-socket | Ball-and-socket line |
| | Location | Map pin | Location marker |
| | Business Object | Rectangular document box | Data box / Object entity |
| **Behavioral** | Business Process | Rightward arrow | Horizontal arrow badge |
| | Business Function | Chevron / Up-arrow | Up-arrow badge |
| | Business Service | Rounded rectangle | Pill / Oval |
| | Business Event | Pointed flag | Tag / Arrowhead flag |
| | Business Interaction | Split circle | Split vertical circle |
| **Passive Structure / Informational** | Representation | Page with wave | Physical or digital representation |
| | Meaning | Speech bubble / Cloud icon | Knowledge / Interpretation concept |
| | Value | Ribbon badge | Relative worth / Utility badge |
| | Product | Box with header stripe | Package of services & contract |
| | Contract | Scroll / Document with line | Formal/informal agreement scroll |

#### 2. Application Layer (`#E0EEEE` / Light Cyan-Blue)

| Aspect | ArchiMate Concept | Primary Visual Icon | Alternate Symbol / Notation |
| :--- | :--- | :--- | :--- |
| **Active Structure** | Application Component | Component box | UML component box (with left prongs) |
| | Application Collaboration | Intersecting rings | Overlapping circles |
| | Application Interface | Ball-and-socket | Socket line / Lollipop |
| **Behavioral** | Application Function | Chevron | Up-arrow badge |
| | Application Process | Rightward arrow | Horizontal process arrow |
| | Application Service | Rounded rectangle | Pill / Oval |
| | Application Event | Pointed flag | Arrowhead tag |
| | Application Interaction | Split circle | Split vertical circle |
| **Passive Structure** | Data Object | Document box | Data entity / payload box |

#### 3. Technology Layer (`#E0FFE0` / Light Green)

| Aspect | ArchiMate Concept | Primary Visual Icon | Alternate Symbol / Notation |
| :--- | :--- | :--- | :--- |
| **Active Structure** | Node | 3D Box | 3D Cube / Block |
| | Device | Monitor / Terminal | Computer / Desktop icon |
| | System Software | 3D Box with disk icon | OS / Middleware block |
| | Infrastructure Interface | Ball-and-socket | Socket line / Lollipop |
| | Network | Solid double-ended arrow | Solid double arrow ($\longleftrightarrow$) |
| | Communication Path | Dashed double arrow | Dashed double arrow ($\dashleftarrow\dashrightarrow$) |
| **Behavioral** | Infrastructure Function | Chevron | Up-arrow badge |
| | Infrastructure Service | Rounded rectangle | Pill / Oval |
| **Passive Structure** | Artifact | Folded-corner page | File / Code / Package icon |

---

### B. ArchiMate Concept Definitions Mapping

#### 1. Business Layer Concepts & Definitions
1. **Business Actor (Active Structure):** An organizational entity capable of performing behavior (e.g. an individual employee, department, customer, or enterprise).
2. **Business Role (Active Structure):** The responsibility to perform specific behavior, to which an actor can be assigned (e.g. Senior Software Developer, Compliance Officer).
3. **Business Collaboration (Active Structure):** An aggregate of two or more business internal active structure elements that work together to perform collective behavior.
4. **Business Interface (Active Structure):** A point of access where a business service is made available to the environment or external actors.
5. **Location (Active Structure):** A conceptual or physical place or position where concepts are located or business activities take place.
6. **Business Object (Active Structure):** An active structural entity that holds business relevance, information, or operational state within the organization.
7. **Business Process (Behavioral):** A sequence of business behaviors that achieves a specific outcome, such as a defined set of products or services.
8. **Business Function (Behavioral):** A collection of business behaviors grouped on the basis of a given set of criteria (e.g. required competencies, resources, or organizational structure).
9. **Business Service (Behavioral):** An explicitly defined, externally exposed business behavior that delivers value to an actor or environment.
10. **Business Event (Behavioral):** A business behavior element that denotes a state change in the business domain.
11. **Business Interaction (Behavioral):** A unit of collective business behavior performed by two or more business roles or actors working together.
12. **Representation (Passive Structure):** The perceptible, physical or digital form of the information carried by a business object (e.g. a PDF report, printed form, or UI screen display).
13. **Meaning (Passive Structure / Informational):** The knowledge, expertise, or cognitive interpretation assigned to a business object or representation.
14. **Value (Passive Structure / Informational):** The relative worth, utility, or importance that a business service, process, or product delivers to a stakeholder.
15. **Product (Passive Structure / Informational):** A coherent package of services and accompanying contractual rights or obligations, offered as a single unit to internal or external customers.
16. **Contract (Passive Structure):** A formal or informal specification of an agreement that defines rights, obligations, and service levels associated with a product or service.

#### 2. Application Layer Concepts & Definitions
1. **Application Component (Active Structure):** An encapsulation of software application functionality aligned to implementation structure, which can be independently deployed, executed, and re-used (e.g. a REST API microservice, web frontend, or database engine).
2. **Application Collaboration (Active Structure):** An aggregate of two or more application components that work together to perform collective application behavior.
3. **Application Interface (Active Structure):** A point of access where an application service is made available to a user, another application component, or a node (e.g. an HTTP REST endpoint, gRPC socket, or message queue listener).
4. **Application Function (Behavioral):** An automated behavior performed by an application component (e.g. data validation, password hashing, or invoice calculation).
5. **Application Process (Behavioral):** A sequence of automated application behaviors that achieves a specific data processing outcome.
6. **Application Service (Behavioral):** An explicitly defined, exposed application behavior that provides functionality to automated components or business processes.
7. **Application Event (Behavioral):** An application behavior element that denotes a state change in an application (e.g. `OrderPlaced`, `BuildFailed`).
8. **Application Interaction (Behavioral):** A unit of collective application behavior performed by two or more application components.
9. **Data Object (Passive Structure):** Data structured for automated processing by application components (e.g. a JSON payload, database table, or XML schema).

#### 3. Technology Layer Concepts & Definitions
1. **Node (Active Structure):** A computational or physical resource that hosts, manipulates, or executes software resources (e.g. a Kubernetes cluster, virtual machine, or server host).
2. **Device (Active Structure):** A physical IT resource upon which system software and applications are deployed (e.g. a developer workstation, hardware server, or router).
3. **System Software (Active Structure):** Software that provides or manages environment capabilities supporting applications (e.g. Docker Engine, Kubernetes OS, Linux kernel, or .NET Runtime).
4. **Infrastructure / Technology Interface (Active Structure):** A point of access where technology services offered by a node are made available to other nodes or application components.
5. **Network / Communication Network (Active Structure):** A set of structures that connects computer systems or electronic devices for transmission of data ($\longleftrightarrow$).
6. **Communication Path (Active Structure):** A logical link between two or more nodes through which nodes exchange data or materials ($\dashleftarrow\dashrightarrow$).
7. **Infrastructure / Technology Function (Behavioral):** A collection of technology behaviors based on hardware or system software capabilities (e.g. container orchestration, disk encryption).
8. **Infrastructure / Technology Service (Behavioral):** An explicitly defined, exposed technology capability delivered by infrastructure nodes (e.g. Blob Storage Service, DNS resolution).
9. **Artifact (Passive Structure):** A piece of physical/digital data used or produced in a software development process or IT deployment (e.g. compiled `.dll` file, Docker image, C# source code file, or NuGet package).

---

## 4. Symbol Disambiguation & Hard Intercept Rules

1. **Active Structure vs. Behavior Intercept:**
   - *Rule:* Active software modules MUST be modeled as `Application Component` (UML box symbol), NEVER as `Application Function` (chevron).
2. **Infrastructure Node vs. Application Component Intercept:**
   - *Rule:* Physical or virtual hosting environments (K8s pods, VMs, workstation hardware) MUST be modeled as `Node` (3D cube) or `Device` (terminal icon), NEVER as `Application Component`.
3. **Source Code / Packages vs. Application Component Intercept:**
   - *Rule:* C# source files, compiled binaries, test scripts, and third-party packages MUST be modeled as `Artifact` (folded-corner page icon), NEVER as `Application Component`.
4. **Process vs. Function vs. Service Intercept:**
   - *Sequential Flow:* Step-by-step workflow $\rightarrow$ `Process` (Rightward arrow).
   - *Capability Grouping:* Grouped business/IT behavior $\rightarrow$ `Function` (Chevron).
   - *Exposed Interface:* Externally consumed capability $\rightarrow$ `Service` (Pill / Oval).

---

## 5. Safety, Boundaries & Error Interception
* **Zero Custom Element Rule:** AI agents must NEVER invent custom ArchiMate element types (e.g. `RegulationElement` or `MicroserviceObject`). They MUST choose from the official elements defined in Section 3.
* **Notation Consistency & Title Purity Rule:**
  - Visual symbol annotations (e.g. `[UML Component Box]`, `[3D Cube]`, `[Folded Page]`, `[Chevron]`, `[Right Arrow]`, `[Pill]`) are reference aliases for human documentation and slide text ONLY.
  - **STRICT TITLE PURITY CONTRACT:** Visual symbol annotations, brackets, and color or status tags (e.g., `[Right Arrow]`, `[Folded Page]`, `[UML Box]`, `[3D Cube]`, `[badge]`, `[Person]`, `[Flag]`, `[Doc box]`, `[Gap]`, `[red]`, `[lilac]`) MUST NEVER be appended to actual element names, titles, or model identifiers in ArchiMate (`.archimate`), LikeC4 (`.c4`), or Viewpoint specifications (`7_viewpoint.md`).
  - **Title Length Limit:** All element names and titles must be clean, readable domain titles strictly **$\le 25$ characters** in length.
* **Notation Consistency in Slides:** Markdown slide deck diagrams (`2_slide_diagrams.md`) may explain visual symbols in legends or slide component breakdowns matching the alternate symbol table, but actual model node titles must remain clean.

---

## 6. Required Output Format

```markdown
### ArchiMate Symbol Validation Audit Report

| Candidate Element | Current Layer & Aspect | Validated ArchiMate Concept | Primary Visual Icon | Alternate Notation Symbol |
| :--- | :--- | :--- | :--- | :--- |
| [Element Name] | [Layer / Aspect] | [Official Concept] | [Primary Icon] | [Alternate Notation] |
```
