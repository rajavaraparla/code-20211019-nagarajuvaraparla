import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    ObjKey = str(datetime.today().timestamp())
    
    s3 = boto3.client("s3")
    data = json.loads(event["Records"][0]["body"])
    s3.put_object(Bucket="sqs-demo-turorial-639232547460", Key=ObjKey+".json", Body=json.dumps(data
))
    print(event)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }