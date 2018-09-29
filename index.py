import json
import datetime
import boto3

def handler(event, context):
	dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('HelloWorldTable')
    response = table.get_item(
	    Key={
	        'sample': 'a'
	    }
	)
	item = response['Item']
    data = {
        'output': item
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
