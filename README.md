# SpaceX Launches Data Pipeline

[![View Live App](https://img.shields.io/badge/View_Live_App-Evidence-blue)](https://spacex.evidence.app/)
[![CI Pipeline Status](https://github.com/Mcanroe/SpaceX-Pipeline/actions/workflows/run_pipeline_workflow.yml/badge.svg)](https://github.com/Mcanroe/SpaceX-Pipeline/actions/workflows/run_pipeline_workflow.yml)

A data pipeline project that ingests, transforms, and visualises SpaceX launch data, providing a  tracker for past and upcoming missions. This project showcases an end-to-end data engineering workflow, from data extraction to interactive dashboard presentation.

## Architecture

![SpaceX Data Pipeline Architecture](https://raw.githubusercontent.com/Mcanroe/SpaceX-Pipeline/refs/heads/main/evidence/static/pipeline.png)

## Table of Contents

- [Overview](#overview)
- [Live Dashboard](#live-dashboard)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Getting Started / Local Setup](#getting-started--local-setup)
  - [Prerequisites](#prerequisites)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set up Python Environment](#2-set-up-python-environment)
  - [3. Configure MotherDuck (Data Warehouse)](#3-configure-motherduck-data-warehouse)
  - [4. Run the Data Pipeline](#4-run-the-data-pipeline)
  - [5. View the Dashboards](#5-view-the-dashboards)
- [Future To-Do's](#future-to-dos)

## Overview

This project was developed to explore modern data stack tools and to serve as a clean and simple tracker for upcoming SpaceX launches. 

Currently the pipeline runs like this:
- Ingestion of data from the [SpaceDevs API](https://ll.thespacedevs.com/docs/#/launches) into a bronze layer in Motherduck.
- Transforms and models the data using dbt into silver and gold layers, while using dbt tests to ensure data quality.
- Build and host the dashboard using Evidence.
- Schedule and automate the data refresh process using GitHub Actions (daily cron job at midnight UTC for `dlt` and `dbt build`) and the dashboard uses Evidence Cloud for scheduling (refresh at 12:05 AM UTC).

## Live Dashboard

Explore the interactive dashboard hosted on Evidence Cloud:
**[https://spacex.evidence.app/](https://spacex.evidence.app/)**

## Tech Stack

- **Data Ingestion:** [dlt (Data Load Tool)](https://dlthub.com/)
- **Data Transformation and Data Testing:** [dbt (Data Build Tool)](https://www.getdbt.com/)
- **Data Warehouse:** [MotherDuck](https://motherduck.com/)
- **Data Visualisation & BI:** [Evidence](https://evidence.dev/)
- **Orchestration/Automation:** [GitHub Actions](https://github.com/features/actions)
- **Programming Language:** Python
- **Package Management:** [uv](https://github.com/astral-sh/uv) (Recommended)

## Project Structure

```
SpaceX-Pipeline/
├── .github/workflows/
│   └── run_pipeline_workflow.yml # Pipeline automation workflow
├── dbt/                        # dbt project for data transformation
│   ├── models/                 # dbt models
│   │   ├── sources.yml
│   │   ├── silver/             # Staging/intermediate data models
│   │   │   ├── launches.sql
│   │   │   ├── pads.sql
│   │   │   └── models.yml      # Schema definitions and data tests for silver models
│   │   └── gold/               # Analytical/mart data models
│   │       ├── pad_overview.sql
│   │       ├── past_launches.sql
│   │       ├── upcoming_launches.sql
│   │       └── models.yml      # Schema definitions and data tests for gold models
│   ├── packages.yml            # dbt package dependencies (e.g., dbt_utils)
│   ├── dbt_project.yml
│   └── profiles.yml
├── dlt/                        # dlt Python scripts for ingestion
│   ├── .dlt/                   # dlt local configuration directory
│   │   └── secrets.toml        # MotherDuck credentials for dlt (uncommitted)
│   └── spacex_pipeline.py      # Data Ingestion script
├── evidence/                   # Evidence project for dashboards
│   ├── pages/                  # Markdown files for dashboard pages
│   ├── sources/motherduck/     # Source configurations for Evidence
│   │   └── connection.options.yaml # MotherDuck connection token (uncommitted)
├── .gitignore
├── pyproject.toml              # Project dependencies for uv
├── README.md
└── uv.lock                     # uv lock file
```

## Data Model

The data is modelled using `dbt`. Raw data is ingested by `dlt` and defined as sources in [`dbt/models/sources.yml`](dbt/models/sources.yml:1). Data quality and integrity are actively managed through `dbt` tests defined within the `models.yml` files for both silver and gold layers. These tests are automatically executed as part of the `dbt build` process.
- **Silver Layer ([`dbt/models/silver/`](dbt/models/silver/)):** Raw data is cleaned and standardised in this layer. Key models include [`launches.sql`](dbt/models/silver/launches.sql:1) for launch details and [`pads.sql`](dbt/models/silver/pads.sql:1) for launch pad information.
- **Gold Layer ([`dbt/models/gold/`](dbt/models/gold/)):** These models are the final, query-ready datasets used by the dashboards. They provide specific views like [`pad_overview.sql`](dbt/models/gold/pad_overview.sql:1), [`past_launches.sql`](dbt/models/gold/past_launches.sql:1), and [`upcoming_launches.sql`](dbt/models/gold/upcoming_launches.sql:1).

## Getting Started / Local Setup

Follow these steps to set up and run the project locally.

### Prerequisites

-   [Git](https://git-scm.com/)
-   [Python](https://www.python.org/downloads/) (version 3.12, as used in CI)
-   [uv](https://github.com/astral-sh/uv) (Recommended Python package manager). Install via `pip install uv` or see official `uv` documentation.
-   A [MotherDuck](https://motherduck.com/) account (the free plan is quite generous).
-   [Node.js and npm](https://nodejs.org/) (for running the Evidence frontend). For easy installation, consider the [Evidence VS Code Extension](https://docs.evidence.dev/install-evidence/).

### 1. Clone the Repository

```bash
git clone https://github.com/Mcanroe/SpaceX-Pipeline.git
cd SpaceX-Pipeline
```

### 2. Set up Python Environment

It's highly recommended to use a virtual environment. `uv` can create and manage this.

```bash
# Create a virtual environment (e.g., .venv)
uv venv
# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# Install dependencies into the virtual environment
uv sync --all-extras
```

### 3. Configure MotherDuck (Data Warehouse)

**a. MotherDuck Account & Token:**
   - Sign up or log in to [MotherDuck](https://motherduck.com/).
   - Obtain your MotherDuck service token from your MotherDuck settings. **Keep this token secure.**

**b. Configure dlt (for data ingestion):**
   The `dlt` script ([`dlt/spacex_pipeline.py`](dlt/spacex_pipeline.py:1)) loads data into a MotherDuck database named `spacex`. You need to provide your MotherDuck token and database name
   in the file named `dlt/.dlt/secrets.toml`. This file should be in your `.gitignore`.
   
   ```toml
   [destination.motherduck.credentials]
   database = "spacex"
   password = "YOUR_MOTHERDUCK_TOKEN"
   ```

**c. Configure dbt (for data transformation):**
   - Your [`dbt/profiles.yml`](dbt/profiles.yml:1) file needs to be configured to connect to MotherDuck. It's best to use the motherduck_token environment variable for this in order to not have to login on every run.
   - Set the `MOTHERDUCK_TOKEN` environment variable in your terminal session:

     ```bash
     export MOTHERDUCK_TOKEN="YOUR_MOTHERDUCK_TOKEN"
     ```
   - Run a quick test to ensure everything is set up correctly:
     ```bash
     dbt debug
     ```

**d. Configure Evidence (for dashboards):**
   - To install Evidence , refer to the [Evidence installation guide](https://docs.evidence.dev/install-evidence/).
   - To connect Evidence to MotherDuck:
      1. Run the Evidence development server.
      2. Add your MotherDuck token via the in-app settings UI.
   - For detailed instructions on setting up evidence with Motherduck, refer to the [Evidence MotherDuck documentation](https://docs.evidence.dev/core-concepts/data-sources/motherduck/#evidence-main-article).


### 4. Run the Data Pipeline

**a. Ingest Data with `dlt`:**
   Ensure your Python virtual environment is activated and you are in the project root.
   ```bash
   uv run python dlt/spacex_pipeline.py
   ```
   This will fetch data from the SpaceX API and load it into your MotherDuck `spacex` database.

**b. Transform Data with `dbt`:**
   Navigate to the `dbt` project directory and run the dbt models:
   ```bash
   cd dbt
   dbt deps  # Install any dbt package dependencies (if any)
   dbt build # Creates/updates silver and gold tables, and runs tests
   cd ..     # Return to project root
   ```
   This step is crucial for populating the `gold` tables that the Evidence dashboards rely on.

### 5. View the Dashboards

**Run the Evidence Development Server:**
   Navigate to the `evidence` directory and start the development server:
   ```bash
   cd evidence
   npm install  # Install Evidence project dependencies (if not already done)
   npm run dev  # Start the development server
   ```
   Or, if you have the Evidence VS Code extension installed, you can run the Evidence server directly by clicking on "Start Evidence" in the bottom left corner of VS Code.

   Open your browser to the local address provided (usually `http://localhost:3000`) to view the dashboard.

## Future To-Do's
*   Expand to include other space agencies and create a more generic dashboard for tracking all launches.
*   Add data quality monitoring and observability, potentially trial [Elementary Data](https://www.elementary-data.com/).
*   Improve Visualisations: Add geographical maps of launch and landing sites (I've experimented with this, but Evidence's current map visualisations can be a bit clunky when dealing with data points spread across the globe).