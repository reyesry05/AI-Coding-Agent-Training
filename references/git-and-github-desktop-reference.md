# Git And GitHub Desktop Reference

A practical reference for learners who need to use Git in their daily workflow.
This guide covers both the Git command line and GitHub Desktop, explains when to reach for each tool, and provides examples grounded in BI, data science, and data engineering work.

## When To Use Git Command Line vs GitHub Desktop

| Situation | Recommended Tool | Why |
| --- | --- | --- |
| Quick status check or simple commit | Either | Both handle basic workflows equally well. |
| Visual diff of notebook or markdown changes | GitHub Desktop | The visual diff viewer is easier to scan than terminal output. |
| Scripting or automation (CI/CD, hooks) | Git CLI | Commands can be embedded in scripts and pipelines. |
| Resolving complex merge conflicts | Git CLI | Fine-grained control over conflict resolution strategies. |
| First-time learner wanting a guided experience | GitHub Desktop | The GUI reduces the chance of accidental destructive actions. |
| Working over SSH on a remote server | Git CLI | No GUI is available in a terminal-only session. |
| Cherry-picking or interactive rebase | Git CLI | GitHub Desktop does not expose these operations. |
| Reviewing changes before committing | GitHub Desktop | The side-by-side diff view makes review faster and more visual. |
| Bulk operations across many repos | Git CLI | Scriptable loops and batch commands are only possible on the CLI. |
| Teams new to source control | GitHub Desktop | Lower learning curve for commit, branch, push, and pull request workflows. |

## GitHub Desktop

### What It Is

GitHub Desktop is a free GUI application from GitHub that simplifies the most common Git operations.
It works with repositories hosted on GitHub and Azure DevOps (via clone URL).

- **Download**: <https://desktop.github.com/>
- **Supported platforms**: Windows, macOS.
- **Works with**: GitHub.com, GitHub Enterprise, and any Git remote (including Azure DevOps).

### Setup

1. Download and install from <https://desktop.github.com/>.
2. Sign in with your GitHub account (File > Options > Accounts).
3. Clone a repository (File > Clone Repository) or add an existing local repo (File > Add Local Repository).

What success looks like:

- The repository appears in the left sidebar with its current branch shown at the top.

Common failure mode and fix:

- Failure: "Repository not found" when cloning a private repo.
- Fix: Confirm you are signed in with an account that has access. For Azure DevOps repos, use the HTTPS clone URL with a PAT embedded or configure Git Credential Manager.

### Core Workflow In GitHub Desktop

#### 1. Pull the latest changes

- Click **Fetch origin** in the toolbar, then **Pull origin** if updates are available.
- Do this before starting new work to avoid merge conflicts.

#### 2. Create a branch

- Click the branch dropdown > **New Branch**.
- Name it descriptively: `feature/add-sales-dashboard-query`, `fix/pipeline-date-filter`.

#### 3. Make changes in VS Code

- Click **Open in Visual Studio Code** from the Repository menu.
- Edit files, notebooks, SQL scripts, or pipeline configs.

#### 4. Review changes

- Return to GitHub Desktop. Changed files appear in the left panel.
- Click each file to see a side-by-side diff.
- Confirm every change is intentional before committing.

#### 5. Commit

- Write a short summary in the commit message box (imperative mood: "Add monthly revenue query").
- Optionally add a longer description.
- Click **Commit to [branch-name]**.

#### 6. Push

- Click **Push origin** to send commits to the remote.

#### 7. Create a pull request

- Click **Create Pull Request** to open the PR form in your browser.
- Fill in reviewers, description, and linked work items.

### Tips For Data Teams

- **Review notebook diffs carefully.** GitHub Desktop renders `.ipynb` changes as JSON diffs. Scan cell outputs and metadata for unintended additions.
- **Use `.gitignore` to exclude generated files.** Add patterns like `*.pyc`, `.ipynb_checkpoints/`, `__pycache__/`, and large data files.
- **Commit often, push regularly.** Small, frequent commits make it easier to find where a query or script broke.

## Git Command Line

### Essential Commands

The table below covers commands that BI, data science, and data engineering practitioners use most often.

#### Configuration

| Command | What It Does | Example |
| --- | --- | --- |
| `git config --global user.name "Your Name"` | Sets your name for all commits. | `git config --global user.name "Carmen Yang"` |
| `git config --global user.email "you@example.com"` | Sets your email for all commits. | `git config --global user.email "cyang@example.com"` |
| `git config --list` | Shows current Git configuration. | `git config --list` |

#### Starting Work

| Command | What It Does | Example |
| --- | --- | --- |
| `git clone <url>` | Downloads a remote repository to your machine. | `git clone https://github.com/team/analytics-repo.git` |
| `git init` | Creates a new Git repository in the current folder. | `cd my-project; git init` |

#### Daily Workflow

| Command | What It Does | Example |
| --- | --- | --- |
| `git status` | Shows which files are changed, staged, or untracked. | `git status` |
| `git add <file>` | Stages a file for the next commit. | `git add queries/monthly-revenue.sql` |
| `git add .` | Stages all changed files in the current directory. | `git add .` |
| `git commit -m "message"` | Records staged changes with a description. | `git commit -m "Add monthly revenue query"` |
| `git pull` | Fetches and merges remote changes into your current branch. | `git pull origin main` |
| `git push` | Sends local commits to the remote repository. | `git push origin feature/sales-dashboard` |

#### Branching

| Command | What It Does | Example |
| --- | --- | --- |
| `git branch` | Lists local branches. The current branch has an asterisk. | `git branch` |
| `git branch <name>` | Creates a new branch without switching to it. | `git branch feature/add-date-filter` |
| `git checkout <branch>` | Switches to an existing branch. | `git checkout feature/add-date-filter` |
| `git checkout -b <name>` | Creates a new branch and switches to it in one step. | `git checkout -b fix/pipeline-timeout` |
| `git switch <branch>` | Modern alternative to `git checkout` for switching branches. | `git switch main` |
| `git switch -c <name>` | Creates and switches to a new branch (modern syntax). | `git switch -c feature/new-report` |
| `git merge <branch>` | Merges the specified branch into the current branch. | `git merge feature/add-date-filter` |
| `git branch -d <name>` | Deletes a branch that has been fully merged. | `git branch -d feature/add-date-filter` |

#### Inspecting History

| Command | What It Does | Example |
| --- | --- | --- |
| `git log --oneline` | Shows a compact commit history. | `git log --oneline -10` |
| `git log --oneline --graph` | Shows commit history with a branch graph. | `git log --oneline --graph --all` |
| `git diff` | Shows unstaged changes in the working directory. | `git diff` |
| `git diff --staged` | Shows changes that are staged for the next commit. | `git diff --staged` |
| `git show <commit>` | Shows the details and diff for a specific commit. | `git show abc1234` |

#### Undoing Changes

| Command | What It Does | Risk Level | Example |
| --- | --- | --- | --- |
| `git restore <file>` | Discards unstaged changes to a file. | Medium -- changes are lost. | `git restore queries/broken-query.sql` |
| `git restore --staged <file>` | Unstages a file without discarding changes. | Safe. | `git restore --staged queries/monthly-revenue.sql` |
| `git reset --soft HEAD~1` | Undoes the last commit but keeps changes staged. | Safe. | `git reset --soft HEAD~1` |
| `git reset --hard HEAD~1` | Undoes the last commit and discards all changes. | **High -- data loss.** | `git reset --hard HEAD~1` |
| `git stash` | Temporarily shelves uncommitted changes. | Safe. | `git stash` |
| `git stash pop` | Restores the most recently stashed changes. | Safe. | `git stash pop` |

#### Working With Remotes

| Command | What It Does | Example |
| --- | --- | --- |
| `git remote -v` | Lists configured remotes and their URLs. | `git remote -v` |
| `git remote add origin <url>` | Connects a local repo to a remote. | `git remote add origin https://dev.azure.com/org/project/_git/repo` |
| `git fetch` | Downloads remote changes without merging. | `git fetch origin` |

### Common Data-Team Scenarios

#### Scenario 1: Save work before experimenting

You have a working pipeline script and want to try a risky change.

```powershell
git stash
# Make experimental changes and test
# If the experiment fails:
git stash pop
# If the experiment works:
git add .; git commit -m "Refactor pipeline date logic"
```

#### Scenario 2: Undo an accidental commit (keep changes)

You committed to `main` by mistake instead of a feature branch.

```powershell
git reset --soft HEAD~1
git checkout -b feature/correct-branch
git commit -m "Add updated revenue query"
```

#### Scenario 3: See what changed in a SQL file

Before committing, review exactly what you changed.

```powershell
git diff queries/monthly-revenue.sql
```

#### Scenario 4: Pull latest and rebase your branch

Keep your feature branch up to date with `main` without creating merge commits.

```powershell
git checkout feature/sales-report
git pull --rebase origin main
```

If conflicts arise, Git will pause and show which files conflict. Edit each file to resolve, then:

```powershell
git add <resolved-file>
git rebase --continue
```

#### Scenario 5: Clone an Azure DevOps repository

Azure DevOps uses HTTPS URLs with a different format than GitHub.

```powershell
git clone https://dev.azure.com/your-org/your-project/_git/your-repo
```

If prompted for credentials, use a Personal Access Token (PAT) as the password. Git Credential Manager handles this automatically after the first authentication.

## .gitignore For Data Projects

A well-configured `.gitignore` prevents large data files, credentials, and generated artifacts from entering the repository.

Example `.gitignore` for a data-team project:

```text
# Python
__pycache__/
*.pyc
*.pyo
.venv/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# Data files (track schemas, not raw data)
*.csv
*.parquet
*.xlsx
data/raw/
data/output/

# Secrets and credentials
.env
*.key
*.pem

# IDE and OS
.vscode/settings.json
.idea/
Thumbs.db
.DS_Store

# Build outputs
dist/
build/
```

Adjust the patterns to match your team's conventions. Some teams track small reference CSVs intentionally -- add exceptions with `!data/reference/*.csv`.

## Decision Guide: CLI vs GitHub Desktop vs VS Code Source Control

| Need | CLI | GitHub Desktop | VS Code Source Control |
| --- | --- | --- | --- |
| Stage and commit changes | Yes | Yes | Yes |
| Visual diff review | Limited (terminal) | Strong (side-by-side) | Good (inline diff) |
| Branch creation and switching | Yes | Yes | Yes |
| Merge conflict resolution | Full control | Basic | Basic |
| Interactive rebase | Yes | No | No |
| Cherry-pick | Yes | No | No |
| Stash management | Yes | Limited | Limited |
| Works without a GUI | Yes | No | Partial (terminal panel) |
| Scriptable and automatable | Yes | No | No |
| Pull request creation | Via `gh` CLI | Yes (opens browser) | Via GitHub extension |
| Best for beginners | Moderate curve | Low curve | Low curve |

## Glossary

| Term | Definition |
| --- | --- |
| **Repository (repo)** | A folder tracked by Git that stores your project files and their full change history. |
| **Clone** | A local copy of a remote repository, including all branches and history. |
| **Branch** | A named line of development. Use branches to isolate work before merging. |
| **Commit** | A snapshot of staged changes with a message describing what changed. |
| **Stage (add)** | Mark a changed file for inclusion in the next commit. |
| **Push** | Send local commits to a remote repository. |
| **Pull** | Download and merge remote changes into the current branch. |
| **Fetch** | Download remote changes without merging them. |
| **Merge** | Combine changes from one branch into another. |
| **Rebase** | Replay commits from one branch onto another to create a linear history. |
| **Stash** | Temporarily save uncommitted changes so you can switch tasks. |
| **Pull request (PR)** | A request to merge changes from one branch into another, with review. |
| **Remote** | A version of your repository hosted on a server (GitHub, Azure DevOps). |
| **HEAD** | A pointer to the current commit on the current branch. |
| **Diff** | A comparison showing what changed between two states. |
| **Conflict** | When two branches change the same lines and Git cannot merge automatically. |
| **PAT (Personal Access Token)** | A credential used instead of a password for Git authentication. |

## Sources

- Git official documentation: <https://git-scm.com/doc>
- GitHub Desktop documentation: <https://docs.github.com/desktop>
- Azure DevOps Git documentation: <https://learn.microsoft.com/azure/devops/repos/git>
- Pro Git book (free): <https://git-scm.com/book/en/v2>
- GitHub training pathways: <https://skills.github.com/>
