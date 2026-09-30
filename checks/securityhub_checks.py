import boto3
from botocore.exceptions import ClientError

from models.finding import Finding

findings = []

def check_securityhub_enabled():
    securityhub = boto3.client("securityhub")

    try:
        securityhub.describe_hub()

        finding = Finding(
            service="Security Hub",
            check="Security Hub Enabled",
            resource="Security Hub",
            status="PASS",
            severity="INFO",
            message="Security Hub is enabled",
            recommendation="No action required.",
        )

        findings.append(finding)

    except ClientError as error:
        error_code = error.response["Error"]["Code"]

        if error_code == "InvalidAccessException":
            finding = Finding(
                service="Security Hub",
                check="Security Hub Enabled",
                resource="Security Hub",
                status="WARN",
                severity="HIGH",
                message="Security Hub is not enabled",
                recommendation="Enable AWS Security Hub to centralise security findings and security posture monitoring.",
            )

            findings.append(finding)

        else:
            raise

        return findings