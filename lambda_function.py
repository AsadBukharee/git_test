import json
from datetime import datetime


def lambda_handler(event, context):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H-%M-%S : %d-%m")
    return {
        'statusCode': 200,
        'body': json.dumps(f"{formatted_time}")
    }
