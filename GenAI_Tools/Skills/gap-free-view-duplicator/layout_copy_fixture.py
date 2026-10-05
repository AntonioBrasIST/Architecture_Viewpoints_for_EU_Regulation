"""Disposable pyArchimate fixture for Step 12 exact-layout copying.

Run with ``python3 layout_copy_fixture.py``. It creates all models in a
temporary directory, then proves that removing a GAP child and GAP root leaves
the surviving visual geometry and retained connection bendpoints unchanged.
"""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyArchimate import ArchiType, Point, check_valid_relationship
from pyArchimate.model import Model


NODE_STYLE_FIELDS = (
    "fill_color",
    "line_color",
    "font_color",
    "font_name",
    "font_size",
    "text_alignment",
    "text_position",
    "opacity",
    "border_type",
    "gradient",
    "icon_color",
    "lc_opacity",
)
CONNECTION_STYLE_FIELDS = (
    "line_color",
    "line_width",
    "font_color",
    "font_name",
    "font_size",
    "show_label",
    "text_position",
)


def relate(model, relationship_type, source, target, **kwargs):
    check_valid_relationship(relationship_type, source.type, target.type, raise_flg=True)
    return model.add_relationship(relationship_type, source, target, **kwargs)


def copy_style(source, target, fields):
    for field in fields:
        setattr(target, field, getattr(source, field))


def clone_node(parent, source_node, element_map, node_map):
    """Copy a visual node without any layout, sizing, or routing operation."""
    clone = parent.add(
        element_map[source_node.ref],
        x=source_node.x,
        y=source_node.y,
        w=source_node.w,
        h=source_node.h,
        node_type=source_node.cat,
        label=source_node.label,
    )
    copy_style(source_node, clone, NODE_STYLE_FIELDS)
    node_map[source_node.uuid] = clone
    for child in source_node.nodes:
        if child.ref in element_map:
            clone_node(clone, child, element_map, node_map)
    return clone


def geometry(node):
    return (node.x, node.y, node.w, node.h, node.cat, node.label)


def assert_matching_nodes(source_node, derived_node, gap_ids):
    assert geometry(source_node) == geometry(derived_node)
    for field in NODE_STYLE_FIELDS:
        assert getattr(source_node, field) == getattr(derived_node, field)
    retained_children = [child for child in source_node.nodes if child.ref not in gap_ids]
    assert len(retained_children) == len(derived_node.nodes)
    for source_child, derived_child in zip(retained_children, derived_node.nodes):
        assert_matching_nodes(source_child, derived_child, gap_ids)


def build_source():
    model = Model("Layout Copy Fixture")
    actor = model.add(ArchiType.BusinessActor, "Delivery Lead")
    process = model.add(ArchiType.BusinessProcess, "Release Review")
    family = model.add(ArchiType.Requirement, "Release Controls")
    control = model.add(ArchiType.Requirement, "Review Evidence")
    gap_child = model.add(ArchiType.Gap, "Missing Approval")
    gap_root = model.add(ArchiType.Gap, "Missing Escalation")

    retained = relate(model, ArchiType.Assignment, actor, process, name="performs")
    relate(model, ArchiType.Composition, family, control, name="contains")
    relate(model, ArchiType.Association, gap_child, family, name="blocks")
    relate(model, ArchiType.Association, gap_root, process, name="blocks")

    overview = model.add(ArchiType.View, "View 0")
    overview.add(family, x=40, y=40, w=280, h=160)

    view = model.add(ArchiType.View, "Stakeholder View")
    actor_node = view.add(actor, x=20, y=310, w=210, h=65)
    actor_node.fill_color = "#DDEBF7"
    process_node = view.add(process, x=20, y=420, w=210, h=65)
    process_node.fill_color = "#FFF2CC"
    family_node = view.add(family, x=340, y=40, w=440, h=230)
    family_node.fill_color = "#FCE4D6"
    control_node = family_node.add(control, x=380, y=90, w=180, h=60)
    control_node.fill_color = "#E2F0D9"
    family_node.add(gap_child, x=580, y=90, w=180, h=60)
    view.add(gap_root, x=860, y=190, w=210, h=65)
    connection = view.add_connection(retained, source=actor_node, target=process_node)
    connection.add_bendpoint(Point(125, 395), Point(230, 395))

    return model, view


def build_gap_free(source, source_view):
    gap_ids = {element.uuid for element in source.elements if element.type == ArchiType.Gap}
    keep_ids = {element.uuid for element in source.elements if element.uuid not in gap_ids}
    derived = Model("Layout Copy Fixture — No Gaps")
    element_map = {
        element.uuid: derived.add(element.type, element.name, desc=element.desc, folder=element.folder)
        for element in source.elements
        if element.uuid in keep_ids
    }
    relationship_map = {}
    for relationship in source.relationships:
        if relationship.source.uuid in keep_ids and relationship.target.uuid in keep_ids:
            relationship_map[relationship.uuid] = relate(
                derived,
                relationship.type,
                element_map[relationship.source.uuid],
                element_map[relationship.target.uuid],
                name=relationship.name,
            )

    view = derived.add(ArchiType.View, "Stakeholder View — No Gaps")
    node_map = {}
    for source_root in source_view.nodes:
        if source_root.ref in element_map:
            clone_node(view, source_root, element_map, node_map)
    for source_connection in source_view.conns:
        if source_connection.ref not in relationship_map:
            continue
        clone = view.add_connection(
            relationship_map[source_connection.ref],
            source=node_map[source_connection.source.uuid],
            target=node_map[source_connection.target.uuid],
        )
        copy_style(source_connection, clone, CONNECTION_STYLE_FIELDS)
        clone.add_bendpoint(
            *(Point(point.x, point.y) for point in source_connection.get_all_bendpoints())
        )
    return derived, view


def main():
    with TemporaryDirectory() as temporary_directory:
        source, _ = build_source()
        source_archive = Path(temporary_directory) / "source_fixture.archimate"
        source.write(str(source_archive))
        serialized_source = Model("Serialized Source")
        serialized_source.read(str(source_archive))
        source = serialized_source
        source_view = next(view for view in source.views if view.name == "Stakeholder View")
        derived, derived_view = build_gap_free(source, source_view)
        gap_ids = {element.uuid for element in source.elements if element.type == ArchiType.Gap}

        archive = Path(temporary_directory) / "gap_free_fixture.archimate"
        derived.write(str(archive))
        round_trip = Model("Round Trip")
        round_trip.read(str(archive))
        derived_view = next(view for view in round_trip.views if view.name == derived_view.name)

        assert not any(element.type == ArchiType.Gap for element in round_trip.elements)
        assert all(view.name != "View 0" for view in round_trip.views)
        assert not round_trip.check_invalid_relationships()
        assert not round_trip.check_invalid_nodes()
        assert not round_trip.check_invalid_conn()

        source_roots = [node for node in source_view.nodes if node.ref not in gap_ids]
        assert len(source_roots) == len(derived_view.nodes)
        for source_root, derived_root in zip(source_roots, derived_view.nodes):
            assert_matching_nodes(source_root, derived_root, gap_ids)

        source_connection = source_view.conns[0]
        derived_connection = derived_view.conns[0]
        assert [
            (point.x, point.y) for point in source_connection.get_all_bendpoints()
        ] == [
            (point.x, point.y) for point in derived_connection.get_all_bendpoints()
        ]

    print("PASS: exact retained geometry, nesting, styles, and bendpoints survived GAP removal.")


if __name__ == "__main__":
    main()
