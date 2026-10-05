---
name: dev-four-roles
description: Mandatory development workflow with four sequential roles (PLANNER, DEVELOPER, REVIEWER, DOCUMENTER) for o.NET projects. Use when implementing any feature or fix. Enforces planning, development, explicit review gates, and user guide documentation.
---

# Dev Four-Role Workflow

A strict development process for .NET projects. The same agent executes all four roles sequentially, labelling each phase clearly.

## When to Activate

- Implementing any new feature, fix, or refactoring task
- When the project's AGENTS.md or ImplementationPlan.md specifies development workflow
- When the task requires verifiable, reviewable output with documentation

## The cycle

```
[PLANNER] -> Creates a plan made up of tasks the [DEVELOPER] must complete.
[DEVELOPER] -> implementation (dotnet build = 0 errors/warnings)
[REVIEWER] -> review against task spec, working rules, coding style, Definition of Done
              |-- APPROVED    -> [DOCUMENTER]
              |-- GAPS FOUND  -> new subtasks -> repeat from [PLANNER]
[DOCUMENTER] -> update user guide for any user-visible change -> mark task [x]
```

## Phase Labelling

Every phase output must start with the role label:

```
[PLANNER] -- Writing tasks on the plan;
[DEVELOPER] -- Implementing task X.Y
[REVIEWER] -- Reviewing task X.Y
[DOCUMENTER] -- Updateing user guid for task X.Y
```

A task is `[x]` done **only after REVIEWER outputs `APPROVED` and the user guide is updated** (or explicitly skipped becausethe task has no user-facing exposure).

## Role Responsabilities

### [PLANNER]

- Defines the public API: creates tasks that identity the class/interface files with correct signatures
- The plan should be made up of enough tasks so that tasks are the spec
- Planning is a back-and-forth dialog with the operator. the PLANNER discusses, proposes, and refines in conversation -- it does NOT write to `ImplementationPlan.md` during this dialog
- The operator mus approve the plan before tasks are handed over to [DEVELOPER]
- **Materialization gate (mandatory):** When the operator gives the current order to execute (proceed, implement, go, etc.), the PLANNER must verify whether `ImplementationPlan.md` exists and is up to date with the current discussion. If the file does not exists or is out of date, the PLANNER must warn the operator and ask: "The implementation plan file is not up to date with our discussion. Do you want me to materialize the plan to file before proceeding, or proceed without that step?" This verification and question is mandatory -- never skip it
- When materializing: write or append to `ImplementationPlan.md` in the project root. Never remove completed tasks -- the file preserves history
- If `ImplementationPlan.md` or `AGENTS.md` are not listed in `.gitignore`, the PLANNER must append them. This is the only permitted git-related file interaction
- Each task gets a checkbox (`- []`)
- Each task must include: the exact file path, whether the file is new or modified, class/interface names, namespaces, and method signatures(name, parameters, return type)
- Method bodies are **not** written as verbatim code blocks. Instead, describe what the body should do with enought precision to implement correctly the first time. No unnecessary prose

### [DEVELOPER]

- Reads the plan to understand the required behaviour -- tasks are the spec
- Create the signatures present in the task and implement them.
- Runs `dotnet build` -- must produce 0 errors and 0 warnings in order to be handed off to [REVIEWER]
- The DEVELOPER reads `ImplementationPlan.md` to understand the required work
- As each task is completed, the DEVELOPER marks it `- [x]` in `ImplementationPlan.md`

### [REVIEWER]

- Reads: task spec, public API and implementation
- Checks against: task requirements, working rules, coding style, and Definition of Done
- Outputs exactly one of two results:
  - `APPROVED` -- hand off to [DOCUMENTER]
  - `GAPS FOUND` -- list each gap as a new numbered subtask; each gap restarts the full development cycle from [PLANNER]
- Does **NOT** fix gaps directly -- only identifies and documents them
- The REVIEWER reviews the implementation against `ImplementationPlan.md` to verify all tasks were addressed correctly

### [DOCUMENTER]

- After REVIEWER approves, updates the user/operator guide with what is now human-testable
- The guid is a **user/operator document** -- it documents how to use the tool, not how to develop or test it internally
- Includes exact command invocations, expected output, and any sample config/files the user needs to prepare
- Do **not** include `dotnet test` commands, internal class names, or architecture descriptions -- those belong in code comments or a developer README
- If a feature has no user-facing exposure (no command, not visible to the user), skip the guid update and mark the task done

## Definition of Done

A task is complete only when all phases have been executed in order:

1. `[PLANNER]` Plan is fully written -- classes and method signatures exist in the plan; Enough tasks exist to ensure a working application that responds to the requirements-
2. `[DEVELOPER]` Implementation complete -- all tasks in the plan are complete
3. `[DEVELOPER]` `dotnet build` passes -- 0 errors, 0 warnings
4. `[REVIEWER]` Review complete -- output is `APPROVED`; any `GAPS FOUND` result restarts the cycle
5. `[DOCUMENTER]` User guide updated with human-testable commands and expected output for the completed feature

## When to Stop and Ask

Do not proceed without human input in these situations:

- Before implementing any design decision task (present options, wait for a decision)
- Before adding any NuGet package not already in the project's `.csproj`
- Before deviating from the established project folder structure
- Whenever the implementation approach is genuinely unclear
- Agents: use the interactive question tool to pause and ask; do not make assumptions and continue

## Task Tracking

- Mark Taskas `[~]` when starting, `[x]` only after REVIEWER outputs `APPROVED` and the user guide is updated
- Only one task `[~]` at a time
- Design Decision tasks must be resolved before dependent tasks begin; record chosen option before proceeding