import json
import boto3

table_name = 'cs125_diettable'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = json.loads(event["body"])

    response = table.put_item(
        Item = {
            "date" : body["date"],
            "meal_id" : body["meal_id"],
            "fdcId" : body["fdcId"],
            "total_carbs" : body["total_carbs"],
            "total_fat" : body["total_fat"],
            "total_protein" : body["total_protein"],
            "total_calories" : body["total_calories"],
            "total_sugars" : body["total_sugars"]
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }