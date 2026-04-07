# Lab: Research And Building Blocks

## Scenario Context

Your team is starting a new data validation project. Instead of asking Copilot to generate everything from scratch, you will research existing solutions, evaluate them, and create reusable building blocks that the team can build on.

## Learner Goal

By the end of this lab, you should be able to:

- conduct structured research using GitHub search and official docs
- evaluate existing repos against quality criteria
- create at least one reusable building block from your research
- document sources and attribution

## Starter State

You begin with:

- a blank research summary document
- a real or hypothetical data validation problem for your team
- VS Code with Copilot Chat open
- no prior research on the topic

## Target State

You finish with:

- a research summary with 2-3 evaluated candidates
- one reusable building block (instruction file, prompt template, or reference doc)
- source attribution for everything used

## Prerequisites And Setup

Goal of the step:

- Define the problem before researching solutions.

Exact actions:

- Write a one-sentence problem statement (for example: "We need a reusable data validation pattern for CSV files ingested into our warehouse").
- Open VS Code and Copilot Chat.

What success looks like:

- You have a clear, bounded problem statement.

Common failure mode and fix:

- Failure: The problem statement is too broad ("improve data quality").
- Fix: Narrow to one specific outcome ("validate column types and null counts before loading").

## Lab Tasks

### Task 1. Search GitHub For Existing Solutions

Goal of the step:

- Find candidate repos or templates that address your problem.

Exact action:

- In Copilot Chat, try:

```text
@github Search for Python CSV validation libraries with good test coverage, updated in the last year
```

- Also search GitHub directly with filters: `stars:>20 language:python topic:data-validation pushed:>2025-01-01`.
- Record at least 3 candidates with their URLs.

What success looks like:

- A list of 3 candidate repos with URLs.

Common failure mode and fix:

- Failure: All results are outdated or unmaintained.
- Fix: Broaden the search terms or check official SDK samples.

### Task 2. Evaluate Candidates

Goal of the step:

- Apply structured criteria to narrow your shortlist.

Exact action:

- For each candidate, fill in this table:

| Criteria | Candidate 1 | Candidate 2 | Candidate 3 |
| --- | --- | --- | --- |
| Last commit date | | | |
| Stars / forks | | | |
| Test coverage | | | |
| License | | | |
| Fits our problem? | | | |

- Ask Copilot to help: `Summarize the README and key features of [repo URL]`.

What success looks like:

- A completed evaluation table with a clear winner or top two.

Common failure mode and fix:

- Failure: The learner picks a repo based on stars alone.
- Fix: Require at least three criteria before making a decision.

### Task 3. Review Official Documentation

Goal of the step:

- Cross-check your research against authoritative sources.

Exact action:

- Search for official patterns that relate to your problem:

```text
Summarize data validation best practices from the Azure Well-Architected Framework
```

- Or for a specific SDK: `What validation patterns does the pandas documentation recommend for CSV ingestion?`
- Note at least one official pattern that applies.

What success looks like:

- One documented official pattern with a source link.

Common failure mode and fix:

- Failure: The learner skips official docs entirely.
- Fix: Require at least one official source before creating any building block.

### Task 4. Create A Reusable Building Block

Goal of the step:

- Turn your research into something the team can reuse.

Exact action:

- Choose one building block type:
  - **Instruction file**: Create `.github/instructions/data-validation.instructions.md` encoding the patterns you found
  - **Prompt template**: Create `.github/prompts/validate-csv-data.prompt.md` with a reusable validation prompt
  - **Reference doc**: Create `references/csv-validation-patterns.md` summarizing your evaluation

- Include a "References" section with links to every source.

What success looks like:

- One file committed to the repo that the team can use immediately.

Common failure mode and fix:

- Failure: The building block copies code without explanation.
- Fix: Add a one-paragraph summary of what was adapted and why.

### Task 5. Peer Review

Goal of the step:

- Verify the building block is clear and reusable.

Exact action:

- Share the building block with a partner.
- The partner should be able to understand and use it without additional explanation.
- If the partner has questions, revise the building block.

What success looks like:

- A partner confirms the building block is self-explanatory.

Common failure mode and fix:

- Failure: The building block assumes context the partner does not have.
- Fix: Add a "Purpose" or "When to use" section at the top.

## Suggested Prompts

```text
@github Search for Python data validation frameworks updated in the last year
```

```text
Summarize the README and key features of [paste repo URL]
```

```text
Compare these two repos for data validation: [URL 1] vs [URL 2]
```

```text
Summarize data validation best practices from the Azure Well-Architected Framework
```

```text
Create an instruction file for CSV data validation based on these patterns: [paste notes]
```

## Expected Observable Output

- A research summary document with 2-3 evaluated candidates
- A completed evaluation table
- One reusable building block file (instruction, prompt, or reference)
- Source attribution in every artifact

## Validation Checklist

- [ ] Research summary contains at least 3 candidates with URLs
- [ ] Evaluation table has at least 3 criteria filled in per candidate
- [ ] At least one official documentation source is cited
- [ ] One reusable building block file is created
- [ ] Building block includes a References section with source links
- [ ] A peer confirmed the building block is usable without extra context

## Reflection And Extension Tasks

- How much time did research save compared to generating from scratch?
- What criteria matter most for your team when evaluating external repos?
- How would you keep your building block library up to date?
- What risks exist when adapting community code for corporate use?

## Solution Guidance

See `solution/` for an example research summary, evaluation table, and building block.
