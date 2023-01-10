
from airflow import DAG

from datetime import datetime

with DAG(
    "practice_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    pass
    