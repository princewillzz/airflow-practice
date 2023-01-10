

from integrations.db_integration import PostgressDB

def calculate_sum_and_notify():

    import os, json, requests


    SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
    if SLACK_WEBHOOK_URL == None:
        raise Exception("No Webhook url found!")

    db_instance = PostgressDB()

    record = db_instance.fetch_data_from_db("SELECT SUM(num), SUM(square_num) FROM harsh", many=False)

    sum_of_num = record[0]
    sum_of_square = record[1]

    msg = f":red_circle: Harsh Testing DAG: total sum of num = {sum_of_num}, total sum of there square is = {sum_of_square} :)"

    payload = json.dumps({
        "text": f":red_circle: Harsh Testing DAG: total sum of num = {sum_of_num}, total sum of there square is = {sum_of_square} :)"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", SLACK_WEBHOOK_URL, headers=headers, data=payload)

    print(response.text)
