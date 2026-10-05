---
name: evidence-grounded-relationship-ledger
description: Converts approved operational or coverage evidence into atomic, source-backed relationship records. Use after fact extraction and before view scoping; never infer a link from co-occurrence, shared stream membership, or general domain knowledge.
---

# Evidence-Grounded Relationship Ledger

## Purpose

Create the relationship graph that later viewpoint stages are allowed to use.
This skill records meaning before presentation: a box may not enter a view merely
because it was mentioned or assigned to a coverage stream.

## Inputs and output

Inputs are approved `OP-*`/`CON-*` facts, approved `COV-*`/`REQ-*` coverage,
typed element candidates, and operator clarifications. Output is an atomic ledger
with one row per relationship:

| Field | Contract |
|---|---|
| Relationship ID | `REL-OP-*`, `REL-COV-*`, `REL-ROLE-*`, or `REL-COMP-*` |
| Source / target | Stable element IDs and textual names |
| Meaning | Source-backed verb phrase such as `builds`, `uses`, `supplies`, or `constrains` |
| ArchiMate relation | Candidate type and direction validated against the exact endpoint types |
| Evidence | Exact `OP-*`, `CON-*`, `COV-*`, `REQ-*`, legal source, or operator clarification |
| Ownership | Coverage ownership when the edge represents regulatory effect |
| Visibility | `visible` or `semantic-only`; the latter is restricted to nested Composition/Aggregation |
| Approval | `proposed`, `approved`, or `rejected` |

## Rules

1. Parse explicit subject-action-object statements. Preserve combined statements
   as multiple atomic edges when named targets differ. For example, “I develop
   microservices; these may be offloads, ETLs, or query services” establishes the
   stakeholder/development behavior plus the named component structure. It is not
   a list of unrelated assets.
2. Co-occurrence, membership in the same paragraph, a shared family, or a shared
   coverage stream is never evidence of a relationship.
3. Preserve the natural-language meaning separately from the ArchiMate type.
   Invoke `archimate-symbol-validator` for type and direction. Use Association only
   when the evidence really expresses a generic association; it is not a fallback
   for missing evidence.
4. `Directly performed` coverage may support Realization when endpoint types and
   evidence allow it. `Stakeholder-constrained`, `Externally owned`, and `Not
   evidenced / unclear owner` must never become stakeholder Realization; represent
   the approved constraint/effect/dependency instead.
5. Legal family containment receives `REL-COMP-*` only after the family and child
   decomposition is source-backed and operator-approved.
6. Show textual endpoint names and meaning before identifiers at every gate.
7. If either endpoint, direction, meaning, evidence, or legal relationship type is
   unresolved, stop and request targeted operator clarification. Do not approve or
   serialize a partial relationship.

## Validation and hand-off

- Relationship IDs are stable and unique across the stakeholder run.
- Every approved relationship has non-empty evidence and exactly two distinct
  endpoints.
- The ledger is append-only across later steps; later agents may reject or return
  an edge upstream, but may not silently rename, redirect, or manufacture one.
- Step 3 presents `Confirm Operational Relationships`; Step 5 presents regulatory
  effect edges in `Confirm Coverage Resolution`; legal-role edges use their own
  role-placement gate.
