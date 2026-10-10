import pendulum

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def print_logical_date(**context):
    dt = context["logical_date"]
    print(f"Logical date: {dt}")

with DAG(
    dag_id="test_print_dag",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Almaty"),
    schedule="@daily",
    catchup=True,
    max_active_runs=2,
    tags=["example"],
) as dag:
    print_date_task = PythonOperator(
        task_id="print_logical_date",
        python_callable=print_logical_date
    )