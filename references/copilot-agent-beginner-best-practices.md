# Copilot Agent Beginner Best Practices

## Purpose

This reference captures baseline beginner practices for using GitHub Copilot and Copilot agents in Visual Studio Code. It is intended to support the module in `materials/01-beginner-copilot-agent-best-practices/` without duplicating the full learning content.

## Quick Decision Guide

| Situation | Best Starting Mode | Why |
| --- | --- | --- |
| Need explanation or orientation | Ask | Lowest risk, read-only, easiest to review |
| Need targeted edits to specific files | Edit | Applies inline changes you can diff-review before accepting |
| Need a step-by-step approach | Plan | Lets the learner inspect the approach before edits |
| Need a bounded implementation task | Agent | Useful when the task is clear and requires multi-step execution |

GitHub Copilot in VS Code now supports four interaction modes ordered from least to most autonomous: Ask, Edit, Plan, Agent.
For details on each mode, see [GitHub Copilot Reimagine Overview](github-copilot-reimagine-overview.md).

## Core Beginner Practices

1. Start with the least autonomy that fits the task.
2. Keep prompts specific and narrow.
3. Add explicit context with `#file`, `#codebase`, or `#fetch` when needed.
4. Review diffs, commands, and claims before accepting output.
5. Start a new session when the task changes significantly.
6. Capture repeated team preferences in custom instructions or prompt files.

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
