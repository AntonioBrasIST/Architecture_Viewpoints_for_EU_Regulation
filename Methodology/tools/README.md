# Traceability lookup

`traceability_lookup.py` queries an `.xlsx` legal traceability matrix and
prints one JSON object to standard output. Install its sole dependency first:

```bash
python3 -m pip install -r tools/requirements.txt
```

Every command requires the workbook path. The CLI does not hard-code a law,
workbook location, or row count.

```bash
python3 tools/traceability_lookup.py row-id --file /path/to/DORA-CELEX:32022R2554.xlsx --row 2
python3 tools/traceability_lookup.py row-text --file /path/to/DORA-CELEX:32022R2554.xlsx --row 2
python3 tools/traceability_lookup.py text-by-id --file /path/to/DORA-CELEX:32022R2554.xlsx --id "Chap.I, Art.1"
```

Legal-index files must be named `<REGULATION>-CELEX:<CELEX>.xlsx`, such as
`DORA-CELEX:32022R2554.xlsx`. Every successful JSON response echoes its parsed
`law` and `celex`, allowing pipeline agents to confirm that the selected legal
index belongs to the regulation being modelled.

`--row` is a one-based data-row number from the `Enacting Terms` worksheet:
`1` is Excel worksheet row `2`; headers and `Recitals` are excluded.

IDs must exactly match the canonical format emitted by `row-id`, with all
non-empty columns in order:

```text
Part X, Title X, Chap.X, Section X, Art.X, Paragraph X, Sub-Paragraph X, Point X, P.Sub-Paragraph X, Sub-Point X, Indent X
```

Recital IDs use `Recital N`. A duplicate canonical ID is returned as an
`AMBIGUOUS_ID` error, with matching row references and no selected text.

## View graph validation

`view_graph.schema.json` defines the machine-readable shape of
`7_view_graph.json`. `view_graph_validator.py` enforces the cross-record rules
that JSON Schema cannot: stable approved relationship IDs, endpoint-specific
evidence, stakeholder presence, zero isolated semantic elements, one weakly
connected component per view, semantic containment, and non-direct ownership
safeguards. A view with more than 30 root elements returns a readability warning
and is invalid for persistence until operator approval is recorded. Relationship
count is never capped.

```bash
python3 tools/view_graph_validator.py /path/to/7_view_graph.json
python3 tools/view_graph_validator.py /path/to/7_view_graph.json \
  --projection /path/to/native_round_trip_projection.json
python3 tools/view_graph_validator.py /path/to/7_view_graph.json \
  --remove-from-view view-id --remove-node GAP-001
```

Native XML, LikeC4, pyArchimate, and slide generators emit a normalized
round-trip projection with `technology` and per-view `node_ids` plus
`relationship_ids`. The optional projection check rejects missing/extra views,
nodes, or relationships after native parsing/render preparation.

The removal mode deletes only named nodes and their incident relationships from
one proposed Step 12 derivative, then re-runs stakeholder, degree, component,
nesting, ownership, and readability checks. It reports exact removed and retained
identities and never creates a bridge or removes additional nodes.

## Gap-free derivative planning

`gap_derivative_plan.py` consumes the normalized, structural GAP inventory made
by Step 12 and determines which narrative sections, slides, or model views are
affected. Clean units and clean artifact types are skipped. If the whole batch
is clean, it returns no outputs and no manifest.

```bash
python3 tools/gap_derivative_plan.py /path/to/gap_inventory.json
```
