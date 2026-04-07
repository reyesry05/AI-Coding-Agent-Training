# Research And Building Blocks

## Learning Objectives

By the end of this module, learners should be able to:

- explain why research is the first step before writing any code or prompt
- find and evaluate existing repos, templates, and community solutions on GitHub
- use the Azure Well-Architected Framework and official docs as quality baselines
- build on top of proven patterns instead of starting from scratch
- create reusable building blocks (instruction files, prompt templates, starter projects) from research findings
- cite sources and attribute prior work in team documentation

## Prerequisites And Setup

Audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Prerequisites:

- Modules 01 through 08 completed or equivalent knowledge
- GitHub account with access to public repositories
- VS Code with GitHub Copilot Chat enabled
- Familiarity with the Research > Ask > Edit > Plan > Agent workflow

Success looks like:

- The learner can demonstrate a structured research workflow before prompting an agent.
- The learner can evaluate whether an existing repo or template is worth building on.

Common failure mode and fix:

- Failure: The learner skips research and asks the agent to generate everything from scratch.
- Fix: Require a research summary document before any code generation begins.

## Walkthrough

### Step 1. Why Research Comes First

Goal of the step:

- Establish that research is not optional; it prevents rework and improves prompt quality.

Exact action:

- Review the Research > Ask > Edit > Plan > Agent workflow from module 01.
- Research is the project-inception step: search top GitHub repos, review official docs, and evaluate existing solutions before writing a single prompt.

What success looks like:

- The learner can explain why research reduces hallucination risk and improves output quality.

Common failure mode and fix:

- Failure: The learner treats research as "just Googling."
- Fix: Show that structured research produces artifacts (a curated link list, a pattern summary, a starter template) rather than just answers.

### Step 2. Search GitHub For Existing Work

Goal of the step:

- Teach learners to find high-quality repos, templates, and community solutions.

Exact action:

- Use GitHub search with filters: `stars:>50`, `language:python`, `topic:data-pipeline`, `pushed:>2025-01-01`.
- Use Copilot Chat: `@github Search for Python data validation frameworks with Pydantic`.
- Evaluate results using these criteria:

| Criteria | What to check |
| --- | --- |
| Maintenance | Last commit date, open issue count, release cadence |
| Quality | Test coverage, CI badge, documentation quality |
| Fit | Does it solve your specific problem or a generic one? |
| License | Is the license compatible with your org policy? |
| Community | Stars, forks, contributor count, responsiveness to issues |

What success looks like:

- The learner produces a shortlist of 2-3 repos with evaluation notes.

Common failure mode and fix:

- Failure: The learner picks the first result without evaluating quality.
- Fix: Require at least three evaluation criteria per candidate.

#### Worked Example: Researching A Data Validation Pattern

Suppose your team needs a reusable way to validate CSV files before loading them into a warehouse. Here is a full research session using GitHub Copilot search and web search.

**Round 1 -- Broad discovery with `@github`**

Open Copilot Chat and type:

```text
@github Search for Python CSV data validation libraries that support schema definition and are actively maintained
```

Copilot searches across public GitHub repos and returns summaries with links. A typical response might surface repos like `great-expectations`, `pandera`, `cerberus`, or `pydantic` with brief descriptions.

> **Tip**: The `@github` participant searches code, repos, issues, and discussions across all of GitHub. It is different from web search -- it queries the GitHub index directly.

**Round 2 -- Narrow the search with filters**

Refine by asking for specifics:

```text
@github Compare pandera and great-expectations for DataFrame validation. Which has more recent commits and better documentation?
```

Or search GitHub directly in a browser with advanced filters:

```text
https://github.com/search?q=csv+validation+language%3Apython+stars%3A%3E100+pushed%3A%3E2025-06-01&type=repositories
```

This filters for: Python repos, 100+ stars, updated in the last year, matching "csv validation."

**Round 3 -- Deep-dive with web search**

Switch to Copilot web search for broader context:

```text
#web What are the pros and cons of pandera vs great-expectations for data pipeline validation in 2025?
```

The `#web` context variable tells Copilot to search the internet, pulling from blog posts, Stack Overflow, and documentation sites. This gives you community opinions and comparison articles that GitHub code search alone would miss.

**Round 4 -- Read and summarize a specific repo**

Once you have a candidate, ask Copilot to analyze it:

```text
#fetch https://github.com/unionai-oss/pandera

Summarize this repo: what problem does it solve, what are its key features, and what is the license?
```

The `#fetch` context variable retrieves the page content so Copilot can summarize it in context.

**Round 5 -- Compile your research summary**

Ask Copilot to help you organize what you found:

```text
Based on our conversation, create a research summary table comparing pandera, great-expectations, and pydantic for CSV validation. Include: purpose, last release, stars, license, and fit for a data engineering team.
```

Expected output (Copilot generates a table like this):

| Criteria | pandera | great-expectations | pydantic |
| --- | --- | --- | --- |
| Purpose | DataFrame schema validation | Full data quality suite | General data validation |
| Last release | 2025-09 | 2025-08 | 2025-10 |
| Stars | ~3.5k | ~10k | ~20k |
| License | MIT | Apache 2.0 | MIT |
| Fit for DE team | High (DataFrame-native) | High (pipeline-native) | Medium (not DataFrame-specific) |

> **Key takeaway**: The research workflow is `@github` (code search) then `#web` (broader context) then `#fetch` (deep-dive on a candidate) then summarize. Each step narrows the search and builds confidence before you write any code.

#### Quick Reference: Search Context Variables

| Variable | What it does | When to use |
| --- | --- | --- |
| `@github` | Searches GitHub repos, code, issues, discussions | Finding existing repos, code patterns, community solutions |
| `#web` | Searches the internet via Bing | Comparison articles, blog posts, opinions, recent announcements |
| `#fetch` | Retrieves a specific URL and loads it as context | Reading a README, docs page, or specific file from a repo |
| `#file` | Loads a local file as context | Comparing external findings against your existing code |

### Step 3. Review Official Documentation And Frameworks

Goal of the step:

- Use authoritative sources as quality baselines before building.

Exact action:

- For Azure workloads, review the [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/).
- For data patterns, check official SDK docs, quickstarts, and sample repos.
- Ask Copilot to summarize key patterns: `Summarize the retry and error-handling patterns in the Azure SDK for Python`.

What success looks like:

- The learner can point to at least one official pattern that applies to their use case.

Common failure mode and fix:

- Failure: The learner relies only on community posts and skips official docs.
- Fix: Require at least one official source in every research summary.

### Step 4. Build On What You Found

Goal of the step:

- Turn research into reusable building blocks instead of discarding it.

Exact action:

- Create building blocks from research findings:
  - **Instruction files** (`.github/instructions/*.instructions.md`): Encode patterns you found.
  - **Prompt templates** (`.github/prompts/*.prompt.md`): Turn common research queries into reusable prompts.
  - **Starter projects** (`labs/*/starter/`): Fork or adapt a high-quality repo as a starting point.
  - **Reference docs** (`references/*.md`): Summarize evaluations and link to sources.

What success looks like:

- The learner creates at least one building block that the team can reuse.

Common failure mode and fix:

- Failure: The learner copies code without understanding or attribution.
- Fix: Require a one-paragraph summary of what was adapted and why, plus a link to the source.

### Step 5. Document Sources And Attribution

Goal of the step:

- Ensure traceability and respect for prior work.

Exact action:

- Add a "Sources" or "References" section to any building block or module that draws on external work.
- Include: repo URL, author or org, license, and what was used or adapted.

What success looks like:

- Every building block includes at least one source link.

Common failure mode and fix:

- Failure: The learner forgets attribution.
- Fix: Add a "References" heading to every template as a structural reminder.

## Hands-On Lab Reference

See [labs/09-research-and-building-blocks/README.md](../../labs/09-research-and-building-blocks/README.md).

## Validation Checklist

- [ ] Learner can describe the Research > Ask > Edit > Plan > Agent workflow.
- [ ] Learner evaluated at least 2-3 existing repos using structured criteria.
- [ ] Learner consulted at least one official documentation source.
- [ ] Learner created at least one reusable building block (instruction file, prompt template, or reference doc).
- [ ] Building block includes source attribution.

## Reflection And Extension Tasks

- What research shortcuts are tempting but risky for your team?
- How would you maintain a shared library of building blocks across your team?
- When should you build from scratch versus adapting existing work?
- How would you evaluate whether a community repo is safe to use in a corporate environment?

## References

- [copilot-agent-beginner-best-practices.md](../../references/copilot-agent-beginner-best-practices.md) -- Research > Ask > Edit > Plan > Agent workflow
- [skills-agents-and-plugins-differences.md](../../references/skills-agents-and-plugins-differences.md) -- Mechanism decision guide
- [What are Agents, Skills, and Instructions](https://awesome-copilot.github.com/learning-hub/what-are-agents-skills-instructions/) -- Fundamentals baseline for choosing advanced artifacts
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/) -- Quality baseline
- [GitHub Search Documentation](https://docs.github.com/search-github) -- Advanced search filters
