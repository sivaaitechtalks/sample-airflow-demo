FROM apache/airflow:2.10.2
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY dags/ /opt/airflow/dags/
COPY src/ /opt/airflow/src/
