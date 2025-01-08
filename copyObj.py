import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Get the source and destination bucket names
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket (replace with your destination bucket name)
    destination_bucket = 'my-bucket-lambda2'

    try:
        # Copy the object to the destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': source_key}
        s3.copy_object(
            CopySource=copy_source,
            Bucket=destination_bucket,
            Key=source_key
        )
        print(f'Successfully copied {source_key} from {source_bucket} to {destination_bucket}')
        return {
            'statusCode': 200,
            'body': json.dumps('Copy operation successful')
        }
    except Exception as e:
        print(f'Error copying file: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
