# ==================================
# AWS CONNECTIVITY TEST
# ==================================

#import boto3

# sts = boto3.client("sts")

# identity = sts.get_caller_identity()

# print(f"Connected to AWS Account: {identity['Account']}")
# print(f"Authenticated as: {identity['Arn']}")

# ==================================
# S3 BUCKET ENUMERATION
# ==================================

from checks.s3_checks import (
    check_bucket_public_access,
    check_bucket_encryption,
    check_bucket_versioning,
)

summary = {
    "PASS": 0,
    "WARN": 0,
    "FAIL": 0
}

check_bucket_public_access(summary)
check_bucket_encryption(summary)
check_bucket_versioning(summary)

print("\nCloudSec Auditor Summary:\n")
print(f"PASS: {summary['PASS']}")
print(f"WARN: {summary['WARN']}")
print(f"FAIL: {summary['FAIL']}")