
import os, json, requests

class SlackTool:

    SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')

    def __init__(self, slack_webhook_url) -> None:
        self.SLACK_WEBHOOK_URL = slack_webhook_url

    # Show alert after fetching data from the DB
    def _send_alert_to_slack(self, message):
        
        url = self.SLACK_WEBHOOK_URL

        payload = json.dumps({
            "text": message
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
