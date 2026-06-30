import boto3


def check_cloudtrail_enabled(summary):
    cloudtrail = boto3.client("cloudtrail")

    print("\nCloudTrail Audit:\n")

    trails = cloudtrail.describe_trails()

    if len(trails["trailList"]) > 0:
        for trail in trails["trailList"]:
            trail_name = trail["Name"]
            print(f"PASS: CloudTrail trail found: {trail_name}")
            summary["PASS"] += 1
    else:
        print("WARN: No CloudTrail trails found")
        summary["WARN"] += 1