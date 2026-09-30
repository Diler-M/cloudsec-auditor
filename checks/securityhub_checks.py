import boto3
from botocore.exceptions import ClientError

from models.finding import Finding
from reporting.console import print_finding


def check_securityhub_enabled(summary):
    securityhub = boto3.client("securityhub")

    print("\nSecurity Hub Audit:\n")

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

        print_finding(finding)
        summary["PASS"] += 1

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

            print_finding(finding)
            summary["WARN"] += 1

        else:
            raise