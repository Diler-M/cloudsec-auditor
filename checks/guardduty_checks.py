import boto3


def check_guardduty_enabled(summary):
    ec2 = boto3.client("ec2")

    regions = ec2.describe_regions()

    enabled_regions = 0
    missing_regions = 0

    print("\nGuardDuty Audit:\n")

    for region in regions["Regions"]:
        region_name = region["RegionName"]

        guardduty = boto3.client("guardduty", region_name=region_name)

        detectors = guardduty.list_detectors()

        if len(detectors["DetectorIds"]) > 0:
            enabled_regions += 1
        else:
            missing_regions += 1

    if enabled_regions > 0:
        print(f"PASS: GuardDuty enabled in {enabled_regions} region(s)")
        summary["PASS"] += 1

    if missing_regions > 0:
        print(f"WARN: GuardDuty missing from {missing_regions} region(s)")
        summary["WARN"] += 1