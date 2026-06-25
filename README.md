# CloudSec Auditor

CloudSec Auditor is a Python and Boto3-based AWS security auditing tool designed to automate common cloud security checks across an AWS environment.

The aim of this project is to demonstrate practical Cloud Security automation by interacting directly with AWS APIs instead of relying solely on manual console checks.

---

## Current Features

### S3 Auditing

- ✅ Enumerate S3 buckets
- ✅ Check Block Public Access configuration
- ✅ Check default server-side encryption
- ✅ Check bucket versioning

### IAM Auditing

- ✅ Audit IAM users for MFA enforcement

### Reporting

- ✅ PASS / WARN / FAIL summary

---

## Planned Features

### IAM

- ⬜ Access key age audit
- ⬜ Administrator account detection
- ⬜ Unused IAM users
- ⬜ Password policy audit

### EC2

- ⬜ Security Groups exposing SSH (22)
- ⬜ Security Groups exposing RDP (3389)
- ⬜ Public EC2 instances
- ⬜ EBS encryption audit
- ⬜ IMDSv2 enforcement

### S3

- ⬜ Bucket policy analysis
- ⬜ Access logging audit
- ⬜ KMS encryption validation
- ⬜ Lifecycle policy audit

### GuardDuty

- ⬜ GuardDuty status
- ⬜ Active findings
- ⬜ Severity summary

### CloudTrail

- ⬜ CloudTrail enabled
- ⬜ Multi-region trail
- ⬜ Log validation enabled

### Reporting

- ⬜ JSON report
- ⬜ CSV report
- ⬜ HTML dashboard

---

## Technologies

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- VS Code

---

## Example Output

```text
S3 Bucket Public Access Audit

PASS: terraform-statefile-diler blocks public access

S3 Bucket Encryption Audit

PASS: terraform-statefile-diler has default encryption enabled using AES256

S3 Bucket Versioning Audit

WARN: terraform-statefile-diler does not have versioning enabled

IAM MFA Audit

PASS: Diler has MFA enabled

CloudSec Auditor Summary

PASS: 3
WARN: 1
FAIL: 0
```

---

## Project Goals

- Learn Python through practical AWS automation.
- Develop real-world Cloud Security auditing capabilities.
- Demonstrate hands-on experience with AWS APIs using Boto3.
- Build a portfolio project representative of work performed by Cloud Security and DevSecOps Engineers.