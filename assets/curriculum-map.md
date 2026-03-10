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
    G --> H[08 Advanced Skills Agents And Plugins]

    A1[Lab 01 Beginner Guardrails] -. practice .-> A
    B1[Lab 02 Setup And Availability] -. practice .-> B
    C1[Lab 03 Safe Prompts] -. practice .-> C
    D1[Lab 04 Context And Instructions] -. practice .-> D
    E1[Lab 05 Data Artifacts] -. practice .-> E
    F1[Lab 06 Review And Validation] -. practice .-> F
    G1[Lab 07 Repo Safe Changes] -. practice .-> G
    H1[Lab 08 Advanced Workflow Design] -. practice .-> H

    subgraph Audience Focus
        BI[Business Intelligence]
        DS[Data Science]
        DE[Data Engineering]
    end

    BI --> A
    DS --> A
    DE --> A

    subgraph Supporting References
        R1[Beginner Best Practices]
        R2[Developer Toolbox]
        R3[Copilot Chat Quick Commands]
        R4[Skills Agents And Plugins Differences]
        R5[Git And GitHub Desktop Reference]
    end

    R1 -. supports .-> A
    R2 -. supports .-> B
    R3 -. supports .-> C
    R4 -. supports .-> H
    R5 -. supports .-> G
```

## Reading The Map

- Modules 01 through 07 are the beginner core sequence.
- Module 08 is the advanced follow-on course.
- Each module has a matching practice lab.
- The first four modules build safe beginner habits.
- Modules 05 through 07 shift into more realistic data-team workflows.
- Module 08 focuses on choosing and governing advanced workflow building blocks.
- Supporting references provide standalone lookup material that reinforces specific modules.

## Supporting References To Module Mapping

| Reference | Primary Module |
| --- | --- |
| Beginner Best Practices | 01 Beginner Best Practices |
| Developer Toolbox | 02 Set Up GitHub Copilot Agents |
| Copilot Chat Quick Commands | 03 First Safe Prompts |
| Skills Agents And Plugins Differences | 08 Advanced Skills Agents And Plugins |
| Git And GitHub Desktop Reference | 07 Repo Workflows In GitHub And Azure DevOps |

## Intended Use

- Use this map in kickoff sessions to explain the full path.
- Use it in facilitator briefings to show where each lab fits.
- Use the reference mapping table to point learners to the right lookup material.
- Update the diagram whenever the curriculum sequence changes.
