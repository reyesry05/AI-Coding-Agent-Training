# Developer Toolbox

Required and recommended tools for the AI Coding Agent Training curriculum.
This guide covers installation, versions, and VS Code extensions needed to complete all modules and labs.

## Quick-Start Checklist

Install these before the first session. Items marked **required** are needed for all modules; **recommended** items unlock specific labs or workflows.

- [x] VS Code
- [x] GitHub Copilot + Copilot Chat extension
- [x] Git
- [x] Python 3.12+
- [x] PowerShell 5.1+ (included with Windows)
- [ ] GitHub CLI (gh)
- [ ] Azure CLI (az)
- [ ] Pandoc
- [ ] markdownlint-cli

## Core Tools

### VS Code

**Required.** The primary environment for all modules.

- **Download**: <https://code.visualstudio.com/download>
- **Install**: Run the installer. Select "Add to PATH" during setup.
- **Verify**: Open a terminal and run `code --version`.

### Git

**Required.** Version control for labs and repo workflow modules (Module 07).

- **Download**: <https://git-scm.com/downloads/win>
- **Install**: Run the installer. Accept defaults. Select "Git from the command line and also from 3rd-party software".
- **Verify**: `git --version`
- **Expected**: 2.40 or later.

### Python

**Required.** Used in notebook labs (Module 05), slide generation scripts, and data pipeline examples.

- **Download**: <https://www.python.org/downloads/>
- **Install**: Check "Add python.exe to PATH" on the first screen, then click Install Now.
- **Verify**: `python --version`
- **Expected**: 3.12 or later.

After installing Python, create a virtual environment for the project:

```powershell
cd "AI Coding Agent Training"
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install python-pptx
```

### GitHub Copilot

**Required.** The AI assistant covered by every module.

- **Install**: Open VS Code, go to Extensions (`Ctrl+Shift+X`), search "GitHub Copilot", install both:
  - `GitHub Copilot`
  - `GitHub Copilot Chat`
- **Activate**: Sign in with a GitHub account that has a Copilot license (individual, business, or enterprise).
- **Verify**: Open Copilot Chat (`Ctrl+Shift+I`) and type "hello".

### PowerShell

**Required.** Windows PowerShell 5.1 is included with Windows. All lab commands assume PowerShell.

- **Verify**: `$PSVersionTable.PSVersion`
- **Expected**: 5.1 or later.

Optional upgrade to PowerShell 7:

- **Download**: <https://github.com/PowerShell/PowerShell/releases>
- **Install**: Run the MSI installer.
- **Verify**: `pwsh --version`

## Recommended CLIs

### GitHub CLI (gh)

Useful for repo workflows (Module 07) and managing pull requests from the command line.

- **Download**: <https://cli.github.com/>
- **Install**: Run the MSI installer.
- **Verify**: `gh --version`
- **Authenticate**: `gh auth login`

### Azure CLI (az)

Needed if labs reference Azure services, deployment, or cloud workflows.

- **Download**: <https://learn.microsoft.com/cli/azure/install-azure-cli-windows>
- **Install**: Run the MSI installer.
- **Verify**: `az version`
- **Authenticate**: `az login`

### Azure Developer CLI (azd)

For end-to-end Azure deployment workflows.

- **Download**: <https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd>
- **Install**:

```powershell
powershell -ex AllSigned -c "Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression"
```

- **Verify**: `azd version`

### Pandoc

Used for document conversion. The PPTX generator provides an alternative, but Pandoc is handy for ad-hoc conversions.

- **Download**: <https://pandoc.org/installing.html>
- **Install**: Run the MSI installer.
- **Verify**: `pandoc --version`

### markdownlint-cli

Enforces the project's markdown standards (MD022, MD032, MD034, MD047) from the command line. Useful for batch linting before commits.

- **Install** (requires Node.js and npm):

```powershell
npm install -g markdownlint-cli
```

- **Verify**: `markdownlint --version`
- **Usage**: `markdownlint "**/*.md" --config .markdownlint.json`

If npm is blocked by execution policy, use the VS Code extension instead (see below).

### Node.js and npm

Required only if you need markdownlint-cli or other npm-based tools.

- **Download**: <https://nodejs.org/en/download>
- **Install**: Run the LTS installer. Defaults are fine.
- **Verify**: `node --version` and `npm --version`
- **Execution policy note**: If npm scripts are blocked, ask IT to allow script execution or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## VS Code Extensions

### Required

Install these from the Extensions panel (`Ctrl+Shift+X`).

| Extension | ID | Purpose |
|---|---|---|
| GitHub Copilot | `github.copilot` | AI code assistant (all modules) |
| GitHub Copilot Chat | `github.copilot-chat` | Chat interface for Copilot (all modules) |
| Python | `ms-python.python` | Python language support and debugging |
| Pylance | `ms-python.vscode-pylance` | Python IntelliSense |
| Jupyter | `ms-toolsai.jupyter` | Notebook support (Module 05) |
| PowerShell | `ms-vscode.powershell` | PowerShell language support |
| markdownlint | `davidanson.vscode-markdownlint` | In-editor markdown linting |

### Recommended

| Extension | ID | Purpose |
|---|---|---|
| Markdown Mermaid | `bierner.markdown-mermaid` | Render Mermaid diagrams in markdown preview |
| YAML | `redhat.vscode-yaml` | YAML syntax and validation |
| Rainbow CSV | `mechatroner.rainbow-csv` | Color-coded CSV viewing |
| PDF Viewer | `tomoki1207.pdf` | View PDFs without leaving VS Code |

### Azure (if using Azure labs)

| Extension | ID | Purpose |
|---|---|---|
| Azure Tools for Copilot | `ms-azuretools.vscode-azure-github-copilot` | Azure + Copilot integration |
| Azure Resources | `ms-azuretools.vscode-azureresourcegroups` | Browse Azure resources |
| Azure Functions | `ms-azuretools.vscode-azurefunctions` | Azure Functions development |
| Azure Storage | `ms-azuretools.vscode-azurestorage` | Storage account management |
| Azure CLI Tools | `ms-vscode.azurecli` | Azure CLI script support |
| Cosmos DB | `ms-azuretools.vscode-cosmosdb` | Cosmos DB explorer |

### AI Assistants (optional, for comparison)

| Extension | ID | Purpose |
|---|---|---|
| Claude Code | `anthropic.claude-code` | Claude AI in VS Code |
| Gemini Code Assist | `google.geminicodeassist` | Google Gemini in VS Code |
| AI Foundry | `teamsdevapp.vscode-ai-foundry` | Azure AI Foundry integration |

### Data (optional, for BI/DE workflows)

| Extension | ID | Purpose |
|---|---|---|
| Snowflake | `snowflake.snowflake-vsc` | Snowflake SQL development |
| Neo4j | `neo4j-extensions.neo4j-for-vscode` | Neo4j graph database |
| Power BI Modeling MCP | `analysis-services.powerbi-modeling-mcp` | Power BI model operations |

## Reading Markdown in VS Code

> **Tip -- Cannot read a `.md` file?** You do NOT need to install anything extra.
> VS Code renders markdown out of the box. Open any `.md` file, then press
> `Ctrl+Shift+V` for a full-screen preview, or `Ctrl+K V` (two separate key
> presses) for a side-by-side view. If you still see raw markdown, make sure the
> file is the active editor tab before pressing the shortcut.

Learners do not need any extra tools to read markdown files. VS Code has built-in support:

| Action | Shortcut | Description |
|---|---|---|
| Full-screen preview | `Ctrl+Shift+V` | Opens rendered markdown in a new tab |
| Side-by-side preview | `Ctrl+K V` (two separate key presses) | Shows source on left, preview on right |
| Toggle editor/preview | Click the preview icon (book with magnifying glass) in the top-right of any `.md` tab | Switches between source and preview |

**Common gotcha:** If pressing `Ctrl+K V` does nothing, you likely pressed both keys at the same time. Press `Ctrl+K` first, release, then press `V`.

With the **markdownlint** extension installed, you also see inline warnings for any formatting issues directly in the editor.

With the **Markdown Mermaid** extension installed, any Mermaid code blocks render as diagrams in the preview.

## Presentation Tools

Two Python scripts generate slide decks from presenter-deck markdown files:

| Script | Output | Command |
|---|---|---|
| `generate_revealjs.py` | `html-slides/*.html` (browser-based) | `.venv\Scripts\python.exe generate_revealjs.py` |
| `generate_pptx.py` | `pptx-output/*.pptx` (PowerPoint) | `.venv\Scripts\python.exe generate_pptx.py` |

The Reveal.js HTML slides require no extra install -- they load from CDN when opened in a browser. Press `S` during a presentation for speaker notes.

The PPTX generator requires `python-pptx` in the virtual environment (installed during Python setup above).

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| `npm` or `gcloud` scripts blocked | PowerShell execution policy | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` or ask IT |
| `python` not recognized | Not added to PATH during install | Reinstall Python and check "Add python.exe to PATH" |
| Copilot not responding | License not activated or extension disabled | Sign out and sign back in to GitHub in VS Code |
| `git push` rejected | Branch divergence or permissions | Pull first with `git pull --rebase`, or check repo access |
| Markdown preview missing styles | Default VS Code theme | This is normal -- preview uses a simplified stylesheet |
| `.venv\Scripts\Activate.ps1` blocked | Execution policy | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
