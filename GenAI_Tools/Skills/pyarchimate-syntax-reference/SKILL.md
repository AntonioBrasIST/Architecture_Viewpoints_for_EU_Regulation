---
name: pyarchimate-syntax-reference
description: Provides exhaustive, version-aware pyArchimate syntax and metamodel legality checks for authoring or reviewing pyArchimate scripts. Use before creating or repairing a script; do not use it to choose architecture concepts from prose or create model artifacts on its own.
---

# AI Skill Specification: pyarchimate_syntax_reference

## 1. Semantic Metadata

* **Skill Identifier:** `pyarchimate_syntax_reference`
* **Short Summary:** Establishes exact installed pyArchimate syntax and automatic-layout-first patterns before a generation skill writes code.
* **LLM Routing Description:**
  > "Use this skill whenever an agent authors, reviews, or repairs a pyArchimate Python script. Do NOT use it as a substitute for ArchiMate semantic modeling, operator approval, or artifact generation."

## 2. Interface Schema (JSON Style)

```json
{
  "name": "pyarchimate_syntax_reference",
  "description": "Inspects installed pyArchimate and provides validated syntax patterns.",
  "parameters": {
    "type": "object",
    "properties": {
      "script_purpose": {"type": "string", "description": "Operation to author or review.", "required": true},
      "python_executable": {"type": "string", "description": "Python executable that imports pyArchimate.", "required": true},
      "relationship_tuples": {"type": "array", "description": "Optional source/type/target tuples to preflight.", "items": {"type": "object"}, "required": false}
    },
    "required": ["script_purpose", "python_executable"]
  },
  "returns": {"type": "object", "description": "Installed API inventory, relationship validation results, approved syntax patterns, and blocking errors."}
}
```

## 3. Runtime Authority

1. Inspect the installed package before writing code. It is authoritative when it differs from web documentation.

```python
import importlib.metadata as metadata
import inspect
from pyArchimate import ArchiType, check_valid_relationship
from pyArchimate.model import Model

print(metadata.version("pyArchimate"))
print([member.name for member in ArchiType])
print(inspect.signature(Model.add_relationship))
```

2. Do not use `relate`, `create_view`, `save`, `view.add_all()`, or `export_svg`. They are not methods in the installed API. If SVG is explicitly requested in another task, use `view.to_svg(str(path))`.
3. Pass a string, not a `Path`, to `Model.write`. Use absolute Archi folder paths such as `"/Views/Overview"`.
4. `View.add` adds a single visual node. The installed package has no native `View.add_all`; use explicit family containment (`parent_node.add`) for child requirements.

## 4. Requirement-Family Containment Pattern

For regulation overviews and stakeholder requirement-family views, generated 10c scripts MUST use both model and visual hierarchy. `Model.add_child(parent.uuid, child.uuid)` records the logical hierarchy; `parent_node.add(child)` creates the visible containment. The parent must be a meaningful Requirement, Constraint, process, or component—not a decorative Grouping.

Do not claim that `apply_layout()` produces a hierarchical layout unless a runtime smoke test verifies that the installed runtime dispatches that algorithm. In the installed 1.12.3 runtime, `apply_layout()` uses its coarse automatic layout/routing path; it does not by itself establish requirement-family containment. Use deterministic, measured packing only for root boxes and let `parent_node.resize()` format nested children.

```python
def add_requirement_family(model, view, parent, children, x, y):
    for child in children:
        model.add_child(parent.uuid, child.uuid)

    parent_node = view.add(parent, x=x, y=y, w=420, h=160)
    for child in children:
        parent_node.add(child)
    parent_node.resize(max_in_row=2 if len(children) <= 11 else 3)
    return parent_node

def add_external_connections(view, relationships):
    for relationship in relationships:
        # Parent-child Composition is semantic only: it has no canvas edge.
        if relationship.type != ArchiType.Composition:
            view.add_connection(relationship)
```

Use two child columns for 1–11 children and three for 12–18. Split a larger family into separately named coherent domains. Pack roots with measured non-overlapping bounds. Relationship count is unlimited: create every approved visible `REL-*` from `7_view_graph.json`. More than 30 roots triggers operator readability review but never edge suppression. Do not set child coordinates, child dimensions, bendpoints, or manual routes.

## 5. Complete ArchiType Catalog

| Category | Types |
| :--- | :--- |
| Business | `BusinessActor`, `BusinessRole`, `BusinessCollaboration`, `BusinessInterface`, `BusinessProcess`, `BusinessFunction`, `BusinessInteraction`, `BusinessEvent`, `BusinessService`, `BusinessObject`, `Contract`, `Representation`, `Product` |
| Application | `ApplicationComponent`, `ApplicationInterface`, `ApplicationInteraction`, `ApplicationCollaboration`, `ApplicationFunction`, `ApplicationProcess`, `ApplicationEvent`, `ApplicationService`, `DataObject` |
| Technology | `Node`, `Device`, `Path`, `CommunicationNetwork`, `SystemSoftware`, `TechnologyCollaboration`, `TechnologyInterface`, `TechnologyFunction`, `TechnologyProcess`, `TechnologyInteraction`, `TechnologyEvent`, `TechnologyService`, `Artifact` |
| Physical | `Equipment`, `Facility`, `DistributionNetwork`, `Material` |
| Motivation | `Stakeholder`, `Driver`, `Assessment`, `Goal`, `Outcome`, `Principle`, `Requirement`, `Constraint`, `Meaning`, `Value` |
| Strategy | `Resource`, `Capability`, `CourseOfAction`, `ValueStream` |
| Implementation & Migration | `WorkPackage`, `Deliverable`, `ImplementationEvent`, `Plateau`, `Gap` |
| Other | `Grouping`, `Location`, `Junction`, `OrJunction`, `AndJunction` |
| Diagram construct | `View` |
| Relationships | `Association`, `Assignment`, `Realization`, `Serving`, `Composition`, `Aggregation`, `Access`, `Influence`, `Triggering`, `Flow`, `Specialization` |

## 6. Canonical Model Pattern

```python
from pathlib import Path
from pyArchimate import ArchiType, check_valid_relationship
from pyArchimate.model import Model

m = Model("Example Model")
actor = m.add(ArchiType.BusinessActor, "Customer", desc="Consumes the service.")
process = m.add(ArchiType.BusinessProcess, "Place Order")
service = m.add(ArchiType.ApplicationService, "Order Service")
data = m.add(ArchiType.DataObject, "Order Data")

def add_relation(rel_type, source, target, **kwargs):
    check_valid_relationship(rel_type, source.type, target.type, raise_flg=True)
    return m.add_relationship(rel_type, source, target, **kwargs)

assignment = add_relation(ArchiType.Assignment, actor, process)
serving = add_relation(ArchiType.Serving, service, process)
access = add_relation(ArchiType.Access, service, data, access_type="ReadWrite")

overview = m.add(ArchiType.View, "Overview", folder="/Views/Overview")
actor_node = overview.add(actor, x=40, y=40)
process_node = overview.add(process, x=300, y=40)
service_node = overview.add(service, x=560, y=40)
data_node = overview.add(data, x=820, y=40)
for relationship in [assignment, serving, access]:
    overview.add_connection(relationship)

if m.check_invalid_relationships() or m.check_invalid_nodes() or m.check_invalid_conn():
    raise RuntimeError("Model integrity validation failed")
output = Path(__file__).with_suffix(".archimate")
m.write(str(output))
round_trip = Model("Round-trip validation")
round_trip.read(str(output))
```

## 7. Relationship Rules

| Relationship | Direction and required pattern |
| :--- | :--- |
| `Association` | Generic semantic link; set `is_directed=True` only when direction is material. |
| `Assignment` | Active structure to behavior it performs. |
| `Realization` | Concrete operational element to the more abstract service, requirement, or outcome it realizes. |
| `Serving` | Provider to consumer. |
| `Composition` | Whole to inseparable part. |
| `Aggregation` | Whole to independently meaningful part. |
| `Access` | Behavior or structure to passive structure; set `access_type` to `Read`, `Write`, `ReadWrite`, or `Access`. |
| `Influence` | Motivational source to influenced element; set `influence_strength` to `+`, `++`, `-`, `--`, or `0` through `10` when known. |
| `Triggering` | Earlier behavior or event to behavior/event it initiates. |
| `Flow` | Sender to receiver of information, value, or material. |
| `Specialization` | Specialized element to its more general element. |

Always verify each exact source/type/target tuple before creation:

```python
check_valid_relationship(rel_type, source.type, target.type, raise_flg=True)
```

## 8. Safety, Boundaries & Error Interception

* **Human-in-the-Loop (HITL) Requirement:** False for syntax inspection. True when its results are used to create model artifacts, under the generator skill's thematic-view approval gate.
* **Deterministic Error Matrix:**

  | Input/State Failure | System Error Action | Return Message to LLM |
  | :--- | :--- | :--- |
  | pyArchimate cannot import | Abort | `Error: pyArchimate is not installed for the selected Python executable.` |
  | API or enum drift | Abort generated code | `Error: Installed pyArchimate API differs from this reference. Inspect installed signatures before continuing.` |
  | Illegal relationship | Raise before model mutation | `Error: Relationship is invalid for the selected source and target types.` |
| Endpoint node absent | Do not add connection | `Error: Both relationship endpoint nodes must belong to the view.` |
  | Isolated node, multiple components, or missing stakeholder | Abort before write | `Error: Generated view violates the approved connected-view graph.` |
  | Layout failure | Do not write output | `Error: Automatic layout failed. Correct view membership or model integrity.` |
  | Archive unreadable | Abort delivery | `Error: Generated .archimate archive cannot be read by pyArchimate.` |

* **Loop Prevention Rule:** If an identical API-drift or validation error occurs twice in one turn, stop and request operator direction.
