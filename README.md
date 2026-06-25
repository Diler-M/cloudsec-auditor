# CloudSec Auditor

CloudSec Auditor is a Python and Boto3-based AWS security auditing tool that automates common cloud security checks against an AWS account.

The aim of this project is to demonstrate practical cloud security automation using AWS APIs instead of relying solely on manual console checks.

---

## Features

### S3 Auditing

- ✅ Enumerate all S3 buckets
- ✅ Check Block Public Access configuration
- ✅ Check default server-side encryption
- ✅ Check bucket versioning
- ✅ Summary of PASS / WARN / FAIL findings

---

## Planned Features

### IAM

- ⬜ Users without MFA
- ⬜ Old access keys
- ⬜ Administrator accounts
- ⬜ Unused IAM users

### EC2

- ⬜ Security Groups exposing SSH (22)
- ⬜ Security Groups exposing RDP (3389)
- ⬜ Unencrypted EBS volumes

### GuardDuty

- ⬜ GuardDuty enabled
- ⬜ Active findings
- ⬜ Severity summary

### Reporting

- ⬜ JSON report
- ⬜ CSV report
- ⬜ HTML report

---

## Technologies

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- VS Code

---

## Current Example Output

```text
S3 Bucket Public Access Audit

PASS: terraform-statefile-diler blocks public access

S3 Bucket Encryption Audit

PASS: terraform-statefile-diler has default encryption enabled using AES256

S3 Bucket Versioning Audit

WARN: terraform-statefile-diler does not have versioning enabled

CloudSec Auditor Summary

PASS: 2
WARN: 1
FAIL: 0
```