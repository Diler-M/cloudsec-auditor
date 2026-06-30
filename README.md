# CloudSec Auditor

CloudSec Auditor is a Python-based AWS security auditing tool built using Boto3.

The project automates common AWS security checks to identify misconfigurations, improve cloud security posture, and demonstrate practical Cloud Security and DevSecOps automation skills.

Rather than manually checking resources in the AWS Console, CloudSec Auditor interacts directly with AWS APIs to perform security audits across multiple AWS services.

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

### Amazon EC2

- ✅ Audit Security Groups exposing SSH (22) to the internet
- ✅ Audit Security Groups exposing RDP (3389) to the internet

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
- ⬜ Unused IAM users
- ⬜ Password policy audit
- ⬜ Console login audit

### Amazon EC2

- ⬜ Public EC2 instance detection
- ⬜ EBS encryption audit
- ⬜ IMDSv2 enforcement
- ⬜ Unattached Security Groups

### AWS GuardDuty

- ⬜ GuardDuty enabled
- ⬜ Active findings
- ⬜ Severity summary

### AWS CloudTrail

- ⬜ CloudTrail enabled
- ⬜ Multi-region trail
- ⬜ Log file validation
- ⬜ S3 log destination audit

### Reporting

- ⬜ JSON report generation
- ⬜ CSV report generation
- ⬜ HTML dashboard
- ⬜ Security score
- ⬜ Severity classification

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

WARN: Diler access key is 571 days old

EC2 Security Group Audit

WARN: launch-wizard-1 (sg-0a788f30fc5c27072) allows SSH from 0.0.0.0/0

CloudSec Auditor Summary

PASS: 3
WARN: 3
FAIL: 0
```

---

## Project Structure

```text
cloudsec-auditor/
│
├── checks/
│   ├── ec2_checks.py
│   ├── iam_checks.py
│   └── s3_checks.py
│
├── reports/
├── docs/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Learning Objectives

This project is helping me develop practical experience with:

- Python programming
- AWS SDK for Python (Boto3)
- AWS API automation
- Cloud Security auditing
- AWS Identity & Access Management (IAM)
- Amazon S3 Security
- Amazon EC2 Security
- Secure coding practices
- Git & GitHub workflows

---

## Future Vision

The long-term goal is to evolve CloudSec Auditor into a lightweight AWS security auditing framework capable of auditing multiple AWS services, producing structured compliance reports, and demonstrating real-world Cloud Security and DevSecOps engineering skills.