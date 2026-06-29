# CloudSec Auditor

CloudSec Auditor is a Python-based AWS security auditing tool built with Boto3.

The project automates common cloud security checks across AWS services, helping identify security misconfigurations and compliance issues without relying on manual inspection in the AWS Console.

This project is being built as a practical learning exercise in Python while demonstrating real-world Cloud Security and DevSecOps automation techniques.

---

## Features

### Amazon S3

- ✅ Enumerate S3 buckets
- ✅ Audit Block Public Access configuration
- ✅ Audit default server-side encryption
- ✅ Audit bucket versioning

### AWS IAM

- ✅ Audit MFA enforcement
- ✅ Audit IAM access key age

### Reporting

- ✅ PASS / WARN / FAIL finding summary

---

## Planned Features

### Amazon S3

- ⬜ Bucket policy analysis
- ⬜ Lifecycle policy audit
- ⬜ Access logging audit
- ⬜ KMS encryption validation

### AWS IAM

- ⬜ Administrator account detection
- ⬜ Inactive IAM users
- ⬜ Password policy audit
- ⬜ Console login audit

### Amazon EC2

- ⬜ Security Groups exposing SSH (22)
- ⬜ Security Groups exposing RDP (3389)
- ⬜ Public EC2 instances
- ⬜ Unencrypted EBS volumes
- ⬜ IMDSv2 enforcement

### AWS GuardDuty

- ⬜ GuardDuty enabled
- ⬜ Active findings
- ⬜ Severity summary

### AWS CloudTrail

- ⬜ CloudTrail enabled
- ⬜ Multi-region trail
- ⬜ Log file validation
- ⬜ S3 logging destination audit

### Reporting

- ⬜ JSON report generation
- ⬜ CSV report generation
- ⬜ HTML dashboard
- ⬜ Security score

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

IAM Access Key Age Audit

PASS: Diler access key is 8 days old

CloudSec Auditor Summary

PASS: 4
WARN: 1
FAIL: 0
```

---

## Project Structure

```
cloudsec-auditor/
│
├── checks/
│   ├── iam_checks.py
│   └── s3_checks.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Learning Objectives

This project is helping me develop practical experience in:

- Python programming
- AWS SDK (Boto3)
- AWS Identity & Access Management (IAM)
- Cloud security automation
- Infrastructure auditing

---

## Future Vision

The long-term goal is to evolve CloudSec Auditor into a lightweight AWS security auditing framework capable of auditing multiple AWS services and generating structured compliance reports suitable for Cloud Security and DevSecOps environments.