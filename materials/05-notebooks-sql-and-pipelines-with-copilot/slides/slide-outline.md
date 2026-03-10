# Slide Outline: Notebooks, SQL, And Pipelines With Copilot

## Slide 1. Title
- Notebooks, SQL, And Pipelines With Copilot
- Safe data-team workflows

Speaker note:
- Assume learners can already control prompt quality and context, then point forward to module 06, where they formalize how to review and accept or reject AI output.

## Slide 2. Learning Objectives
- Use Copilot safely with notebooks, SQL, and pipelines
- Separate explanation from editing work
- Require reproducibility and validation checks
- Preserve business and operational meaning

## Slide 3. Why Data Artifacts Need Extra Care
- plausible output can still be wrong
- data work has hidden assumptions
- reproducibility and operations matter

## Slide 4. Start With Explanation
- explain first
- identify assumptions
- ask for missing prerequisites

## Slide 5. Notebook Workflow (DS) -- Before And After
- Before: bare Prophet fit/predict with no config or shape check
- After: AI adds seasonality flags, data-version comment, forecast horizon, row-count print
- Review: are seasonality settings and horizon correct for your data?
- Decision: Keep, Revise, or Reject?

## Slide 6. SQL Workflow (BI) -- Before And After
- Before: revenue query with MoM change but no comments or guards
- After: AI adds business-definition comment, prior-month column, MoM percentage, divide-by-zero guard
- Review: is the net revenue definition correct? Is the extra column useful or noise?
- Decision: Keep, Revise, or Reject?

## Slide 7. Pipeline Workflow (DE) -- Before And After
- Before: ADF copy activity with SELECT * and no date filter
- After: AI adds explicit columns, date filter, partitioned sink, retry and timeout policy
- Review: is the partition path correct? Is the timeout realistic for your data volume?
- Decision: Keep, Revise, or Reject?

## Slide 8. Safe Improvement Types
- checklist
- prerequisites section
- troubleshooting note
- validation note

## Slide 9. What Not To Delegate Too Early
- major logic rewrites
- business rule changes
- dependency-sensitive pipeline edits

## Slide 10. Observable Outputs
- explanation
- assumptions list
- checklist
- human validation note

## Slide 11. Review Questions
- what changed
- what stayed the same
- what still needs human validation

## Slide 12. Artifact Risk Exercise
- choose one artifact
- explain it
- identify risks
- add one low-risk improvement

## Slide 13. Readiness Check
- learner can distinguish safe vs risky edits
- learner can preserve meaning
- learner can record human review items

## Slide 14. Risk Debrief
- which artifact felt riskiest?
- what review rule matters most?

## Slide 15. References
- VS Code prompt engineering guide
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: `materials/05-notebooks-sql-and-pipelines-with-copilot/README.md`
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
