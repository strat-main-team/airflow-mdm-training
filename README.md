# airflow-mdm-training

🚀 MDM Engineering Lab: Airflow, PySpark & Splink
This repository contains a 2-week intensive learning path and a hands-on mini-project focused on Master Data Management (MDM). The goal is to build a "Golden Record" pipeline using the Modern Data Stack locally on Docker.

📌 Project Overview
The "Golden Record" pipeline ingests messy customer data, standardizes it via PySpark, uses Splink for probabilistic record linkage, and orchestrates the entire flow using Apache Airflow.

🗓️ 2-Week Learning Path
Week 1: The Orchestration Layer
Day 1-2: Docker-Airflow environment setup & volume persistence.

Day 3: Airflow Fundamentals: DAGs, Operators (Python, Bash), and the Scheduler.

Day 4: Data Engineering foundations: Standardizing strings and cleaning schemas with PySpark.

Day 5: Airflow Variables & Connections: Managing local file paths and database URIs.

Reading: DAMA-DMBOK Data Quality Dimensions.

Week 2: The MDM Intelligence
Day 8-9: Introduction to Splink: Blocking rules and Fellegi-Sunter model basics.

Day 10: Probabilistic Matching: Identifying "Jon Doe" vs "John Doe" using Levenshtein distance.

Day 11: Survivorship Logic: Merging attributes to create the "Golden Record."

Day 12-13: Data Quality Gates: Using Airflow Sensors to validate de-duplication rates.

Day 14: Final Documentation: Exporting results and lineage mapping.

🏗️ Mini-Project: Unified Customer View
1. The Dataset
Source: Kaggle - Customer Search Data (De-duping)

Context: This dataset contains duplicate entries with typos in names, addresses, and emails—perfect for testing record linkage logic.

Setup: Download the CSV, rename it to raw_customers.csv, and place it in the /data folder.

2. Pipeline Architecture
Extract: Airflow detects the file in the /data volume.

Transform (Cleaning): PySpark converts all strings to lowercase, removes special characters, and formats phone numbers.

Match (Splink): A probabilistic model assigns a unique_id to matching records across different systems.

Survivorship: A "Golden Record" is created by taking the most recent or most complete data point for each cluster.

Load: The final table is written to a local DuckDB file for analysis.

🛠️ Setup & Usage
Prerequisites
Docker & Docker Compose

Git

Installation
Clone this repository:

Bash
git clone <your-repo-link>
cd mdm-airflow-project
Build the environment:

Bash
docker-compose up --build
Access the tools:

Airflow UI: http://localhost:8080 (Admin / see logs for password)

Jupyter Lab: http://localhost:8888 (For prototyping Splink models)


📖 Key MDM References
Splink Docs: Linkage Theory & Tutorials

Probabilistic Matching: Robin Linacre’s Introduction to Linkage

Airflow Docs: Best Practices for DAGs