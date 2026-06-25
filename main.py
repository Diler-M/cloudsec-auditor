from checks.s3_checks import (
    check_bucket_public_access,
    check_bucket_encryption,
    check_bucket_versioning,
)

from checks.iam_checks import (
    check_iam_mfa,
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

print("\nCloudSec Auditor Summary:\n")
print(f"PASS: {summary['PASS']}")
print(f"WARN: {summary['WARN']}")
print(f"FAIL: {summary['FAIL']}")