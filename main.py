import argparse

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


def print_summary(summary):
    print("\nCloudSec Auditor Summary:\n")
    print(f"PASS: {summary['PASS']}")
    print(f"WARN: {summary['WARN']}")
    print(f"FAIL: {summary['FAIL']}")


def main():
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

    args = parser.parse_args()

    summary = {
        "PASS": 0,
        "WARN": 0,
        "FAIL": 0,
    }

    if args.s3 or args.all:
        check_bucket_public_access(summary)
        check_bucket_encryption(summary)
        check_bucket_versioning(summary)

    if args.iam or args.all:
        check_iam_mfa(summary)
        check_access_key_age(summary)

    if args.ec2 or args.all:
        check_ec2_sg(summary)

    if args.cloudtrail or args.all:
        check_cloudtrail_enabled(summary)

    if args.guardduty or args.all:
        check_guardduty_enabled(summary)

    if args.securityhub or args.all:
        check_securityhub_enabled(summary)

    print_summary(summary)


if __name__ == "__main__":
    main()