# Curriculum Map

This file provides a visual overview of the current training sequence for BI, data science, and data engineering teams.

```mermaid
flowchart TD
    A[01 Beginner Best Practices] --> B[02 Set Up GitHub Copilot Agents]
    B --> C[03 First Safe Prompts]
    C --> D[04 Context And Instructions]
    D --> E[05 Notebooks SQL And Pipelines]
    E --> F[06 Review And Verify AI Output]
    F --> G[07 Repo Workflows In GitHub And Azure DevOps]

    A1[Lab 01 Beginner Guardrails] -. practice .-> A
    B1[Lab 02 Setup And Availability] -. practice .-> B
    C1[Lab 03 Safe Prompts] -. practice .-> C
    D1[Lab 04 Context And Instructions] -. practice .-> D
    E1[Lab 05 Data Artifacts] -. practice .-> E
    F1[Lab 06 Review And Validation] -. practice .-> F
    G1[Lab 07 Repo Safe Changes] -. practice .-> G

    subgraph Audience Focus
        BI[Business Intelligence]
        DS[Data Science]
        DE[Data Engineering]
    end

    BI --> A
    DS --> A
    DE --> A
```

## Reading The Map
- Modules 01 through 07 are designed as a progressive sequence.
- Each module has a matching practice lab.
- The first four modules build safe beginner habits.
- Modules 05 through 07 shift into more realistic data-team workflows.

## Intended Use
- Use this map in kickoff sessions to explain the full path.
- Use it in facilitator briefings to show where each lab fits.
- Update the diagram whenever the curriculum sequence changes.
