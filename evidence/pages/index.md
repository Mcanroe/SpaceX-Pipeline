---
title: SpaceX Launch Data
hide_title: true
description: SpaceX Launch Tracker
---

# SpaceX Launch Data

This project tracks past and upcoming SpaceX launches. 

The data pipeline is structured as follows:

![pipeline](https://raw.githubusercontent.com/Mcanroe/SpaceX-Pipeline/refs/heads/main/evidence/static/pipeline.png)

Currently the pipeline runs once a week, is triggered by a cron job, and uses Github Actions as an orchestrator.


<details>
<summary>Why build this?</summary>
Space is cool. Data is cool. 

Combining space and data is even cooler.
</details>

---
<details>
<summary>Aren't there many SpaceX dashboards on GitHub already?</summary>
Yes, but most of them use an outdated API.
</details>

---
<details>
<summary>Why only SpaceX?</summary>
No particular reason. I might add other space agencies in the future.
</details>

---
<details>
<summary>Why use **insert tool choice**?</summary>

dlt - For a simple task like this, it didn't make sense to use other heavy ingestion tools.

dbt - Top dog for data transformation , offers built in data quality checks, and works really well with Motherduck unlike sqlmesh (which works but is not as intuitive).

Motherduck - This one's debatable , honestly the main reason is that their free plan is quite generous (unlike Snowflake that has an expiry date).

evidence - Looked really nice , unlike other BI tools their offering works really well for a static site aka personal projects. I also liked their code first approach rather than the usual drag and drop interface.
</details>


