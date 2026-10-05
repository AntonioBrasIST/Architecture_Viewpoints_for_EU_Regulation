#!/usr/bin/env python3
"""Validate the pipeline's evidence-backed view graph manifest.

The validator is deliberately technology-neutral. Native model generators must
round-trip their output into this contract before persistence.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


RELATION_PREFIXES = ("REL-OP-", "REL-COV-", "REL-ROLE-", "REL-COMP-")
SEMANTIC_ONLY_TYPES = {"Composition", "Aggregation"}
EVIDENCE_PREFIXES = ("OP-", "CON-", "REQ-", "COV-", "ROLE-", "SRC-")
NON_DIRECT_OWNERSHIP = {
    "Stakeholder-constrained",
    "Externally owned",
    "Not evidenced / unclear owner",
}
OWNERSHIP_STATES = NON_DIRECT_OWNERSHIP | {"Directly performed"}
PROJECTION_TECHNOLOGIES = {"xml", "likec4", "pyarchimate", "slides"}


def _duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic validation report for a view graph manifest."""

    errors: list[str] = []
    warnings: list[str] = []
    view_reports: list[dict[str, Any]] = []

    if manifest.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")

    threshold = manifest.get("root_warning_threshold", 30)
    if threshold != 30:
        errors.append("root_warning_threshold must be 30")

    stakeholder = manifest.get("stakeholder_anchor")
    if not isinstance(stakeholder, str) or not stakeholder:
        errors.append("stakeholder_anchor must name one node")

    raw_nodes = manifest.get("nodes", [])
    raw_relationships = manifest.get("relationships", [])
    raw_views = manifest.get("views", [])
    if not isinstance(raw_nodes, list) or not isinstance(raw_relationships, list) or not isinstance(raw_views, list):
        return {
            "valid": False,
            "errors": errors + ["nodes, relationships, and views must be arrays"],
            "warnings": warnings,
            "views": view_reports,
        }

    node_ids = [node.get("id") for node in raw_nodes if isinstance(node, dict)]
    relation_ids = [rel.get("id") for rel in raw_relationships if isinstance(rel, dict)]
    view_ids = [view.get("id") for view in raw_views if isinstance(view, dict)]
    for label, values in (("node", node_ids), ("relationship", relation_ids), ("view", view_ids)):
        invalid = [value for value in values if not isinstance(value, str) or not value]
        if invalid:
            errors.append(f"every {label} must have a non-empty string id")
        for duplicate in sorted(_duplicates([value for value in values if isinstance(value, str)])):
            errors.append(f"duplicate {label} id: {duplicate}")

    nodes = {node["id"]: node for node in raw_nodes if isinstance(node, dict) and isinstance(node.get("id"), str)}
    relationships = {
        rel["id"]: rel
        for rel in raw_relationships
        if isinstance(rel, dict) and isinstance(rel.get("id"), str)
    }

    if stakeholder and stakeholder not in nodes:
        errors.append(f"stakeholder_anchor references unknown node: {stakeholder}")

    for node_id, node in nodes.items():
        if not isinstance(node.get("name"), str) or not node["name"].strip():
            errors.append(f"{node_id}: node name is required")
        if not isinstance(node.get("type"), str) or not node["type"].strip():
            errors.append(f"{node_id}: ArchiMate element type is required")
        parent_id = node.get("parent_id")
        if parent_id is not None and parent_id not in nodes:
            errors.append(f"{node_id}: unknown parent_id {parent_id!r}")
        if parent_id == node_id:
            errors.append(f"{node_id}: node cannot be its own parent")

    for node_id in nodes:
        visited: set[str] = set()
        current = node_id
        while current in nodes and nodes[current].get("parent_id") is not None:
            if current in visited:
                errors.append(f"{node_id}: containment cycle detected")
                break
            visited.add(current)
            current = nodes[current]["parent_id"]

    for relation_id, relation in relationships.items():
        if not relation_id.startswith(RELATION_PREFIXES):
            errors.append(f"{relation_id}: unsupported stable relationship id prefix")
        source = relation.get("source")
        target = relation.get("target")
        if source == target:
            errors.append(f"{relation_id}: self-relationships do not satisfy connectivity")
        for endpoint_name, endpoint in (("source", source), ("target", target)):
            if endpoint not in nodes:
                errors.append(f"{relation_id}: unknown {endpoint_name} node {endpoint!r}")
        if relation.get("approval_status") != "approved":
            errors.append(f"{relation_id}: relationship is not operator-approved")
        relation_type = relation.get("type")
        if not isinstance(relation_type, str) or not relation_type:
            errors.append(f"{relation_id}: ArchiMate relationship type is required")
        meaning = relation.get("meaning")
        if not isinstance(meaning, str) or not meaning.strip():
            errors.append(f"{relation_id}: natural-language meaning is required")
        candidate = relation.get("archimate_candidate")
        if not isinstance(candidate, str) or not candidate.strip():
            errors.append(f"{relation_id}: ArchiMate candidate rationale is required")
        evidence = relation.get("evidence_refs")
        if not isinstance(evidence, list) or not evidence or not all(isinstance(item, str) and item for item in evidence):
            errors.append(f"{relation_id}: evidence_refs must contain at least one source identifier")
        elif not all(item.startswith(EVIDENCE_PREFIXES) for item in evidence):
            errors.append(f"{relation_id}: evidence_refs contain an unsupported identifier")
        else:
            has_operational = any(item.startswith(("OP-", "CON-")) for item in evidence)
            has_requirement = any(item.startswith("REQ-") for item in evidence)
            if relation_id.startswith("REL-OP-") and not has_operational:
                errors.append(f"{relation_id}: operational relationship requires OP-* or CON-* evidence")
            if relation_id.startswith("REL-COV-") and not (has_operational and has_requirement):
                errors.append(f"{relation_id}: coverage relationship requires both REQ-* and OP-*/CON-* evidence")
        visibility = relation.get("visibility")
        if visibility not in {"visible", "semantic-only"}:
            errors.append(f"{relation_id}: visibility must be visible or semantic-only")
        if visibility == "semantic-only" and relation.get("type") not in SEMANTIC_ONLY_TYPES:
            errors.append(f"{relation_id}: only Composition/Aggregation may use semantic-only nesting")
        ownership = relation.get("coverage_ownership")
        if relation_id.startswith("REL-COV-") and ownership not in OWNERSHIP_STATES:
            errors.append(f"{relation_id}: coverage_ownership must name one approved ownership state")
        if relation.get("type") == "Realization" and ownership in NON_DIRECT_OWNERSHIP:
            errors.append(f"{relation_id}: non-direct coverage cannot be a Realization")
        if relation_id.startswith("REL-COV-") and relation.get("type") == "Realization" and ownership != "Directly performed":
            errors.append(f"{relation_id}: coverage Realization requires Directly performed ownership")

    used_relationships: set[str] = set()
    for view in raw_views:
        if not isinstance(view, dict):
            errors.append("every view must be an object")
            continue
        view_id = view.get("id", "<unknown-view>")
        view_name = view.get("name")
        if not isinstance(view_name, str) or not view_name.strip():
            errors.append(f"{view_id}: view name is required")
        purpose = view.get("purpose")
        if not isinstance(purpose, str) or not purpose.strip():
            errors.append(f"{view_id}: view purpose is required")
        members = view.get("node_ids", [])
        edges = view.get("relationship_ids", [])
        if not isinstance(members, list) or not isinstance(edges, list):
            errors.append(f"{view_id}: node_ids and relationship_ids must be arrays")
            continue
        if len(members) != len(set(members)):
            errors.append(f"{view_id}: duplicate node membership")
        if len(edges) != len(set(edges)):
            errors.append(f"{view_id}: duplicate relationship membership")
        member_set = set(members)
        if stakeholder not in member_set:
            errors.append(f"{view_id}: stakeholder anchor is missing")
        unknown_members = sorted(member_set - nodes.keys())
        if unknown_members:
            errors.append(f"{view_id}: unknown nodes {unknown_members}")

        adjacency: dict[str, set[str]] = defaultdict(set)
        degrees = {node_id: 0 for node_id in member_set}
        for relation_id in edges:
            relation = relationships.get(relation_id)
            if relation is None:
                errors.append(f"{view_id}: unknown relationship {relation_id}")
                continue
            used_relationships.add(relation_id)
            source = relation.get("source")
            target = relation.get("target")
            if source not in member_set or target not in member_set:
                errors.append(f"{view_id}: {relation_id} has an endpoint outside the view")
                continue
            if relation.get("visibility") == "semantic-only":
                source_node = nodes.get(source, {})
                target_node = nodes.get(target, {})
                nested = target_node.get("parent_id") == source or source_node.get("parent_id") == target
                if not nested:
                    errors.append(f"{view_id}: {relation_id} is semantic-only without matching nesting")
            adjacency[source].add(target)
            adjacency[target].add(source)
            degrees[source] += 1
            degrees[target] += 1

        isolated = sorted(node_id for node_id, degree in degrees.items() if degree == 0)
        if isolated:
            errors.append(f"{view_id}: isolated elements {isolated}")

        components: list[list[str]] = []
        remaining = set(member_set)
        while remaining:
            start = min(remaining)
            queue: deque[str] = deque([start])
            component: set[str] = set()
            while queue:
                current = queue.popleft()
                if current in component:
                    continue
                component.add(current)
                queue.extend(adjacency[current] - component)
            remaining -= component
            components.append(sorted(component))
        if len(components) != 1:
            errors.append(f"{view_id}: expected one connected component, found {len(components)}: {components}")

        roots = [
            node_id
            for node_id in member_set
            if nodes.get(node_id, {}).get("parent_id") not in member_set
        ]
        if len(roots) > threshold:
            warnings.append(
                f"{view_id}: {len(roots)} root elements exceeds the advisory threshold of {threshold}; "
                "operator readability approval is required"
            )
            if view.get("readability_approval") != "approved":
                errors.append(
                    f"{view_id}: readability_approval must be 'approved' when root count exceeds {threshold}"
                )

        view_reports.append(
            {
                "id": view_id,
                "name": view_name,
                "node_count": len(member_set),
                "relationship_count": len(edges),
                "root_count": len(roots),
                "readability_approval_required": len(roots) > threshold,
                "isolated": isolated,
                "components": components,
            }
        )

    unused = sorted(relationships.keys() - used_relationships)
    if unused:
        errors.append(f"relationships unused by every view: {unused}")
    if not raw_views:
        errors.append("at least one view is required")

    return {"valid": not errors, "errors": errors, "warnings": warnings, "views": view_reports}


def validate_projection(manifest: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    """Compare a native or slide round-trip projection with the graph authority."""

    errors: list[str] = []
    technology = projection.get("technology")
    if technology not in PROJECTION_TECHNOLOGIES:
        errors.append(
            "projection technology must be one of " + ", ".join(sorted(PROJECTION_TECHNOLOGIES))
        )

    expected_views = {
        view.get("id"): view
        for view in manifest.get("views", [])
        if isinstance(view, dict) and isinstance(view.get("id"), str)
    }
    raw_projected_views = projection.get("views", [])
    if not isinstance(raw_projected_views, list):
        return {"valid": False, "errors": errors + ["projection views must be an array"]}
    projected_views = {
        view.get("id"): view
        for view in raw_projected_views
        if isinstance(view, dict) and isinstance(view.get("id"), str)
    }
    if len(projected_views) != len(raw_projected_views):
        errors.append("every projected view must have a unique non-empty id")

    missing_views = sorted(expected_views.keys() - projected_views.keys())
    extra_views = sorted(projected_views.keys() - expected_views.keys())
    if missing_views:
        errors.append(f"projection is missing views: {missing_views}")
    if extra_views:
        errors.append(f"projection has extra views: {extra_views}")

    for view_id in sorted(expected_views.keys() & projected_views.keys()):
        expected = expected_views[view_id]
        actual = projected_views[view_id]
        for field in ("node_ids", "relationship_ids"):
            actual_values = actual.get(field)
            if not isinstance(actual_values, list):
                errors.append(f"{view_id}: projected {field} must be an array")
                continue
            if len(actual_values) != len(set(actual_values)):
                errors.append(f"{view_id}: projected {field} contains duplicates")
            expected_set = set(expected.get(field, []))
            actual_set = set(actual_values)
            missing = sorted(expected_set - actual_set)
            extra = sorted(actual_set - expected_set)
            if missing:
                errors.append(f"{view_id}: projected {field} is missing {missing}")
            if extra:
                errors.append(f"{view_id}: projected {field} has extra {extra}")

    return {"valid": not errors, "errors": errors, "technology": technology}


def validate_view_after_removal(
    manifest: dict[str, Any], view_id: str, removed_node_ids: set[str]
) -> dict[str, Any]:
    """Validate one Step 12 view after removing only named GAP nodes and incident edges."""

    views = [
        view
        for view in manifest.get("views", [])
        if isinstance(view, dict) and view.get("id") == view_id
    ]
    if len(views) != 1:
        return {
            "valid": False,
            "errors": [f"expected exactly one source view named {view_id!r}"],
            "removed_node_ids": sorted(removed_node_ids),
        }
    source_view = views[0]
    source_members = set(source_view.get("node_ids", []))
    unknown_removals = sorted(removed_node_ids - source_members)
    if unknown_removals:
        return {
            "valid": False,
            "errors": [f"removed nodes are not members of {view_id}: {unknown_removals}"],
            "removed_node_ids": sorted(removed_node_ids),
        }

    nodes_by_id = {
        node.get("id"): node
        for node in manifest.get("nodes", [])
        if isinstance(node, dict) and isinstance(node.get("id"), str)
    }
    non_gap_removals = sorted(
        node_id
        for node_id in removed_node_ids
        if not node_id.startswith("GAP-")
        and str(nodes_by_id.get(node_id, {}).get("type", "")).lower() != "gap"
    )
    if non_gap_removals:
        return {
            "valid": False,
            "errors": [f"removal is restricted to structurally classified GAP nodes: {non_gap_removals}"],
            "removed_node_ids": sorted(removed_node_ids),
        }

    relationships = {
        relationship.get("id"): relationship
        for relationship in manifest.get("relationships", [])
        if isinstance(relationship, dict) and isinstance(relationship.get("id"), str)
    }
    retained_members = source_members - removed_node_ids
    retained_relationship_ids: list[str] = []
    removed_relationship_ids: list[str] = []
    for relationship_id in source_view.get("relationship_ids", []):
        relationship = relationships.get(relationship_id, {})
        if relationship.get("source") in removed_node_ids or relationship.get("target") in removed_node_ids:
            removed_relationship_ids.append(relationship_id)
        else:
            retained_relationship_ids.append(relationship_id)

    retained_nodes = [
        node
        for node in manifest.get("nodes", [])
        if isinstance(node, dict) and node.get("id") in retained_members
    ]
    retained_relationships = [
        relationships[relationship_id]
        for relationship_id in retained_relationship_ids
        if relationship_id in relationships
    ]
    filtered_view = {
        key: value
        for key, value in source_view.items()
        if key not in {"node_ids", "relationship_ids"}
    }
    filtered_view["node_ids"] = [
        node_id for node_id in source_view.get("node_ids", []) if node_id in retained_members
    ]
    filtered_view["relationship_ids"] = retained_relationship_ids
    filtered_manifest = {
        "schema_version": manifest.get("schema_version"),
        "root_warning_threshold": manifest.get("root_warning_threshold"),
        "stakeholder_anchor": manifest.get("stakeholder_anchor"),
        "nodes": retained_nodes,
        "relationships": retained_relationships,
        "views": [filtered_view],
    }
    report = validate_manifest(filtered_manifest)
    report.update(
        {
            "source_view_id": view_id,
            "removed_node_ids": sorted(removed_node_ids),
            "removed_relationship_ids": removed_relationship_ids,
            "retained_node_ids": filtered_view["node_ids"],
            "retained_relationship_ids": retained_relationship_ids,
        }
    )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to 7_view_graph.json")
    parser.add_argument(
        "--projection",
        type=Path,
        help="Optional native/slide round-trip projection to compare with the manifest",
    )
    parser.add_argument(
        "--remove-from-view",
        metavar="VIEW_ID",
        help="Validate a Step 12 filtered view after structural GAP removal",
    )
    parser.add_argument(
        "--remove-node",
        action="append",
        default=[],
        metavar="NODE_ID",
        help="Node to remove with its incident relationships; repeat as needed",
    )
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)], "warnings": [], "views": []}, indent=2))
        return 1
    if args.remove_from_view and args.projection is not None:
        print(json.dumps({"valid": False, "errors": ["projection and removal modes are mutually exclusive"]}, indent=2))
        return 1
    if args.remove_from_view:
        if not args.remove_node:
            print(json.dumps({"valid": False, "errors": ["--remove-from-view requires --remove-node"]}, indent=2))
            return 1
        report = validate_view_after_removal(data, args.remove_from_view, set(args.remove_node))
    else:
        if args.remove_node:
            print(json.dumps({"valid": False, "errors": ["--remove-node requires --remove-from-view"]}, indent=2))
            return 1
        report = validate_manifest(data)
    if args.projection is not None and report["valid"]:
        try:
            projection = json.loads(args.projection.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
            return 1
        report["projection"] = validate_projection(data, projection)
        if not report["projection"]["valid"]:
            report["valid"] = False
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
