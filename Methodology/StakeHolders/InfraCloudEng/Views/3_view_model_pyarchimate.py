#!/usr/bin/env python3
"""Build the approved DORA stakeholder viewpoint with pyArchimate.

Authority is the approved graph manifest.  The script retains its stable node
and relationship identities in descriptions so the generated archive can be
round-tripped into the graph contract.
"""

from __future__ import annotations

import hashlib
import importlib.metadata as metadata
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from pyArchimate import ArchiType, check_valid_relationship
from pyArchimate.model import Model


VIEWS_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
GRAPH_PATH = VIEWS_DIRECTORY.parent / "7_view_graph.json"
BASELINE_PATH = VIEWS_DIRECTORY / "0_dora_regulation_overview.archimate"
OUTPUT_PATH = Path(__file__).with_suffix(".archimate")

sys.path.insert(0, str(REPOSITORY_ROOT / "Methodology" / "tools"))
from view_graph_validator import validate_manifest, validate_projection  # noqa: E402


# Recorded approvals: all 17 thematic views were approved individually during
# the slide-diagram loop.  The operator also approved the three native-model
# semantic corrections and the exact legal/control titles over 25 characters.
THEMATIC_VIEW_APPROVALS = {
    "DORA Regulation Overview",
    "ICT Risk Governance",
    "Platform & Asset Management",
    "Provider Dependencies",
    "Access & Security",
    "Controlled Change",
    "Monitoring & Detection",
    "Continuity Preparedness",
    "Recovery & Restoration",
    "Operational Learning",
    "Crisis Communication",
    "Incident Management",
    "Incident Classification",
    "Resilience Testing",
    "Cross-platform Support",
    "Investigation Tooling",
    "Emergency Change Context",
}

TITLE_EXCEPTION_APPROVAL = (
    "Operator approved retaining exact approved legal/control titles that exceed "
    "the 25-character readability recommendation."
)


def stable_id(description: str | None, label: str) -> str:
    match = re.search(rf"^Stable {label} ID: ([^\n]+)$", description or "", re.M)
    if not match:
        raise RuntimeError(f"Missing stable {label} identity in native description")
    return match.group(1)


def load_graph() -> dict:
    graph = json.loads(GRAPH_PATH.read_text())
    report = validate_manifest(graph)
    if not report["valid"]:
        raise RuntimeError(f"Approved graph is invalid: {report['errors']}")
    approved_names = {view["name"] for view in graph["views"]}
    if approved_names != THEMATIC_VIEW_APPROVALS:
        missing = sorted(approved_names - THEMATIC_VIEW_APPROVALS)
        extra = sorted(THEMATIC_VIEW_APPROVALS - approved_names)
        raise RuntimeError(f"Thematic approval mismatch; missing={missing}, extra={extra}")
    if metadata.version("pyArchimate") != "1.12.3":
        raise RuntimeError("Installed pyArchimate version differs from the approved 1.12.3 syntax reference")
    return graph


def assert_title_purity(nodes: dict[str, dict]) -> None:
    violations = [
        node["name"]
        for node in nodes.values()
        if "[" in node["name"] or "]" in node["name"] or "[Gap]" in node["name"]
    ]
    if violations:
        raise RuntimeError(f"Element title purity violations: {violations}")


def node_description(node: dict) -> str:
    description = f"Stable node ID: {node['id']}\n{node.get('documentation', '')}".rstrip()
    if len(node["name"]) > 25:
        description += "\n\n" + TITLE_EXCEPTION_APPROVAL
    return description


def relationship_description(relation: dict) -> str:
    lines = [
        f"Stable relationship ID: {relation['id']}",
        f"Approved meaning: {relation['meaning']}",
        "Evidence references: " + ", ".join(relation["evidence_refs"]),
    ]
    if relation.get("coverage_ownership"):
        lines.append("Coverage ownership: " + relation["coverage_ownership"])
    if relation.get("access_type"):
        lines.append("Access type: " + relation["access_type"])
    return "\n".join(lines)


def baseline_fingerprint(graph: dict, nodes: dict[str, dict], relationships: dict[str, dict]) -> str:
    """Read and verify the immutable View 0 semantic core before reproduction."""

    baseline = Model("Immutable baseline verification")
    baseline.read(str(BASELINE_PATH))
    overview = graph["views"][0]
    expected_nodes = {node_id: nodes[node_id] for node_id in overview["node_ids"]}
    native_by_name = {element.name: element for element in baseline.elements}
    if set(native_by_name) != {node["name"] for node in expected_nodes.values()}:
        raise RuntimeError("Immutable View 0 element set differs from the approved graph baseline")
    for node in expected_nodes.values():
        native = native_by_name[node["name"]]
        if native.type != getattr(ArchiType, node["type"]):
            raise RuntimeError(f"Immutable View 0 type mismatch for {node['name']}")
    baseline_relationship_ids = {
        stable_id(relationship.desc, "relationship") for relationship in baseline.relationships
    }
    if baseline_relationship_ids != set(overview["relationship_ids"]):
        raise RuntimeError("Immutable View 0 relationship set differs from the approved graph baseline")
    payload = {
        "nodes": sorted((node["id"], node["name"], node["type"]) for node in expected_nodes.values()),
        "relationships": sorted(overview["relationship_ids"]),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def add_relationship(model: Model, relation: dict, elements: dict[str, object]):
    relation_type = getattr(ArchiType, relation["type"])
    source = elements[relation["source"]]
    target = elements[relation["target"]]
    check_valid_relationship(relation_type, source.type, target.type, raise_flg=True)
    if relation_type == ArchiType.Realization and relation.get("coverage_ownership") != "Directly performed":
        raise RuntimeError(f"Non-direct realization is prohibited: {relation['id']}")
    kwargs = {
        "name": relation["meaning"],
        "desc": relationship_description(relation),
        "is_directed": relation_type == ArchiType.Association,
    }
    if relation_type == ArchiType.Access:
        kwargs["access_type"] = relation.get("access_type", "Access")
    return model.add_relationship(relation_type, source, target, **kwargs)


def ensure_model_integrity(model: Model, stage: str) -> None:
    failures = {
        "invalid_relationships": model.check_invalid_relationships(),
        "invalid_nodes": model.check_invalid_nodes(),
        "invalid_connections": model.check_invalid_conn(),
    }
    failures = {name: value for name, value in failures.items() if value}
    if failures:
        raise RuntimeError(f"{stage} native integrity validation failed: {failures}")


def visual_children(nodes: dict[str, dict], members: set[str]) -> dict[str, list[str]]:
    children: dict[str, list[str]] = defaultdict(list)
    for node_id in members:
        parent_id = nodes[node_id].get("parent_id")
        if parent_id in members:
            children[parent_id].append(node_id)
    return children


def add_nested_children(parent_visual, parent_id: str, children: dict[str, list[str]], elements: dict[str, object]):
    child_ids = children.get(parent_id, [])
    for child_id in child_ids:
        child_visual = parent_visual.add(elements[child_id])
        add_nested_children(child_visual, child_id, children, elements)
    if child_ids:
        parent_visual.resize(max_in_row=3 if len(child_ids) >= 12 else 2)


def add_view(model: Model, view_spec: dict, nodes: dict[str, dict], relationships: dict[str, dict], elements: dict[str, object]):
    view_id = view_spec["id"]
    folder = "/Views/Overview" if view_id == "VIEW-DORA-OVERVIEW" else "/Views/Thematic"
    view = model.add(
        ArchiType.View,
        view_spec["name"],
        desc=f"Stable view ID: {view_id}\nPurpose: {view_spec['purpose']}",
        folder=folder,
    )
    members = set(view_spec["node_ids"])
    children = visual_children(nodes, members)
    roots = [node_id for node_id in view_spec["node_ids"] if nodes[node_id].get("parent_id") not in members]
    visuals: dict[str, object] = {}

    if view_id == "VIEW-DORA-OVERVIEW":
        baseline_positions = {
            "ROLE-INFRA-CLOUD-DBA": (40, 780, 240, 70),
            "ORG-BANK": (340, 780, 180, 70),
            "ROLE-DORA-FINANCIAL-ENTITY": (570, 780, 200, 70),
        }
        for node_id, (x, y, width, height) in baseline_positions.items():
            visuals[node_id] = view.add(elements[node_id], x=x, y=y, w=width, h=height)
        framework_id = "REQ-DORA-RESILIENCE"
        framework_visual = view.add(elements[framework_id], x=840, y=40, w=1680, h=1200)
        visuals[framework_id] = framework_visual
        add_nested_children(framework_visual, framework_id, children, elements)
    else:
        framework_id = "REQ-DORA-RESILIENCE"
        framework_visual = view.add(elements[framework_id], x=980, y=40, w=900, h=900)
        visuals[framework_id] = framework_visual
        add_nested_children(framework_visual, framework_id, children, elements)
        external_roots = [node_id for node_id in roots if node_id != framework_id]
        for index, node_id in enumerate(external_roots):
            x = 40 + (index % 3) * 290
            y = 80 + (index // 3) * 120
            visuals[node_id] = view.add(elements[node_id], x=x, y=y, w=240, h=80)
            add_nested_children(visuals[node_id], node_id, children, elements)

    missing_visuals = set(view_spec["node_ids"]) - set(
        stable_id(node.concept.desc, "node") for node in _walk_nodes(view.nodes)
    )
    if missing_visuals:
        raise RuntimeError(f"{view_id}: missing visual nodes {sorted(missing_visuals)}")

    for relation_id in view_spec["relationship_ids"]:
        relation = relationships[relation_id]
        if relation["type"] in {"Composition", "Aggregation"}:
            continue
        view.add_connection(relation["native"])
    return view


def _walk_nodes(nodes):
    for node in nodes:
        yield node
        yield from _walk_nodes(node.nodes)


def project_round_trip(graph: dict, round_trip: Model) -> dict:
    node_ids_by_uuid = {element.uuid: stable_id(element.desc, "node") for element in round_trip.elements}
    relation_ids_by_uuid = {
        relationship.uuid: stable_id(relationship.desc, "relationship")
        for relationship in round_trip.relationships
    }
    graph_relations = {relation["id"]: relation for relation in graph["relationships"]}
    projected_views = []
    for expected_view in graph["views"]:
        stable_view = next(
            view
            for view in round_trip.views
            if stable_id(view.desc, "view") == expected_view["id"]
        )
        visual_nodes = {node_ids_by_uuid[node.ref]: node for node in _walk_nodes(stable_view.nodes)}
        node_ids = sorted(visual_nodes)
        connected_ids = {relation_ids_by_uuid[connection.ref] for connection in stable_view.conns}
        semantic_ids = set()
        for relation_id in expected_view["relationship_ids"]:
            relation = graph_relations[relation_id]
            if relation["type"] not in {"Composition", "Aggregation"}:
                continue
            source_visual = visual_nodes[relation["source"]]
            target_visual = visual_nodes[relation["target"]]
            if target_visual.parent is not source_visual:
                raise RuntimeError(
                    f"{expected_view['id']}: semantic containment is missing for {relation_id}"
                )
            semantic_ids.add(relation_id)
        projected_views.append(
            {
                "id": expected_view["id"],
                "node_ids": node_ids,
                "relationship_ids": sorted(connected_ids | semantic_ids),
            }
        )
    return {"technology": "pyarchimate", "views": projected_views}


def main() -> None:
    graph = load_graph()
    nodes = {node["id"]: node for node in graph["nodes"]}
    relation_specs = {relation["id"]: relation for relation in graph["relationships"]}
    assert_title_purity(nodes)
    immutable_baseline_fingerprint = baseline_fingerprint(graph, nodes, relation_specs)

    model = Model("DORA InfraCloudEng")
    elements = {
        node_id: model.add(
            getattr(ArchiType, node["type"]),
            node["name"],
            desc=node_description(node),
        )
        for node_id, node in nodes.items()
    }

    for node in nodes.values():
        if node.get("parent_id"):
            model.add_child(elements[node["parent_id"]].uuid, elements[node["id"]].uuid)

    relationships = {}
    for relation in graph["relationships"]:
        native = add_relationship(model, relation, elements)
        relationships[relation["id"]] = native
        relation["native"] = native

    for view_spec in graph["views"]:
        add_view(model, view_spec, nodes, relation_specs, elements)

    ensure_model_integrity(model, "Pre-write")
    model.write(str(OUTPUT_PATH))

    round_trip = Model("DORA InfraCloudEng Round Trip")
    round_trip.read(str(OUTPUT_PATH))
    ensure_model_integrity(round_trip, "Round-trip")

    round_trip_node_ids = {stable_id(element.desc, "node") for element in round_trip.elements}
    round_trip_relationship_ids = {
        stable_id(relationship.desc, "relationship") for relationship in round_trip.relationships
    }
    if round_trip_node_ids != set(nodes):
        raise RuntimeError("Round-trip node identity mismatch")
    if round_trip_relationship_ids != set(relation_specs):
        raise RuntimeError("Round-trip relationship identity mismatch")

    projection = project_round_trip(graph, round_trip)
    projection_report = validate_projection(graph, projection)
    if not projection_report["valid"]:
        raise RuntimeError(f"Round-trip projection mismatch: {projection_report['errors']}")

    print(
        json.dumps(
            {
                "output": str(OUTPUT_PATH),
                "nodes": len(nodes),
                "relationships": len(relation_specs),
                "views": len(graph["views"]),
                "immutable_baseline_fingerprint": immutable_baseline_fingerprint,
                "projection": projection_report,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
