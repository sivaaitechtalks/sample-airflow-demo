from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_task():
    print("Hello from Airflow!")


with DAG(
    dag_id="dummy_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    default_args={"retries": 2},
):

    hello = PythonOperator(
        task_id="hello_task",
        python_callable=hello_task,
    )
