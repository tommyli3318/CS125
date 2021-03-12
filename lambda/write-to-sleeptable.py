import json
import boto3

table_name = 'cs125_sleeptable'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = json.loads(event["body"])

    response = table.put_item(
        Item = {
            "date" : body["date"],
            "sleep_quality": body["sleep_quality"],
            "sleep_start": body["sleep_start"],
            "sleep_time": body["sleep_time"]
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }