from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from mdm.deduplicate import run_deduplication


with DAG(
dag_id="customer_mdm_pipeline",
start_date=datetime(2024, 1, 1),
schedule_interval="@daily",
catchup=False
) as dag:


dedupe = PythonOperator(
task_id="run_splink_deduplication",
python_callable=run_deduplication
)


dedupe