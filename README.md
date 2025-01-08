# S3 Lambda Copy Object Project

## Overview

This project involves using an AWS Lambda function to copy an object from one S3 bucket to another whenever a new object is uploaded to the source bucket. The Lambda function is triggered by an S3 event notification, and the object is copied to the destination bucket using the AWS SDK for Python (Boto3).

## Steps to Set Up the Project

### 1. **Create Lambda Function**

1. Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create function**.
3. Choose **Author from scratch**.
4. Set a name for your function (e.g., `CopyS3ObjectFunction`).
5. Set the runtime to **Python 3.8** (or later).
6. Create a new execution role with basic Lambda permissions or use an existing role.

### 2. **Write Lambda Function Code**

The Python code to be used for the Lambda function is available in the script file `copy_obj.py`. The script performs the following tasks:

- **Extract the source bucket name and object key** from the incoming S3 event.
- **Check if the object exists** in the source bucket using the `head_object` method.
- **Copy the object** to the destination bucket using the `copy_object` method.
- Handles **errors** like `NoSuchKey` in case the object doesn't exist in the source bucket.

You can download the full code from the file `copy_obj.py` and upload it to your Lambda function.

### 3. **Set IAM Role Permissions**

Ensure that the Lambda function's execution role has the following permissions:
- `s3:GetObject` for the source bucket.
- `s3:PutObject` for the destination bucket.

Example of a minimal IAM policy for Lambda permissions:

### 4. **Configure S3 Event Notification**

1. Go to the **source S3 bucket** in the [S3 Console](https://console.aws.amazon.com/s3/).
2. Under the **Properties** tab, scroll to **Event notifications** and click **Create event notification**.
3. Set an **Event name** (e.g., `ObjectCreatedEvent`).
4. In **Event types**, select **All object create events**.
5. In **Send to**, choose **Lambda function**.
6. Select the Lambda function you created earlier.
7. Save the event notification.

The source bucket will now automatically trigger the Lambda function whenever an object is uploaded.

### 5. **Test the Lambda Function**

1. **Upload an Object**: Upload a file to the source S3 bucket to trigger the event.
2. **Verify the Copy**: Check the destination bucket to ensure the object is copied.
3. **Check Logs**: If there are issues, view the logs in the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/) under the Lambda function’s log group for debugging.

### 6. **Optional: Enable S3 Logging**

You can enable **server access logging** for the source S3 bucket to track any errors related to the event notification.

1. In the **Properties** tab of the source bucket, go to **Server access logging**.
2. Enable logging to capture information about requests made to the bucket.

### Troubleshooting

- **NoSuchKey Error**: If the error `NoSuchKey` occurs, it means the object key is incorrect or doesn't exist in the source bucket. Check the event object and ensure the key is correct and properly decoded.
- **Permission Issues**: Ensure the Lambda function’s IAM role has both `s3:GetObject` and `s3:PutObject` permissions for the respective buckets.

---

## Conclusion

This setup allows you to automatically copy objects between S3 buckets using a Lambda function triggered by object uploads. Make sure to handle permissions and ensure the object key is correct when troubleshooting issues.

The Lambda function code is available in the file `copy_obj.py`. Please upload this file to your Lambda function to make this process work.
