
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from dotenv import load_dotenv


from tasks.create_dummy_schema_task import create_dummy_schema

load_dotenv()


with DAG(
    "slack_sql_integration_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    initialization_task = PythonOperator(
        task_id='initialization_task',
        python_callable=create_dummy_schema
    )


    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )


    initialization_task >> t1
    