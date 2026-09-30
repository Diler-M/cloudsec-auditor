import boto3

from models.finding import Finding
from reporting.console import print_finding
from utils.aws import get_all_regions


def check_guardduty_enabled(summary):
    regions = get_all_regions()

    enabled_regions = 0
    missing_regions = 0

    print("\nGuardDuty Audit:\n")

    for region in regions:
        region_name = region["RegionName"]

        guardduty = boto3.client(
            "guardduty",
            region_name=region_name
        )

        detectors = guardduty.list_detectors()

        if len(detectors["DetectorIds"]) > 0:
            enabled_regions += 1
        else:
            missing_regions += 1

    if enabled_regions > 0:
        finding = Finding(
            service="GuardDuty",
            check="GuardDuty Enabled",
            resource="AWS Regions",
            status="PASS",
            severity="INFO",
            message=f"GuardDuty is enabled in {enabled_regions} region(s)",
            recommendation="No action required.",
        )

        print_finding(finding)
        summary["PASS"] += 1

    if missing_regions > 0:
        finding = Finding(
            service="GuardDuty",
            check="GuardDuty Enabled",
            resource="AWS Regions",
            status="WARN",
            severity="HIGH",
            message=f"GuardDuty is not enabled in {missing_regions} region(s)",
            recommendation="Review the affected regions and enable GuardDuty where monitoring is required.",
        )

        print_finding(finding)
        summary["WARN"] += 1