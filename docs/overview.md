# Jupyter Governance Overview

:::{note}
Jupyter transitioned from a [Benevolent Dictator For Life (BDFL) + Steering Council](archive/governance.md) governance model to this current governance model in December 2022.

This document provides a brief informational summary of the Project Jupyter governance model. In case of any substantive discrepancy with the official descriptions of each body, the underlying governance documents should be considered as the source of truth, and we will update this overview as needed.
:::


```mermaid
---
title: Jupyter Governance
config:
  themeVariables:
    fontSize: 12px
  flowchart:
    nodeSpacing: 12
    rankSpacing: 14
    padding: 4
    diagramPadding: 4
    subGraphTitleMargin:
      top: 0
      bottom: 10
---
flowchart TB
  NF["NumFOCUS"]

  subgraph LFAM["Linux Foundation Ecosystem"]
    LFC["LF Charities<br/><small>501(c)(3)</small>"]
    LF["Linux Foundation<br/><small>&nbsp;501(c)(6)&nbsp;</small>"]
  end

  subgraph JF["Jupyter Foundation"]
    PM["Premier Members"]
    GM["General Members"]
    AM["Associate Members"]
    GB["Governing Board"]
    FUND[("Funds")]
  end

  subgraph PJ["Project Jupyter"]
    UOC(["Union of Councils"])
    EC["Executive Council"]
    SC["Standing Committees"]
    WG["Working Groups"]
    SSC["Software Steering Council"]

    subgraph SP["Subprojects"]
      direction LR
      subgraph SPA[" "]
        direction LR
        A1["Frontends"]
        A2["JupyterHub &amp; Binder"]
        A3["Voilà"]
        A4["Server"]
        A5["Widgets"]
        A6["Kernels"]
        A7["Foundations & Standards"]
        A8["Security"]
        A9["Accessibility"]
        A10["Jupyter Book"]
      end
      subgraph SPB[" "]
        direction LR
        B1["nbdime"]
        B2["nbgrader"]
        B3["nbviewer"]
        B4["ipyparallel"]
        B5["other repos"]
      end
    end
  end

  NF -.-> LFC
  LFC ==> PJ
  LF ===> JF

  PM -->|"1 each"| GB
  GM -->|"1 per 5 · max 3"| GB
  AM -.-x|"none"| GB
  EC ==>|"all"| GB
  PM & GM -.-> FUND
  GB ==> FUND
  FUND ==> PJ

  UOC --> EC
  EC --> SC
  EC --> WG
  EC --> SSC
  SC --> SSC
  WG -.-> SSC
  SSC <-->|"1 each"| SPA
  SSC -->|"council"| SPB

  classDef legal fill:#EEF2FF,stroke:#4F46E5,color:#1E1B4B
  classDef money fill:#FEF3C7,stroke:#B45309,color:#451A03
  classDef ec fill:#F37726,stroke:#B4501A,color:#FFFFFF,font-weight:bold
  classDef ssc fill:#FFE3CC,stroke:#F37726,stroke-width:2px,color:#3B1D0A
  classDef body fill:#FFF8F2,stroke:#E0A27A,color:#3B1D0A
  classDef sp fill:#FFFFFF,stroke:#E0A27A,color:#3B1D0A
  classDef old fill:#F3F4F6,stroke:#9CA3AF,stroke-dasharray:4 3,color:#6B7280

  class LF,LFC legal
  class PM,GM,AM,GB,FUND money
  class EC ec
  class SSC ssc
  class UOC,SC,WG body
  class A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5 sp
  class NF old

  style LFAM fill:#F8F9FF,stroke:#A5B4FC,color:#312E81
  style JF fill:#FFFBEB,stroke:#F59E0B,color:#78350F
  style PJ fill:#FFFDFB,stroke:#F37726,stroke-width:2px,color:#9A3412
  style SP fill:#FFFFFF,stroke:#E0A27A,color:#9A3412
  style SPA fill:#FFF8F2,stroke:#E0A27A
  style SPB fill:#FFF8F2,stroke:#E0A27A,stroke-dasharray:4 3
```


Jupyter’s governance model is anchored on three bodies that complement each other:

1. The [**Executive Council (EC)**](executive_council.md) is ultimately responsible for all dimensions of the Project (including, but not limited to, software, legal, financial, community, operations, inclusion and diversity, etc.). The members of the EC actively work to carry out the Project's mission in accordance with its values and to support operations through delegation to the Software Steering Council (SSC), Software Subprojects, Standing Committees, and Working Groups. These other bodies will report to the EC, and the EC is expected to support, oversee, manage, and ensure the success of operations across Jupyter. For more detail, see the [Executive Council document](executive_council.md).

   **Current Members:**

   ```{team-members} executive_council
   ```

2. The [**Software Steering Council (SSC)**](software_steering_council.md) has jurisdiction over software-related decisions across Project Jupyter, with a primary focus on coordination across projects and decisions that have impact across many Jupyter Subprojects. It is also a mechanism for representatives of each project to share information and expertise. Technical decisions and processes where the SSC isn't explicitly involved are automatically delegated to the individual projects to manage their day-to-day activities, create new repositories in their orgs, etc., with independence and autonomy. For more details, see the [Software Steering Council document](software_steering_council.md).

   **Current Members:**

   ```{team-members} software_steering_council
   ```

3. The [**Jupyter Foundation**](./jupyter_foundation.md) is a directed fund of the Linux Foundation 501(c)(6) that exists to provide resources and strategic counsel to Project Jupyter. The Executive Council serves on the Jupyter Foundation Governing Board. For more details, see the [Jupyter Foundation document](./jupyter_foundation.md).

   **Current Governing Board Members:**

   ```{team-members} jupyter_foundation
   ```

Additionally, the Executive Council (EC) receives input from a Community Advisory Panel. This panel advises the EC with perspectives and connections that may reach beyond the active Jupyter community.

## Other major components of the organization

In addition to these three bodies, the following are other major parts of the Project related to governance.

### Software Subprojects

[Software Subprojects](software_subprojects.md) in the Jupyter community are official areas of focus and effort within the Jupyter ecosystem. They often map to a single GitHub organization. Subprojects must abide by the [Jupyter Code of Conduct](conduct/code_of_conduct.md), Jupyter decision-making and governance processes (e.g. respecting the project's trademark policies), as well as commit to certain technical limitations and scope. Each Subproject maintains a Subproject Council and elects one person from the Subproject Council to serve on the Software Steering Council. For more details, see the [Software Subprojects document](software_subprojects.md).

### Standing Committees and Working Groups

In addition to the software work on Jupyter that is coordinated through the Software Steering Council (SSC), much of the project’s work expands beyond software. Examples include code of conduct incident response, diversity and inclusion, operations, legal, fundraising, events, community, and marketing. [Standing Committees and Working Groups](standing_committees_and_working_groups.md) carry out this non-software related work of the project by delegation from the Executive Council (EC).

The primary difference between Standing Committees and Working Groups is that Standing Committees are intended to be permanent; they are only created and dissolved by a joint vote of the EC and SSC. In contrast, Working Groups can be created and dissolved by the EC acting alone.

For more details, see the [Standing Committees and Working Groups document](standing_committees_and_working_groups.md).

### Union of Councils

The Union of Councils represents the combination of councils, sub-councils, and working groups in Jupyter.
See [the Union of Councils section](#union-of-councils) for more information.


### Distinguished Contributors

The [Distinguished Contributors](distinguished_contributors.md) are a group of Jupyter community members that have gone above-and-beyond in their support of the project over the years, making substantial and sustained contributions in any area of activity (software development, governance, community engagement, events, etc.). The Jupyter community confers membership in this group as a way of recognizing their effort and saying “thank you.” For more details, see the [Distinguished Contributors document](distinguished_contributors.md).

## Decision-making and voting procedures

The EC, SSC, Standing Committees and Working Groups all use uniform voting procedures outlined in the [Decision-Making Guide](decision_making.md).

