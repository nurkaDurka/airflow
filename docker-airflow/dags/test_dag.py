import pendulum

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def extract():
    print("Extract for Airflow!")

def transform():
    print("Transform for Airflow!")

def load():
    print("Load for Airflow!")

with DAG(
    dag_id="test_dag",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Almaty"),
    schedule="@daily",
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )
    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    extract_task >> transform_task >> load_task