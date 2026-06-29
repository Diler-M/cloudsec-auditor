import boto3
from datetime import datetime, timezone

def check_iam_mfa(summary):
    iam = boto3.client("iam")

    users = iam.list_users()

    print("\nIAM MFA Audit:\n")

    for user in users["Users"]:
        user_name = user["UserName"]

        mfa_devices = iam.list_mfa_devices(
            UserName=user_name
        )

        if len(mfa_devices["MFADevices"]) > 0:
            print(f"PASS: {user_name} has MFA enabled")
            summary["PASS"] += 1
        else:
            print(f"WARN: {user_name} does not have MFA enabled")
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
                print(f"PASS: {user_name} access key is {key_age_days} days old")
                summary["PASS"] += 1
            else:
                print(f"WARN: {user_name} access key is {key_age_days} days old")
                summary["WARN"] += 1