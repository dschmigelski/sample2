import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello Familia'
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
