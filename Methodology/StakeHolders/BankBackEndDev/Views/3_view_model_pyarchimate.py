#!/usr/bin/env python3
"""Build the approved DORA stakeholder views from the immutable View 0 archive.

This script is deliberately manifest-driven.  It reads the approved Step 7 graph
and extends, rather than recreates or alters, the approved View 0 archive.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from pyArchimate import ArchiType, Model, check_valid_relationship


SCRIPT_DIR = Path(__file__).resolve().parent
STAKEHOLDER_DIR = SCRIPT_DIR.parent
BASELINE_PATH = SCRIPT_DIR / "0_dora_regulation_overview.archimate"
GRAPH_PATH = STAKEHOLDER_DIR / "7_view_graph.json"
OUTPUT_PATH = SCRIPT_DIR / "3_view_model_pyarchimate.archimate"

# These hashes bind this reproducible model to the approved immutable baseline
# and exact Step 7 graph used at the Step 10c thematic-view gates.
EXPECTED_BASELINE_SHA256 = (
    "9217ee6b6d80ee6b532920494f7173014549382aabfe8a13ad0930d2ae71c64f"
)
EXPECTED_GRAPH_SHA256 = (
    "e6217913460b3abdcd9d74e981edd7885c50c367a6eaa7cf1dc3076f85dbc579"
)

REUSED_BASELINE_NODES = {
    "OP:Back-end-Developer": "Back-end Developer",
    "OP:Employer-Bank": "Employer Bank",
}
BASELINE_ROLE_RELATIONSHIP_ID = "REL-ROLE-001"


def stable_id(key: str) -> str:
    """Return an archive-stable UUID that cannot collide with View 0 IDs."""
    return str(uuid5(NAMESPACE_URL, f"dora-bank-backend-view/{key}"))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_graph() -> dict:
    if digest(BASELINE_PATH) != EXPECTED_BASELINE_SHA256:
        raise ValueError("Immutable View 0 archive hash does not match its approved source.")
    if digest(GRAPH_PATH) != EXPECTED_GRAPH_SHA256:
        raise ValueError("Step 7 graph hash does not match the approved Step 10c input.")

    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    if graph.get("schema_version") != "1.0":
        raise ValueError("Unsupported view-graph schema.")
    if graph.get("stakeholder_anchor") != "OP:Back-end-Developer":
        raise ValueError("Unexpected stakeholder anchor.")

    node_ids = [node["id"] for node in graph["nodes"]]
    relationship_ids = [rel["id"] for rel in graph["relationships"]]
    if len(node_ids) != len(set(node_ids)):
        raise ValueError("Graph contains duplicate node IDs.")
    if len(relationship_ids) != len(set(relationship_ids)):
        raise ValueError("Graph contains duplicate relationship IDs.")
    return graph


def archi_type(type_name: str):
    try:
        return getattr(ArchiType, type_name)
    except AttributeError as exc:
        raise ValueError(f"Unsupported ArchiMate type in graph: {type_name}") from exc


def ordered_unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def bullet_lines(label: str, values: list[str]) -> list[str]:
    if not values:
        return []
    return [label, *(f"- {value}" for value in values)]


def node_description(node: dict) -> str:
    """Keep graph, evidence, ownership, and legal anchors in documentation."""
    documentation = node.get("documentation", {})
    lines = [
        f"Graph node ID: {node['id']}",
        f"Canonical endpoint name: {node['name']}",
        f"ArchiMate type: {node['type']}",
    ]

    if node["id"].startswith("FAM-"):
        lines.extend(
            [
                "Approved requirement family.",
                f"Purpose: {documentation['purpose']}",
            ]
        )
        lines.extend(
            bullet_lines(
                "Child requirement IDs:",
                documentation["child_requirement_ids"],
            )
        )
        lines.extend(bullet_lines("Coverage IDs:", documentation["coverage_ids"]))
        lines.extend(
            bullet_lines(
                "Legal text IDs (child roll-up):",
                ordered_unique(documentation["direct_legal_text_id_rollup"]),
            )
        )
    elif node["id"].startswith("REQ:"):
        lines.extend(
            [
                "Approved granular DORA requirement.",
                f"Source requirement ID: {documentation['source_requirement_id']}",
                f"Full atomic duty: {documentation['full_atomic_duty']}",
                f"Coverage ID: {documentation['coverage_id']}",
                f"Ownership: {documentation['ownership']}",
                f"Citation: {documentation['citation_and_direct_legal_text_ids']}",
            ]
        )
        lines.extend(
            bullet_lines(
                "Legal text IDs:",
                documentation["direct_legal_text_ids"],
            )
        )
    else:
        lines.append(
            f"Ledger endpoint name: {documentation['ledger_endpoint_name']}"
        )
    return "\n".join(lines)


def relationship_description(relationship: dict, nodes: dict[str, dict]) -> str:
    """Retain all approved ledger evidence without making it a visible title."""
    source_name = nodes[relationship["source"]]["name"]
    target_name = nodes[relationship["target"]]["name"]
    lines = [
        f"Relationship ID: {relationship['id']}",
        f"Endpoints: {source_name} -> {target_name}",
        f"Direction: {source_name} to {target_name}",
        f"Meaning: {relationship['meaning']}",
        f"Candidate rationale: {relationship['archimate_candidate']}",
        "Evidence references:",
        *(f"- {evidence}" for evidence in relationship["evidence_refs"]),
    ]
    if relationship.get("evidence_detail"):
        lines.append(f"Evidence detail: {relationship['evidence_detail']}")
    if relationship.get("coverage_ownership"):
        lines.append(f"Coverage ownership: {relationship['coverage_ownership']}")
    lines.append(f"Operator status: {relationship['approval_status']}.")
    return "\n".join(lines)


def assert_title_purity(nodes: dict[str, dict]) -> None:
    invalid = [
        node["name"]
        for node in nodes.values()
        if len(node["name"]) > 25
        or "[" in node["name"]
        or "]" in node["name"]
        or "[Gap]" in node["name"]
    ]
    if invalid:
        raise ValueError(f"Visible title-purity violation: {invalid}")


def capture_baseline_fingerprint(model: Model) -> dict:
    """Capture View 0 semantics before adding Step 7 graph material."""
    return {
        "elements": {
            uuid: (element.type, element.name, element.desc)
            for uuid, element in model.elems_dict.items()
        },
        "relationships": {
            uuid: (
                relationship.type,
                relationship.name,
                relationship.source.uuid,
                relationship.target.uuid,
                relationship.desc,
            )
            for uuid, relationship in model.rels_dict.items()
        },
        "views": {
            uuid: (view.name, view.desc)
            for uuid, view in model.views_dict.items()
        },
    }


def find_single_baseline_element(model: Model, name: str):
    matches = [element for element in model.elems_dict.values() if element.name == name]
    if len(matches) != 1:
        raise ValueError(
            f"Expected one reusable baseline element named {name!r}; found {len(matches)}."
        )
    return matches[0]


def find_baseline_role_relationship(model: Model, node_map: dict):
    matches = [
        relationship
        for relationship in model.rels_dict.values()
        if relationship.type == ArchiType.Assignment
        and relationship.source.uuid == node_map["OP:Employer-Bank"].uuid
        and relationship.target.uuid == node_map["OP:Back-end-Developer"].uuid
        and relationship.desc.startswith(
            f"Relationship ID: {BASELINE_ROLE_RELATIONSHIP_ID}\n"
        )
    ]
    if len(matches) != 1:
        raise ValueError(
            "The immutable baseline does not contain the approved "
            "REL-ROLE-001 relationship exactly once."
        )
    return matches[0]


def add_checked_relationship(
    model: Model,
    relationship: dict,
    source,
    target,
    nodes: dict[str, dict],
):
    relationship_type = archi_type(relationship["type"])
    check_valid_relationship(
        relationship_type,
        source.type,
        target.type,
        raise_flg=True,
    )
    return model.add_relationship(
        relationship_type,
        source,
        target,
        uuid=stable_id(f"relationship/{relationship['id']}"),
        name=relationship["meaning"],
        desc=relationship_description(relationship, nodes),
        is_directed=True if relationship_type == ArchiType.Association else None,
    )


def materialize_graph(model: Model, graph: dict) -> tuple[dict, dict]:
    """Create every graph node and relation; only REL-ROLE-001 is reused."""
    nodes = {node["id"]: node for node in graph["nodes"]}
    relationships = {rel["id"]: rel for rel in graph["relationships"]}
    assert_title_purity(nodes)

    node_map = {}
    for node_id, baseline_name in REUSED_BASELINE_NODES.items():
        node = nodes[node_id]
        element = find_single_baseline_element(model, baseline_name)
        if element.type != archi_type(node["type"]):
            raise ValueError(f"Baseline type mismatch for reusable node {node_id}.")
        node_map[node_id] = element

    for node in graph["nodes"]:
        if node["id"] in node_map:
            continue
        node_map[node["id"]] = model.add(
            archi_type(node["type"]),
            node["name"],
            uuid=stable_id(f"element/{node['id']}"),
            desc=node_description(node),
            folder=(
                "/Motivation/Stakeholder Requirements"
                if node["type"] == "Requirement"
                else "/Business/Stakeholder Context"
            ),
        )

    relationship_map = {
        BASELINE_ROLE_RELATIONSHIP_ID: find_baseline_role_relationship(model, node_map)
    }
    for relationship in graph["relationships"]:
        relationship_id = relationship["id"]
        source = node_map[relationship["source"]]
        target = node_map[relationship["target"]]
        if relationship_id == BASELINE_ROLE_RELATIONSHIP_ID:
            if (
                relationship["type"] != "Assignment"
                or relationship["source"] != "OP:Employer-Bank"
                or relationship["target"] != "OP:Back-end-Developer"
            ):
                raise ValueError("REL-ROLE-001 no longer matches the approved baseline.")
            continue
        if (
            relationship["type"] == "Realization"
            and relationship.get("coverage_ownership") != "Directly performed"
        ):
            raise ValueError(
                f"Non-direct coverage must not be modelled as Realization: {relationship_id}."
            )
        relationship_map[relationship_id] = add_checked_relationship(
            model,
            relationship,
            source,
            target,
            nodes,
        )
        if relationship["type"] == "Composition":
            if not relationship["source"].startswith("FAM-"):
                raise ValueError(f"Unexpected composition parent: {relationship_id}.")
            model.add_child(source.uuid, target.uuid)

    if set(relationship_map) != set(relationships):
        raise ValueError("Relationship materialization does not match the graph manifest.")
    if model.check_invalid_relationships():
        raise ValueError("Native model contains an invalid ArchiMate relationship.")
    return node_map, relationship_map


def family_child_ids(view: dict, relationships: dict[str, dict]) -> dict[str, list[str]]:
    """Return each visible family’s visible children in approved composition order."""
    result: dict[str, list[str]] = {}
    for relationship_id in view["relationship_ids"]:
        relationship = relationships[relationship_id]
        if relationship["type"] != "Composition":
            continue
        result.setdefault(relationship["source"], []).append(relationship["target"])
    return result


def layout_view(
    model: Model,
    view_spec: dict,
    nodes: dict[str, dict],
    relationships: dict[str, dict],
    node_map: dict,
    relationship_map: dict,
) -> None:
    """Pack operational roots above nested requirement-family containers."""
    view = model.add(
        ArchiType.View,
        view_spec["name"],
        uuid=stable_id(f"view/{view_spec['id']}"),
        desc=(
            f"Approved thematic view {view_spec['id']}.\n"
            f"Purpose: {view_spec['purpose']}.\n"
            f"Stakeholder path: {view_spec['stakeholder_path']}\n"
            "Composition is represented by matching requirement-family nesting; "
            "all other approved relations have visible connections."
        ),
        folder="/Views/Stakeholder",
    )
    view_node_ids = set(view_spec["node_ids"])
    relationship_ids = view_spec["relationship_ids"]
    children_by_family = family_child_ids(view_spec, relationships)
    child_ids = {
        child_id
        for children in children_by_family.values()
        for child_id in children
    }
    family_ids = [
        node_id
        for node_id in view_spec["node_ids"]
        if node_id.startswith("FAM-")
    ]
    if set(children_by_family) != set(family_ids):
        raise ValueError(
            f"Composition-family membership mismatch in {view_spec['id']}."
        )
    if not child_ids <= view_node_ids:
        raise ValueError(f"Nested child is absent from {view_spec['id']}.")

    root_operational_ids = sorted(
        view_node_ids - child_ids - set(family_ids),
        key=lambda node_id: nodes[node_id]["name"],
    )
    visual_nodes = {}
    operational_columns = 5
    for index, node_id in enumerate(root_operational_ids):
        column, row = index % operational_columns, index // operational_columns
        visual_nodes[node_id] = view.add(
            node_map[node_id],
            40 + column * 220,
            40 + row * 90,
            190,
            55,
        )

    operational_rows = (
        (len(root_operational_ids) + operational_columns - 1) // operational_columns
    )
    family_top = 70 + max(operational_rows, 1) * 90
    family_column_gap = 600
    family_row_gap = 620
    for index, family_id in enumerate(family_ids):
        column, row = index % 2, index // 2
        family_node = view.add(
            node_map[family_id],
            40 + column * family_column_gap,
            family_top + row * family_row_gap,
            430,
            100,
        )
        visual_nodes[family_id] = family_node
        children = children_by_family[family_id]
        for child_id in children:
            visual_nodes[child_id] = family_node.add(
                node_map[child_id],
                0,
                0,
                120,
                55,
            )
        family_node.resize(
            max_in_row=3 if len(children) > 11 else 2,
            keep_kids_size=True,
            w=120,
            h=55,
            gap_x=20,
            gap_y=20,
        )

    if set(visual_nodes) != view_node_ids:
        missing = sorted(view_node_ids - set(visual_nodes))
        extra = sorted(set(visual_nodes) - view_node_ids)
        raise ValueError(
            f"Visual projection mismatch in {view_spec['id']}; "
            f"missing={missing}, extra={extra}."
        )

    for relationship_id in relationship_ids:
        relationship = relationships[relationship_id]
        if relationship["type"] == "Composition":
            continue
        source_id, target_id = relationship["source"], relationship["target"]
        if source_id not in visual_nodes or target_id not in visual_nodes:
            raise ValueError(
                f"Visible relationship endpoint missing in {view_spec['id']}: "
                f"{relationship_id}."
            )
        view.add_connection(
            relationship_map[relationship_id],
            visual_nodes[source_id],
            visual_nodes[target_id],
            uuid=stable_id(
                f"view/{view_spec['id']}/connection/{relationship_id}"
            ),
        )


def materialize_views(
    model: Model,
    graph: dict,
    node_map: dict,
    relationship_map: dict,
) -> None:
    nodes = {node["id"]: node for node in graph["nodes"]}
    relationships = {rel["id"]: rel for rel in graph["relationships"]}
    graph_node_ids = set(nodes)
    graph_relationship_ids = set(relationships)
    projected_nodes: set[str] = set()
    projected_relationships: set[str] = set()

    for view_spec in graph["views"]:
        if graph["stakeholder_anchor"] not in view_spec["node_ids"]:
            raise ValueError(f"Stakeholder anchor missing from {view_spec['id']}.")
        if not set(view_spec["node_ids"]) <= graph_node_ids:
            raise ValueError(f"Unknown node in {view_spec['id']}.")
        if not set(view_spec["relationship_ids"]) <= graph_relationship_ids:
            raise ValueError(f"Unknown relationship in {view_spec['id']}.")
        layout_view(
            model,
            view_spec,
            nodes,
            relationships,
            node_map,
            relationship_map,
        )
        projected_nodes.update(view_spec["node_ids"])
        projected_relationships.update(view_spec["relationship_ids"])

    if projected_nodes != graph_node_ids:
        raise ValueError("Some graph nodes are absent from all thematic views.")
    if projected_relationships != graph_relationship_ids:
        raise ValueError("Some graph relationships are absent from all thematic views.")


def walk_nodes(nodes):
    """Yield every root and nested visual node in a view."""
    for node in nodes:
        yield node
        yield from walk_nodes(node.nodes)


def assert_round_trip_projection(
    round_trip: Model,
    graph: dict,
    node_map: dict,
    relationship_map: dict,
) -> None:
    """Verify each persisted thematic canvas is the approved graph projection."""
    relationships = {rel["id"]: rel for rel in graph["relationships"]}
    for view_spec in graph["views"]:
        view = round_trip.views_dict.get(stable_id(f"view/{view_spec['id']}"))
        if view is None:
            raise ValueError(f"Missing thematic view after round-trip: {view_spec['id']}.")

        visual_nodes = list(walk_nodes(view.nodes))
        actual_node_refs = {node.ref for node in visual_nodes}
        expected_node_refs = {
            node_map[node_id].uuid for node_id in view_spec["node_ids"]
        }
        if actual_node_refs != expected_node_refs:
            raise ValueError(
                f"Round-trip node projection mismatch in {view_spec['id']}."
            )

        actual_parent_by_ref = {
            node.ref: getattr(node.parent, "ref", None)
            for node in visual_nodes
        }
        for relationship_id in view_spec["relationship_ids"]:
            relationship = relationships[relationship_id]
            if relationship["type"] != "Composition":
                continue
            child_ref = node_map[relationship["target"]].uuid
            parent_ref = node_map[relationship["source"]].uuid
            if actual_parent_by_ref.get(child_ref) != parent_ref:
                raise ValueError(
                    f"Round-trip containment mismatch in {view_spec['id']}: "
                    f"{relationship_id}."
                )

        actual_connection_refs = {connection.ref for connection in view.conns}
        expected_connection_refs = {
            relationship_map[relationship_id].uuid
            for relationship_id in view_spec["relationship_ids"]
            if relationships[relationship_id]["type"] != "Composition"
        }
        if actual_connection_refs != expected_connection_refs:
            raise ValueError(
                f"Round-trip connection projection mismatch in {view_spec['id']}."
            )


def assert_round_trip(
    round_trip: Model,
    graph: dict,
    baseline_fingerprint: dict,
    node_map: dict,
    relationship_map: dict,
) -> None:
    """Verify baseline preservation, native integrity, and graph exactness."""
    round_trip_baseline = capture_baseline_fingerprint(round_trip)
    for category, expected in baseline_fingerprint.items():
        for uuid, fingerprint in expected.items():
            actual = round_trip_baseline[category].get(uuid)
            if actual != fingerprint:
                raise ValueError(
                    f"Immutable baseline {category[:-1]} changed: {uuid}."
                )

    expected_element_count = len(baseline_fingerprint["elements"]) + (
        len(graph["nodes"]) - len(REUSED_BASELINE_NODES)
    )
    expected_relationship_count = len(baseline_fingerprint["relationships"]) + (
        len(graph["relationships"]) - 1
    )
    expected_view_count = len(baseline_fingerprint["views"]) + len(graph["views"])
    if len(round_trip.elems_dict) != expected_element_count:
        raise ValueError("Round-trip element count mismatch.")
    if len(round_trip.rels_dict) != expected_relationship_count:
        raise ValueError("Round-trip relationship count mismatch.")
    if len(round_trip.views_dict) != expected_view_count:
        raise ValueError("Round-trip view count mismatch.")
    if round_trip.check_invalid_relationships():
        raise ValueError("Round-trip model contains invalid relationships.")
    assert_round_trip_projection(round_trip, graph, node_map, relationship_map)

    nodes = {node["id"]: node for node in graph["nodes"]}
    relationships = {rel["id"]: rel for rel in graph["relationships"]}
    for node_id, expected_element in node_map.items():
        actual_element = round_trip.elems_dict.get(expected_element.uuid)
        if actual_element is None:
            raise ValueError(f"Missing graph node after round-trip: {node_id}.")
        if (
            actual_element.name != nodes[node_id]["name"]
            or actual_element.type != archi_type(nodes[node_id]["type"])
        ):
            raise ValueError(f"Graph node drift after round-trip: {node_id}.")

    for relationship_id, expected_relationship in relationship_map.items():
        actual_relationship = round_trip.rels_dict.get(expected_relationship.uuid)
        expected = relationships[relationship_id]
        if actual_relationship is None:
            raise ValueError(
                f"Missing graph relationship after round-trip: {relationship_id}."
            )
        if (
            actual_relationship.type != archi_type(expected["type"])
            or actual_relationship.source.uuid
            != node_map[expected["source"]].uuid
            or actual_relationship.target.uuid
            != node_map[expected["target"]].uuid
        ):
            raise ValueError(
                f"Graph relationship drift after round-trip: {relationship_id}."
            )


def build_model() -> tuple[Model, dict, dict, dict]:
    graph = load_graph()
    model = Model("DORA stakeholder extension")
    model.read(str(BASELINE_PATH))
    baseline_fingerprint = capture_baseline_fingerprint(model)
    node_map, relationship_map = materialize_graph(model, graph)
    materialize_views(model, graph, node_map, relationship_map)
    return model, graph, baseline_fingerprint, node_map, relationship_map


def main() -> None:
    model, graph, baseline_fingerprint, node_map, relationship_map = build_model()
    model.write(str(OUTPUT_PATH))

    round_trip = Model("DORA stakeholder extension round trip")
    round_trip.read(str(OUTPUT_PATH))
    assert_round_trip(
        round_trip,
        graph,
        baseline_fingerprint,
        node_map,
        relationship_map,
    )
    print(
        f"Wrote {OUTPUT_PATH.name}: {len(round_trip.elems_dict)} elements, "
        f"{len(round_trip.rels_dict)} relationships, "
        f"{len(round_trip.views_dict)} views."
    )


if __name__ == "__main__":
    main()
