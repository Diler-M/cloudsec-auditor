import boto3

from models.finding import Finding


def check_cloudtrail_enabled():
    cloudtrail = boto3.client("cloudtrail")

    findings = []

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

            findings.append(finding)

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

        findings.append(finding)

    return findings