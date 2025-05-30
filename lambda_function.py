import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

# Initialize the DynamoDB client

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
dynamodb_table = dynamodb.Table('my-DynamoDB')

operations_path = '/operations'

def lambda_handler(event, context):
    print('Request event:', event)
    response = None

    try:
        http_method = event.get('httpMethod')
        path = event.get('path')

        if path != operations_path:
            return build_response(404, 'Invalid path')

        if http_method == 'GET':
            response = get_items()
        elif http_method == 'POST':
            body = json.loads(event['body'])
            response = create_item(body)
        elif http_method == 'PATCH':
            body = json.loads(event['body'])
            response = update_item(body['ID'], body['updateKey'], body['updateValue'])
        elif http_method == 'DELETE':
            body = json.loads(event['body'])
            response = delete_item(body['ID'])
        else:
            response = build_response(400, 'Invalid HTTP Method')

    except Exception as e:
        print('Error:', e)
        response = build_response(500, f'Internal server error: {str(e)}')

    return response

def get_items():
    try:
        response = dynamodb_table.scan()
        return build_response(200, response.get('Items', []))
    except ClientError as e:
        return build_response(400, e.response['Error']['Message'])

def create_item(item):
    try:
        dynamodb_table.put_item(Item=item)
        return build_response(200, {'Message': 'Item created successfully', 'Item': item})
    except ClientError as e:
        return build_response(400, e.response['Error']['Message'])

def update_item(item_id, update_key, update_value):
    try:
        response = dynamodb_table.update_item(
            Key={'ID': item_id},
            UpdateExpression=f'SET {update_key} = :val',
            ExpressionAttributeValues={':val': update_value},
            ReturnValues='UPDATED_NEW'
        )
        return build_response(200, {'Message': 'Item updated', 'UpdatedAttributes': response.get('Attributes')})
    except ClientError as e:
        return build_response(400, e.response['Error']['Message'])

def delete_item(item_id):
    try:
        response = dynamodb_table.delete_item(
            Key={'ID': item_id},
            ReturnValues='ALL_OLD'
        )
        return build_response(200, {'Message': 'Item deleted', 'DeletedItem': response.get('Attributes')})
    except ClientError as e:
        return build_response(400, e.response['Error']['Message'])

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        return super(DecimalEncoder, self).default(obj)

def build_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body, cls=DecimalEncoder)
    }
