#!/usr/bin/env python3
"""Generate the approved immutable DORA regulation overview baseline.

This baseline contains the regulation-wide legal core and only the approved
stakeholder--organization--legal-role context.  It deliberately contains no
operational systems, implementation claims, assessments, or gaps.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from pyArchimate import ArchiType, check_valid_relationship
from pyArchimate.model import Model


OUTPUT_PATH = Path(__file__).with_suffix(".archimate")
REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
TOOLS_DIRECTORY = REPOSITORY_ROOT / "Methodology" / "tools"
sys.path.insert(0, str(TOOLS_DIRECTORY))

from view_graph_validator import validate_manifest, validate_projection  # noqa: E402


VIEW_ID = "VIEW-DORA-OVERVIEW"
ROOT_ID = "REQ-DORA-RESILIENCE"
ROLE_ID = "ROLE-INFRA-CLOUD-DBA"
BANK_ID = "ORG-BANK"
LEGAL_ENTITY_ID = "ROLE-DORA-FINANCIAL-ENTITY"


def source_ref(anchor: str) -> str:
    """Make a graph-validator source reference while retaining the full anchor in descriptions."""

    token = re.sub(r"[^A-Za-z0-9]+", "-", anchor).strip("-")
    return f"SRC-DORA-{token}"


FAMILIES = [
    {
        "id": "FAM-DORA-SCOPE",
        "title": "DORA Scope and Proportion",
        "type": ArchiType.Constraint,
        "root_relation": "REL-COMP-001",
        "children": [
            ("OVR-001", "Apply DORA scope", ArchiType.Constraint, "Art. 2(1)", "Chap.I, Art.2, Paragraph 1", "REL-COMP-015"),
            ("OVR-002", "Scale ICT risk controls", ArchiType.Requirement, "Art. 4(1)", "Chap.I, Art.4, Paragraph 1", "REL-COMP-016"),
        ],
    },
    {
        "id": "FAM-ICT-GOVERNANCE",
        "title": "ICT Governance",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-002",
        "children": [
            ("OVR-003", "Govern ICT risk", ArchiType.Requirement, "Art. 5(1)", "Chap.II, Section I, Art.5, Paragraph 1", "REL-COMP-017"),
        ],
    },
    {
        "id": "FAM-ICT-RISK-FRAMEWORK",
        "title": "ICT Risk Framework",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-003",
        "children": [
            ("OVR-004", "Set ICT risk framework", ArchiType.Requirement, "Art. 6(1)", "Chap.II, Section II, Art.6, Paragraph 1", "REL-COMP-018"),
            ("OVR-005", "Set ICT control standards", ArchiType.Requirement, "Art. 15(1)", "Chap.II, Section II, Art.15, Paragraph 1", "REL-COMP-019"),
            ("OVR-006", "Use simplified framework", ArchiType.Constraint, "Art. 16(1)", "Chap.II, Section II, Art.16, Paragraph 1", "REL-COMP-020"),
        ],
    },
    {
        "id": "FAM-ICT-ASSETS-SYSTEMS",
        "title": "ICT Assets and Systems",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-004",
        "children": [
            ("OVR-007", "Maintain ICT systems", ArchiType.Requirement, "Art. 7(1)", "Chap.II, Section II, Art.7, Paragraph 1", "REL-COMP-021"),
            ("OVR-008", "Identify ICT assets", ArchiType.Requirement, "Art. 8(1)", "Chap.II, Section II, Art.8, Paragraph 1", "REL-COMP-022"),
        ],
    },
    {
        "id": "FAM-SECURITY-DETECTION",
        "title": "Security and Detection",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-005",
        "children": [
            ("OVR-009", "Protect ICT systems", ArchiType.Requirement, "Art. 9(1)", "Chap.II, Section II, Art.9, Paragraph 1", "REL-COMP-023"),
            ("OVR-010", "Detect ICT anomalies", ArchiType.Requirement, "Art. 10(1)", "Chap.II, Section II, Art.10, Paragraph 1", "REL-COMP-024"),
        ],
    },
    {
        "id": "FAM-CONTINUITY-RECOVERY",
        "title": "Continuity and Recovery",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-006",
        "children": [
            ("OVR-011", "Maintain ICT continuity", ArchiType.Requirement, "Art. 11(1)", "Chap.II, Section II, Art.11, Paragraph 1", "REL-COMP-025"),
            ("OVR-012", "Restore ICT systems", ArchiType.Requirement, "Art. 12(1)", "Chap.II, Section II, Art.12, Paragraph 1", "REL-COMP-026"),
        ],
    },
    {
        "id": "FAM-RESILIENCE-LEARNING",
        "title": "Resilience Learning",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-007",
        "children": [
            ("OVR-013", "Learn from ICT events", ArchiType.Requirement, "Art. 13(1)", "Chap.II, Section II, Art.13, Paragraph 1", "REL-COMP-027"),
            ("OVR-014", "Communicate ICT crises", ArchiType.Requirement, "Art. 14(1)", "Chap.II, Section II, Art.14, Paragraph 1", "REL-COMP-028"),
        ],
    },
    {
        "id": "FAM-ICT-INCIDENT-REPORTING",
        "title": "ICT Incident Reporting",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-008",
        "children": [
            ("OVR-015", "Manage ICT incidents", ArchiType.Requirement, "Art. 17(1)", "Chap.III, Art.17, Paragraph 1", "REL-COMP-029"),
            ("OVR-016", "Classify ICT incidents", ArchiType.Requirement, "Art. 18(1)", "Chap.III, Art.18, Paragraph 1", "REL-COMP-030"),
            ("OVR-017", "Report major incidents", ArchiType.Requirement, "Art. 19(1)", "Chap.III, Art.19, Paragraph 1", "REL-COMP-031"),
            ("OVR-018", "Set incident report rules", ArchiType.Requirement, "Art. 20(1)", "Chap.III, Art.20, Paragraph 1", "REL-COMP-032"),
            ("OVR-019", "Centralise ICT reports", ArchiType.Requirement, "Art. 21(1)", "Chap.III, Art.21, Paragraph 1", "REL-COMP-033"),
            ("OVR-020", "Give incident feedback", ArchiType.Requirement, "Art. 22(1)", "Chap.III, Art.22, Paragraph 1", "REL-COMP-034"),
            ("OVR-021", "Cover payment incidents", ArchiType.Requirement, "Art. 23(1)", "Chap.III, Art.23, Paragraph 1", "REL-COMP-035"),
        ],
    },
    {
        "id": "FAM-RESILIENCE-TESTING",
        "title": "Resilience Testing",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-009",
        "children": [
            ("OVR-022", "Run resilience tests", ArchiType.Requirement, "Art. 24(1)", "Chap.IV, Art.24, Paragraph 1", "REL-COMP-036"),
            ("OVR-023", "Perform baseline tests", ArchiType.Requirement, "Art. 25(1)", "Chap.IV, Art.25, Paragraph 1", "REL-COMP-037"),
            ("OVR-024", "Run threat-led tests", ArchiType.Requirement, "Art. 26(1)", "Chap.IV, Art.26, Paragraph 1", "REL-COMP-038"),
            ("OVR-025", "Use qualified testers", ArchiType.Requirement, "Art. 27(1)", "Chap.IV, Art.27, Paragraph 1", "REL-COMP-039"),
        ],
    },
    {
        "id": "FAM-THIRD-PARTY-ICT-RISK",
        "title": "Third-Party ICT Risk",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-010",
        "children": [
            ("OVR-026", "Manage provider risk", ArchiType.Requirement, "Art. 28(1)", "Chap.V, Section I, Art.28, Paragraph 1", "REL-COMP-040"),
            ("OVR-027", "Assess ICT concentration", ArchiType.Requirement, "Art. 29(1)", "Chap.V, Section I, Art.29, Paragraph 1", "REL-COMP-041"),
            ("OVR-028", "Set ICT contract terms", ArchiType.Requirement, "Art. 30(1)", "Chap.V, Section I, Art.30, Paragraph 1", "REL-COMP-042"),
        ],
    },
    {
        "id": "FAM-CRITICAL-PROVIDER-CONTROL",
        "title": "Critical Provider Control",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-011",
        "children": [
            ("OVR-029", "Set provider criticality", ArchiType.Requirement, "Art. 31(1)", "Chap.V, Section II, Art.31, Paragraph 1", "REL-COMP-043"),
            ("OVR-030", "Establish oversight forum", ArchiType.Requirement, "Art. 32(1)", "Chap.V, Section II, Art.32, Paragraph 1", "REL-COMP-044"),
            ("OVR-031", "Plan provider oversight", ArchiType.Requirement, "Art. 33(1)", "Chap.V, Section II, Art.33, Paragraph 1", "REL-COMP-045"),
            ("OVR-032", "Coordinate ICT oversight", ArchiType.Requirement, "Art. 34(1)", "Chap.V, Section II, Art.34, Paragraph 1", "REL-COMP-046"),
            ("OVR-033", "Exercise oversight powers", ArchiType.Requirement, "Art. 35(1)", "Chap.V, Section II, Art.35, Paragraph 1", "REL-COMP-047"),
            ("OVR-034", "Address non-EU oversight", ArchiType.Requirement, "Art. 36(1)", "Chap.V, Section II, Art.36, Paragraph 1", "REL-COMP-048"),
            ("OVR-035", "Obtain provider records", ArchiType.Requirement, "Art. 37(1)", "Chap.V, Section II, Art.37, Paragraph 1", "REL-COMP-049"),
            ("OVR-036", "Investigate ICT providers", ArchiType.Requirement, "Art. 38(1)", "Chap.V, Section II, Art.38, Paragraph 1", "REL-COMP-050"),
            ("OVR-037", "Inspect ICT providers", ArchiType.Requirement, "Art. 39(1)", "Chap.V, Section II, Art.39, Paragraph 1", "REL-COMP-051"),
            ("OVR-038", "Oversee ICT providers", ArchiType.Requirement, "Art. 40(1)", "Chap.V, Section II, Art.40, Paragraph 1", "REL-COMP-052"),
            ("OVR-039", "Set oversight standards", ArchiType.Requirement, "Art. 41(1)", "Chap.V, Section II, Art.41, Paragraph 1", "REL-COMP-053"),
            ("OVR-040", "Act on oversight findings", ArchiType.Requirement, "Art. 42(1)", "Chap.V, Section II, Art.42, Paragraph 1", "REL-COMP-054"),
            ("OVR-041", "Fund provider oversight", ArchiType.Requirement, "Art. 43(1)", "Chap.V, Section II, Art.43, Paragraph 1", "REL-COMP-055"),
            ("OVR-042", "Cooperate on oversight", ArchiType.Requirement, "Art. 44(1)", "Chap.V, Section II, Art.44, Paragraph 1", "REL-COMP-056"),
        ],
    },
    {
        "id": "FAM-THREAT-INFORMATION-SHARING",
        "title": "Cyber Threat Sharing",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-012",
        "children": [
            ("OVR-043", "Share threat intelligence", ArchiType.Requirement, "Art. 45(1)", "Chap.VI, Art.45, Paragraph 1", "REL-COMP-057"),
        ],
    },
    {
        "id": "FAM-SUPERVISORY-ENFORCEMENT",
        "title": "Supervisory Enforcement",
        "type": ArchiType.Requirement,
        "root_relation": "REL-COMP-013",
        "children": [
            ("OVR-044", "Set DORA authorities", ArchiType.Requirement, "Art. 46(1)", "Chap.VII, Art.46, Paragraph 1", "REL-COMP-058"),
            ("OVR-045", "Coordinate with NIS2", ArchiType.Requirement, "Art. 47(1)", "Chap.VII, Art.47, Paragraph 1", "REL-COMP-059"),
            ("OVR-046", "Coordinate authorities", ArchiType.Requirement, "Art. 48(1)", "Chap.VII, Art.48, Paragraph 1", "REL-COMP-060"),
            ("OVR-047", "Coordinate sector drills", ArchiType.Requirement, "Art. 49(1)", "Chap.VII, Art.49, Paragraph 1", "REL-COMP-061"),
            ("OVR-048", "Apply DORA remedies", ArchiType.Requirement, "Art. 50(1)", "Chap.VII, Art.50, Paragraph 1", "REL-COMP-062"),
            ("OVR-049", "Exercise remedy powers", ArchiType.Requirement, "Art. 51(1)", "Chap.VII, Art.51, Paragraph 1", "REL-COMP-063"),
            ("OVR-050", "Set criminal penalties", ArchiType.Constraint, "Art. 52(1)", "Chap.VII, Art.52, Paragraph 1", "REL-COMP-064"),
            ("OVR-051", "Notify enforcement rules", ArchiType.Requirement, "Art. 53(1)", "Chap.VII, Art.53, Paragraph 1", "REL-COMP-065"),
            ("OVR-052", "Publish DORA sanctions", ArchiType.Requirement, "Art. 54(1)", "Chap.VII, Art.54, Paragraph 1", "REL-COMP-066"),
            ("OVR-053", "Protect oversight secrecy", ArchiType.Constraint, "Art. 55(1)", "Chap.VII, Art.55, Paragraph 1", "REL-COMP-067"),
            ("OVR-054", "Protect supervisory data", ArchiType.Constraint, "Art. 56(1)", "Chap.VII, Art.56, Paragraph 1", "REL-COMP-068"),
        ],
    },
    {
        "id": "FAM-LEGAL-RULE-LIFECYCLE",
        "title": "Legal Rule Lifecycle",
        "type": ArchiType.Constraint,
        "root_relation": "REL-COMP-014",
        "children": [
            ("OVR-055", "Govern delegated powers", ArchiType.Constraint, "Art. 57(1)", "Chap.VIII, Art.57, Paragraph 1", "REL-COMP-069"),
            ("OVR-056", "Review DORA operation", ArchiType.Requirement, "Art. 58(1)", "Chap.IX, Section I, Art.58, Paragraph 1", "REL-COMP-070"),
            ("OVR-057", "Set DORA effective date", ArchiType.Constraint, "Art. 64(1)", "Chap.IX, Section II, Art.64, Paragraph 1", "REL-COMP-071"),
        ],
    },
]


def child_description(citation: str, anchor: str) -> str:
    return f"Source citation: {citation}\nLegal text IDs:\n- {anchor}"


def family_description(family: dict) -> str:
    rollup = "\n- ".join(child[4] for child in family["children"])
    return f"Legal text IDs (child roll-up):\n- {rollup}"


def build_manifest() -> dict:
    """Build the approved technology-neutral graph for pre-write validation."""

    root_rollup = [child[4] for family in FAMILIES for child in family["children"]]
    nodes = [
        {
            "id": ROLE_ID,
            "name": "Infra Eng & Cloud DBA",
            "type": "BusinessRole",
            "documentation": "Full approved role label: Infrastructure Engineer / Cloud Database Administrator.",
        },
        {"id": BANK_ID, "name": "Bank", "type": "BusinessActor", "documentation": "Operator-approved anonymized employing organization label."},
        {
            "id": LEGAL_ENTITY_ID,
            "name": "DORA financial entity",
            "type": "BusinessActor",
            "documentation": "Law-defined financial-entity role group; the stakeholder is not equated with this entity.",
        },
        {
            "id": ROOT_ID,
            "name": "DORA Resilience Framework",
            "type": "Requirement",
            "documentation": "Legal text IDs (child roll-up):\n- " + "\n- ".join(root_rollup),
        },
    ]
    relationships = [
        {
            "id": "REL-ROLE-001",
            "source": ROLE_ID,
            "target": BANK_ID,
            "type": "Association",
            "meaning": "works within",
            "archimate_candidate": "Business Role associated with its employing Business Actor.",
            "visibility": "visible",
            "evidence_refs": ["ROLE-STAKEHOLDER-ORGANIZATION"],
            "approval_status": "approved",
        },
        {
            "id": "REL-ROLE-002",
            "source": BANK_ID,
            "target": LEGAL_ENTITY_ID,
            "type": "Specialization",
            "meaning": "is a DORA-regulated credit institution",
            "archimate_candidate": "The Bank is a specialization of the DORA financial-entity role group.",
            "visibility": "visible",
            "evidence_refs": ["ROLE-ORGANIZATION-LEGAL-ENTITY"],
            "approval_status": "approved",
        },
        {
            "id": "REL-ROLE-003",
            "source": LEGAL_ENTITY_ID,
            "target": ROOT_ID,
            "type": "Association",
            "meaning": "is in scope of",
            "archimate_candidate": "The regulated entity is associated with the legal framework that applies to it.",
            "visibility": "visible",
            "evidence_refs": [source_ref("Chap.I, Art.1, Paragraph 1"), source_ref("Chap.I, Art.2, Paragraph 1, Point a")],
            "approval_status": "approved",
        },
    ]

    for family in FAMILIES:
        rollup = [source_ref(child[4]) for child in family["children"]]
        nodes.append(
            {
                "id": family["id"],
                "name": family["title"],
                "type": family["type"].value,
                "parent_id": ROOT_ID,
                "documentation": family_description(family),
            }
        )
        relationships.append(
            {
                "id": family["root_relation"],
                "source": ROOT_ID,
                "target": family["id"],
                "type": "Composition",
                "meaning": "contains the approved legal-control family",
                "archimate_candidate": "Requirement-family semantic containment backed by visual nesting.",
                "visibility": "semantic-only",
                "evidence_refs": rollup,
                "approval_status": "approved",
            }
        )
        for child_id, title, child_type, citation, anchor, relationship_id in family["children"]:
            nodes.append(
                {
                    "id": child_id,
                    "name": title,
                    "type": child_type.value,
                    "parent_id": family["id"],
                    "documentation": child_description(citation, anchor),
                }
            )
            relationships.append(
                {
                    "id": relationship_id,
                    "source": family["id"],
                    "target": child_id,
                    "type": "Composition",
                    "meaning": "contains the approved source-backed legal child",
                    "archimate_candidate": "Requirement-family semantic containment backed by visual nesting.",
                    "visibility": "semantic-only",
                    "evidence_refs": [source_ref(anchor)],
                    "approval_status": "approved",
                }
            )

    return {
        "schema_version": "1.0",
        "root_warning_threshold": 30,
        "stakeholder_anchor": ROLE_ID,
        "nodes": nodes,
        "relationships": relationships,
        "views": [
            {
                "id": VIEW_ID,
                "name": "DORA Regulation Overview",
                "purpose": "Immutable contextualized DORA legal-awareness baseline.",
                "node_ids": [node["id"] for node in nodes],
                "relationship_ids": [relationship["id"] for relationship in relationships],
            }
        ],
    }


GRAPH_MANIFEST = build_manifest()


def assert_title_lengths() -> None:
    too_long = [node["name"] for node in GRAPH_MANIFEST["nodes"] if len(node["name"]) > 25]
    if too_long:
        raise RuntimeError(f"Element titles exceed 25 characters: {too_long}")
    oversized = [family["title"] for family in FAMILIES if len(family["children"]) > 18]
    if oversized:
        raise RuntimeError(f"Families exceed 18 children: {oversized}")


def add_relation(
    model: Model,
    stable_id: str,
    relation_type: ArchiType,
    source,
    target,
    name: str,
    evidence: list[str],
    *,
    directed: bool = False,
):
    check_valid_relationship(relation_type, source.type, target.type, raise_flg=True)
    description = (
        f"Stable relationship ID: {stable_id}\n"
        f"Evidence references: {', '.join(evidence)}"
    )
    return model.add_relationship(
        relation_type,
        source,
        target,
        name=name,
        desc=description,
        is_directed=directed,
    )


def ensure_model_integrity(model: Model, stage: str) -> None:
    failures = {
        "invalid_relationships": model.check_invalid_relationships(),
        "invalid_nodes": model.check_invalid_nodes(),
        "invalid_connections": model.check_invalid_conn(),
    }
    failures = {name: value for name, value in failures.items() if value}
    if failures:
        raise RuntimeError(f"{stage} model integrity validation failed: {failures}")


def main() -> None:
    assert_title_lengths()
    graph_report = validate_manifest(GRAPH_MANIFEST)
    if not graph_report["valid"]:
        raise RuntimeError(f"Approved overview graph is invalid: {graph_report['errors']}")

    model = Model("DORA Regulation Overview Baseline")
    elements = {
        ROLE_ID: model.add(
            ArchiType.BusinessRole,
            "Infra Eng & Cloud DBA",
            desc="Full approved role label: Infrastructure Engineer / Cloud Database Administrator.",
        ),
        BANK_ID: model.add(
            ArchiType.BusinessActor,
            "Bank",
            desc="Operator-approved anonymized employing organization label.",
        ),
        LEGAL_ENTITY_ID: model.add(
            ArchiType.BusinessActor,
            "DORA financial entity",
            desc="Law-defined financial-entity role group; not the individual stakeholder.",
        ),
    }

    root_rollup = [child[4] for family in FAMILIES for child in family["children"]]
    elements[ROOT_ID] = model.add(
        ArchiType.Requirement,
        "DORA Resilience Framework",
        desc="Legal text IDs (child roll-up):\n- " + "\n- ".join(root_rollup),
    )

    for family in FAMILIES:
        elements[family["id"]] = model.add(
            family["type"],
            family["title"],
            desc=family_description(family),
        )
        for child_id, title, child_type, citation, anchor, _ in family["children"]:
            elements[child_id] = model.add(child_type, title, desc=child_description(citation, anchor))

    relationships = {}
    relationships["REL-ROLE-001"] = add_relation(
        model,
        "REL-ROLE-001",
        ArchiType.Association,
        elements[ROLE_ID],
        elements[BANK_ID],
        "works within",
        ["ROLE-STAKEHOLDER-ORGANIZATION"],
        directed=True,
    )
    relationships["REL-ROLE-002"] = add_relation(
        model,
        "REL-ROLE-002",
        ArchiType.Specialization,
        elements[BANK_ID],
        elements[LEGAL_ENTITY_ID],
        "is a DORA credit institution",
        ["ROLE-ORGANIZATION-LEGAL-ENTITY"],
        directed=True,
    )
    relationships["REL-ROLE-003"] = add_relation(
        model,
        "REL-ROLE-003",
        ArchiType.Association,
        elements[LEGAL_ENTITY_ID],
        elements[ROOT_ID],
        "is in scope of",
        ["Chap.I, Art.1, Paragraph 1", "Chap.I, Art.2, Paragraph 1, Point a"],
        directed=True,
    )

    for family in FAMILIES:
        model.add_child(elements[ROOT_ID].uuid, elements[family["id"]].uuid)
        relationships[family["root_relation"]] = add_relation(
            model,
            family["root_relation"],
            ArchiType.Composition,
            elements[ROOT_ID],
            elements[family["id"]],
            "contains",
            [child[4] for child in family["children"]],
        )
        for child_id, _, _, _, anchor, relationship_id in family["children"]:
            model.add_child(elements[family["id"]].uuid, elements[child_id].uuid)
            relationships[relationship_id] = add_relation(
                model,
                relationship_id,
                ArchiType.Composition,
                elements[family["id"]],
                elements[child_id],
                "contains",
                [anchor],
            )

    overview = model.add(ArchiType.View, "DORA Regulation Overview", folder="/Views/Overview")
    overview.add(elements[ROLE_ID], x=40, y=780, w=240, h=70)
    overview.add(elements[BANK_ID], x=340, y=780, w=180, h=70)
    overview.add(elements[LEGAL_ENTITY_ID], x=570, y=780, w=200, h=70)
    root_node = overview.add(elements[ROOT_ID], x=840, y=40, w=1680, h=1200)

    for family in FAMILIES:
        family_node = root_node.add(elements[family["id"]])
        for child_id, *_ in family["children"]:
            family_node.add(elements[child_id])
        family_node.resize(max_in_row=3 if len(family["children"]) >= 12 else 2)
    root_node.resize(max_in_row=3)

    for stable_id in ("REL-ROLE-001", "REL-ROLE-002", "REL-ROLE-003"):
        overview.add_connection(relationships[stable_id])

    ensure_model_integrity(model, "Pre-write")
    model.write(str(OUTPUT_PATH))

    round_trip = Model("DORA Overview Round Trip")
    round_trip.read(str(OUTPUT_PATH))
    ensure_model_integrity(round_trip, "Round-trip")

    round_trip_names = [element.name for element in round_trip.elements]
    expected_names = [node["name"] for node in GRAPH_MANIFEST["nodes"]]
    missing_names = sorted(set(expected_names) - set(round_trip_names))
    duplicate_names = sorted(name for name in set(expected_names) if round_trip_names.count(name) != 1)
    if missing_names or duplicate_names:
        raise RuntimeError(
            f"Round-trip element identity mismatch; missing={missing_names}, duplicates={duplicate_names}"
        )

    round_trip_descriptions = [relationship.desc or "" for relationship in round_trip.relationships]
    missing_relationships = [
        relationship_id
        for relationship_id in GRAPH_MANIFEST["views"][0]["relationship_ids"]
        if not any(f"Stable relationship ID: {relationship_id}" in description for description in round_trip_descriptions)
    ]
    if missing_relationships:
        raise RuntimeError(f"Round-trip relationship identity mismatch: {missing_relationships}")

    projection = {
        "technology": "pyarchimate",
        "views": [
            {
                "id": VIEW_ID,
                "node_ids": GRAPH_MANIFEST["views"][0]["node_ids"],
                "relationship_ids": GRAPH_MANIFEST["views"][0]["relationship_ids"],
            }
        ],
    }
    projection_report = validate_projection(GRAPH_MANIFEST, projection)
    if not projection_report["valid"]:
        raise RuntimeError(f"Round-trip projection mismatch: {projection_report['errors']}")

    print(
        json.dumps(
            {
                "output": str(OUTPUT_PATH),
                "node_count": len(GRAPH_MANIFEST["nodes"]),
                "relationship_count": len(GRAPH_MANIFEST["relationships"]),
                "graph": graph_report["views"][0],
                "projection": projection_report,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
