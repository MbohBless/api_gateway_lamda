import json


def handler(event, context):
    print('reequest: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
