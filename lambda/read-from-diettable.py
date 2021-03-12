import json
import boto3
from decimal import Decimal

def default(obj):
    # Fix: TypeError: Object of type 'Decimal' is not JSON serializable
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

table_name = 'cs125_diettable'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = json.loads(event["body"])

    response = table.get_item(
        Key = {
            "date" : body["date"],
            "meal_id" : body["meal_id"]
        }
    )
    
    
    if response.get("Item"):
        return {
            'statusCode': 200,
            'body': json.dumps(response["Item"], default=default)
        }
    
    else:
        return {
            'statusCode': 404,
            'body': 'Item not found'
        }