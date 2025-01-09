# Restricting EC2 Instance Creation to t2.medium and Preventing t3.medium

This guide describes how to restrict AWS users to only create EC2 instances of type `t2.medium` and prevent them from creating `t3.medium` instances using IAM policies. The guide covers the full process, including policy creation, attaching the policy to users, and testing.

## Step 1: Log in to the AWS Management Console
- Open the [AWS Management Console](https://aws.amazon.com/console/).
- Ensure that you have necessary permissions to modify IAM policies.

## Step 2: Navigate to IAM Policies
1. In the AWS Management Console, navigate to **IAM**.
2. In the left-hand menu, select **Policies**.
3. Click the **Create policy** button.

## Step 3: Create a New Policy
You will define a custom policy that allows users to create EC2 instances only of the type `t2.medium` and denies `t3.medium`.

### Policy JSON
Use the policy.JSON to create your policy. This policy allows users to perform EC2 `RunInstances` actions, but only for `t2.medium` instances, and explicitly denies the creation of `t3.medium` instances.
# EC2 Instance Type Restriction: Review, Testing, and Optional Steps

## Step 4: Review and Create Policy
1. After pasting the policy JSON into the editor, click **Review policy**.
2. Provide a name for the policy (e.g., `AllowOnlyT2MediumInstances`) and an optional description.
3. Click **Create policy** to save the policy.

## Step 5: Attach the Policy to a User, Group, or Role
1. Navigate to **Users** or **Groups** in IAM, depending on who you want to apply the policy to.
2. Select the user or group you want to attach the policy to.
3. Under the **Permissions** tab, click **Add permissions**.
4. Choose **Attach policies directly**.
5. Search for the policy you just created (`AllowOnlyT2MediumInstances`).
6. Select the policy and click **Next: Review** to confirm.
7. Click **Add permissions** to apply the policy.

## Step 6: Test the Policy
To test that the policy works:

1. Log in as the user who was assigned the policy.
2. Try launching an EC2 instance of type `t2.medium` — it should succeed.
3. Try launching an EC2 instance of type `t3.medium` — it should fail.

### Additional Testing:
- **Launch `t2.medium` Instance**: Try creating a new EC2 instance of type `t2.medium`. It should be allowed, and the instance creation should succeed.
- **Launch `t3.medium` Instance**: Try creating an EC2 instance of type `t3.medium`. This action should be denied, and you will receive an error message stating that the operation is not permitted.

## Step 7: Monitoring and Auditing
You can monitor attempts to launch `t3.medium` instances by checking **CloudTrail** logs for `RunInstances` actions. If a user tries to launch a restricted instance type, it will be logged as a `Deny` event.

### Setting Up CloudTrail Logs:
1. Navigate to the **CloudTrail** service in the AWS Management Console.
2. Go to the **Event history** section.
3. Set filters to search for `RunInstances` events.
4. Look for any denied actions related to instance type creation.

## Step 8: Optional - Creating a Custom Role for EC2 Access
If you want to restrict a specific role (for
