---
name: git-interaction

description: This skill activates when an agent wants to use git, or the user mentions anything git related
---

# AI Skill Specification: git_interaction

## 1. Semantic Metadata
* **Skill Identifier:** `git_interaction`
* **Short Summary:** Enforces strict rules for agent interaction with Git, limiting operations to `.gitignore` modifications for specific files.
* **LLM Routing Description:**
  > "Use this tool whenever an agent needs to interact with Git or when a user's request involves Git operations (e.g., committing, pulling, pushing, ignoring files). Do NOT use this tool for any Git operation beyond adding `.AGENTS.md`, `ImplementationPlan.md`, or `.idea` to `.gitignore`."

## 2. Interface Schema (JSON Style)
```json
{
  "name": "git_interaction",
  "description": "Enforces strict rules for agent interaction with Git, limiting operations to .gitignore modifications for specific files.",
  "parameters": {
    "type": "object",
    "properties": {},
    "required": []
  },
  "returns": {
    "type": "object",
    "description": "Returns a confirmation message if an allowed Git operation is performed, or an error message if a forbidden operation is attempted."
  }
}
```

## 3. Core Logic & Execution Flow
1. **Pre-execution Verification:**
   - The agent must identify if the requested action is a Git operation.
   - If it is a Git operation, the agent must check if it falls under the explicitly allowed actions: adding `.AGENTS.md`, `ImplementationPlan.md`, or `.idea` to `.gitignore`.
2. **Main Processing Path:**
   - **Allowed Action:**
     - If the action is to add `.AGENTS.md` to `.gitignore`: Proceed with the operation.
     - If the action is to add `ImplementationPlan.md` to `.gitignore`: Proceed with the operation.
     - If the action is to add `.idea` to `.gitignore`: Proceed with the operation.
   - **Forbidden Action:**
     - If the action is any other Git command (e.g., commit, pull, push, branch, clone), immediately stop the operation.
3. **State & Context Preservation:**
   - This skill does not alter session history or external state beyond the `.gitignore` file.

## 4. Safety, Boundaries & Error Interception
* **Human-in-the-Loop (HITL) Requirement:** True - Any attempt to perform a Git operation not explicitly allowed by this skill requires immediate human intervention and clarification.
* **Deterministic Error Matrix:**
  | Input/State Failure | System Error Action | Return Message to LLM |
  | :--- | :--- | :--- |
  | Attempted Forbidden Git Operation | Abort Bash command | `"Error: Forbidden Git operation. Agents are only permitted to add '.AGENTS.md', 'ImplementationPlan.md', or '.idea' to .gitignore."` |
  | `.gitignore` file not found during allowed operation | Create `.gitignore` if it doesn't exist, then proceed. | `".gitignore file created/updated with specified entry."` |
* **Loop Prevention Rule:** "If this tool repeatedly attempts a forbidden Git operation within the same conversation turn, abort and ask the user for manual clarification."
