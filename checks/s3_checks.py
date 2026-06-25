import boto3


def check_bucket_public_access(summary):
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
                summary["PASS"] += 1
            else:
                print(f"FAIL: {bucket_name} may allow public access")
                summary["FAIL"] += 1

        except Exception:
            print(f"WARN: {bucket_name} has no Public Access Block configuration")
            summary["WARN"] += 1


def check_bucket_encryption(summary):
    s3 = boto3.client("s3")

    buckets = s3.list_buckets()

    print("\nS3 Bucket Encryption Audit:\n")

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        try:
            response = s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            rules = response["ServerSideEncryptionConfiguration"]["Rules"]

            encryption_type = rules[0]["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]

            print(f"PASS: {bucket_name} has default encryption enabled using {encryption_type}")
            summary["PASS"] += 1

        except Exception:
            print(f"FAIL: {bucket_name} does not have default encryption enabled")
            summary["FAIL"] += 1


def check_bucket_versioning(summary):
    s3 = boto3.client("s3")

    buckets = s3.list_buckets()

    print("\nS3 Bucket Versioning Audit:\n")

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        response = s3.get_bucket_versioning(
            Bucket=bucket_name
        )

        status = response.get("Status", "Disabled")

        if status == "Enabled":
            print(f"PASS: {bucket_name} has versioning enabled")
            summary["PASS"] += 1
        else:
            print(f"WARN: {bucket_name} does not have versioning enabled")
            summary["WARN"] += 1