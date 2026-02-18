# airflow-mdm-training

🚀 MDM Engineering Lab: Airflow, PySpark & Splink
This repository contains a 2-week intensive learning path and a hands-on mini-project focused on Master Data Management (MDM). The goal is to build a "Golden Record" pipeline using the Modern Data Stack locally on Docker.

📌 Project Overview
The "Golden Record" pipeline ingests messy customer data, standardizes it via PySpark, uses Splink for probabilistic record linkage, and orchestrates the entire flow using Apache Airflow.

📌 Pre-requisites
1. Docker Desktop
2. Git hub account
3. WSL 

🗓️ 2-Week Learning Path

Day 1-2: Docker-Airflow environment setup & volume persistence.

Day 3-5: Airflow Fundamentals: DAGs, Operators (Python, Bash), and the Scheduler on  [Airflow 101 Learning Path - Astronomer Academy](https://academy.astronomer.io/path/airflow-101).

Day 6-7: DAMA-DMBOK Data Quality Dimensions.
Reading: [DAMA-DMBOK Summary](https://www.linkedin.com/pulse/dama-dmbok-data-management-body-knowledge-summary-sunil-zarikar-tygyf/)

Day 8-9: [Introduction to Splink](https://moj-analytical-services.github.io/splink/demos/tutorials/00_Tutorial_Introduction.html)
Day 10: Probabilistic Matching: Identifying "Jon Doe" vs "John Doe" using Levenshtein distance.

Day 11-14: Mini Project 
https://github.com/strat-main-team/airflow-mdm-training/blob/main/MiniProject.md

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
Splink Docs: [Linkage Theory & Tutorials](https://moj-analytical-services.github.io/splink/)

Probabilistic Matching: [Robin Linacre’s Introduction to Linkage](https://www.robinlinacre.com/probabilistic_linkage/)

Airflow Docs: [Best Practices for DAGs](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
