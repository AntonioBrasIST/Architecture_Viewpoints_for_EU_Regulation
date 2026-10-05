---
name: stakeholder-legal-role-mapper
description: Maps a stakeholder through their employing organization to a law-defined entity or role group using only approved organizational and legal-applicability evidence. Use before the contextualized regulation overview; never equate an employee with the regulated entity.
---

# Stakeholder Legal-Role Mapper

## Purpose

Create an evidence-backed path explaining where the viewpoint's stakeholder sits
relative to the regulation's named role groups.

## Required inputs

- The textual stakeholder role and its operational evidence.
- The employing or represented organization, if explicitly known.
- The law-defined entity/role group and canonical legal source.
- Explicit applicability evidence or an operator-confirmed applicability fact.

## Output contract

Produce a Legal-Role Placement Ledger containing distinct nodes for:

1. stakeholder role or actor;
2. employing/represented organization;
3. law-defined entity or role group.

Each `REL-ROLE-*` row records textual source and target names, relationship meaning,
validated ArchiMate types/direction, evidence, and approval. A typical confirmed
path is `Back-end Developer — works within → Bank — specializes → Financial
Entity`; it does not state that the individual developer is a financial entity.

## Rules and gate

- Never infer legal applicability from organization size, location, industry, or
  regulation selection.
- Never collapse the person/role, organization, and legal group into one element.
- Use `archimate-symbol-validator` for every proposed ArchiMate tuple.
- If employment or legal qualification is missing, halt and ask the operator for
  the missing fact.
- Gate 5.6 `Confirm Stakeholder Legal Role` presents textual names, meanings, and
  evidence first; stable IDs appear secondarily. Persist only approved rows.
- The approved chain is immutable input to the contextualized Overview and must be
  present in every downstream view graph.
