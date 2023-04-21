## Server Status Checker

The `ServerStatusChecker` class is a Python script that checks if a server is running or down. It sends a message to a Slack channel if the server is down and starts the server using Docker Compose. This script is written in Python 3.

### Dependencies

The script requires the following dependencies to work correctly:

- requests
- pytz

### Setup

To use this script, you need to set up a few things:

1. **Slack webhook URL**: You will need a Slack webhook URL to send messages to a Slack channel. If you don't have one, follow the instructions [here](https://api.slack.com/messaging/webhooks) to set it up.

2. **Server endpoint URL**: You will need to input the URL of the server you want to check.

3. **Server name**: You will need to input a name for the server you want to check.

4. **Current working directory**: You will need to set the current working directory to the directory containing the Docker Compose file.

### How it Works

The `check_server_status()` method sends an HTTP GET request to the server endpoint URL and checks if the server is running. If the HTTP GET request returns a status code other than 200, it sends a message to the Slack channel using the webhook URL to notify that the server is down. If the Slack API returns a status code other than 200, an error message is printed to the console. If the Slack API returns a 200 status code, the message is sent to the Slack channel, and the Docker Compose up command is run using the `subprocess` module.

If the HTTP GET request returns a 200 status code, the server is up, and a message is printed to the console to confirm that the server is up and running.

### How to Run

The `handler()` function at the bottom of the script is used to run the script. You can run this script in any Python environment or use it as an AWS Lambda function. Before running the script, you need to input the Slack webhook URL, server endpoint URL, and server name.

### Example Usage

```python
webhook_url = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'
endpoint_url = 'http://example.com'
server_name = 'Example Server'

server_checker = ServerStatusChecker(webhook_url=webhook_url, url=endpoint_url, server_name=server_name)
server_checker.check_server_status()
```

The script can also be run as an AWS Lambda function. To do this, copy and paste the code into the AWS Lambda function editor and set the required environment variables. You can then invoke the function manually or set up an event trigger to run the function at regular intervals.
