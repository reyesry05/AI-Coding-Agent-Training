# Copilot Chat Quick Command Reference

A fast-lookup cheat sheet for slash commands, context variables, and mode switches available in GitHub Copilot Chat within VS Code.
Print this page or keep it open as a side tab during labs.

## Slash Commands

Commands you type at the start of the chat input box.

| Command | What It Does | When To Use |
| --- | --- | --- |
| `/clear` | Clears the entire conversation history and resets context. | Context window is cluttered or you are switching to a new task. |
| `/help` | Shows available commands and usage tips. | You forget a command or want to explore options. |
| `/new` | Starts a new chat session (keeps history in sidebar). | You want a fresh conversation without losing the old one. |
| `/newNotebook` | Creates a new Jupyter notebook from a description. | Starting a data exploration or analysis task from scratch. |
| `/search` | Performs a semantic search across the workspace. | You need to find code, files, or patterns quickly. |
| `/tests` | Generates unit tests for the selected code or active file. | After writing a function and wanting quick test scaffolding. |
| `/fix` | Proposes a fix for problems in the selected code. | You have a lint error, bug, or failing test and want a quick fix. |
| `/fixTestFailure` | Analyzes a failing test and suggests a fix. | A test run failed and you want Copilot to diagnose it. |
| `/explain` | Explains the selected code or active file in plain language. | You encounter unfamiliar code and need to understand it. |
| `/doc` | Adds or updates documentation comments for the selection. | Adding docstrings, JSDoc, or header comments to functions. |
| `/setupTests` | Scaffolds a testing framework for the current project. | Starting a new project and need test infrastructure. |

## Context Variables

Type `#` in the chat input to attach specific context to your prompt.

| Variable | What It Attaches | Example Use |
| --- | --- | --- |
| `#file` | A specific file from the workspace. | `#file:schema.sql Explain the relationships in this schema.` |
| `#selection` | The currently highlighted code in the editor. | `#selection Refactor this loop to use a list comprehension.` |
| `#codebase` | Searches the full workspace for relevant context. | `#codebase Where is the database connection configured?` |
| `#terminalLastCommand` | The last command and its output from the terminal. | `#terminalLastCommand Why did this command fail?` |
| `#terminalSelection` | The currently selected text in the terminal. | `#terminalSelection Parse this error and suggest a fix.` |
| `#problems` | Current errors and warnings from the Problems panel. | `#problems Fix the lint violations in my project.` |
| `#changes` | Uncommitted changes (git diff). | `#changes Summarize what I changed and draft a commit message.` |
| `#fetch` | Fetches a URL and includes its content as context. | `#fetch:https://example.com/api-docs Use this API reference to write a client.` |

## Chat Modes

Switch modes using the dropdown at the top of the Copilot Chat panel or type the mode keyword.

GitHub Copilot Chat offers four modes, ordered from least to most autonomous.

| Mode | Behavior | Best For |
| --- | --- | --- |
| **Ask** | Read-only answers. Does not modify files. | Exploring, learning, asking questions, understanding code. |
| **Edit** | Proposes inline edits to specific files you indicate. | Targeted changes to one or a few files with full diff review. |
| **Plan** | Generates a step-by-step plan for review before applying changes. | Multi-step tasks where you want to inspect the approach first. |
| **Agent** | Autonomous multi-step execution with tool access (terminal, file edits, search). | Complex tasks spanning multiple files, running commands, scaffolding projects. |

## Agent Mode Tool Approvals

When running in Agent mode, Copilot may request permission to use tools. Understand the approval options.

| Option | What It Means |
| --- | --- |
| **Continue** | Approve the single pending action. |
| **Continue (allow for session)** | Auto-approve this tool type for the rest of the chat session. |
| **Cancel** | Reject the pending action. Copilot will try an alternative. |

To change the default approval behavior (including auto-approving everything), see [Copilot Agent Approval Settings](copilot-agent-approval-settings.md).

## Keyboard Shortcuts (Windows)

| Shortcut | Action |
| --- | --- |
| `Ctrl+Alt+I` | Open or focus Copilot Chat panel. |
| `Ctrl+Shift+I` | Start Copilot Edits (multi-file edit session). |
| `Ctrl+I` | Open inline chat in the active editor. |
| `Ctrl+Shift+Alt+L` | Add selection to Copilot Chat as context. |
| `Ctrl+Enter` | Send message (in chat input). |
| `Escape` | Dismiss inline chat or suggestion. |

## Quick Tips

- **Start fresh often.** Use `/clear` or `/new` when switching tasks to prevent stale context from confusing responses.
- **Be specific with context.** Attach `#file` or `#selection` instead of relying on Copilot to guess which code you mean.
- **Escalate gradually.** Start with Ask mode to understand, move to Edit for targeted changes, use Agent for multi-step work.
- **Review before accepting.** Always check diffs in Edit mode and terminal commands in Agent mode before approving.
- **Use `#codebase` sparingly.** It searches broadly and may pull in irrelevant context. Prefer `#file` when you know the target.

## Source

Based on official GitHub Copilot documentation at <https://docs.github.com/copilot> and VS Code Copilot documentation at <https://code.visualstudio.com/docs/copilot/overview>.
Commands and features may change as Copilot evolves -- verify against the `/help` output in your current VS Code version.
