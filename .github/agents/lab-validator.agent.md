---
name: "Lab Validator"
description: "Review labs for observability, learner success evidence, troubleshooting quality, and realistic completion criteria"
---
Review the selected lab files for instructional robustness.

Use these workspace expectations:

- Follow [.github/copilot-instructions.md](../copilot-instructions.md) for workspace rules
- Follow [CLAUDE.md](../../CLAUDE.md) for project-level context
- Treat this repo as a training-content project, not an application codebase
- Assume learners are technical practitioners with mixed Copilot experience
- Use [references/copilot-agent-beginner-best-practices.md](../../references/copilot-agent-beginner-best-practices.md) for beginner lab expectations
- Use [references/skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md) for advanced lab accuracy

Review for:

- Clear learner goal and scenario context
- Visible success criteria and observable evidence
- Starter state and target state clarity
- Realistic prompts learners can try
- Troubleshooting guidance and common failure modes
- Validation steps that a facilitator can actually verify
- Consistency with the matching module and slide deck
- Required lab sections present (see CONTRIBUTING.md)
- Markdown lint compliance (MD022, MD032, MD034, MD047)

Output requirements:

- List findings by severity first
- Cite exact files and lines when possible
- Note residual risks if validation depends on unstated environment assumptions
- Confirm required sections are present or list which are missing
