# Beginner Best Practices For GitHub Copilot Agents In VS Code

## Learning Objectives

By the end of this module, learners should be able to:

- Choose the right Copilot interaction mode for the task: Ask, Plan, or Agent.
- Write prompts that are specific, scoped, and grounded in the right context.
- Review AI-generated changes before accepting them.
- Use custom instructions to make Copilot more consistent across repeated work.
- Recognize the limits of AI agents and apply basic safety and verification guardrails.

## Prerequisites And Setup

Initial target audience:

- Business intelligence teams
- Data science teams
- Data engineering teams

Required setup:

- GitHub Copilot is enabled for the learner's account.
- Visual Studio Code is installed with GitHub Copilot and GitHub Copilot Chat enabled.
- Agents are enabled in VS Code if the organization allows them.
- The learner has a small workspace open in VS Code so prompts have real context.

Success looks like:

- The Chat view opens successfully.
- The learner can see the agent picker and model picker.
- The learner can submit a prompt and review the result.

Common failure mode and fix:

- If agents are missing, confirm the account has Copilot access and that agent features are enabled by policy.

## Walkthrough

Recommended beginner workflow:

1. Start with `Ask` when you need explanation, orientation, or low-risk guidance.
2. Use `Plan` when the task is multi-step and you want to review the approach before changes are made.
3. Use `Agent` only after the task is clear enough that autonomous edits are appropriate.
4. Add context explicitly with `#` references when the workspace is large or the request is ambiguous.
5. Review diffs, terminal actions, and outputs before treating the result as correct.
6. Capture repeated preferences in instructions instead of restating them in every prompt.

## Best Practices For Beginners

### 1. Match The Agent To The Job

Use the lightest-weight option that fits the task.

- Use `Ask` for explanation, concept checks, and file understanding.
- Use `Plan` for feature design, training-outline generation, or breaking a large task into stages.
- Use `Agent` for well-scoped implementation work where you are ready to review edits.

Why this matters:
Beginners often give a high-autonomy agent a vague prompt and then spend more time undoing changes than reviewing useful work.

### 2. Keep Prompts Specific And Narrow

Prefer a small, testable ask over a broad one.

Better prompt:
`Review this README and add a validation checklist for a beginner lab.`

Weaker prompt:
`Make this training better.`

Useful prompt ingredients:

- Goal
- Scope
- Constraints
- Expected output
- Files or folders to use

Example:
`Using #codebase, draft a beginner-friendly README for a VS Code lab that teaches a BI, DS, or DE team how to use Copilot safely. Keep it Windows-first, include validation steps, and do not create more than one file.`

### 3. Give The Agent The Right Context

Do not assume the model sees everything you mean.

- Use the active file and selection for local questions.
- Add `#file`, `#folder`, or `#codebase` when the answer depends on workspace content.
- Use `#fetch <URL>` when you need current web documentation.
- Use `@vscode` or other chat participants when the question is tool-specific.

Why this matters:
Good context reduces hallucination, avoids generic answers, and helps the model choose the right files or references.

### 4. Break Large Tasks Into Smaller Turns

Do not start with a compound request if the learner cannot evaluate the output.

Preferred sequence:

1. Ask for a plan.
2. Review and adjust the plan.
3. Implement one part.
4. Review the result.
5. Continue to the next part.

This is especially important for beginners because it makes the agent's reasoning and outputs easier to inspect.

### 5. Review Before Accepting Changes

Treat Copilot as a fast collaborator, not an authority.

- Review inline diffs.
- Check file names and placement.
- Verify commands before running them.
- Confirm the output matches the original ask.
- Discard or refine changes that solve the wrong problem.

Minimum beginner rule:
Never accept a change you cannot explain.

### 6. Verify Facts, Commands, And Outputs

Copilot can be helpful and still be wrong.

- Validate commands in the stated shell.
- Compare technical claims against official docs.
- For generated content, confirm completeness and consistency.
- For code, run the relevant checks or manual validation.

Important limit:
GitHub states that learners remain responsible for reviewing and validating generated output.

### 7. Use Custom Instructions For Repeated Preferences

Once a team repeats the same guidance, move it into instructions.

Good candidates for instructions:

- Preferred writing style
- Training module structure
- Validation requirements
- Folder conventions
- Windows-first command expectations

Keep instructions concise, focused, and limited to non-obvious rules.

### 8. Watch Context Window Growth

Long sessions accumulate noise.

- Start a new session when the task changes significantly.
- Use `/compact` if the session is getting long but should stay focused.
- Avoid mixing unrelated tasks into one conversation.

### 9. Prefer Official Sources For Beginner Learning

For training content, ground guidance in first-party references from:

- VS Code documentation
- GitHub Copilot documentation
- Official product tutorials and how-to guides

This reduces drift and makes the material easier to maintain.

### 10. Teach Safe Skepticism Early

Beginners should learn these habits immediately:

- AI output is draft output.
- Good prompts reduce error; they do not eliminate error.
- The user owns the final decision.
- Sensitive data should not be pasted casually into prompts.

## Hands-On Lab Reference

Use the accompanying lab to practice:

- Choosing the right mode for a task.
- Improving vague prompts.
- Adding context with `#file`, `#codebase`, and `#fetch`.
- Reviewing and validating output.

Lab files:

- `labs/01-beginner-copilot-agent-best-practices/README.md`
- `labs/01-beginner-copilot-agent-best-practices/starter/README.md`
- `labs/01-beginner-copilot-agent-best-practices/solution/README.md`

## Audience-Specific Examples

- BI example: ask Copilot to improve a lab README for a Power BI or SQL reporting workflow without changing the business rules.
- DS example: ask Copilot to explain a notebook workflow, summarize model evaluation steps, or draft a reproducible experiment checklist.
- DE example: ask Copilot to review a pipeline README, clarify data movement steps, or generate a safe validation checklist for schema or job changes.

## Validation Checklist

- The learner can describe when to use `Ask`, `Plan`, and `Agent`.
- The learner can improve a vague prompt into a specific one.
- The learner can add context with `#file`, `#codebase`, or `#fetch`.
- The learner reviews AI edits before accepting them.
- The learner can explain why instructions files help with repeatability.
- The learner can identify at least three limitations or risks of AI-generated output.

## Reflection Tasks

- Which Copilot mode feels safest for beginners, and why?
- What type of context most improves answer quality in your workflow?
- What is one example of an answer that looked correct but still required verification?
- Which repeated team preference should become a custom instruction?

## References

See the shared reference file: [Beginner Copilot Agent Best Practices](../../references/copilot-agent-beginner-best-practices.md).

The slide assets for this module are here:

- `materials/01-beginner-copilot-agent-best-practices/slides/slide-outline.md`
- `materials/01-beginner-copilot-agent-best-practices/slides/presenter-deck.md`


