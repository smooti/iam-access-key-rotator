import boto3

# Initialize the IAM client
iam_client = boto3.client('iam')

# Retrieve a list of all IAM users in the AWS account
users = iam_client.list_users()["Users"]

def bold_text(text):
	# Function to apply bold text
	return f'\033[1m{text}\033[0m'

for user in users:
	# Check if the user is using MFA
	if not iam_client.list_mfa_devices(UserName=user["UserName"])["MFADevices"]:
		print(f"{bold_text(user["UserName"])} is not using MFA")
