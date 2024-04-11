import json


def handler(event, context):
    parameters = event['pathParameters']
    query_string = event['queryStringParameters']
    # body = json.loads(event['body'])
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'parameters': parameters,
            'query_string': query_string,
           
        })
    }
