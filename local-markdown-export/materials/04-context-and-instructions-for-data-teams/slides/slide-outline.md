# Slide Outline: Context And Instructions For Data Teams

## Slide 1. Title
- Context And Instructions For Data Teams
- Better context, better Copilot output

## Slide 2. Learning Objectives
- Distinguish implicit and explicit context
- Choose `#file` or `#codebase`
- Identify recurring rules for instructions
- Avoid context pollution in long sessions

## Slide 3. Why Context Matters
- Better context reduces generic output
- Better context reduces hallucination risk
- Better context makes review easier

## Slide 4. Sources Of Context
- Active file and selection
- `#file`
- `#codebase`
- `#fetch`
- Reusable instructions

## Slide 5. Use The Narrowest Useful Context
- Single file question: `#file`
- Multi-file discovery: `#codebase`
- Current docs: `#fetch`

## Slide 6. BI Example
- Attach a report README
- Ask for business-language explanation
- Ask where validation guidance belongs

## Slide 7. DS Example
- Attach a notebook note
- Ask for prerequisites and reproducibility gaps
- Identify repeated experiment guidance

## Slide 8. DE Example
- Use `#codebase` to find validation or troubleshooting points
- Identify repeatable pipeline rules

## Slide 9. When Context Becomes Noise
- unrelated chat topics
- too many attached files
- stale task history
- generic results from overloaded context

## Slide 10. What Belongs In Instructions
- recurring team rules
- environment assumptions
- output standards
- validation requirements

## Slide 11. Context Comparison Demo
- Ask once without explicit context
- Ask again with `#file` or `#codebase`
- compare relevance and specificity

## Slide 12. Hands-On Lab
- create before-and-after context comparison
- identify one instruction candidate
- decide whether to start a fresh chat

## Slide 13. Validation Checklist
- learner can improve output with context
- learner can name one instruction candidate
- learner can explain session hygiene

## Slide 14. Reflection
- What context helped most?
- What team rule should become permanent?

## Slide 15. References
- Chat context docs
- Custom instructions docs
- AI best practices
