from checks.s3_checks import (
    check_bucket_public_access,
    check_bucket_encryption,
    check_bucket_versioning,
)

from checks.iam_checks import (
    check_iam_mfa,
    check_access_key_age,
)

from checks.ec2_checks import (
    check_ec2_sg
)

from checks.cloudtrail_checks import (
    check_cloudtrail_enabled
)

summary = {
    "PASS": 0,
    "WARN": 0,
    "FAIL": 0,
}

check_bucket_public_access(summary)
check_bucket_encryption(summary)
check_bucket_versioning(summary)

check_iam_mfa(summary)
check_access_key_age(summary)

check_ec2_sg(summary)

check_cloudtrail_enabled(summary)

print("\nCloudSec Auditor Summary:\n")
print(f"PASS: {summary['PASS']}")
print(f"WARN: {summary['WARN']}")
print(f"FAIL: {summary['FAIL']}")