import boto3


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