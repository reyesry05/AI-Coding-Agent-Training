# Developer Environment Starter Guide (Windows + VS Code)

Use this guide to get a developer productive in VS Code quickly, with smooth Copilot workflow, markdown readability, and repository connectivity.

This guide intentionally does not repeat full tool installation steps. For that, use [Developer Toolbox](developer-toolbox.md).

## Goal

Set up a Windows developer workstation so day-1 Copilot and repository work is fast, safe, and predictable.

## Use This Guide In Order

1. Complete baseline tools from [Developer Toolbox](developer-toolbox.md).
2. Configure VS Code for daily work (including markdown preview and safe approvals).
3. Connect to a GitHub or Azure DevOps repository.
4. Run the health checks.

## 15-Minute Setup Path

| Step | Target outcome | Typical time |
| --- | --- | --- |
| 1. Accounts and sign-in | Copilot and Git auth are ready | 3 min |
| 2. VS Code workspace setup | Workspace is trusted and practical defaults are active | 4 min |
| 3. Agent approval workflow | Low-friction approvals without unsafe full autonomy | 3 min |
| 4. Repository connection | Clone and pull work from GitHub or Azure DevOps | 3 min |
| 5. Health check | Confirm end-to-end readiness | 2 min |

## Step 1. Accounts And Sign-In

Goal of the step:

- Ensure identity and license prerequisites are complete before troubleshooting editor behavior.

Exact action:

1. Open VS Code.
2. Sign in to GitHub from the Accounts menu.
3. Confirm GitHub Copilot and GitHub Copilot Chat are installed and enabled.
4. In terminal, verify Git identity:

```powershell
git config --global user.name
git config --global user.email
```

What success looks like:

- Copilot Chat opens and accepts prompts.
- `git config` returns your expected identity values.

Common failure mode and fix:

- Failure: Signed in with the wrong GitHub identity.
- Fix: Sign out in VS Code Accounts, sign back in with the licensed account.

## Step 2. VS Code Workspace Setup

Goal of the step:

- Make VS Code easier to use for docs and coding tasks on day 1.

Exact action:

1. Open your project folder in VS Code.
1. If prompted, click **Trust this workspace**.
1. Open **Settings** with `Ctrl+,` and verify baseline options:

- `Workbench: Editor: Enable Preview` = enabled
- `Workbench: Settings: Open Default Settings` = JSON (optional, recommended for advanced users)

1. Open Command Palette (`Ctrl+Shift+P`) and run **Preferences: Open User
   Settings (JSON)**.
1. Use these exact paths if you need to open `settings.json` directly:

- Windows: `%APPDATA%\\Code\\User\\settings.json`
- Windows expanded example: `C:\\Users\\<username>\\AppData\\Roaming\\Code\\User\\settings.json`
- macOS: `~/Library/Application Support/Code/User/settings.json`

1. Add or confirm this `settings.json` template (copy/paste):

```jsonc
{
   // ---------- General workflow ----------
  "explorer.confirmDelete": false,
  "git.enableSmartCommit": true,
  "chat.viewSessions.orientation": "stacked",

   // ---------- Markdown review defaults ----------
   // Open markdown in rendered preview by default.
   "workbench.editorAssociations": {
      "*.md": "vscode.markdown.preview.editor"
   },
   "[markdown]": {
      "editor.wordWrap": "on",
      "editor.quickSuggestions": false
   },

   // ---------- Copilot tool approvals ----------
   // DANGER: Keep terminal/command auto-approval OFF to prevent unattended
   // system, Azure, GitHub, or remote repository changes.
   "chat.tools.terminal.autoApprove": false,
   "chat.tools.command.autoApprove": false,
   "chat.tools.edits.autoApprove": {
      // Allow low-risk documentation updates only.
      "references/**": true,
      "materials/**": true,
      "labs/**": true,
      "**": false
   },

   // ---------- Web search ----------
   // Enables external web lookup in chat tools.
   // DANGER: Data may come from outside your repository context.
   "chat.anthropic.tools.websearch.enabled": true,

   // ---------- File access scope ----------
   // Keep read scope narrow to reduce accidental data exposure.
  "chat.additionalReadAccessPaths": [
      "${workspaceFolder}",
      "${workspaceFolder}/references"
  ]
}
```

1. Do not enable blanket auto-approval for terminal or command tools. Keep
   those manual, and only auto-approve edits in low-risk documentation paths.

1. Guardrail profile for documentation-focused workflows:

```jsonc
{
   // Keep command execution manual.
   "chat.tools.terminal.autoApprove": false,
   "chat.tools.command.autoApprove": false,
   "chat.tools.edits.autoApprove": {
      // Allow docs-only edits and block everything else.
      "references/**": true,
      "materials/**": true,
      "labs/**": true,
      "**": false
   }
}
```

1. Save `settings.json` and confirm there is only one
   `chat.additionalReadAccessPaths` key.
1. Open markdown preview with `Ctrl+Shift+V` (single tab preview).
1. Open side-by-side markdown preview with `Ctrl+K`, then `V`.
1. Install or confirm these extensions:

- `github.copilot`
- `github.copilot-chat`
- `davidanson.vscode-markdownlint`

1. In a markdown file, run **Markdown: Open Preview to the Side** from Command
   Palette to verify command access if shortcuts fail.
1. Set permanent default formatted view for `.md` files (one-time):

1. Right-click any markdown file tab.
1. Select **Open With...**.
1. Choose **Markdown Preview**.
1. Select **Set as Default**.
1. Reopen any markdown file and confirm it opens in rendered format by default.

What success looks like:

- Markdown files render correctly in preview.
- Markdown files open in rendered format by default after reopening VS Code.
- Copilot Chat and markdown lint diagnostics are visible.
- `settings.json` saves without duplicate keys for the same setting.

Common failure mode and fix:

- Failure: `Ctrl+K V` does nothing.
- Fix: Press `Ctrl+K`, release keys, then press `V`.
- Failure: A setting appears ignored in `settings.json`.
- Fix: Remove duplicate keys (for example duplicate `chat.additionalReadAccessPaths`) and keep a single final definition.
- Failure: Markdown still opens in plain text editor.
- Fix: Run **Open With...** on a markdown tab and set **Markdown Preview** as
   default again, then restart VS Code.

## Step 3. Agent Approval Workflow (Smooth + Safe)

Goal of the step:

- Reduce repetitive approval clicks while preserving control for risky actions.

Exact action:

1. Open Copilot Chat and switch to Agent mode.
2. Run a low-risk prompt, such as documenting a README section.
3. Use session-scoped allow only for low-risk edit tools in docs paths.
4. Keep terminal and command actions manual to prevent system, Azure, GitHub,
   and remote repository changes.

What success looks like:

- Fewer repeated prompts for the same safe tool type in the same chat session.
- You still review risky actions individually.

Common failure mode and fix:

- Failure: Everything is auto-approved with no review habit.
- Fix: Turn off `chat.tools.terminal.autoApprove` and
   `chat.tools.command.autoApprove`, then restrict
   `chat.tools.edits.autoApprove` to docs-only paths.

## Step 4. Connect To Repository (GitHub Or Azure DevOps)

Goal of the step:

- Establish a reliable clone/pull/push workflow from VS Code terminal.

### Option A: GitHub repository

Exact action:

1. Copy the HTTPS clone URL from GitHub.
2. In PowerShell terminal:

```powershell
git clone https://github.com/<org>/<repo>.git
cd <repo>
git remote -v
git pull
```

What success looks like:

- Repository is cloned locally.
- `git remote -v` shows `origin` with expected URL.
- `git pull` completes without auth failure.

Common failure mode and fix:

- Failure: Authentication prompt loops or fails.
- Fix: Re-authenticate using Git Credential Manager, then retry.

### Option B: Azure DevOps repository

Exact action:

1. Copy the HTTPS clone URL from Azure DevOps (`https://dev.azure.com/.../_git/...`).
1. In PowerShell terminal:

```powershell
git clone https://dev.azure.com/<org>/<project>/_git/<repo>
cd <repo>
git remote -v
git pull
```

1. When authentication prompts appear, use this order:

- First choice: **Sign in with browser** (recommended for most BI/DE teams on
   corporate Microsoft Entra ID).
- Second choice: **PAT** only when browser/device sign-in is blocked by policy,
   proxy, or conditional access issues.

1. Browser sign-in flow (recommended):

1. In the Git Credential Manager prompt, select **Sign in with your browser**.
1. Sign in with your work account used for Azure DevOps access.
1. Complete MFA or conditional access prompts.
1. Accept consent for Git Credential Manager if prompted.
1. Return to terminal and re-run `git pull` to confirm access.

1. PAT fallback flow (if browser sign-in fails):

1. In Azure DevOps, open user settings and create a new Personal Access Token.
1. Set a short expiration (team policy based).
1. Minimum scope for repo work: **Code (Read & write)**.
1. Copy the PAT once and store it in your approved password vault.
1. Retry `git pull`; if asked for credentials, use your Azure DevOps username
   and paste PAT as password.

1. Validate that auth is working:

```powershell
git remote -v
git pull
git fetch --all --prune
```

What success looks like:

- Clone succeeds and `origin` points to your Azure DevOps repo.
- Pull and fetch succeed without repeated auth prompts.
- Subsequent Git commands reuse stored credentials in the same workstation profile.

Common failure mode and fix:

- Failure: `fatal: Authentication failed`.
- Fix: Open **Windows Credential Manager**, remove stale `dev.azure.com`
   entries, then retry browser sign-in. If browser sign-in still fails, use PAT
   fallback with **Code (Read & write)** scope.
- Failure: MFA succeeds but terminal still denies access.
- Fix: Confirm your account has repo permission in the Azure DevOps project and
   verify the clone URL matches the correct org/project/repo path.

## Step 5. Health Check Commands

Run these in a VS Code PowerShell terminal:

```powershell
code --version
git --version
gh --version
az version
```

Expected result:

- `code` and `git` are required and should always return versions.
- `gh` and `az` are optional, based on your workflow.

If `gh` or `az` are missing, install them from [Developer Toolbox](developer-toolbox.md).

## Quick Decision Guide

| If you need to... | Do this first | Then do this |
| --- | --- | --- |
| Read markdown cleanly | `Ctrl+Shift+V` | Use `Ctrl+K`, `V` for side-by-side |
| Reduce approval friction | Use Agent mode on low-risk task | Choose **Continue (allow for session)** |
| Connect to GitHub repo | Clone with HTTPS URL | Verify with `git remote -v` and `git pull` |
| Connect to Azure DevOps repo | Clone `dev.azure.com` HTTPS URL | Use browser sign-in first, PAT fallback if needed |
| Confirm readiness | Run version checks | Run one test prompt in Copilot Chat |

## Day-1 Team Baseline (Recommended)

Use this baseline for onboarding consistency:

- VS Code + Copilot extensions installed
- Workspace trusted
- Markdown preview shortcuts validated
- Agent approvals set to session-scoped for low-risk tasks
- One successful clone + pull from GitHub or Azure DevOps
- One successful Copilot Chat prompt in the target repo

## Manager Onboarding Checklist (Copy/Paste)

Use this section as a ready-to-run checklist for new team members.

### Before first coding task

- Confirm developer has a licensed GitHub Copilot account and correct sign-in identity in VS Code.
- Confirm VS Code workspace opens in trusted mode.
- Confirm markdown preview works with `Ctrl+Shift+V` and `Ctrl+K`, `V`.
- Confirm Copilot Chat opens and responds in the target repository.

### Source control readiness

- Confirm repository clone succeeds from GitHub or Azure DevOps.
- Confirm `git remote -v` shows expected `origin` URL.
- Confirm `git pull` succeeds without repeated auth prompts.
- Confirm PAT process is documented for Azure DevOps users.

### Copilot operating guardrails

- Require Ask or Plan before Agent on unfamiliar tasks.
- Allow session-scoped approvals only for low-risk repetitive actions.
- Keep manual approval for destructive commands or external system changes.
- Require diff review before commit or pull request creation.

### Evidence to collect in week 1

- One screenshot of markdown side-by-side preview.
- One sample prompt and Copilot response tied to a real repo task.
- One reviewed diff showing keep, revise, or reject decision.
- One troubleshooting note captured by the learner.

### Completion criteria

- Developer can run day-1 tasks without setup help.
- Developer can explain when to use Ask, Plan, and Agent.
- Developer can connect and authenticate to the team repo workflow.
- Developer follows review and approval checkpoints consistently.

## Related References

- [Developer Toolbox](developer-toolbox.md)
- [Git And GitHub Desktop Reference](git-and-github-desktop-reference.md)
- [Copilot Chat Quick Command Reference](copilot-chat-quick-commands.md)
- [Repo Workflows In GitHub And Azure DevOps module](../materials/07-repo-workflows-github-and-azure-devops/README.md)

## First-Party Sources

- VS Code setup and docs: <https://code.visualstudio.com/docs/setup/setup-overview>
- VS Code Copilot overview: <https://code.visualstudio.com/docs/copilot/overview>
- VS Code Copilot chat: <https://code.visualstudio.com/docs/copilot/chat/copilot-chat>
- VS Code markdown basics: <https://code.visualstudio.com/docs/languages/markdown>
- GitHub Copilot docs: <https://docs.github.com/copilot>
- Azure DevOps Git docs: <https://learn.microsoft.com/azure/devops/repos/git>
