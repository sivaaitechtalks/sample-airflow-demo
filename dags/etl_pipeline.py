from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_from_s3
from src.transform import clean_data


def run_etl():
    df = extract_from_s3()
    df_clean = clean_data(df)
    if df_clean is not None:
        print("Data cleaned successfully."
              )

with DAG(
    "simple_etl_mwaa",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    etl_task
