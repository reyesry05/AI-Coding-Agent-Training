# Slide Outline: Review And Verify AI Output For Data Work

## Slide 1. Title
- Review And Verify AI Output For Data Work
- BI, DS, and DE review habits

Speaker note:
- Assume learners already know how to make safer low-risk improvements from module 05 and point forward to module 07, where the same review habits are applied in shared repositories.

## Slide 2. Learning Objectives
- identify data-team-specific risks
- review beyond wording and style
- document human validation work
- make keep, revise, or reject decisions

## Slide 3. Why Review Is Different In Data Work
- business meaning can drift
- reproducibility can break
- operational assumptions can be missed

## Slide 4. Review Categories
- business correctness
- reproducibility
- operational reliability
- scope and fit

## Slide 5. BI Review Lens -- Spot The Business Logic Error
- Scenario: AI rewrote a DAX Net Revenue measure
- Error: AI silently dropped the Discounts subtraction
- Impact: net revenue overstated in every report
- Verdict: Reject -- always compare to the approved definition

## Slide 6. DS Review Lens -- Spot The Reproducibility Gap
- Scenario: AI added a preprocessing shuffle to a notebook cell
- Error: `df.sample(frac=1)` has no random seed, defeating `random_state=42` in `train_test_split`
- Impact: every run produces a different split
- Verdict: Revise -- add seed to `.sample()` or remove the shuffle

## Slide 7. DE Review Lens -- Spot The Dependency Issue
- Scenario: AI optimized a pipeline SQL query by adding a JOIN
- Error: new JOIN to `staging.products` creates an undeclared upstream dependency
- Impact: if products table is not refreshed before this job, data is stale or missing
- Verdict: Reject -- the new join is not in the DAG schedule

## Slide 8. What Counts As Evidence
- source file comparison
- explicit checklist
- visible validation note
- diff review

## Slide 9. Human Validation Boundaries
- what AI can draft
- what humans must still decide

## Slide 10. Keep, Revise, Or Reject
- keep when bounded and correct
- revise when useful but incomplete
- reject when meaning or risk is unclear

## Slide 11. Build Review Into Prompts
- preserve meaning
- include validation
- list assumptions
- limit scope

## Slide 12. Review Decision Exercise
- review one AI result
- identify one risk
- identify one human follow-up
- make a decision

## Slide 13. Decision Readiness Check
- learner can name a risk category
- learner can review beyond style
- learner can justify a decision

## Slide 14. Approval Debrief
- what risk matters most for your team?
- what should always need human approval?

## Slide 15. References
- VS Code AI best practices
- GitHub Copilot best practices
- Workspace module: `materials/06-review-and-verify-ai-output-for-data-work/README.md`
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
