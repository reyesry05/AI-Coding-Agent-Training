# GitHub Copilot: Reimagine Software Development

## Purpose

This reference summarizes key themes from the Microsoft "GitHub Copilot: Reimagine Software Development" deck (February 2025).
It serves as a factual anchor for training materials and ensures the curriculum reflects current GitHub Copilot capabilities.

## The Problem GitHub Copilot Addresses

Most organizations report that 30 percent of their development projects are over budget and late.
Common pressures include pop-up projects, flat budgets, migration backlogs, tight deadlines, developer turnover, vulnerabilities, slow code reviews, legacy code, and agile competitors.

Developers spend only about 14 percent of their time writing new code.
The rest goes to design, architecture, planning, refactoring, migrating, research, testing, documentation, and bug fixing.

## The Future Is Agentic Workflows

GitHub groups Copilot capabilities into three pillars:

| Pillar | Scope |
| --- | --- |
| Create (in the IDE) | Code completion, chat modes, agent mode, MCP, extensions, custom agents |
| Collaborate (across the SDLC) | Coding agent, code review, Copilot Spaces, Agent HQ |
| Operate (in the cloud) | Copilot for Azure, SRE Agent, MCP servers for Azure and GitHub |

An agentic layer spans all three pillars.

## Evolution Of GitHub Copilot

| Date | Milestone |
| --- | --- |
| June 2021 | Code completions |
| March 2023 | Chat |
| November 2023 | Workspace |
| October 2024 | Multi-file edits |
| February 2025 | Agent mode |
| May 2025 | Coding agent |

## Evolution Of Agentic Workflows

| Generation | Label | Description |
| --- | --- | --- |
| Gen 1 | Pair programming | Human works, AI suggests |
| Gen 2 | Pair programming | Human asks, AI answers |
| Gen 3 | Peer programming | Humans and AI collaborate |

## Four Interaction Modes In VS Code

GitHub Copilot now offers four distinct modes, ordered from least to most autonomous:

| Mode | What It Does | When To Use |
| --- | --- | --- |
| Ask Mode | Answers programming questions without touching code | Need explanation, orientation, or a quick lookup |
| Edit Mode | Applies inline, review-ready code edits across selected files | Know exactly which files to change and can describe the update |
| Plan Mode | Creates, refines, and executes step-by-step implementation plans | Want to review and approve the approach before any edits happen |
| Agent Mode | Autonomously plans steps, selects files, runs tools, and iterates until the task is complete | Task is well-scoped and you want end-to-end execution with review |

Spec Kit can kickstart spec-driven development alongside Plan Mode.

## GitHub Copilot Meets You Where You Are

- **Favorite IDE**: VS Code, Visual Studio, JetBrains, and more.
- **Models of choice**: Multiple model providers available.
- **Extensibility**: VS Code Marketplace extensions and MCP servers.

## Key Features

### Create (In The IDE)

- **Code completion**: Inline suggestions as you type.
- **Next Edit Suggestions**: Predicts the next logical edit location and content.
- **Copilot Vision**: Visual context awareness for richer assistance.
- **Model Context Protocol (MCP)**: Connects Copilot to external tools and data sources (Azure, GitHub, Playwright, Dev Box, deployment environments).
- **Agent Mode**: Autonomous multi-step task execution.
- **Custom Agents**: Specialized versions of the coding agent tailored with prompts, tools, and MCP servers.
- **App Modernization**: Upgrade and migrate legacy applications.
- **Copilot for Azure**: Azure context, best practices, IaC generation, deploy, manage, and troubleshoot.

### Collaborate (Across The SDLC)

- **Coding Agent** (GA): Assign issues to GitHub Copilot and receive pull requests back, validated with tests and linters. Works through PR review iteration. Customizable with dev environments, instructions, and MCP servers.
- **Code Review + Code Quality**: An intelligent agent that reviews code from multiple angles (planning, customizing, deduplicating). Code Quality (public preview) surfaces quality issues in PRs and backlogs.
- **Copilot Spaces** (GA): Ground Copilot in curated files, docs, pull requests, issues, and custom instructions. Share Spaces with teams and attach to repositories. Accessible in the IDE via the GitHub MCP Server.
- **Agent HQ** (Public Preview): A single platform to assign, steer, and track multiple coding agents from different model providers. Includes enterprise-grade agentic code review, a control plane for AI governance, and a metrics dashboard.

### Operate (In The Cloud)

- **Copilot for Azure**: Bring Azure context to GitHub Copilot. Generate Azure code and infrastructure as code. Deploy, manage, and troubleshoot from agent mode.
- **Azure SRE Agent** (Preview): AI-powered incident management and resource optimization. Automatic incident management, proactive diagnosis, automated deployments and rollbacks, continuous health monitoring.
- **GitHub MCP Server**: Automate GitHub workflows, extract repository data, manage issues and PRs, build tools for the GitHub ecosystem.
- **Azure MCP Server**: Azure best practices, context and resources, tooling for 40-plus Azure service areas, extended coding agent capabilities.

## Copilot Metrics Dashboard (Public Preview)

Track adoption and usage with granular IDE metrics:

- IDE active users (daily, weekly)
- Languages used and language usage per day
- Model usage per language and per day
- Code completions rate
- Agent adoption
- Chat requests and average per active user
- Requests per chat mode

Extend available metrics via API or JSON download.

## GitHub Copilot Adoption Stages

| Stage | Focus |
| --- | --- |
| Evaluation | Evaluate business and technical case to adopt Copilot |
| Adoption | Teams are enabled and actively using Copilot |
| Optimization | Positive impact on organization-specific goals |
| Sustained Efficiency | Continuous evaluation and improvement |

Leading indicators come first; organization-specific measures follow.

## Ten Use Cases To Maximize Copilot Potential

1. Code Completion
2. Code Refactoring and Optimization
3. Documentation and Comment Generation
4. Test Generation
5. Bug Fixing and Debugging Assistance
6. Code Conversion
7. Infrastructure as Code and Automation
8. Copilot in the CLI
9. SQL Query Optimization
10. Learning and Skill Development

## Adoption Journey

| Step | Description |
| --- | --- |
| Drive adoption | GitHub Copilot Adoption Factory with Microsoft and GitHub |
| Integrate and track | GitHub DevX offer with Microsoft ISD |
| Optimize | Value-based delivery workshops |
| Build dashboards | Data visualization with a Microsoft partner |

## Relevance To This Curriculum

| MS Deck Theme | Curriculum Module |
| --- | --- |
| Four interaction modes (Ask, Edit, Plan, Agent) | Modules 01, 03 |
| Prompt engineering and safe prompts | Modules 01, 03, 04 |
| Context and instructions | Module 04 |
| Coding agent and code review | Module 08 |
| MCP servers (GitHub, Azure) | Module 08 |
| Custom agents and Agent HQ | Module 08 |
| Copilot Spaces | Module 08 |
| Metrics dashboard and adoption stages | Module 02 (setup awareness) |
| Notebooks, SQL, pipelines use cases | Module 05 |
| Review and verification | Module 06 |
| Repository workflows | Module 07 |
| Evolution timeline and agentic generations | Module 01 (motivation) |

## Source

Microsoft "GitHub Copilot: Reimagine Software Development" presentation, February 2025. 43 slides.
PDF stored at `references/GHCP.pdf` in this workspace.
