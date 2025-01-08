# S3 Lambda Object Copying Project

## Overview

This project demonstrates the use of an AWS Lambda function to copy objects from one S3 bucket to another automatically when new objects are uploaded to the source bucket. The Lambda function is triggered by an S3 event notification and utilizes the AWS SDK for Python (Boto3) to copy the object to the destination bucket.

## Project Setup Steps

### 1. **Create a Lambda Function**

1. Visit the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click on **Create function**.
3. Choose **Author from scratch**.
4. Provide a name for your Lambda function, such as `CopyS3ObjectFunction`.
5. Select **Python 3.8** (or a later version) as the runtime.
6. Either create a new execution role with basic Lambda permissions or choose an existing role.

### 2. **Upload Lambda Function Code**

The code required for the Lambda function is contained in the `copyObj.py` file. The code performs the following operations:

- Retrieves the **source bucket name** and **object key** from the incoming S3 event.
- Verifies the **existence of the object** in the source bucket using `head_object`.
- **Copies the object** to the destination bucket using `copy_object`.
- Handles errors such as `NoSuchKey`, which occurs if the object is missing in the source bucket.

To implement this code:

- Go to the Lambda function code editor, click on **Code**.
- Paste the contents of `copyObj.py` into the editor.
- Click on **Deploy** to apply the changes.

### 3. **Assign IAM Role Permissions**

Make sure the Lambda function's execution role (`Lambda_s3_role`) has the following permissions:
- `s3:GetObject` for the source bucket.
- `s3:PutObject` for the destination bucket.

To assign the IAM role:
- Navigate to **Configuration** → **Permissions** → **Execution Role**.
- Click **Edit**, then select the `Lambda_s3_role`.

### 4. **Create the S3 Buckets**

Set up the **source** and **destination** S3 buckets where the objects will be uploaded and copied. Make sure the source bucket is configured to trigger the Lambda function when an object is uploaded.

### 5. **Set Up S3 Event Notification**

1. Open the **source S3 bucket** in the [S3 Console](https://console.aws.amazon.com/s3/).
2. Go to the **Properties** tab and scroll down to **Event notifications**.
3. Click **Create event notification**.
4. Enter an **Event name** (e.g., `ObjectCreatedEvent`).
5. In **Event types**, select **All object create events**.
6. In **Send to**, choose **Lambda function**.
7. Select the Lambda function you created earlier.
8. Click **Save** to enable the event notification.

From this point, the source bucket will trigger the Lambda function each time an object is uploaded.

### 6. **Test the Lambda Function**

1. **Upload an Object**: Add a file to the source S3 bucket to trigger the event.
2. **Verify Object Copying**: Check the destination bucket to confirm the object has been copied successfully.
3. **Check CloudWatch Logs**: If you encounter issues, inspect the logs in the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/) to debug the Lambda function.

### 7. **Optional: Enable S3 Logging**

To monitor events and troubleshoot any issues, you can enable **server access logging** for the source S3 bucket.

1. Go to the **Properties** tab of the source bucket.
2. Scroll down to **Server access logging** and enable it.
3. Choose a destination bucket to store the log files.

### Troubleshooting Tips

- **NoSuchKey Error**: This error occurs if the object key is incorrect or the object does not exist in the source bucket. Verify the object key in the event and ensure it's properly decoded.
- **Permission Issues**: Ensure that the IAM role associated with the Lambda function has both `s3:GetObject` (for the source bucket) and `s3:PutObject` (for the destination bucket) permissions.

---

## Conclusion

This project enables automatic copying of objects between S3 buckets using a Lambda function triggered by object uploads. Ensure that the Lambda function has the appropriate permissions and that the object key is correct when troubleshooting any issues.

The Lambda function code can be found in the file `copyObj.py`. Please upload this script to your Lambda function to enable the process.
