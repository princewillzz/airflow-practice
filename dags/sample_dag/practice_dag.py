
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from dotenv import load_dotenv


from tasks.create_dummy_schema_task import create_dummy_schema
from tasks.load_data_task import load_data

load_dotenv()


with DAG(
    "slack_sql_integration_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # initiatize schemas
    initialization_task = PythonOperator(
        task_id='initialization_task',
        python_callable=create_dummy_schema
    )

    # load data in the DB
    populate_data_to_source = PythonOperator(
        task_id="populate_data_to_source",
        python_callable=load_data
    )


    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )


    initialization_task >> populate_data_to_source >> t1
    