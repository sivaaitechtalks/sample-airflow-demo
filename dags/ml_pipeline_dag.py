import sys
import os
from pathlib import Path

# Add parent directory to Python path
dag_folder = Path(__file__).parent
project_root = dag_folder.parent
sys.path.insert(0, str(project_root))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.data_injestion import ingest
from scripts.data_processing import process
from scripts.train_model import train
from scripts.evaluate_model import evaluate

default_args = {
    'owner': 'airflow',
    "start_date": datetime(2024, 1, 1),
}

with DAG('ml_pipeline_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    ingest_task = PythonOperator(
        task_id='data_ingestion',
        python_callable=ingest,
        op_kwargs={'output_path': 'data/raw/data.csv'}
    )

    process_task = PythonOperator(
        task_id='data_processing',
        python_callable=process,
        op_kwargs={
            'input_path': 'data/raw/data.csv',
            'output_train': 'data/processed/train.csv',
            'output_test': 'data/processed/test.csv'
        }
    )

    train_task = PythonOperator(
        task_id='model_training',
        python_callable=train,
        op_kwargs={
            'train_path': 'data/processed/train.csv',
            'model_output_path': 'data/model/model.pkl'
        }
    )

    evaluate_task = PythonOperator(
        task_id='model_evaluation',
        python_callable=evaluate,
        op_kwargs={
            'test_path': 'data/processed/test.csv',
            'model_path': 'data/model/model.pkl'
        }
    )

    ingest_task >> process_task >> train_task >> evaluate_task