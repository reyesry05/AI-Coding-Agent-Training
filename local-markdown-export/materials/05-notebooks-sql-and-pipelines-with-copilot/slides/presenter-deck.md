# Presenter Deck: Notebooks, SQL, And Pipelines With Copilot

## Slide 1. Title
On-screen content:
- Notebooks, SQL, And Pipelines With Copilot
- Safe data-team workflows

Presenter notes:
- This module is where Copilot starts touching higher-risk artifacts. The message is simple: explain first, edit later.

## Slide 2. Learning Objectives
On-screen content:
- Use Copilot safely with notebooks, SQL, and pipelines
- Separate explanation from editing work
- Require reproducibility and validation checks
- Preserve business and operational meaning

Presenter notes:
- Reinforce that data workflows often look simple on the surface but hide important assumptions.

## Slide 3. Why Data Artifacts Need Extra Care
On-screen content:
- plausible output can still be wrong
- data work has hidden assumptions
- reproducibility and operations matter

Presenter notes:
- Emphasize that readable AI output is not the same as correct data behavior.

## Slide 4. Start With Explanation
On-screen content:
- explain first
- identify assumptions
- ask for missing prerequisites

Presenter notes:
- This is the default safe move before any change request.

## Slide 5. Notebook Workflow
On-screen content:
- summarize notebook steps
- find reproducibility gaps
- add prerequisites or checklist

Presenter notes:
- Tie this to DS and analytics workflows where notebook execution context is often incomplete.

## Slide 6. SQL Workflow
On-screen content:
- explain joins, filters, aggregations
- preserve business meaning
- request comments before optimization

Presenter notes:
- Make it clear that optimization without business validation is not acceptable.

## Slide 7. Pipeline Workflow
On-screen content:
- explain flow and dependencies
- identify failure points
- add validation or troubleshooting notes

Presenter notes:
- Operational reliability is the main risk here.

## Slide 8. Safe Improvement Types
On-screen content:
- checklist
- prerequisites section
- troubleshooting note
- validation note

Presenter notes:
- These are useful because they improve clarity without changing core logic.

## Slide 9. What Not To Delegate Too Early
On-screen content:
- major logic rewrites
- business rule changes
- dependency-sensitive pipeline edits

Presenter notes:
- Tell learners that the point is not to avoid AI. The point is to sequence AI use correctly.

## Slide 10. Observable Outputs
On-screen content:
- explanation
- assumptions list
- checklist
- human validation note

Presenter notes:
- Observable outputs create a reviewable trail.

## Slide 11. Review Questions
On-screen content:
- what changed
- what stayed the same
- what still needs human validation

Presenter notes:
- These three questions work across notebooks, SQL, and pipeline documentation.

## Slide 12. Hands-On Lab
On-screen content:
- choose one artifact
- explain it
- identify risks
- add one low-risk improvement

Presenter notes:
- Keep the artifact small enough to review fully in the session.

## Slide 13. Validation Checklist
On-screen content:
- learner can distinguish safe vs risky edits
- learner can preserve meaning
- learner can record human review items

Presenter notes:
- Use this to check that learners are not drifting into over-delegation.

## Slide 14. Reflection
On-screen content:
- which artifact felt riskiest?
- what review rule matters most?

Presenter notes:
- Pull examples from BI, DS, and DE work separately if possible.

## Slide 15. References
On-screen content:
- prompt engineering guide
- AI best practices
- GitHub Copilot best practices

Presenter notes:
- Point learners back to first-party docs for product updates.
