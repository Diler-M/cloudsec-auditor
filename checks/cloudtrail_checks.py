import boto3

from models.finding import Finding
from reporting.console import print_finding


def check_cloudtrail_enabled(summary):
    cloudtrail = boto3.client("cloudtrail")

    print("\nCloudTrail Audit:\n")

    trails = cloudtrail.describe_trails()

    if len(trails["trailList"]) > 0:
        for trail in trails["trailList"]:
            trail_name = trail["Name"]

            finding = Finding(
                service="CloudTrail",
                check="Trail Detection",
                resource=trail_name,
                status="PASS",
                severity="INFO",
                message="CloudTrail trail is configured",
                recommendation="No action required.",
            )

            print_finding(finding)
            summary["PASS"] += 1

    else:
        finding = Finding(
            service="CloudTrail",
            check="Trail Detection",
            resource="CloudTrail",
            status="WARN",
            severity="HIGH",
            message="No CloudTrail trails found",
            recommendation="Configure AWS CloudTrail to record account activity.",
        )

        print_finding(finding)
        summary["WARN"] += 1