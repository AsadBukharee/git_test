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
        'body': json.dumps(f"Time is :  {formatted_time} and Requests Version is : {requests.__version__} and envs = {os.getenv('AWS_ACCESS_KEY_ID')} , {os.getenv('AWS_SECRET_ACCESS_KEY')}")
    }
