import json
from datetime import datetime
import requests
import os

def lambda_handler(event, context):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H-%M-%S : %d-%m")

    # Print the version of the requests library

    return {
        'statusCode': 200,
        'body': json.dumps(f" envs = {os.getenv('POST_MARK_KEY')} , {os.getenv('EMAIL_SENDER')} " )
    }
