#!/usr/bin/env python3
"""Create the approved immutable DORA View 0 baseline.

This reproducible pyArchimate source holds only the approved legal core and
stakeholder/legal-role chain. It makes no operational, compliance, or gap claim.
"""
from __future__ import annotations

from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from pyArchimate import ArchiType, Model, check_valid_relationship

LAW = "Regulation (EU) 2022/2554 (DORA); CELEX 32022R2554"
OUTPUT_PATH = Path(__file__).with_suffix(".archimate")

FAMILIES = [
    [
        "Proportionate DORA Use",
        "REL-ROLE-003",
        [
            [
                "Scale ICT Rules",
                [
                    "Chap.I, Art.4, Paragraph 1"
                ]
            ],
            [
                "Scale Resilience Rules",
                [
                    "Chap.I, Art.4, Paragraph 2"
                ]
            ]
        ]
    ],
    [
        "ICT Risk Governance",
        "REL-ROLE-004",
        [
            [
                "Governance Controls",
                [
                    "Chap.II, Section I, Art.5, Paragraph 1"
                ]
            ],
            [
                "Management ICT Ownership",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point a"
                ]
            ],
            [
                "Data Protection Policy",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point b"
                ]
            ],
            [
                "ICT Role Coordination",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point c"
                ]
            ],
            [
                "Resilience Strategy",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point d"
                ]
            ],
            [
                "Continuity Plan Oversight",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point e"
                ]
            ],
            [
                "ICT Audit Oversight",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point f"
                ]
            ],
            [
                "Resilience Resources",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point g"
                ]
            ],
            [
                "Provider Policy Oversight",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point h"
                ]
            ],
            [
                "Provider Risk Reporting",
                [
                    "Chap.II, Section I, Art.5, Paragraph 2, Sub-Paragraph 1, Point i"
                ]
            ],
            [
                "Third-Party Role",
                [
                    "Chap.II, Section I, Art.5, Paragraph 3"
                ]
            ],
            [
                "Management ICT Training",
                [
                    "Chap.II, Section I, Art.5, Paragraph 4"
                ]
            ]
        ]
    ],
    [
        "ICT Risk Framework",
        "REL-ROLE-005",
        [
            [
                "Document ICT Framework",
                [
                    "Chap.II, Section II, Art.6, Paragraph 1"
                ]
            ],
            [
                "Protect ICT Assets",
                [
                    "Chap.II, Section II, Art.6, Paragraph 2"
                ]
            ],
            [
                "Mitigate ICT Risk",
                [
                    "Chap.II, Section II, Art.6, Paragraph 3"
                ]
            ],
            [
                "Provide ICT Risk Data",
                [
                    "Chap.II, Section II, Art.6, Paragraph 3"
                ]
            ],
            [
                "Independent ICT Control",
                [
                    "Chap.II, Section II, Art.6, Paragraph 4"
                ]
            ],
            [
                "Separate Controls",
                [
                    "Chap.II, Section II, Art.6, Paragraph 4"
                ]
            ],
            [
                "Review ICT Framework",
                [
                    "Chap.II, Section II, Art.6, Paragraph 5"
                ]
            ],
            [
                "Improve ICT Framework",
                [
                    "Chap.II, Section II, Art.6, Paragraph 5"
                ]
            ],
            [
                "Provide Review Report",
                [
                    "Chap.II, Section II, Art.6, Paragraph 5"
                ]
            ],
            [
                "Audit ICT Framework",
                [
                    "Chap.II, Section II, Art.6, Paragraph 6"
                ]
            ],
            [
                "Remediate Audit Findings",
                [
                    "Chap.II, Section II, Art.6, Paragraph 7"
                ]
            ],
            [
                "Retain Outsourcing Duty",
                [
                    "Chap.II, Section II, Art.6, Paragraph 10"
                ]
            ]
        ]
    ],
    [
        "ICT Resilience Strategy",
        "REL-ROLE-006",
        [
            [
                "Align Strategy",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point a"
                ]
            ],
            [
                "Set ICT Risk Tolerance",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point b"
                ]
            ],
            [
                "Set Security Objectives",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point c"
                ]
            ],
            [
                "Maintain ICT Architecture",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point d"
                ]
            ],
            [
                "Define Incident Defences",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point e"
                ]
            ],
            [
                "Evidence Resilience State",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point f"
                ]
            ],
            [
                "Run Resilience Tests",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point g"
                ]
            ],
            [
                "Plan Incident Disclosure",
                [
                    "Chap.II, Section II, Art.6, Paragraph 8, Point h"
                ]
            ]
        ]
    ],
    [
        "Secure ICT Operations",
        "REL-ROLE-007",
        [
            [
                "Maintain Reliable Systems",
                [
                    "Chap.II, Section II, Art.7, Paragraph 1"
                ]
            ],
            [
                "Identify ICT Assets",
                [
                    "Chap.II, Section II, Art.8, Paragraph 1"
                ]
            ],
            [
                "Assess ICT Risk",
                [
                    "Chap.II, Section II, Art.8, Paragraph 2"
                ]
            ],
            [
                "Map Provider Dependencies",
                [
                    "Chap.II, Section II, Art.8, Paragraph 5"
                ]
            ],
            [
                "Monitor ICT Security",
                [
                    "Chap.II, Section II, Art.9, Paragraph 1"
                ]
            ],
            [
                "Protect Systems and Data",
                [
                    "Chap.II, Section II, Art.9, Paragraph 2"
                ]
            ],
            [
                "Manage Secure Access",
                [
                    "Chap.II, Section II, Art.9, Paragraph 4, Point c"
                ]
            ],
            [
                "Control ICT Changes",
                [
                    "Chap.II, Section II, Art.9, Paragraph 4, Point e"
                ]
            ]
        ]
    ],
    [
        "Detect and Recover",
        "REL-ROLE-008",
        [
            [
                "Detect ICT Problems",
                [
                    "Chap.II, Section II, Art.10, Paragraph 1"
                ]
            ],
            [
                "Respond to Incidents",
                [
                    "Chap.II, Section II, Art.11, Paragraph 2, Point b"
                ]
            ],
            [
                "Maintain Continuity Plans",
                [
                    "Chap.II, Section II, Art.11, Paragraph 1"
                ]
            ],
            [
                "Assess Disruption Impact",
                [
                    "Chap.II, Section II, Art.11, Paragraph 2, Point d",
                    "Chap.II, Section II, Art.11, Paragraph 5"
                ]
            ],
            [
                "Test Recovery Plans",
                [
                    "Chap.II, Section II, Art.11, Paragraph 6, Point a"
                ]
            ],
            [
                "Manage Crisis Information",
                [
                    "Chap.II, Section II, Art.11, Paragraph 2, Point e"
                ]
            ],
            [
                "Backup and Restore Data",
                [
                    "Chap.II, Section II, Art.12, Paragraph 1, Point a",
                    "Chap.II, Section II, Art.12, Paragraph 1, Point b"
                ]
            ],
            [
                "Protect Recovery Data",
                [
                    "Chap.II, Section II, Art.12, Paragraph 4"
                ]
            ]
        ]
    ],
    [
        "ICT Learning and Response",
        "REL-ROLE-009",
        [
            [
                "Gather Threat Information",
                [
                    "Chap.II, Section II, Art.13, Paragraph 1"
                ]
            ],
            [
                "Review Major Incidents",
                [
                    "Chap.II, Section II, Art.13, Paragraph 2"
                ]
            ],
            [
                "Check Incident Response",
                [
                    "Chap.II, Section II, Art.13, Paragraph 2, Sub-Paragraph 2"
                ]
            ],
            [
                "Apply Incident Lessons",
                [
                    "Chap.II, Section II, Art.13, Paragraph 3"
                ]
            ],
            [
                "Monitor ICT Risk Trends",
                [
                    "Chap.II, Section II, Art.13, Paragraph 4"
                ]
            ],
            [
                "Report to Management",
                [
                    "Chap.II, Section II, Art.13, Paragraph 5"
                ]
            ],
            [
                "Train Staff and Leaders",
                [
                    "Chap.II, Section II, Art.13, Paragraph 6"
                ]
            ],
            [
                "Track Technology Change",
                [
                    "Chap.II, Section II, Art.13, Paragraph 7"
                ]
            ],
            [
                "Plan Crisis Disclosure",
                [
                    "Chap.II, Section II, Art.14, Paragraph 1"
                ]
            ],
            [
                "Set Comms Policies",
                [
                    "Chap.II, Section II, Art.14, Paragraph 2"
                ]
            ],
            [
                "Assign Incident Contact",
                [
                    "Chap.II, Section II, Art.14, Paragraph 3"
                ]
            ]
        ]
    ],
    [
        "Incident Management",
        "REL-ROLE-010",
        [
            [
                "Manage ICT Incidents",
                [
                    "Chap.III, Art.17, Paragraph 1"
                ]
            ],
            [
                "Record Incident Lessons",
                [
                    "Chap.III, Art.17, Paragraph 2"
                ]
            ],
            [
                "Use Incident Warnings",
                [
                    "Chap.III, Art.17, Paragraph 3, Point a"
                ]
            ],
            [
                "Classify Incidents",
                [
                    "Chap.III, Art.17, Paragraph 3, Point b",
                    "Chap.III, Art.18, Paragraph 1"
                ]
            ],
            [
                "Classify Cyber Threats",
                [
                    "Chap.III, Art.18, Paragraph 2"
                ]
            ],
            [
                "Assign Incident Roles",
                [
                    "Chap.III, Art.17, Paragraph 3, Point c"
                ]
            ],
            [
                "Report to Management",
                [
                    "Chap.III, Art.17, Paragraph 3, Point e"
                ]
            ],
            [
                "Restore Secure Services",
                [
                    "Chap.III, Art.17, Paragraph 3, Point f"
                ]
            ],
            [
                "Report Major Incidents",
                [
                    "Chap.III, Art.19, Paragraph 1"
                ]
            ],
            [
                "Inform Affected Clients",
                [
                    "Chap.III, Art.19, Paragraph 3"
                ]
            ],
            [
                "Retain Reporting Duty",
                [
                    "Chap.III, Art.19, Paragraph 5"
                ]
            ],
            [
                "Handle Payment Incidents",
                [
                    "Chap.III, Art.23, Paragraph 1"
                ]
            ]
        ]
    ],
    [
        "Resilience Testing",
        "REL-ROLE-011",
        [
            [
                "Maintain Test Programme",
                [
                    "Chap.IV, Art.24, Paragraph 1"
                ]
            ],
            [
                "Use Diverse Test Methods",
                [
                    "Chap.IV, Art.24, Paragraph 2",
                    "Chap.IV, Art.25, Paragraph 1"
                ]
            ],
            [
                "Use Independent Testing",
                [
                    "Chap.IV, Art.24, Paragraph 4"
                ]
            ],
            [
                "Fix Test Findings",
                [
                    "Chap.IV, Art.24, Paragraph 5"
                ]
            ],
            [
                "Test Critical Systems",
                [
                    "Chap.IV, Art.24, Paragraph 6"
                ]
            ],
            [
                "Perform Required TLPT",
                [
                    "Chap.IV, Art.26, Paragraph 1"
                ]
            ],
            [
                "Scope Critical Functions",
                [
                    "Chap.IV, Art.26, Paragraph 2"
                ]
            ],
            [
                "Include Cloud Providers",
                [
                    "Chap.IV, Art.26, Paragraph 3"
                ]
            ],
            [
                "Control TLPT Effects",
                [
                    "Chap.IV, Art.26, Paragraph 5"
                ]
            ],
            [
                "Report TLPT Results",
                [
                    "Chap.IV, Art.26, Paragraph 6",
                    "Chap.IV, Art.26, Paragraph 7"
                ]
            ],
            [
                "Use Qualified Testers",
                [
                    "Chap.IV, Art.27, Paragraph 1"
                ]
            ],
            [
                "Manage Tester Contracts",
                [
                    "Chap.IV, Art.26, Paragraph 8",
                    "Chap.IV, Art.27, Paragraph 2"
                ]
            ]
        ]
    ],
    [
        "ICT Third-Party Risk",
        "REL-ROLE-012",
        [
            [
                "Manage Provider Risk",
                [
                    "Chap.V, Section I, Art.28, Paragraph 1"
                ]
            ],
            [
                "Retain DORA Duty",
                [
                    "Chap.V, Section I, Art.28, Paragraph 1, Point a"
                ]
            ],
            [
                "Assess Dependencies",
                [
                    "Chap.V, Section I, Art.28, Paragraph 1, Point b"
                ]
            ],
            [
                "Maintain Provider Policy",
                [
                    "Chap.V, Section I, Art.28, Paragraph 2"
                ]
            ],
            [
                "Maintain Contract Log",
                [
                    "Chap.V, Section I, Art.28, Paragraph 3"
                ]
            ],
            [
                "Assess Provider Contracts",
                [
                    "Chap.V, Section I, Art.28, Paragraph 4"
                ]
            ],
            [
                "Use Secure Providers",
                [
                    "Chap.V, Section I, Art.28, Paragraph 5"
                ]
            ],
            [
                "Audit Provider Services",
                [
                    "Chap.V, Section I, Art.28, Paragraph 6"
                ]
            ],
            [
                "Keep Termination Rights",
                [
                    "Chap.V, Section I, Art.28, Paragraph 7"
                ]
            ],
            [
                "Maintain Exit Strategies",
                [
                    "Chap.V, Section I, Art.28, Paragraph 8"
                ]
            ],
            [
                "Manage Concentration Risk",
                [
                    "Chap.V, Section I, Art.29, Paragraph 1"
                ]
            ],
            [
                "Manage Subcontract Risk",
                [
                    "Chap.V, Section I, Art.29, Paragraph 2"
                ]
            ],
            [
                "Set Contract Terms",
                [
                    "Chap.V, Section I, Art.30, Paragraph 1"
                ]
            ],
            [
                "Specify Provider Services",
                [
                    "Chap.V, Section I, Art.30, Paragraph 2, Point a"
                ]
            ],
            [
                "Protect Data Recovery",
                [
                    "Chap.V, Section I, Art.30, Paragraph 2, Point d"
                ]
            ],
            [
                "Require Provider Help",
                [
                    "Chap.V, Section I, Art.30, Paragraph 2, Point e"
                ]
            ],
            [
                "Monitor Critical Services",
                [
                    "Chap.V, Section I, Art.30, Paragraph 3, Point a"
                ]
            ],
            [
                "Plan Service Transition",
                [
                    "Chap.V, Section I, Art.30, Paragraph 3, Point f"
                ]
            ]
        ]
    ],
    [
        "Critical ICT Oversight",
        "REL-ROLE-013",
        [
            [
                "Name Critical Providers",
                [
                    "Chap.V, Section II, Art.31, Paragraph 1"
                ]
            ],
            [
                "Notify Provider Status",
                [
                    "Chap.V, Section II, Art.31, Paragraph 5"
                ]
            ],
            [
                "Use EU Subsidiary",
                [
                    "Chap.V, Section II, Art.31, Paragraph 12"
                ]
            ],
            [
                "Coordinate Oversight",
                [
                    "Chap.V, Section II, Art.32, Paragraph 1"
                ]
            ],
            [
                "Oversee Provider Risk",
                [
                    "Chap.V, Section II, Art.33, Paragraph 3"
                ]
            ],
            [
                "Investigate Providers",
                [
                    "Chap.V, Section II, Art.35, Paragraph 1"
                ]
            ],
            [
                "Issue Recommendations",
                [
                    "Chap.V, Section II, Art.35, Paragraph 2"
                ]
            ],
            [
                "Follow Oversight Findings",
                [
                    "Chap.V, Section II, Art.42, Paragraph 3"
                ]
            ],
            [
                "Adjust Contracts",
                [
                    "Chap.V, Section II, Art.42, Paragraph 8"
                ]
            ],
            [
                "Require Cooperation",
                [
                    "Chap.V, Section II, Art.42, Paragraph 9"
                ]
            ],
            [
                "Fund Oversight",
                [
                    "Chap.V, Section II, Art.43, Paragraph 1"
                ]
            ],
            [
                "Coordinate Globally",
                [
                    "Chap.V, Section II, Art.44, Paragraph 1"
                ]
            ]
        ]
    ],
    [
        "Cyber Threat Sharing",
        "REL-ROLE-014",
        [
            [
                "Share Threat Intelligence",
                [
                    "Chap.VI, Art.45, Paragraph 1, Point a"
                ]
            ],
            [
                "Use Trusted Communities",
                [
                    "Chap.VI, Art.45, Paragraph 1, Point b"
                ]
            ],
            [
                "Protect Shared Data",
                [
                    "Chap.VI, Art.45, Paragraph 1, Point c"
                ]
            ],
            [
                "Set Participation Rules",
                [
                    "Chap.VI, Art.45, Paragraph 2"
                ]
            ],
            [
                "Notify Membership Changes",
                [
                    "Chap.VI, Art.45, Paragraph 3"
                ]
            ]
        ]
    ],
    [
        "DORA Supervision",
        "REL-ROLE-015",
        [
            [
                "Supervise Institutions",
                [
                    "Chap.VII, Art.46, Paragraph 1, Point a"
                ]
            ],
            [
                "Coordinate Supervision",
                [
                    "Chap.VII, Art.47, Paragraph 1",
                    "Chap.VII, Art.48, Paragraph 1"
                ]
            ],
            [
                "Run Sector Exercises",
                [
                    "Chap.VII, Art.49, Paragraph 1"
                ]
            ],
            [
                "Investigate DORA Duties",
                [
                    "Chap.VII, Art.50, Paragraph 1"
                ]
            ],
            [
                "Order DORA Remediation",
                [
                    "Chap.VII, Art.50, Paragraph 2, Point c"
                ]
            ],
            [
                "Set DORA Penalties",
                [
                    "Chap.VII, Art.50, Paragraph 3",
                    "Chap.VII, Art.51, Paragraph 1"
                ]
            ],
            [
                "Coordinate Enforcement",
                [
                    "Chap.VII, Art.52, Paragraph 1"
                ]
            ],
            [
                "Notify National Rules",
                [
                    "Chap.VII, Art.53, Paragraph 1"
                ]
            ],
            [
                "Publish Final Penalties",
                [
                    "Chap.VII, Art.54, Paragraph 1"
                ]
            ],
            [
                "Protect Supervisory Info",
                [
                    "Chap.VII, Art.55, Paragraph 1"
                ]
            ],
            [
                "Protect Supervisory Data",
                [
                    "Chap.VII, Art.56, Paragraph 1"
                ]
            ]
        ]
    ],
    [
        "DORA Legal Lifecycle",
        "REL-ROLE-016",
        [
            [
                "Maintain Delegated Rules",
                [
                    "Chap.VIII, Art.57, Paragraph 1"
                ]
            ],
            [
                "Review DORA Operation",
                [
                    "Chap.IX, Section I, Art.58, Paragraph 1"
                ]
            ],
            [
                "Apply DORA Requirements",
                [
                    "Chap.IX, Section II, Art.64, Paragraph 1"
                ]
            ]
        ]
    ]
]

def stable_id(key: str) -> str:
    return str(uuid5(NAMESPACE_URL, f"dora-view-0/{key}"))


def ordered_union(children) -> tuple[str, ...]:
    return tuple(dict.fromkeys(anchor for _, anchors in children for anchor in anchors))


def legal_text(ids) -> str:
    return "\n".join(f"- {anchor}" for anchor in ids)


def relation_description(relationship_id, source, target, evidence) -> str:
    return (
        f"Relationship ID: {relationship_id}\n"
        f"Endpoints: {source} -> {target}\n"
        f"Direction: {source} to {target}\n"
        f"Evidence: {evidence}\n"
        "Operator status: approved."
    )


def add_checked_relationship(model, relationship_id, rel_type, source, target, name, evidence):
    check_valid_relationship(rel_type, source.type, target.type, raise_flg=True)
    return model.add_relationship(
        rel_type,
        source,
        target,
        uuid=stable_id(relationship_id),
        name=name,
        desc=relation_description(relationship_id, source.name, target.name, evidence),
        is_directed=True if rel_type == ArchiType.Association else None,
    )


def assert_title_purity() -> None:
    visible_titles = (
        "Back-end Developer",
        "Employer Bank",
        "Credit Institution",
        *(family for family, _, _ in FAMILIES),
        *(title for _, _, children in FAMILIES for title, _ in children),
    )
    invalid = [
        title
        for title in visible_titles
        if len(title) > 25 or "[" in title or "]" in title or "Art." in title
    ]
    if invalid:
        raise ValueError(f"Visible title-purity violation: {invalid}")


def build_model() -> Model:
    assert_title_purity()
    model = Model(
        "DORA Regulation Overview",
        uuid=stable_id("model"),
        desc=(
            f"Immutable legal baseline for {LAW}.\n"
            "Approved scope: legal requirement core and stakeholder/legal-role "
            "chain only. No operational implementation, compliance conclusion, "
            "or gap is represented."
        ),
    )
    view = model.add(
        ArchiType.View,
        "DORA Overview",
        uuid=stable_id("view"),
        desc=(
            "View 0 baseline. Legal identifiers are documentation fields and "
            "intentionally excluded from visible labels."
        ),
        folder="/Views/Overview",
    )

    stakeholder = model.add(
        ArchiType.BusinessRole,
        "Back-end Developer",
        uuid=stable_id("stakeholder"),
        desc="Approved stakeholder anchor; not the regulated entity.",
        folder="/Business/Stakeholders",
    )
    employer = model.add(
        ArchiType.BusinessActor,
        "Employer Bank",
        uuid=stable_id("employer"),
        desc=(
            "Approved employing organisation: a major private bank whose platform "
            "supports DORA critical or important functions."
        ),
        folder="/Business/Organisation",
    )
    credit_institution = model.add(
        ArchiType.BusinessActor,
        "Credit Institution",
        uuid=stable_id("credit-institution"),
        desc=(
            "Law-defined entity group placed through the employer; not a "
            "classification of the individual stakeholder."
        ),
        folder="/Business/Legal Role",
    )

    stakeholder_node = view.add(stakeholder, 40, 40, 170, 55)
    employer_node = view.add(employer, 280, 40, 170, 55)
    credit_node = view.add(credit_institution, 520, 40, 190, 55)

    assignment = add_checked_relationship(
        model, "REL-ROLE-001", ArchiType.Assignment, employer, stakeholder,
        "assigned by", "Approved stakeholder legal-role placement.",
    )
    specialization = add_checked_relationship(
        model, "REL-ROLE-002", ArchiType.Specialization, employer, credit_institution,
        "specializes as",
        "Approved stakeholder legal-role placement: employer is a credit institution.",
    )
    view.add_connection(assignment, employer_node, stakeholder_node)
    view.add_connection(specialization, employer_node, credit_node)

    family_nodes = []
    associations = []
    composition_count = 0
    for family_index, (family_title, role_relationship_id, children) in enumerate(FAMILIES):
        anchors = ordered_union(children)
        family = model.add(
            ArchiType.Requirement,
            family_title,
            uuid=stable_id(f"family/{family_index + 1}"),
            desc=(
                "Approved DORA requirement family.\n"
                "Direct legal-text ID roll-up, ordered from child requirements:\n"
                f"{legal_text(anchors)}"
            ),
            folder="/Motivation/DORA Requirement Families",
        )
        column, row = family_index % 2, family_index // 2
        family_node = view.add(family, 40 + column * 620, 170 + row * 500, 430, 100)
        family_nodes.append(family_node)
        associations.append(
            add_checked_relationship(
                model, role_relationship_id, ArchiType.Association,
                credit_institution, family, "must apply",
                "Approved View 0 legal-role chain and requirement-family gate.",
            )
        )

        for child_index, (child_title, child_anchors) in enumerate(children):
            child = model.add(
                ArchiType.Requirement,
                child_title,
                uuid=stable_id(f"family/{family_index + 1}/child/{child_index + 1}"),
                desc=(
                    "Approved granular DORA requirement.\n"
                    "Verified direct legal-text IDs:\n"
                    f"{legal_text(child_anchors)}"
                ),
                folder="/Motivation/DORA Requirements",
            )
            composition_count += 1
            composition_id = f"REL-COMP-{composition_count:03d}"
            add_checked_relationship(
                model, composition_id, ArchiType.Composition, family, child,
                "contains",
                "Approved requirement-family containment; represented by visual nesting.",
            )
            family_node.add(child, 0, 0, 120, 55)

        family_node.resize(
            max_in_row=3 if len(children) > 11 else 2,
            keep_kids_size=True, w=120, h=55, gap_x=20, gap_y=20,
        )

    for family_node, association in zip(family_nodes, associations, strict=True):
        view.add_connection(association, credit_node, family_node)

    if composition_count != 134:
        raise ValueError(f"Expected 134 composition relationships, found {composition_count}.")
    invalid_relationships = model.check_invalid_relationships()
    if invalid_relationships:
        raise ValueError(f"Invalid ArchiMate relationships: {invalid_relationships}")
    return model


def main() -> None:
    model = build_model()
    model.write(str(OUTPUT_PATH))

    round_trip = Model("DORA Overview Round Trip")
    round_trip.read(str(OUTPUT_PATH))
    expected_elements = 3 + len(FAMILIES) + sum(len(children) for _, _, children in FAMILIES)
    expected_relationships = 2 + len(FAMILIES) + 134
    if len(round_trip.elems_dict) != expected_elements:
        raise ValueError(
            f"Round-trip element count mismatch: {len(round_trip.elems_dict)} != {expected_elements}"
        )
    if len(round_trip.rels_dict) != expected_relationships:
        raise ValueError(
            f"Round-trip relationship count mismatch: {len(round_trip.rels_dict)} != {expected_relationships}"
        )
    if len(round_trip.views_dict) != 1:
        raise ValueError(f"Round-trip view count mismatch: {len(round_trip.views_dict)} != 1")
    print(
        f"Wrote {OUTPUT_PATH.name}: {expected_elements} elements, "
        f"{expected_relationships} relationships, 1 view."
    )


if __name__ == "__main__":
    main()
