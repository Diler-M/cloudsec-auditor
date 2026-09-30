import boto3
from botocore.exceptions import ClientError

from models.finding import Finding


def check_bucket_public_access():
    s3 = boto3.client("s3")
    findings = []
    
    buckets = s3.list_buckets()

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
                finding = Finding(
                    service="S3",
                    check="Block Public Access",
                    resource=bucket_name,
                    status="PASS",
                    severity="INFO",
                    message="Bucket blocks public access",
                    recommendation="No action required.",
                )

                findings.append(finding)

            else:
                finding = Finding(
                    service="S3",
                    check="Block Public Access",
                    resource=bucket_name,
                    status="FAIL",
                    severity="HIGH",
                    message="Bucket does not have all public access protections enabled",
                    recommendation="Enable all four S3 Block Public Access settings.",
                )

                findings.append(finding)

        except ClientError as error:
            error_code = error.response["Error"]["Code"]

            if error_code == "NoSuchPublicAccessBlock":
                finding = Finding(
                    service="S3",
                    check="Block Public Access",
                    resource=bucket_name,
                    status="WARN",
                    severity="HIGH",
                    message="Bucket has no Public Access Block configuration",
                    recommendation="Enable S3 Block Public Access for the bucket.",
                )

                findings.append(finding)

            else:
                raise

    return findings


def check_bucket_encryption():
    s3 = boto3.client("s3")
    findings = []

    buckets = s3.list_buckets()

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        try:
            response = s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            rules = response["ServerSideEncryptionConfiguration"]["Rules"]

            encryption_type = rules[0][
                "ApplyServerSideEncryptionByDefault"
            ]["SSEAlgorithm"]

            finding = Finding(
                service="S3",
                check="Default Encryption",
                resource=bucket_name,
                status="PASS",
                severity="INFO",
                message=f"Default encryption enabled using {encryption_type}",
                recommendation="No action required.",
            )

            findings.append(finding)

        except ClientError as error:
            error_code = error.response["Error"]["Code"]

            if error_code == "ServerSideEncryptionConfigurationNotFoundError":
                finding = Finding(
                    service="S3",
                    check="Default Encryption",
                    resource=bucket_name,
                    status="FAIL",
                    severity="HIGH",
                    message="Bucket does not have default encryption enabled",
                    recommendation="Enable default server-side encryption for the S3 bucket.",
                )

                findings.append(finding)

            else:
                raise

    return findings


def check_bucket_versioning():
    s3 = boto3.client("s3")
    findings = []

    buckets = s3.list_buckets()

    for bucket in buckets["Buckets"]:
        bucket_name = bucket["Name"]

        response = s3.get_bucket_versioning(
            Bucket=bucket_name
        )

        status = response.get("Status", "Disabled")

        if status == "Enabled":
            finding = Finding(
                service="S3",
                check="Bucket Versioning",
                resource=bucket_name,
                status="PASS",
                severity="INFO",
                message="Bucket versioning is enabled",
                recommendation="No action required.",
            )

            findings.append(finding)

        else:
            finding = Finding(
                service="S3",
                check="Bucket Versioning",
                resource=bucket_name,
                status="WARN",
                severity="MEDIUM",
                message="Bucket versioning is not enabled",
                recommendation="Enable S3 Versioning to improve protection against accidental deletion or overwrite.",   
            )

            findings.append(finding)

    return findings
