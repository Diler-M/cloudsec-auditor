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

from checks.s3_checks import list_buckets

list_buckets()

