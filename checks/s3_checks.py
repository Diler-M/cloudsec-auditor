import boto3


def list_buckets():
    s3 = boto3.client("s3")

    buckets = s3.list_buckets()

    print("\nS3 Bucket Public Access Audit:\n")

    for bucket in buckets["Buckets"]:

        bucket_name = bucket["Name"]

        try:
            response = s3.get_public_access_block(
                Bucket=bucket_name
            )

            config = response["PublicAccessBlockConfiguration"]

            if (
                config["BlockPublicAcls"]
                and config["IgnorePublicAcls"]
                and config["BlockPublicPolicy"]
                and config["RestrictPublicBuckets"]
            ):
                print(f"PASS: {bucket_name} blocks public access")

            else:
                print(f"FAIL: {bucket_name} may allow public access")

        except Exception as e:
            print(f"WARN: {bucket_name} has no Public Access Block configuration")