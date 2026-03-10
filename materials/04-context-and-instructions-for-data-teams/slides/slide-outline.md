# Slide Outline: Context And Instructions For Data Teams

## Slide 1. Title
- Context And Instructions For Data Teams
- Better context, better Copilot output

Speaker note:
- Assume learners can already write safer prompts from module 03 and point forward to module 05, where those context habits are applied to notebooks, SQL, and pipelines.

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
- Attach a KPI glossary or semantic model note
- Ask for a business-language explanation of gross margin logic
- Ask where validation guidance for monthly revenue should live

## Slide 7. DS Example
- Attach a notebook header or experiment README
- Ask for environment, package, data snapshot, and random-seed gaps
- Identify repeated experiment guidance worth turning into instructions

## Slide 8. DE Example
- Use `#codebase` to find validation or troubleshooting points in an ingestion workflow
- Identify repeatable rules for backfill runs and upstream table checks

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

## Slide 12. Context Comparison Exercise
- create before-and-after context comparison
- identify one instruction candidate
- decide whether to start a fresh chat

## Slide 13. Readiness Check
- learner can improve output with context
- learner can name one instruction candidate
- learner can explain session hygiene

## Slide 14. Instruction Debrief
- What context helped most?
- What team rule should become permanent?

## Slide 15. References
- VS Code chat context docs
- VS Code custom instructions docs
- VS Code AI best practices
- Workspace instructions: `.github/copilot-instructions.md`
- Workspace reference: `references/copilot-agent-beginner-best-practices.md`
