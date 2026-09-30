import argparse

from reporting.console import print_finding

from checks.s3_checks import (
    check_bucket_public_access,
    check_bucket_encryption,
    check_bucket_versioning,
)

from checks.iam_checks import (
    check_iam_mfa,
    check_access_key_age,
)

from checks.ec2_checks import check_ec2_sg
from checks.cloudtrail_checks import check_cloudtrail_enabled
from checks.guardduty_checks import check_guardduty_enabled
from checks.securityhub_checks import check_securityhub_enabled
from checks.macie_checks import check_macie_enabled, check_macie_findings
from reporting.json_report import write_json_report




def print_summary(summary):
    print("\nCloudSec Auditor Summary:\n")
    print(f"PASS: {summary['PASS']}")
    print(f"WARN: {summary['WARN']}")
    print(f"FAIL: {summary['FAIL']}")

def process_findings(findings, summary, all_findings):
    if not findings:
        print("INFO: No applicable resources found.\n")
        return

    for finding in findings:
        print_finding(finding)
        summary[finding.status] += 1
        all_findings.append(finding)

def main():
    all_findings = []
    parser = argparse.ArgumentParser(
        description="CloudSec Auditor - AWS security auditing tool"
    )

    parser.add_argument(
        "--s3",
        action="store_true",
        help="Run S3 security checks"
    )

    parser.add_argument(
        "--iam",
        action="store_true",
        help="Run IAM security checks"
    )

    parser.add_argument(
        "--ec2",
        action="store_true",
        help="Run EC2 security checks"
    )

    parser.add_argument(
        "--cloudtrail",
        action="store_true",
        help="Run CloudTrail security checks"
    )

    parser.add_argument(
        "--guardduty",
        action="store_true",
        help="Run GuardDuty security checks"
    ) 

    parser.add_argument(
        "--securityhub",
        action="store_true",
        help="Run Security Hub security checks"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all security checks"
    )

    parser.add_argument(
    "--macie",
    action="store_true",
    help="Run Amazon Macie audit"
    )

    parser.add_argument(
    "--json",
    action="store_true",
    help="Write findings to a JSON report"
    )

    args = parser.parse_args()

    summary = {
        "PASS": 0,
        "WARN": 0,
        "FAIL": 0,
    }

    if args.s3 or args.all:
        findings = check_bucket_public_access()

        print("\nS3 Bucket Public Access Audit:\n")

        process_findings(findings, summary, all_findings)

        findings = check_bucket_encryption()

        print("\nS3 Bucket Encryption Audit:\n")

        process_findings(findings, summary, all_findings)

        findings = check_bucket_versioning()

        print("\nS3 Bucket Versioning Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.iam or args.all:
        findings = check_iam_mfa()

        print("\nIAM MFA Audit:\n")

        process_findings(findings, summary, all_findings)

        findings = check_access_key_age()

        print("\nIAM Access Key Age Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.ec2 or args.all:
        findings = check_ec2_sg()

        print("\nEC2 Security Group Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.cloudtrail or args.all:
        findings = check_cloudtrail_enabled()

        print("\nCloudTrail Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.guardduty or args.all:
        findings = check_guardduty_enabled()

        print("\nGuardDuty Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.securityhub or args.all:
        findings = check_securityhub_enabled()

        print("\nSecurity Hub Audit:\n")

        process_findings(findings, summary, all_findings)

    if args.macie or args.all:
        findings = check_macie_enabled()

        print("\nAmazon Macie Audit:\n")

        process_findings(findings, summary, all_findings)

        findings = check_macie_findings()

        print("\nAmazon Macie Sensitive Data Findings:\n")

        process_findings(findings, summary, all_findings)

    print_summary(summary)

    if args.json:
        output_path = write_json_report(all_findings, summary)
        print(f"\nJSON report written to: {output_path}")
    
if __name__ == "__main__":
    main()