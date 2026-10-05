---
name: archimate-xml-generator
description: Converts a formalized ArchiMate viewpoint specification (7_viewpoint.md), view explanation (1_view_explanation.md), and slide diagrams (2_slide_diagrams.md) into a fully compliant, well-formed ArchiMate 3.x XML model file (.archimate) ready for import into Archi.
---

# AI Skill Specification: archimate-xml-generator

## 1. Semantic Metadata
* **Skill Identifier:** `archimate-xml-generator`
* **Short Summary:** Generates a valid ArchiMate 3.x `.archimate` XML file compatible with Archi, instantiating elements, relationships, folders, diagram views (`ArchimateDiagramModel`), canvas objects (`DiagramObject`), layout bounds, color styles, and connections.
* **LLM Routing Description:**
  > "Use this skill when you need to materialize a formalized ArchiMate viewpoint specification into a concrete `.archimate` XML model file. The skill requires the viewpoint specification (`7_viewpoint.md`), the view explanation narrative (`1_view_explanation.md`), and the slide diagrams (`2_slide_diagrams.md`). It outputs a fully compliant ArchiMate 3.x XML model file for Archi."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "archimate-xml-generator",
  "description": "Generates a complete, valid ArchiMate 3.x XML file (.archimate) for Archi based on a viewpoint specification.",
  "parameters": {
    "type": "object",
    "properties": {
      "viewpoint_spec": {
        "type": "string",
        "description": "The contents of 7_viewpoint.md (element catalog, relationship catalog, visual rules)."
      },
      "view_explanation": {
        "type": "string",
        "description": "The contents of Views/1_view_explanation.md (narrative walkthrough & impact guide)."
      },
      "slide_diagrams": {
        "type": "string",
        "description": "The contents of Views/2_slide_diagrams.md (informal markdown slide diagrams)."
      },
      "view_graph": {
        "type": "string",
        "description": "The approved 7_view_graph.json node and relationship authority."
      }
    },
    "required": ["viewpoint_spec", "view_explanation", "slide_diagrams", "view_graph"]
  },
  "returns": {
    "type": "object",
    "description": "A valid, well-formed ArchiMate 3.x XML document (.archimate)."
  }
}
```

## 3. Real Reference XML Code Snippets (Derived from Archi Reference Models)

### Snippet A: Minimal Baseline Model Skeleton (from `CleanTemplateFile.archimate`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate" name="CleanTemplate" id="id-model-0001" version="5.0.0">
  <folder name="Strategy" id="id-folder-0001" type="strategy"/>
  <folder name="Business" id="id-folder-0002" type="business"/>
  <folder name="Application" id="id-folder-0003" type="application"/>
  <folder name="Technology &amp; Physical" id="id-folder-0004" type="technology"/>
  <folder name="Motivation" id="id-folder-0005" type="motivation"/>
  <folder name="Implementation &amp; Migration" id="id-folder-0006" type="implementation_migration"/>
  <folder name="Other" id="id-folder-0007" type="other"/>
  <folder name="Relations" id="id-folder-0008" type="relations"/>
  <folder name="Views" id="id-folder-0009" type="diagrams">
    <element xsi:type="archimate:ArchimateDiagramModel" name="Default View" id="id-view-0001"/>
  </folder>
</archimate:model>
```

### Snippet B: Element Declarations with Documentation & Subfolders (from `eIDAS2.archimate`)
```xml
<folder name="Business" id="id-folder-0002" type="business">
  <element xsi:type="archimate:BusinessActor" name="European Commission" id="id-elem-0001"/>
  <element xsi:type="archimate:BusinessActor" name="European Digital Identity Cooperation Group" id="id-elem-0002">
    <documentation>In order to support and facilitate Member States’ cross-border cooperation and exchange of information...</documentation>
  </element>
</folder>
```

### Snippet C: Relationship Declarations in `Relations` Folder (from `eIDAS2.archimate`)
```xml
<folder name="Relations" id="id-folder-0008" type="relations">
  <element xsi:type="archimate:AssignmentRelationship" id="id-rel-0001" source="id-elem-0001" target="id-elem-0002"/>
  <element xsi:type="archimate:AccessRelationship" name="(using)" id="id-rel-0002" source="id-elem-0003" target="id-elem-0004" accessType="2"/>
  <element xsi:type="archimate:ServingRelationship" id="id-rel-0003" source="id-elem-0005" target="id-elem-0006"/>
  <element xsi:type="archimate:TriggeringRelationship" id="id-rel-0004" source="id-elem-0007" target="id-elem-0008"/>
  <element xsi:type="archimate:RealizationRelationship" id="id-rel-0005" source="id-elem-0009" target="id-elem-0010"/>
</folder>
```

### Snippet D: Complete Diagram View (`ArchimateDiagramModel`) with DiagramObjects and Connections
```xml
<element xsi:type="archimate:ArchimateDiagramModel" name="General Provisions" id="id-view-0001">
  <!-- Visual Source Node on Canvas -->
  <child xsi:type="archimate:DiagramObject" id="id-dobj-0001" archimateElement="id-elem-0001" fillColor="#E6E6FA">
    <bounds x="840" y="564" width="279" height="74"/>
    <!-- Connection originating from this DiagramObject on canvas -->
    <sourceConnection xsi:type="archimate:Connection" id="id-conn-0001" source="id-dobj-0001" target="id-dobj-0002" archimateRelationship="id-rel-0001">
      <bendpoint startX="147" startY="-3" endX="-9" endY="69"/>
    </sourceConnection>
  </child>
  <!-- Visual Target Node on Canvas receiving incoming connection -->
  <!-- MANDATORY: targetConnections attribute MUST be declared on target DiagramObject -->
  <child xsi:type="archimate:DiagramObject" id="id-dobj-0002" targetConnections="id-conn-0001" archimateElement="id-elem-0002" fillColor="#E6E6FA">
    <bounds x="588" y="540" width="120" height="55"/>
  </child>
</element>
```

### Snippet E: Requirement-Family Visual Nesting
```xml
<!-- The outer box is a meaningful Requirement or Constraint, never Grouping. -->
<child xsi:type="archimate:DiagramObject" id="id-dobj-0010" archimateElement="id-elem-0010" fillColor="#E0FFE0">
  <bounds x="240" y="160" width="480" height="260"/>
  <!-- Nested Inner Child Elements with RELATIVE Inner Coordinates -->
  <!-- A child requirement is contained here; its Composition relationship is semantic only. -->
  <child xsi:type="archimate:DiagramObject" id="id-dobj-0011" archimateElement="id-elem-0011" fillColor="#E0EEEE">
    <bounds x="20" y="35" width="200" height="60"/>
  </child>
  <child xsi:type="archimate:DiagramObject" id="id-dobj-0012" archimateElement="id-elem-0012" fillColor="#E0EEEE">
    <bounds x="240" y="35" width="210" height="60"/>
  </child>
  <child xsi:type="archimate:DiagramObject" id="id-dobj-0013" archimateElement="id-elem-0013" fillColor="#FFFACD">
    <bounds x="20" y="140" width="430" height="85"/>
  </child>
</child>
```

### Snippet F: Pattern B - Horizontal Process Stream (Left-to-Right Flow)
```xml
<!-- Step 1: Trigger Event -->
<child xsi:type="archimate:DiagramObject" id="id-dobj-0020" archimateElement="id-elem-0020" fillColor="#FFFACD">
  <bounds x="40" y="200" width="160" height="55"/>
  <sourceConnection xsi:type="archimate:Connection" id="id-conn-0010" source="id-dobj-0020" target="id-dobj-0021" archimateRelationship="id-rel-0015"/>
</child>
<!-- Step 2: Primary Business Process (Placed to the right X2 > X1) -->
<child xsi:type="archimate:DiagramObject" id="id-dobj-0021" targetConnections="id-conn-0010" archimateElement="id-elem-0021" fillColor="#FFFACD">
  <bounds x="240" y="200" width="200" height="55"/>
  <sourceConnection xsi:type="archimate:Connection" id="id-conn-0011" source="id-dobj-0021" target="id-dobj-0022" archimateRelationship="id-rel-0016"/>
</child>
<!-- Step 3: Approval / Gate Event (Placed further right X3 > X2) -->
<child xsi:type="archimate:DiagramObject" id="id-dobj-0022" targetConnections="id-conn-0011" archimateElement="id-elem-0022" fillColor="#FFFACD">
  <bounds x="480" y="200" width="180" height="55"/>
</child>
```

### Snippet G: Pattern C - Contextual Callout Notes (`archimate:Note`)
```xml
<!-- Floating Callout Note explaining operational friction or regulatory gap -->
<child xsi:type="archimate:Note" id="id-dobj-0030" textAlignment="1">
  <bounds x="260" y="320" width="240" height="65"/>
  <sourceConnection id="id-conn-0020" source="id-dobj-0030" target="id-dobj-0021">
    <documentation>Operational Friction: Manual PR poke bottleneck delays pipeline execution.</documentation>
  </sourceConnection>
  <content>Friction Point (ASMT-PR01): Developer manually pokes reviewer to trigger gate.</content>
</child>
```

## 4. ArchiMate XML Syntax & Structural Standards

### A. Root Model Header & Namespace Declarations
```xml
<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:archimate="http://www.archimatetool.com/archimate" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="[Model Name]" id="id-model-0001" version="5.0.0">
```
* **CRITICAL NAMESPACE RULE:** The root element tag MUST be `<archimate:model ...>` with namespace declarations `xmlns:archimate="http://www.archimatetool.com/archimate"` and `xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`.
* **PYTHON / SCRIPTING WARNING:** If generating XML using Python's `xml.etree.ElementTree`, you MUST execute `ET.register_namespace("archimate", "http://www.archimatetool.com/archimate")` BEFORE writing the file. If not registered, Python renames the namespace prefix to `xmlns:ns0`, causing Archi to fail to resolve element types with errors like `Class 'BusinessActor' is not found or is abstract`.

### B. ID Namespace Uniqueness & Collision Prevention (MANDATORY)
* **CRITICAL ID RULE:** In Archi's EMF model schema, EVERY object (`model`, `folder`, `element`, `relationship`, `ArchimateDiagramModel`, `DiagramObject`, `Connection`) implements `Identifier` (`id="..."`). EMF maintains a single global lookup map (`intrinsicIDToEObjectMap`) across the entire file.
* **NEVER REUSE ID SEQUENCES ACROSS OBJECT TYPES:** Reusing numeric sequences (e.g. assigning `id-001` to Folder #1 and `id-001` to Element #1) creates an ID collision. The Folder object overwrites the Element concept in EMF's map. When a `DiagramObject` references `archimateElement="id-001"`, EMF resolves it to a `Folder` object instead of an `ArchimateElement`, triggering a `NullPointerException` or `Class not found` error in Archi.
* **MANDATORY ID PREFIX SCHEME:** Every object category MUST use a distinct, prefixed UUID range:
  - Root Folders: `id-folder-0001` to `id-folder-0009`
  - Model Elements: `id-elem-0001` to `id-elem-XXXX`
  - Relationships: `id-rel-0001` to `id-rel-XXXX`
  - Diagram View Models: `id-view-0001` to `id-view-XXXX`
  - Diagram Canvas Objects: `id-dobj-0001` to `id-dobj-XXXX`
  - Canvas Connections: `id-conn-0001` to `id-conn-XXXX`

### C. Standard Folder Taxonomy (Strict Order & Naming)
The root `<archimate:model>` MUST contain the 9 standard ArchiMate folders in exact order:
1. Strategy: `<folder name="Strategy" id="id-folder-0001" type="strategy"/>`
2. Business: `<folder name="Business" id="id-folder-0002" type="business">...elements...</folder>`
3. Application: `<folder name="Application" id="id-folder-0003" type="application">...elements...</folder>`
4. Technology & Physical: `<folder name="Technology &amp; Physical" id="id-folder-0004" type="technology">...elements...</folder>`
5. Motivation: `<folder name="Motivation" id="id-folder-0005" type="motivation">...elements...</folder>`
6. Implementation & Migration: `<folder name="Implementation &amp; Migration" id="id-folder-0006" type="implementation_migration">...elements...</folder>`
7. Other: `<folder name="Other" id="id-folder-0007" type="other"/>`
8. Relations: `<folder name="Relations" id="id-folder-0008" type="relations">...relationships...</folder>`
9. Views: `<folder name="Views" id="id-folder-0009" type="diagrams">...diagram views...</folder>`

### D. Element Declarations
Elements are placed inside their corresponding layer folder (or subfolder).
Format:
```xml
<element xsi:type="archimate:[ElementType]" name="[Element Name]" id="id-elem-[Index]">
  <documentation>[Optional Context / DORA Citation / Operational Footprint Note]</documentation>
</element>
```
* **STRICT TITLE PURITY & LENGTH GUARDRAIL (MANDATORY):**
  - **Length Limit:** The `name="..."` attribute MUST be $\le 25$ characters.
  - **Zero Notation Brackets in Titles:** NEVER include visual notation symbols or brackets in element names (e.g., NO `[Right Arrow]`, `[Folded Page]`, `[UML Box]`, `[badge]`, `[Person]`, `[Flag]`, `[3D Cube]`, `[Pill]`, `[Terminal]`, `[Doc box]`, `[red]`, `[lilac]`).
  - **Zero `[Gap]` Prefix in Titles:** Do NOT prefix gap element names with `[Gap]`. Use the element type `archimate:Gap` and a clean descriptive title (e.g., `Crash Test Absence`, `BCP Drill Absence`).
  - **Documentation Placement:** Detailed explanations, visibility limits (e.g., "potential visibility limit from junior seat, may live elsewhere"), regulatory citations, and approved canonical legal-text IDs belong strictly in the `<documentation>...</documentation>` child tag, NEVER in the `name="..."` attribute. A legal child Requirement/Constraint uses `Legal text IDs: [id; ...]`; its family parent uses `Legal text IDs (child roll-up): [id; ...]`. Serialize only IDs already approved in the ledger; never match legal text during generation.
* **ArchiMate 3.x `xsi:type` Mapping:**
  - *Motivation:* `archimate:Requirement`, `archimate:Assessment`, `archimate:Constraint`, `archimate:Goal`, `archimate:Driver`, `archimate:Principle`, `archimate:Stakeholder`.
  - *Business:* `archimate:BusinessActor`, `archimate:BusinessRole`, `archimate:BusinessProcess`, `archimate:BusinessEvent`, `archimate:BusinessObject`, `archimate:BusinessFunction`, `archimate:BusinessService`.
  - *Application:* `archimate:ApplicationComponent`, `archimate:ApplicationProcess`, `archimate:ApplicationFunction`, `archimate:ApplicationService`, `archimate:DataObject`, `archimate:Artifact`.
  - *Technology:* `archimate:Node`, `archimate:SystemSoftware`, `archimate:TechnologyService`, `archimate:Artifact`, `archimate:Device`.
  - *Implementation:* `archimate:WorkPackage`, `archimate:Deliverable`, `archimate:Gap`.

### E. Relationship Declarations
Relationships MUST be placed in the `Relations` folder (`id-folder-0008`).
Format:
```xml
<element xsi:type="archimate:[RelationType]" id="id-rel-[Index]" source="id-elem-[SourceIndex]" target="id-elem-[TargetIndex]">
  <documentation>[Semantic Justification from 7_viewpoint.md]</documentation>
</element>
```
* **Requirement-Family Realization Scheme:**
  - **Family $\rightarrow$ Child Composition:** `archimate:CompositionRelationship` where `source` is a meaningful parent `archimate:Requirement` or `archimate:Constraint` and `target` is its specific child requirement. The relationship remains in the model but has no canvas connection when nested containment communicates it.
  - **Operational Element $\rightarrow$ Requirement Realization:** `archimate:RealizationRelationship` where `source` is an operational process, application component, or artifact and `target` is the granular statutory requirement (`REQ-*`) that it realizes.
  - **Unrealized Requirements / Gaps:** If a statutory requirement is not realized by the stakeholder's footprint, model it as an unrealized requirement, or link it via `archimate:AssociationRelationship` to an `archimate:Assessment` (friction) or `archimate:Gap` element.
* **Relation `xsi:type` Mapping:**
  - `Assignment` $\rightarrow$ `archimate:AssignmentRelationship`
  - `Realization` $\rightarrow$ `archimate:RealizationRelationship`
  - `Serving` $\rightarrow$ `archimate:ServingRelationship`
  - `Access` $\rightarrow$ `archimate:AccessRelationship` (optional `accessType="1"` [read], `"2"` [write], `"3"` [read/write])
  - `Triggering` $\rightarrow$ `archimate:TriggeringRelationship`
  - `Flow` $\rightarrow$ `archimate:FlowRelationship`
  - `Composition` $\rightarrow$ `archimate:CompositionRelationship`
  - `Aggregation` $\rightarrow$ `archimate:AggregationRelationship`
  - `Association` $\rightarrow$ `archimate:AssociationRelationship`

### F. Diagram View Declarations & Bi-Directional Connection Binding
Diagram Views MUST be placed in the `Views` folder (`id-folder-0009`) or one of its operational subfolders.
Format:
```xml
<element xsi:type="archimate:ArchimateDiagramModel" name="[View Name]" id="id-view-[Index]">
  <!-- Visual Source Node on Canvas -->
  <child xsi:type="archimate:DiagramObject" id="id-dobj-[SourceIndex]" archimateElement="id-elem-[SourceElementIndex]" fillColor="[HexColor]">
    <bounds x="[X1]" y="[Y1]" width="[W1]" height="[H1]"/>
    <!-- Connection originating from this DiagramObject on canvas -->
    <sourceConnection xsi:type="archimate:Connection" id="id-conn-[Index]" source="id-dobj-[SourceIndex]" target="id-dobj-[TargetIndex]" archimateRelationship="id-rel-[RelIndex]">
      <bendpoint startX="[XOffset1]" startY="[YOffset1]" endX="[XOffset2]" endY="[YOffset2]"/>
    </sourceConnection>
  </child>
  <!-- Visual Target Node on Canvas receiving incoming connection -->
  <!-- MANDATORY: targetConnections attribute MUST be declared on target DiagramObject -->
  <child xsi:type="archimate:DiagramObject" id="id-dobj-[TargetIndex]" targetConnections="id-conn-[Index]" archimateElement="id-elem-[TargetElementIndex]" fillColor="[HexColor]">
    <bounds x="[X2]" y="[Y2]" width="[W2]" height="[H2]"/>
  </child>
</element>
```
* **MANDATORY BI-DIRECTIONAL CONNECTION BINDING:** In Archi's EMF model parser, `<sourceConnection>` defines the connection origin on the source card. However, the receiving target card MUST declare `targetConnections="id-conn-XXXX"`. If omitted, Archi fails to anchor the line endpoint to the target card and defaults the connection endpoint to `(0, 0)` or the viewport origin, causing connections to move when the viewport moves.
* **MULTIPLE TARGET CONNECTIONS:** If a target `DiagramObject` receives multiple incoming connections, list their connection IDs as space-separated values (`targetConnections="id-conn-0001 id-conn-0005"`).
* **CONNECTIONS REFER TO DIAGRAM OBJECT IDs:** In `sourceConnection`, attributes `source` and `target` MUST reference canvas `DiagramObject` IDs (`id-dobj-XXXX`), NOT raw model element IDs (`id-elem-XXXX`).
* **ORTHOGONAL ROUTING VIA BENDPOINTS:** For connections that span non-adjacent cards or cross rows, calculate orthogonal `<bendpoint startX="..." startY="..." endX="..." endY="..." />` offsets. Route connection lines through gutters between cards rather than slicing straight through intermediate elements.

### G. Professional Enterprise Architect Layout & Composition Rules
- **STRICT PROHIBITION OF FLAT MECHANICAL GRIDS:**
  - Generating flat mechanical matrix grid layouts ($X = X_0 + i \cdot \Delta X, Y = Y_0 + j \cdot \Delta Y$) where all elements sit as isolated cards is STRICTLY FORBIDDEN.
  - Every view MUST employ professional Enterprise Architecture composition patterns (container nesting, horizontal process streams, callout notes) matching reference models like `nis2.archimate`.
- **Color Codes (Matching Viewpoint Visual Rules):**
  - Motivation / Requirements: `#E6E6FA` (Lavender)
  - Business Layer: `#FFFACD` (Lemon)
  - Application Layer: `#E0EEEE` (Light Blue)
  - Technology Layer: `#E0FFE0` (Light Green)
  - Implementation Layer: `#FFDAB9` (Peach)
  - Friction Points (`ASMT-*`): `#FFA500` (Amber/Orange)
  - Regulatory Gaps (`GAP-*`): `#FF6B6B` (Light Red)
- **Visual Enclosure & Requirement-Family Nesting (Pattern A - Snippet E):**
  - Obtain the approved requirement-family ledger before layout. Each displayed parent must be a meaningful `Requirement`, `Constraint`, process, or component; `Grouping` is never an outer family box.
  - Each displayed child MUST be semantically composed by its parent and rendered as a nested `<child>` with **relative inner bounds** ($x, y$ relative to the parent). Do not draw a `sourceConnection` for that parent-child composition.
  - Render every visible `REL-*` assigned by `7_view_graph.json`. Preserve evidence
    and ownership in documentation; never emit stakeholder Realization for
    constrained, externally owned, or unclear-owner coverage. Composition/
    Aggregation is semantic-only only when matching nesting communicates it.
  - Use two child columns for 1–11 children and three for 12–18. Split a larger family into separately named coherent domains; do not split a family arbitrarily.
- **Process & Workflow Directionality (Pattern B - Snippet F):**
  - Sequential processes, events, and triggers follow a clear left-to-right operational flow ($X_1 < X_2 < X_3$).
- **Contextual Callout Notes (Pattern C - Snippet G):**
  - Annotate operational friction points (`ASMT-*`) and regulatory gaps (`GAP-*`) with floating callout boxes (`archimate:Note`) linked directly to relevant elements via callout lines.

### H. View Decomposition, Folder Taxonomy & Mandatory Overview View

1. **Dynamic Operational Lifecycle Folder Taxonomy:**
   - Under `<folder name="Views" id="id-folder-0009" type="diagrams">`, diagram views MUST NEVER be dumped as a single monolithic diagram directly in the root `Views` folder.
   - Instead, the generator MUST create subfolders named after the **Operational Lifecycle Phases** extracted from the stakeholder's operational footprint (`3_operational_footprint.md`), narrative guide (`Views/1_view_explanation.md`), and slide deck (`Views/2_slide_diagrams.md`).
   
   - **TEMPLATE & ADAPTABILITY RULE:**
     The folder names listed below are **representative examples operating as a structural template**. They MUST be adapted dynamically to align with the specific stakeholder role, domain, and legislative context:
     
     - **Generalized Architectural Template Pattern:**
       - `0. Overview & Master Architecture` (Mandatory)
       - `1. [Ingestion / Design / Setup / Maintenance Phase]`
       - `2. [Execution / Peer Review / Governance Gate Phase]`
       - `3. [Validation / Testing / Compliance Audit Phase]`
       - `4. [Monitoring / Telemetry / Reporting Phase]`
       - `5. [Emergency Response / Incident Containment / Exception Handling Phase]`
     
     - **Example A (Software Developer / DORA Context):**
       - `0. Overview & Master Architecture`
       - `1. Code Maintenance & Package Governance`
       - `2. Peer Review & Deployment Gates`
       - `3. Testing & Resilience Validation`
       - `4. Telemetry & Anomaly Observation`
       - `5. Incident Response & Emergency Patching`
     
     - **Example B (Compliance Officer / NIS2 Context):**
       - `0. Overview & Master Architecture`
       - `1. Risk Assessment & Asset Mapping`
       - `2. Incident Notification & Reporting Gates`
       - `3. Supply Chain Risk Oversight`
       - `4. Supervisory Audits & Enforcement`

2. **MANDATORY Regulation Overview View:**
   - **Always Required:** Every final `.archimate` model MUST reproduce the approved immutable regulation baseline as a top-level **Regulation Overview Map** (`ArchimateDiagramModel`) placed inside the `0. Overview & Master Architecture` subfolder inside the `Views` folder.
   - **Scope:** Contextualized View 0 contains the immutable legal core plus the
     approved stakeholder–organization–legal-role chain. It contains no other
     stakeholder operations, gaps, compliance status, Article, annex, or hidden
     catalog nodes.

3. **Readability and Connectivity Contract:**
   - Relationship count is unlimited and no approved edge may be suppressed for
     layout. More than **30 root boxes** triggers an operator readability warning
     and optional thematic split; it is not a validity failure.
   - Every semantic element has degree at least one, every view contains the
     stakeholder, and every view has exactly one weakly connected component.

4. **Clean View Naming Rule (NO Preamble / Numbering Prefixes):**
   - Diagram view titles (`name="..."` attribute on `<element xsi:type="archimate:ArchimateDiagramModel">`) MUST contain ONLY the clean, professional descriptive title (e.g. `Master Architecture Overview`, `Code Maintenance & Package Governance`, `Peer Review & Deployment Gates`, `Testing & Resilience Validation`).
   - **STRICTLY FORBIDDEN PREAMBLES:** Do NOT prefix view names with preambles or numbering prefixes such as `View X - `, `View 1: `, `Slide 1: `, `Diagram X - `, or similar prefixes. The surrounding folder structure already provides ordering and categorization.

## 5. Execution Step-by-Step

1. **Ingest & Parse Inputs:** Read the approved Coverage and Relationship Ledgers,
   contextualized immutable overview baseline, `7_viewpoint.md`,
   `7_view_graph.json`, narrative, and slides. Validate the graph with
   `Methodology/tools/view_graph_validator.py` before generation.
2. **Catalog Extraction & ID Prefix Assignment:**
   - Extract 100% of defined elements from Part A of `7_viewpoint.md`. Assign unique IDs using the `id-elem-XXXX` namespace.
   - Extract 100% of approved `REL-*` tuples and per-view membership from
     `7_view_graph.json`. Map them to XML relationship IDs without changing their
     evidence identity, endpoints, type, or direction.
3. **Folder Construction:** Instantiate standard folder hierarchy using `id-folder-0001` through `id-folder-0009`. Create operational lifecycle subfolders inside `id-folder-0009` (`Views`), starting with `0. Overview & Master Architecture`.
4. **View & Diagram Layout Synthesis:**
   - Reproduce the immutable **Regulation Overview Map** inside `0. Overview & Master Architecture` with family/child equivalence to the baseline, then add stakeholder-specific views separately.
   - Use the thematic slide breakdowns from `Views/2_slide_diagrams.md` and narrative clusters from `Views/1_view_explanation.md` to define 1 or more `ArchimateDiagramModel` views (`id-view-XXXX`) placed inside their respective operational lifecycle subfolders.
   - **Interactive Family-by-Family Loop:** Before constructing the XML, present each planned family and actual layout preview to the operator using the `question` tool:
     * **Header:** `Confirm Requirement Family`
     * **Question:** `"For '[Parent]', the nested child controls are [List]. Visible external links are [List]. The parent-child Composition relationships are semantic only and will not be drawn. Does this family name, decomposition, and layout preview communicate the intended control domain?"`
     * **Options:** `Yes (Recommended)`, `No` (with custom feedback)
     * **Execution Rule:** Loop sequentially for all planned container boxes. Proceed with final XML compilation and save strictly after 100% of container layouts are validated and approved.
   - For each element placed on a diagram canvas, create a `DiagramObject` node with unique ID `id-dobj-XXXX`, appropriate bounds ($x, y, w, h$), `fillColor`, and `archimateElement` mapping (`id-elem-XXXX`).
   - Nest every child requirement inside its actual requirement-family `DiagramObject` with relative bounds. Retain its Composition relationship in `Relations`, but do not emit a canvas connection for it.
   - For every approved visible relationship active on the canvas, generate a
     `sourceConnection` and target binding. Do not select a density-safe subset.
5. **XML Self-Validation & Requirement-Family Layout Protocol (Mandatory Pre-Persistence):**
   - Verify XML well-formedness (closing tags, escaped ampersands `&amp;`, valid attributes).
   - Verify namespace registration (`ET.register_namespace("archimate", "http://www.archimatetool.com/archimate")` if using Python).
   - Verify 100% ID uniqueness across all object categories (`id-folder-*`, `id-elem-*`, `id-rel-*`, `id-view-*`, `id-dobj-*`, `id-conn-*`).
   - Verify bi-directional connection binding (`targetConnections` present on every target `DiagramObject`).
   - Verify every visible family has an actual meaningful parent element, every displayed child is both composed by it and nested beneath its `DiagramObject`, and no parent-child Composition is a canvas connection.
   - Reject vague standalone child names, legal boilerplate, generic foundation buckets, bracketed names, and titles over 25 characters.
   - Verify 100% element and relationship coverage from `7_viewpoint.md`, and that every `COV-*` appears in model documentation and at least one stakeholder view. Verify that all non-direct coverage uses the approved external/dependency representation rather than a false realization.
   - Verify no overlapping roots or duplicate links. Relationship count is
     unlimited. If roots exceed 30, require recorded readability approval and
     retain the complete graph.
   - Project each generated view back to `7_view_graph.json`; reject isolated
     nodes, multiple components, a missing stakeholder, or node/relationship drift.
   - Verify no dangling or invalid `archimateElement`, `archimateRelationship`, `source`, or `target` references exist.
   - Verify final View 0 has the same legal-core and stakeholder/legal-role-chain
     fingerprints as the immutable baseline and does not write to the baseline path.
6. **Output:** Output the finalized `.archimate` XML document.
