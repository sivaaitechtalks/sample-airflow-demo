import logging
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

def datainjested():
    logging.info("Data is injested")
    
def dataprocessing():
    logging.info("Data is processed"
        )
    
def dataloaded():
    logging.info("Data is loaded")


with DAG(
    dag_id="dummy_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    default_args={"retries": 2},
):

    hello = PythonOperator(
        task_id="hello_task",
        python_callable=datainjested,
    )
    process = PythonOperator(
        task_id="process_task",
        python_callable=dataprocessing,
    )
    
    load = PythonOperator(
        task_id="load_task",    
        python_callable=dataloaded,
    )
    
    hello >> process >> load