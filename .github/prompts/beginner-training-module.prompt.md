---
name: "Beginner Training Module"
description: "Create a beginner-friendly GitHub Copilot or agent training module for this workspace"
argument-hint: "Topic, audience, duration, and desired output"
agent: "agent"
---
Create one beginner-friendly training module for this workspace.

Use these workspace expectations:

- Follow the module structure defined in [.github/copilot-instructions.md](../copilot-instructions.md)
- Follow project-level context in [CLAUDE.md](../../CLAUDE.md)
- Use beginner guidance from [references/copilot-agent-beginner-best-practices.md](../../references/copilot-agent-beginner-best-practices.md)
- Treat this as a curriculum project, not a software project
- Keep the material Windows-first unless the request explicitly says otherwise
- Default to BI, data science, or data engineering scenarios when the user does not specify another audience
- Assume teams may use either GitHub repositories or Azure DevOps repositories

Required output:

- Create or update one module README under `materials/<module-name>/README.md`
- Create a lab README under `labs/<module-name>/README.md`
- Include in the module README: learning objectives, prerequisites and setup, walkthrough, hands-on lab, validation checklist, reflection tasks
- Include suggested learner prompts they can try in VS Code
- Include at least one common failure mode and fix
- Add references to official first-party documentation when relevant
- Update the root `README.md` module index and `assets/curriculum-map.md`

Quality constraints:

- Write for beginners with direct, plain language
- Keep prompts specific and safe
- Prefer Research (project inception), then Ask, then Edit, then Plan, then Agent as the learner progression unless the request says otherwise. Research means using AI agents to search top GitHub repos for proven patterns and reviewing Azure Well-Architected Framework guidance before writing code; it is done once at project start, not repeated per task.
- Require visible validation steps and observable outputs
- Do not assume advanced coding experience unless the request explicitly says so
- Avoid assuming GitHub-hosted source control only; mention Azure DevOps when repository workflow matters
- Enforce markdown lint rules: MD022, MD032, MD034, MD047
- If requirements are ambiguous, ask clarifying questions before creating the module

Expected input from the user:

- Topic
- Target audience
- Duration or depth
- Whether the module is coding, non-coding, or mixed

If the user does not provide one of those inputs, ask only for the missing essentials.
