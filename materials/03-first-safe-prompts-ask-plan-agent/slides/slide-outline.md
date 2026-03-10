# Slide Outline: First Safe Prompts For Ask, Plan, And Agent

## Slide 1. Title
- First Safe Prompts For Ask, Plan, And Agent
- Beginner module for BI, DS, and DE teams

Speaker note:
- Assume setup is complete from module 02 and point forward to module 04, where learners will improve output by supplying better context.

## Slide 2. Learning Objectives
- Choose Ask, Plan, or Agent appropriately
- Improve vague prompts into safe prompts
- Add scope, output, and validation criteria
- Review Agent output before accepting it

## Slide 3. Why First Prompts Matter
- Bad first prompts create bad first habits
- Safer prompts reduce wasted edits and rework
- Prompt quality matters more than prompt length

## Slide 4. Ask, Plan, And Agent At A Glance
- Ask: explain, orient, summarize
- Plan: break work into reviewable steps
- Agent: perform bounded implementation work

## Slide 5. Signs A Prompt Is Too Weak
- vague goal
- unclear scope
- missing audience
- no validation method
- too much autonomy too early

## Slide 6. Safe Prompt Formula
- Goal
- Scope
- Audience
- Expected output
- Validation step

## Slide 7. BI Example -- Prompt-Driven DAX Improvement
- Weak prompt: "make this measure better" produces bare `SUMX` with no guard
- Specific prompt: add error handling, business-definition comment, preserve logic
- AI output: zero-revenue guard, finance-approved comment, VAR pattern
- Review question: which output would you approve in a shared Power BI model?

## Slide 8. DS Example -- Prompt-Driven Notebook Improvement
- Weak prompt: "add documentation" produces one-line comment
- Specific prompt: add prerequisites cell with Python version, packages, data path, seed
- AI output: structured prerequisites block another DS can reproduce from
- Review question: which output helps a teammate reproduce the experiment?

## Slide 9. DE Example -- Prompt-Driven SQL Transformation Fix
- Weak prompt: "fix this query" adds COALESCE but misses key filters
- Specific prompt: add NULL check, filter test accounts, comment upstream dependency
- AI output: production-ready transform with operational context
- Review question: which output is safe to deploy to production?

## Slide 10. Compare Outputs By Mode
- Ask output: explanation
- Plan output: sequence
- Agent output: change proposal

## Slide 11. Review Before Accepting
- Inspect scope
- Check file count
- Verify one visible condition
- Reject or refine if needed

## Slide 12. Prompt Practice Drill
- Write one Ask prompt
- Write one Plan prompt
- Write one Agent prompt
- Compare outputs and record one validation step

## Slide 13. Readiness Check
- Learner can distinguish modes
- Learner can improve a weak prompt
- Learner can constrain Agent output

## Slide 14. Team Debrief
- Which mode feels safest to start with?
- What makes a prompt reviewable?

## Slide 15. References
- VS Code chat overview
- VS Code prompt engineering guide
- VS Code AI best practices
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
