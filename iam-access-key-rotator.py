import boto3
from datetime import datetime, timezone

# Initialize the IAM client
iam = boto3.client('iam')

# Define the maximum allowed age (in days) for an IAM access key before it must be disabled
KEY_AGE_LIMIT = 90

# Retrieve a list of all IAM users in the AWS account
users = iam.list_users()["Users"]

for user in users:
  username = user["UserName"]

  # Get all access keys associated with the current IAM user
  access_keys = iam.list_access_keys(UserName=username)["AccessKeyMetadata"]
		
  for key in access_keys:
    key_id = key["AccessKeyId"]
    created_date = key["CreateDate"]

    # Calculate the key's age in days
    key_age = (datetime.now(timezone.utc) - created_date).days

    # If the key is older than the allowed limit and is still active, disable it
    if key_age > KEY_AGE_LIMIT and key["Status"] == "Active":
      iam.update_access_key(UserName=username, AccessKeyId=key_id, Status="Inactive")
      print(f"Disabled IAM access key {key_id} for user {username} (Age: {key_age} days)")
