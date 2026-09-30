import boto3

from models.finding import Finding
from botocore.exceptions import ClientError



def check_macie_enabled():
    macie = boto3.client("macie2")
    region = macie.meta.region_name
    findings = []

    try:
        macie.get_macie_session()

        finding = Finding(
            service="Macie",
            check="Macie Enabled",
            resource="Amazon Macie",
            region=region,
            status="PASS",
            severity="INFO",
            message="Amazon Macie is enabled",
            recommendation="No action required.",
        )

        findings.append(finding)

    except ClientError as error:
        error_code = error.response["Error"]["Code"]
        error_message = error.response["Error"]["Message"]

        if error_code == "AccessDeniedException" and "Macie is not enabled" in error_message:
            finding = Finding(
                service="Macie",
                check="Macie Enabled",
                resource="Amazon Macie",
                region=region,
                status="WARN",
                severity="HIGH",
                message="Amazon Macie is not enabled",
                recommendation="Enable Amazon Macie to support discovery and monitoring of sensitive data in S3.",
            )

            findings.append(finding)

        else:
            raise

    return findings

def check_macie_findings():
    macie = boto3.client("macie2")
    findings = []
    finding_ids = []

    paginator = macie.get_paginator("list_findings")

    for page in paginator.paginate():
        finding_ids.extend(page.get("findingIds", []))

    if not finding_ids:
        return findings

    response = macie.get_findings(
        findingIds=finding_ids
    )

    for macie_finding in response.get("findings", []):
        finding_type = macie_finding.get("type", "")
        severity = macie_finding.get("severity", {}).get("description", "Unknown")
        region = macie_finding.get("region", "unknown")

        s3_object = macie_finding.get("resourcesAffected", {}).get("s3Object", {})
        resource = s3_object.get("path", "Unknown S3 object")

        sensitive_data = (
            macie_finding
            .get("classificationDetails", {})
            .get("result", {})
            .get("sensitiveData", [])
        )

        detections = []

        for category in sensitive_data:
            for detection in category.get("detections", []):
                data_type = detection.get("type", "UNKNOWN")
                count = detection.get("count", 0)

                detections.append(
                    f"{count} occurrence(s) of {data_type}"
                )

        if detections:
            message = "Macie detected " + ", ".join(detections)
        else:
            message = f"Macie detected sensitive data: {finding_type}"

        finding = Finding(
            service="Macie",
            check="Sensitive Data Finding",
            resource=resource,
            status="FAIL",
            severity=severity.upper(),
            message=message,
            recommendation="Review the sensitive data, confirm whether it is required, and restrict access or remove it where appropriate.",
            region=region,
        )

        findings.append(finding)

    return findings

