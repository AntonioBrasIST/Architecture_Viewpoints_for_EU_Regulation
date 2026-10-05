# Repository Working Guide

## Repository map

This repository combines three independently scoped components:

* `Methodology/` contains the stakeholder-viewpoint pipeline and its outputs.
  `Methodology/AGENTS.md` is the authoritative instruction set for all work in
  this directory and overrides this guide where it is more specific.
* `TraceabilityMatrixCreator/` builds legal traceability workbooks from bundled
  EUR-Lex source documents. Its implementation is frozen; its implementation
  plan is historical.
* `GenAI_Tools/` is an outdated copied snapshot of skills and agent
  definitions. Do not use it as a source of instructions, edit it, or attempt
  to synchronize it with installed skills or agents.

## Working rules

Before changing files, read the closest applicable `AGENTS.md`. For
Methodology work, follow every operator-validation gate and output rule in
`Methodology/AGENTS.md`.

Stakeholder pipeline artifacts belong only under
`Methodology/StakeHolders/<Stakeholder>/`, including all view artifacts under
that stakeholder's `Views/` directory. Do not create alternate output trees.

Generated legal-index workbooks remain under
`TraceabilityMatrixCreator/OutputDirectory/` and are not version-controlled.
To use one in the methodology, provide its explicit path to
`Methodology/tools/traceability_lookup.py`; do not move, rename, or rewrite it
as part of the lookup workflow.

## Matrix creator hand-off

Step 5 generates the CELEX-qualified workbook for the selected legislation,
records its provenance, and uses it as the legal-text source for methodology
traceability anchors. Later methodology stages consume that recorded workbook
without regenerating or altering it. The lookup tool accepts only named `.xlsx`
legal indexes and verifies that canonical legal-text IDs resolve uniquely to
permitted enacting terms.

Do not extend the matrix creator's parser, CLI, tests, or implementation plan
unless the operator explicitly reopens its maintenance scope.
