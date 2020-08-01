from urllib.parse import unquote_plus
import json
import subprocess 

def execute_code_directly(code):
    res = subprocess.run(
        ["python3"],
        stdout=subprocess.PIPE,
        input=bytes(code, 'utf-8')
    )

    return json.loads(res.stdout.decode('utf-8'))

def lambda_handler(event, context):
    body = execute_code_directly(
            unquote_plus(event['queryStringParameters']['code']))

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

