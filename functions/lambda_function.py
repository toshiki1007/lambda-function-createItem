import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key
import json
import datetime
import uuid
import layer

region = "us-west-2"
session = Session(
    region_name=region
)
dynamodb = session.resource('dynamodb')

table = dynamodb.Table('Item')
nowdate = '{0:%Y-%m-%d}'.format(datetime.datetime.now())

def response(status_code, new_record, error_msg):
    return {
        'statusCode': status_code,
        'body': new_record,
        'errorMessage': error_msg
    }

def lambda_handler(event, context):
    input = event['Input']

    item_id = str(uuid.uuid4())
    author = input['author']
    description = input['description']
    item_image = input['itemImage']
    item_name = input['itemName']
    price = input['price']
    seller_id = input['sellerId']

    try:
        put_response = table.put_item(
            Item={
                'itemId': item_id,
                'author': author,
                'description': description,
                'itemImage': item_image,
                'itemName': item_name,
                'price': price,
                'sellerId': seller_id,
                'buyerId': 'None',
                'registerDate': '{0:%Y-%m-%d}'.format(datetime.datetime.now()),
                'sellingDate': '9999-99-99',
            }
        )
    except:
        return response(400, None, '商品登録エラー')

    new_record = table.get_item(
        Key={
            'itemId': item_id,
        }
    )['Item']

    return response(200, new_record, None)