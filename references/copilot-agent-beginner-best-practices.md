# Copilot Agent Beginner Best Practices

## Purpose

This reference captures baseline beginner practices for using GitHub Copilot and Copilot agents in Visual Studio Code. It is intended to support the module in `materials/01-beginner-copilot-agent-best-practices/` without duplicating the full learning content.

## Full Beginner Workflow

The complete beginner workflow has two levels:

- **Project-inception step (Research)**: Done once when starting a new project. Search top GitHub repos for proven patterns and review Azure Well-Architected Framework guidance before writing any code.
- **Per-task loop (Ask > Edit > Plan > Agent)**: Repeated for each task within the project. Choose the lowest-autonomy mode that fits the job.

```text
Research  (project start, do once)
    └── Ask  (orientation, explanation)
         └── Edit  (targeted file changes)
              └── Plan  (multi-step work)
                   └── Agent  (bounded implementation)
```

## Quick Decision Guide

| Situation | Step / Mode | Why |
| --- | --- | --- |
| Starting a new project (ML model, pipeline, architecture) | Research | Surfaces proven GitHub patterns and Azure WAF guidance before you write code |
| Need explanation or orientation | Ask | Lowest risk, read-only, easiest to review |
| Need targeted edits to specific files | Edit | Applies inline changes you can diff-review before accepting |
| Need a step-by-step approach | Plan | Lets the learner inspect the approach before edits |
| Need a bounded implementation task | Agent | Useful when the task is clear and requires multi-step execution |

GitHub Copilot in VS Code now supports four per-task interaction modes ordered from least to most autonomous: Ask, Edit, Plan, Agent.
For details on each mode, see [GitHub Copilot Reimagine Overview](github-copilot-reimagine-overview.md).

## Research Step: Before You Write Code

When starting a new project -- such as a new ML forecasting model, data pipeline, or cloud workload -- spend time researching before opening a code file.

### What to do

- Use `@github` in Copilot Chat to search public repos for similar problems:
  - `@github Find the top Python repos for time-series forecasting with scikit-learn`
  - `@github Show me examples of Azure ML pipelines with feature stores`
- Review README files, issues, architecture diagrams, and test suites in top repos for patterns, trade-offs, and anti-patterns.
- Look up the Azure Well-Architected Framework guidance for your workload type. You can use an agent skill or ask Copilot directly:
  - `Using @azure, what does the Azure Well-Architected Framework recommend for a batch ML training workload?`
- Note key design decisions, library choices, and known failure modes before writing any code.

### When to use it

- At project inception for new builds.
- When designing a system architecture.
- When evaluating library or framework choices.

### When to skip it

- Routine daily coding tasks (bug fixes, small edits, script tweaks). For those, go straight to Ask > Edit > Plan > Agent.
- Experienced engineers can internalize this step mentally -- the principle is to learn from proven work before building from scratch.

### Tools that help

- `@github` chat participant for public repo search.
- Agent skills: `azure-compliance`, `azure-prepare`, `azure-ai`, and `microsoft-foundry` can surface WAF and service-specific guidance.
- Direct Copilot Ask mode with `#fetch` for documentation URLs.

## Core Beginner Practices

1. Research proven patterns before starting a new project.
2. Start with the least autonomy that fits the task.
3. Keep prompts specific and narrow.
4. Add explicit context with `#file`, `#codebase`, or `#fetch` when needed.
5. Review diffs, commands, and claims before accepting output.
6. Start a new session when the task changes significantly.
7. Capture repeated team preferences in custom instructions or prompt files.

## What Beginners Should Avoid

- Large, compound prompts that are hard to verify.
- Using Agent before the scope is clear.
- Accepting output that sounds correct without checking it.
- Mixing unrelated tasks in a single chat session.

## Official Sources

### GitHub Docs

- [What is GitHub Copilot?](https://docs.github.com/en/copilot/get-started/what-is-github-copilot)
- [About GitHub Copilot Chat](https://docs.github.com/en/copilot/concepts/chat)
- [Use GitHub Copilot agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents)

### VS Code Docs

- [Chat overview](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [Using agents in Visual Studio Code](https://code.visualstudio.com/docs/copilot/agents/overview)
- [Agents tutorial](https://code.visualstudio.com/docs/copilot/agents/agents-tutorial)
- [Prompt engineering in VS Code](https://code.visualstudio.com/docs/copilot/guides/prompt-engineering-guide)
- [Manage context for AI](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)
- [Use custom instructions in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Review AI-generated code edits](https://code.visualstudio.com/docs/copilot/chat/review-code-edits)
- [Troubleshooting GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/troubleshooting)

## Related Files

- [Beginner Best Practices For GitHub Copilot Agents In VS Code](../materials/01-beginner-copilot-agent-best-practices/README.md)
- [GitHub Copilot Reimagine Overview](github-copilot-reimagine-overview.md)
