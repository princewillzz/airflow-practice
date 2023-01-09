

from airflow import DAG
from airflow.operators.python import PythonOperator

import psycopg2
from datetime import datetime
import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
if SLACK_WEBHOOK_URL == None:
    raise Exception("No Webhook url found!")

def connect():
    # Fill in the parameters for your PostgreSQL database
    conn = psycopg2.connect(host="localhost",
                            database="harshtiwari",
                            user="tutorial_dag",
                            password="password")
    return conn

# Task 1
# Create a table with my name if it doesn't exist
def create_schema_task():

    # Connect to the database
    conn = connect()

    # Create a cursor object
    cursor = conn.cursor()

    table_name = "harsh"
    columns = "id SERIAL PRIMARY KEY, num INT, square_num INT"

    # Execute a SQL query
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

    conn.commit();

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Task 2
# populate the table with some random data
def _populate_data_to_source():
    # Connect to the database
    conn = connect()

    # Create a cursor object
    cur = conn.cursor()

    for index in range(1, 11):
        # Execute a SQL query
        cur.execute(f"INSERT INTO harsh (num, square_num) values({index}, {index**2})")

    conn.commit();

    # Close the cursor and connection
    cur.close()
    conn.close()

# TASK 3
# Show alert after fetching data from the DB
def _send_alert_to_slack():
    # Connect to the database
    conn = connect()

    # Create a cursor object
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(num), SUM(square_num) FROM harsh");

    records = cursor.fetchone()

    sum_of_num = records[0]
    sum_of_square = records[1]

    print("Sum of num: ", sum_of_num)
    print("Sum of square: ", sum_of_square)
    os.environ["no_proxy"]="*"


    url = SLACK_WEBHOOK_URL

    payload = json.dumps({
        "text": f":red_circle: Harsh Testing DAG: total sum of num = {sum_of_num}, total sum of there square is = {sum_of_square} :)"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


with DAG(
    "practice_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:


    initialization_task = PythonOperator(
        task_id='initialization_task',
        python_callable=create_schema_task
    )
    
    populate_data_to_source = PythonOperator(
        task_id="populate_data_to_source",
        python_callable=_populate_data_to_source
    )

    # Define a PythonOperator to call the function to send the Slack notification
    send_notification_task = PythonOperator(
        task_id='send_slack_notification',
        python_callable=_send_alert_to_slack,
    )


    initialization_task >> populate_data_to_source >> send_notification_task

