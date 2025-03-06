**IAM Access Key Rotator**
==========================

**Overview**
------------

This script disables IAM access keys that are older than a specified age limit (default: 90 days) in an AWS account. It iterates through all IAM users and their access keys, calculates the age of each key, and updates the key status to "Inactive" if it exceeds the age limit.

**Requirements**
---------------

* Python 3.x
* Boto3 library (install with `pip install boto3`)
* AWS credentials configured (e.g., via `~/.aws/credentials` file or environment variables)

**Usage**
-----

1. Install the required Boto3 library.
2. Configure your AWS credentials.
3. Run the script using Python (e.g., `python iam-access-key-rotator.py`).

**Configuration**
---------------

* `KEY_AGE_LIMIT`: The maximum allowed age (in days) for an IAM access key before it must be disabled. Default: 90 days.

**Notes**
-----

* This script only disables access keys that are older than the specified age limit and still active.
* It does not delete access keys or affect any other IAM resources.
* Make sure to test this script in a non-production environment before running it in production.
