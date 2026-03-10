# Copilot Agent Approval Settings

GitHub Copilot in VS Code requires explicit approval before it runs terminal commands, edits files, fetches URLs, or uses MCP tools. These prompts are a safety feature, but they can slow experienced users down. This reference explains every approval setting, how to relax them per-workspace or globally, and the risks involved.

## Default Behavior

Out of the box, Agent mode pauses and asks for confirmation before each of these actions:

| Action | What You See |
| --- | --- |
| Run a terminal command | "Copilot wants to run a command in the terminal. Continue?" |
| Edit or create a file | Diff view with Accept / Discard buttons |
| Fetch a URL | "Copilot wants to access [url]. Continue?" |
| Use an MCP tool | "Copilot wants to use [tool name]. Continue?" |

You can approve once, approve for the session, or cancel. This is safe but verbose when you trust the workspace.

## Settings Reference

Open settings with `Ctrl+,` and search for `chat.tools` or use the JSON settings file directly (`Ctrl+Shift+P` then "Preferences: Open User Settings (JSON)").

### Global Auto-Approve (Master Switch)

| Setting | Type | Default | Effect |
| --- | --- | --- | --- |
| `chat.tools.global.autoApprove` | `boolean` | `false` | When `true`, auto-approves terminal commands, file edits, tool invocations, and agent actions across the board. |

This is the single biggest lever. Setting it to `true` is the fastest path to full YOLO mode.

### Terminal Command Approval

| Setting | Type | Default | Effect |
| --- | --- | --- | --- |
| `chat.tools.terminal.autoApprove` | `object` | `{}` | Regex-based rules that auto-approve matching terminal commands. |

The value is an object whose keys are regex patterns (wrapped in `/`). Each key maps to an approval rule:

```jsonc
"chat.tools.terminal.autoApprove": {
    // Auto-approve every command (YOLO)
    "/.*/": {
        "approve": true,
        "matchCommandLine": true
    }
}
```

For a safer allowlist, name each pattern explicitly:

```jsonc
"chat.tools.terminal.autoApprove": {
    "/^python /":          { "approve": true, "matchCommandLine": true },
    "/^pip /":             { "approve": true, "matchCommandLine": true },
    "/^git (status|diff|log)/": { "approve": true, "matchCommandLine": true },
    "/^Get-ChildItem/":    { "approve": true, "matchCommandLine": true },
    "/^Test-Path/":        { "approve": true, "matchCommandLine": true }
}
```

- `"approve": true` -- skip the confirmation dialog for matches.
- `"matchCommandLine": true` -- match against the full command line, not just the binary name.

### URL Access Approval

| Setting | Type | Default | Effect |
| --- | --- | --- | --- |
| `chat.tools.urls.autoApprove` | `object` | `{}` | Glob-based rules that auto-approve URL fetches. |

```jsonc
"chat.tools.urls.autoApprove": {
    "https://*": true     // Auto-approve all HTTPS fetches
}
```

Narrow it to trusted domains when possible:

```jsonc
"chat.tools.urls.autoApprove": {
    "https://learn.microsoft.com/*": true,
    "https://github.com/*": true,
    "https://code.visualstudio.com/*": true
}
```

### Edit Retry Confirmation

| Setting | Type | Default | Effect |
| --- | --- | --- | --- |
| `chat.editing.confirmEditRequestRetry` | `boolean` | `true` | When `false`, Copilot does not ask for confirmation when retrying an edit request. |

## Quick Profiles

### Full YOLO (Auto-Approve Everything)

Add these to your user or workspace `settings.json`:

```jsonc
// WARNING: Copilot will run commands and edit files without asking.
// Only use in trusted, version-controlled workspaces.
"chat.tools.global.autoApprove": true,
"chat.tools.terminal.autoApprove": {
    "/.*/": { "approve": true, "matchCommandLine": true }
},
"chat.tools.urls.autoApprove": {
    "https://*": true
},
"chat.editing.confirmEditRequestRetry": false
```

**When to use**: Personal sandboxes, scratch repos, or training labs where you want uninterrupted flow and the workspace is under version control.

### Balanced (Recommended for Teams)

```jsonc
// Auto-approve safe commands and trusted URLs.
// Still ask before running unknown commands.
"chat.tools.global.autoApprove": false,
"chat.tools.terminal.autoApprove": {
    "/^python /":          { "approve": true, "matchCommandLine": true },
    "/^pip /":             { "approve": true, "matchCommandLine": true },
    "/^git (status|diff|log)/": { "approve": true, "matchCommandLine": true },
    "/^Get-ChildItem/":    { "approve": true, "matchCommandLine": true },
    "/^Test-Path/":        { "approve": true, "matchCommandLine": true },
    "/^Select-String/":    { "approve": true, "matchCommandLine": true }
},
"chat.tools.urls.autoApprove": {
    "https://learn.microsoft.com/*": true,
    "https://github.com/*": true,
    "https://code.visualstudio.com/*": true
},
"chat.editing.confirmEditRequestRetry": true
```

**When to use**: Day-to-day work in a trusted repo. You still get confirmation for anything outside the allowlist.

### Locked Down (Default Behavior, Explicit)

```jsonc
// Ask before every action. Useful for demos and shared machines.
"chat.tools.global.autoApprove": false,
"chat.tools.terminal.autoApprove": {},
"chat.tools.urls.autoApprove": {},
"chat.editing.confirmEditRequestRetry": true
```

**When to use**: Demonstrations, compliance-sensitive environments, or when onboarding new users who should see every confirmation.

## User Settings vs Workspace Settings

| Scope | File Location | Who It Affects |
| --- | --- | --- |
| **User settings** | `%APPDATA%\Code\User\settings.json` | Every workspace you open. |
| **Workspace settings** | `.vscode/settings.json` in the repo root | Only the current workspace. Overrides user settings. |

**Recommendation**: Keep user settings at the default (locked down). Relax approval settings only in workspace `settings.json` files for repos you trust. This way opening an untrusted folder does not auto-approve dangerous actions.

## Applying YOLO Mode to a Training Lab

If you are running a hands-on lab from this curriculum and want learners to move quickly:

1. Create `.vscode/settings.json` in the lab workspace folder.
2. Paste the Full YOLO profile above.
3. Verify the workspace is under version control (`git init` if not) so any unwanted edits can be reverted.
4. Remind learners to review the git diff after each Agent session before committing.

**Do not commit `.vscode/settings.json` with YOLO settings to a shared repository** unless the team has agreed. Add it to `.gitignore` or use a `.vscode/settings.json.example` template instead.

## Risks And Guardrails

| Risk | Mitigation |
| --- | --- |
| Agent runs a destructive command (`rm -rf`, `DROP TABLE`) | Use regex allowlists in `chat.tools.terminal.autoApprove` instead of `/.*/`. Keep the workspace under version control. |
| Agent edits a file you did not intend | Keep `chat.tools.global.autoApprove` at `false` and approve edits individually. Review `git diff` before committing. |
| MCP tool sends data to an external service | Leave `chat.tools.global.autoApprove` at `false` so MCP calls still prompt. |
| URL fetch leaks question context to an external site | Restrict `chat.tools.urls.autoApprove` to specific trusted domains instead of `https://*`. |
| HTTP fetch exposes data in transit | Never auto-approve plain `http://*`. Use HTTPS-only patterns. |

## Verifying Your Current Settings

Run this in the VS Code command palette (`Ctrl+Shift+P`):

```text
Preferences: Open User Settings (JSON)
```

Search for `chat.tools` to see all active overrides. If a setting is missing, the default (ask every time) applies.

You can also check from PowerShell:

```powershell
# Show all Copilot approval settings in your user config
$settingsPath = "$env:APPDATA\Code\User\settings.json"
if (Test-Path $settingsPath) {
    Get-Content $settingsPath | Select-String "chat\.(tools|editing)"
} else {
    Write-Output "No user settings.json found."
}
```

## DANGEROUS: Complete Auto-Approve Settings.json Sample

> **WARNING -- THIS REMOVES ALL SAFETY GUARDRAILS.**
> Copilot will run terminal commands, edit and create files, fetch any URL, and call MCP tools **without asking you first**. A single bad prompt can delete files, drop database tables, push to production, or send data to external services. **Use only in disposable, version-controlled sandboxes where you can revert everything.**

Copy the entire block below into `.vscode/settings.json` at the root of a workspace to auto-approve every Copilot agent action.

```jsonc
// .vscode/settings.json
// =====================================================================
//  FULL AUTO-APPROVE ("YOLO MODE") -- ALL GUARDRAILS DISABLED
//  DANGEROUS: Copilot will act without confirmation on EVERY action.
//  Only use in trusted, disposable, version-controlled workspaces.
// =====================================================================
{
    // --- Master switch -----------------------------------------------
    // Auto-approves terminal commands, file edits, tool invocations,
    // and agent actions globally. This one setting does most of the work.
    "chat.tools.global.autoApprove": true,

    // --- Terminal commands -------------------------------------------
    // Regex /.*/  matches EVERY command line.
    // Copilot will run rm, drop, git push --force, etc. without asking.
    "chat.tools.terminal.autoApprove": {
        "/.*/": {
            "approve": true,
            "matchCommandLine": true
        }
    },

    // --- URL access --------------------------------------------------
    // Auto-approve fetches to any HTTPS URL.
    // Your prompt context may be sent as part of the request.
    "chat.tools.urls.autoApprove": {
        "https://*": true
    },

    // --- Edit retries ------------------------------------------------
    // Skip confirmation when Copilot retries a failed edit.
    "chat.editing.confirmEditRequestRetry": false
}
```

### What Each Setting Unlocks

| Setting | What Copilot Can Do Without Asking | Worst-Case Scenario |
| --- | --- | --- |
| `chat.tools.global.autoApprove: true` | Run commands, edit files, call tools, invoke agents | Any of the scenarios below, all at once |
| `chat.tools.terminal.autoApprove: /.*/` | Run any terminal command: installs, deletes, git operations, shell scripts | `rm -rf /`, `DROP DATABASE production`, `git push --force origin main` |
| `chat.tools.urls.autoApprove: https://*` | Fetch any HTTPS URL, sending your prompt context in the request | Proprietary code snippets or internal project names sent to an external site |
| `chat.editing.confirmEditRequestRetry: false` | Retry edits silently when the first attempt fails | Repeated overwrites of a file without your knowledge |

### Before You Enable This

- [ ] The workspace is under version control (`git init` if not).
- [ ] You have no uncommitted work you cannot afford to lose.
- [ ] No MCP servers with write access to production systems are registered.
- [ ] You understand that **every action Copilot takes is immediate and irreversible** until you manually undo it.
- [ ] You will run `git diff` after every Agent session before committing.

### How To Revert

Delete the `.vscode/settings.json` file or remove the settings. Copilot immediately returns to requiring approval for every action.

```powershell
# Remove the workspace settings file to restore all defaults
Remove-Item .vscode/settings.json
```

## Related Files

- [copilot-chat-quick-commands.md](copilot-chat-quick-commands.md) -- Chat modes and session-level approval buttons
- [copilot-agent-beginner-best-practices.md](copilot-agent-beginner-best-practices.md) -- When to use each mode and how to review output
- [developer-toolbox.md](developer-toolbox.md) -- Tool installation and VS Code setup
- <https://code.visualstudio.com/docs/copilot/chat/agent-mode> -- Official VS Code docs on Agent mode
