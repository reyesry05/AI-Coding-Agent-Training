# Repository Visibility And Sharing

## Purpose

This reference explains how this training repository is intended to be shared and when it should remain public versus private.

## Current Decision

- Current visibility: public
- Reason: the repository content is generic GitHub Copilot and VS Code training material.
- Constraint: no company-specific code, credentials, architecture details, customer data, or internal-only procedures should be stored here.

## When Public Is Appropriate

Use a public repository when:

- the content is generic and reusable,
- examples do not expose internal systems,
- screenshots and sample prompts are sanitized,
- references point to public first-party documentation,
- the training value improves when the material is easy to share.

## When Private Is Required

Use a private repository when:

- the content contains internal architecture or operating procedures,
- examples reference private repositories, internal URLs, or internal tools,
- screenshots expose company data,
- the material includes credentials, secrets, or environment-specific details,
- the audience is restricted to internal employees or partners.

## Practical Review Checklist Before Publishing

- Verify that prompts do not mention internal project names unless they are already public.
- Verify that screenshots do not show internal URLs, tenant names, emails, tokens, or data.
- Verify that sample files do not contain confidential business logic.
- Verify that repo history does not include accidentally committed secrets.
- Verify that references point to public documentation where possible.

## Recommended Sharing Model

For this repository:

- keep the generic curriculum public,
- separate future internal variants into a private repository,
- document the boundary clearly so contributors know what can be published.

## Related Files

- `README.md`
- `CONTRIBUTING.md`
- `.github/copilot-instructions.md`
