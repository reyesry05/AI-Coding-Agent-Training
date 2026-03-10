# Presenter Deck: Context And Instructions For Data Teams

## Slide 1. Title
On-screen content:
- Context And Instructions For Data Teams
- Better context, better Copilot output

Presenter notes:
- This module is about reliability. The same model can look weak or strong depending on the context supplied.

## Slide 2. Learning Objectives
On-screen content:
- Distinguish implicit and explicit context
- Choose `#file` or `#codebase`
- Identify recurring rules for instructions
- Avoid context pollution in long sessions

Presenter notes:
- Explain that this module moves from prompt quality to context quality.

## Slide 3. Why Context Matters
On-screen content:
- Better context reduces generic output
- Better context reduces hallucination risk
- Better context makes review easier

Presenter notes:
- Stress that context is one of the highest-leverage improvements a learner can make.

## Slide 4. Sources Of Context
On-screen content:
- Active file and selection
- `#file`
- `#codebase`
- `#fetch`
- Reusable instructions

Presenter notes:
- Introduce instructions as a way to avoid repeating stable team preferences.

## Slide 5. Use The Narrowest Useful Context
On-screen content:
- Single file question: `#file`
- Multi-file discovery: `#codebase`
- Current docs: `#fetch`

Presenter notes:
- Point out that too much context can be as unhelpful as too little.

## Slide 6. BI Example
On-screen content:
- Attach a report README
- Ask for business-language explanation
- Ask where validation guidance belongs

Presenter notes:
- Keep the example tied to analytics documentation and business meaning.

## Slide 7. DS Example
On-screen content:
- Attach a notebook note
- Ask for prerequisites and reproducibility gaps
- Identify repeated experiment guidance

Presenter notes:
- Emphasize the value of making assumptions explicit.

## Slide 8. DE Example
On-screen content:
- Use `#codebase` to find validation or troubleshooting points
- Identify repeatable pipeline rules

Presenter notes:
- Use a workflow example that spans files so `#codebase` feels justified.

## Slide 9. When Context Becomes Noise
On-screen content:
- unrelated chat topics
- too many attached files
- stale task history
- generic results from overloaded context

Presenter notes:
- This is where session hygiene matters. Starting fresh is often the right move.

## Slide 10. What Belongs In Instructions
On-screen content:
- recurring team rules
- environment assumptions
- output standards
- validation requirements

Presenter notes:
- Distinguish stable defaults from one-off task details.

## Slide 11. Context Comparison Demo
On-screen content:
- Ask once without explicit context
- Ask again with `#file` or `#codebase`
- compare relevance and specificity

Presenter notes:
- This is the simplest demo in the module and often the most persuasive.

## Slide 12. Hands-On Lab
On-screen content:
- create before-and-after context comparison
- identify one instruction candidate
- decide whether to start a fresh chat

Presenter notes:
- Learners should leave with one concrete instruction idea, not just theory.

## Slide 13. Validation Checklist
On-screen content:
- learner can improve output with context
- learner can name one instruction candidate
- learner can explain session hygiene

Presenter notes:
- Require learners to describe the improvement, not just say it felt better.

## Slide 14. Reflection
On-screen content:
- What context helped most?
- What team rule should become permanent?

Presenter notes:
- Push learners to connect this to their real workflow.

## Slide 15. References
On-screen content:
- Chat context docs
- Custom instructions docs
- AI best practices

Presenter notes:
- Encourage teams to keep instructions small and high-value.
