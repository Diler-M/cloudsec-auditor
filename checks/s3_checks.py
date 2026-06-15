import boto3


def list_buckets():
    s3 = boto3.client("s3")

    buckets = s3.list_buckets()

    print("\nS3 Buckets Found:\n")

    for bucket in buckets["Buckets"]:
        print(f"- {bucket['Name']}")