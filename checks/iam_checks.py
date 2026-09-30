import boto3
from datetime import datetime, timezone
from botocore.exceptions import ClientError

from models.finding import Finding
from reporting.console import print_finding

def check_iam_mfa(summary):
    iam = boto3.client("iam")

    users = iam.list_users()

    print("\nIAM MFA Audit:\n")

    for user in users["Users"]:
        user_name = user["UserName"]

        try:
            iam.get_login_profile(UserName=user_name)

        except ClientError as error:
            error_code = error.response["Error"]["Code"]

            if error_code == "NoSuchEntity":
                continue

            raise

        mfa_devices = iam.list_mfa_devices(
            UserName=user_name
        )

        if len(mfa_devices["MFADevices"]) > 0:
            finding = Finding(
                service="IAM",
                check="MFA",
                resource=user_name,
                status="PASS",
                severity="INFO",
                message="MFA is enabled",
                recommendation="No action required.",
            )

            print_finding(finding)
            summary["PASS"] += 1

        else:
            finding = Finding(
                service="IAM",
                check="MFA",
                resource=user_name,
                status="WARN",
                severity="HIGH",
                message="Console access is enabled but MFA is not configured",
                recommendation="Enable MFA for the IAM user's console access.",
            )

            print_finding(finding)
            summary["WARN"] += 1

def check_access_key_age(summary):
    iam = boto3.client("iam")

    users = iam.list_users()

    print("\nIAM Access Key Age Audit:\n")

    today = datetime.now(timezone.utc)

    for user in users["Users"]:
        user_name = user["UserName"]

        access_keys = iam.list_access_keys(
            UserName=user_name
        )

        for access_key in access_keys["AccessKeyMetadata"]:
            create_date = access_key["CreateDate"]

            key_age = today - create_date
            key_age_days = key_age.days

            if key_age_days <= 90:
                finding = Finding(
                    service="IAM",
                    check="Access Key Age",
                    resource=user_name,
                    status="PASS",
                    severity="INFO",
                    message=f"Access key is {key_age_days} days old",
                    recommendation="No action required.",
                )

                summary["PASS"] += 1

            else:
                finding = Finding(
                    service="IAM",
                    check="Access Key Age",
                    resource=user_name,
                    status="WARN",
                    severity="MEDIUM",
                    message=f"Access key is {key_age_days} days old",
                    recommendation="Rotate access keys older than 90 days.",
                )

                summary["WARN"] += 1

            print_finding(finding)