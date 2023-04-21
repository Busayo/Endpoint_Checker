import json
import requests
import subprocess
from datetime import datetime
import pytz
import sys


class ServerStatusChecker:
    def __init__(self, webhook_url, url, server_name):
        self.webhook_url = webhook_url
        self.url = url
        self.server_name = server_name

    def check_server_status(self):
        # Set the timezone to West Africa (UTC+1)
        tz = pytz.timezone('Africa/Lagos')

        # Perform HTTP GET request
        response = requests.get(self.url)

        # If HTTP GET request does not return 200 i.e returns an error, then carry out the IF block
        if response.status_code != 200:
            message = {
                'text': f'{self.server_name} server seems to be down. Now running "docker-compose up".'}

            # Send message to Slack channel
            slack_response = requests.post(
                self.webhook_url, data=json.dumps(message))
            # If slack response returns error i.e does not return 200, carry out IF block
            if slack_response.status_code != 200:
                now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
                print(f'{now} {self.server_name} server down. Request to Slack returned an error: {slack_response.status_code}, {slack_response.text}')
            # If slack response is successful, i.e returns 200, carry out ELSE block
            else:
                now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
                print(
                    f'{now} {self.server_name} server is down. Message successfully sent to Slack.')
                print(f'{now} Now running the Docker Compose up command')

                # Run docker compose up command

                # input current working directory containing docker compose file in cwd='here'
                result = subprocess.run(
                    ['docker-compose', 'up'], cwd='', capture_output=True)
                print(result.stdout.decode('utf-8'))

        # If the HTTP Get request returns 200 status code, carry out the ELSE block
        else:
            now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
            print(f'{now} The {self.server_name} server is up and running')


def handler(event, context):
    webhook_url = ''  # input slack or teams webhook url
    endpoint_url = ''  # input server endpoint

    server_checker = ServerStatusChecker(
        webhook_url=webhook_url, url=endpoint_url, server_name='')  # input server name

    server_checker.check_server_status()
    return 'Hello from AWS Lambda using Python' + sys.version + '!' + '\n status: 200'


handler({}, {})
