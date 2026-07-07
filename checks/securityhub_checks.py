import boto3
from botocore.exceptions import ClientError


def check_securityhub_enabled(summary):
    securityhub = boto3.client("securityhub")

    print("\nSecurity Hub Audit:\n")

    try:
        securityhub.describe_hub()
        print("PASS: Security Hub is enabled")
        summary["PASS"] += 1
    except ClientError:
        print("WARN: Security Hub is not enabled")
        summary["WARN"] += 1