# Mini Project: E‑Commerce Customer MDM using Splink, Airflow, and Postgres

This project demonstrates an **end‑to‑end Master Data Management (MDM) pipeline** using the **Brazilian E‑Commerce Public Dataset by Olist**. It focuses on **customer deduplication and identity resolution** using probabilistic record linkage with **Splink**, orchestrated via **Apache Airflow**, and persisted into **PostgreSQL** as a customer master.

This is designed to be **portfolio‑ready** and representative of real‑world data engineering + data governance work.

---

### Prerequisites

* Docker
* Docker Compose
* Ports available on your machine:

  * Postgres: **5433** (host) → 5432 (container)
  * Airflow UI: **8081** (host) → 8080 (container)

---

### Step 1: Stop any running containers

```bash
docker-compose down
```

---

### Step 2: Start PostgreSQL only

Airflow needs its metadata database available before initialization.

```bash
docker-compose up -d postgres
```

Verify Postgres is running:

```bash
docker ps
```

You should see the `postgres` container in a running state.

---

### Step 3: Initialize the Airflow metadata database

Run the initialization command **inside the Airflow container** using Airflow **2.6.3**:

```bash
docker-compose run --rm airflow airflow db init
```

Expected output (example):

```
INFO  [airflow.db.init] Initializing metadata database
INFO  [alembic.runtime.migration] Running upgrade
INFO  [airflow.db.init] Initialized the metadata database
```

This step is required **only once** unless you wipe volumes.

---

### Step 4: Create an Airflow admin user

Without this, you cannot log in to the Airflow UI.

```bash
docker-compose run --rm airflow airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```

This step is also required **only once**.

---

### Step 5: Start Airflow services

```bash
docker-compose up
```

Wait ~30 seconds for the webserver to start.

---

### Step 6: Access the Airflow UI

Open your browser:

```
http://localhost:8081
```

Login credentials:

* **Username:** admin
* **Password:** admin

You should now see the DAG:

```
ecommerce_customer_mdm_pipeline
```

The DAG is paused by default — this is expected behavior.

---

### Step 7: Run the pipeline

1. Unpause the DAG
2. Trigger it manually or wait for the scheduled run

Airflow will:

* Read customer records from Postgres staging
* Run Splink deduplication
* Write master customer records back to Postgres

---

## 9. Troubleshooting

### Port already allocated (5432 or 8080)

* Postgres runs on **host port 5433**
* Airflow UI runs on **host port 8081**

Update `docker-compose.yml` if these ports are in use.

---

## 1. Business Context

E‑commerce platforms often store customers at the **order level**, resulting in:

* Duplicate customer records
* Inconsistent identifiers across systems
* Fragmented customer views

**Objective:**

* Resolve customer identities across multiple records
* Produce a **golden customer master** table
* Orchestrate the process using production‑style tooling

---

## 2. Dataset Reference

**Brazilian E‑Commerce Public Dataset by Olist (Kaggle)**
[https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Primary file used:

* `olist_customers_dataset.csv`

Key fields:

* `customer_id` – order‑level identifier
* `customer_unique_id` – consistent person identifier
* `customer_zip_code_prefix`
* `customer_city`
* `customer_state`

For MDM simulation, the dataset is treated as if it originated from **multiple downstream systems** (search, CRM, marketing).

---

## 3. Architecture Overview

```
CSV Sources (Olist)
        |
        v
Airflow DAG (Orchestration)
        |
        v
Postgres Staging Tables
        |
        v
Splink Probabilistic Matching (DuckDB)
        |
        v
Customer Master Table (Postgres)
```

---

## 4. Project Structure

```
ecommerce-mdm-splink/
│
├── airflow/
│   ├── dags/
│   │   └── ecommerce_mdm_dag.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── olist_customers_dataset.csv
│   └── processed/
│
├── mdm/
│   ├── splink_settings.py
│   ├── deduplicate.py
│   └── utils.py
│
├── postgres/
│   └── init.sql
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## 5. Data Model

### Staging Table

Stores raw customer records from source systems.

```sql
CREATE TABLE ecommerce_customer_staging (
    source_system TEXT,
    customer_id TEXT,
    customer_unique_id TEXT,
    zip_code_prefix INTEGER,
    city TEXT,
    state TEXT
);
```

### Master Table

Stores deduplicated, clustered customer entities.

```sql
CREATE TABLE ecommerce_customer_master (
    master_customer_id UUID PRIMARY KEY,
    customer_unique_id TEXT,
    zip_code_prefix INTEGER,
    city TEXT,
    state TEXT,
    source_count INT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 6. Deduplication Logic

* **Blocking rules** reduce comparison space
* **Probabilistic matching** handles imperfect identifiers
* **Clustering** produces master customer entities

Splink is configured with:

* `customer_unique_id`
* geographic attributes (city, state)

The DuckDB backend is used for local, in‑memory performance.

---

## 7. Orchestration (Airflow)

The Airflow DAG performs:

1. Read customer records from Postgres staging
2. Execute Splink deduplication
3. Persist master records to Postgres

The pipeline is scheduled to run daily and can be extended with sensors and validations.

---

## 8. Running the Project

```bash
docker-compose up --build
```

* Airflow UI: [http://localhost:8080](http://localhost:8080)
* PostgreSQL: localhost:5432

---

## 9. Key Learning Outcomes

* Designing a **realistic MDM pipeline**
* Using **probabilistic record linkage** instead of exact matching
* Orchestrating data quality‑critical workflows with Airflow
* Structuring data engineering projects for production readiness

---

## 10. Next‑Step Enhancements

These extensions elevate the project to **senior‑level / production‑grade MDM**:

### Data Quality & Validation

* Null checks, uniqueness checks before Splink
* Schema validation using Great Expectations

### Survivorship Rules

* Define attribute precedence (e.g., most recent city)
* Source system trust ranking

### Historical Tracking

* Implement **SCD Type 2** for customer master
* Track merges and splits over time

### Match Governance

* Persist match confidence scores
* Add manual review thresholds

### Observability

* Log match rates and cluster sizes
* Expose metrics to Prometheus/Grafana

### Scaling

* Replace DuckDB with Spark backend
* Partition matching by geography

### Security & Governance

* PII masking
* Row‑level access policies

---

