# 🔒 CloudSec Auditor

CloudSec Auditor is a Python-based AWS security auditing tool built using **Boto3**.

It automates common AWS security checks across multiple AWS services to identify misconfigurations, improve cloud security posture, and demonstrate practical Cloud Security and DevSecOps engineering skills.

Instead of manually inspecting resources in the AWS Console, CloudSec Auditor queries AWS APIs directly and performs automated security audits.

---

# ✨ Features

## Amazon S3

- ✅ Enumerate S3 buckets
- ✅ Audit Block Public Access
- ✅ Audit default server-side encryption
- ✅ Audit bucket versioning

## AWS IAM

- ✅ Audit MFA enforcement
- ✅ Audit IAM access key age

## Amazon EC2

- ✅ Multi-region Security Group discovery
- ✅ Detect Security Groups exposing SSH (22)
- ✅ Detect Security Groups exposing RDP (3389)

## AWS CloudTrail

- ✅ Audit CloudTrail trail configuration

## Command Line Interface

- ✅ Run individual service audits
- ✅ Run all audits with a single command

Supported commands:

```bash
python main.py --all
python main.py --s3
python main.py --iam
python main.py --ec2
python main.py --cloudtrail
```

## Reporting

- ✅ PASS / WARN / FAIL summary

---

# 📋 Example Output

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

PASS: Diler access key is 0 days old

EC2 Security Group Audit

WARN: eu-west-1 - launch-wizard-1 (sg-xxxxxxxxxxxxxxxxx) allows SSH from 0.0.0.0/0

CloudTrail Audit

PASS: CloudTrail trail found: management-events

CloudSec Auditor Summary

PASS: 5
WARN: 2
FAIL: 0
```

---

# 🛠 Technologies

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- VS Code

---

# 📁 Project Structure

```text
cloudsec-auditor/
│
├── checks/
│   ├── cloudtrail_checks.py
│   ├── ec2_checks.py
│   ├── iam_checks.py
│   └── s3_checks.py
│
├── docs/
├── reports/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚧 Roadmap

## Amazon S3

- ⬜ Bucket policy analysis
- ⬜ Lifecycle policy audit
- ⬜ Access logging audit
- ⬜ KMS encryption validation

## AWS IAM

- ⬜ Administrator account detection
- ⬜ Unused IAM users
- ⬜ Password policy audit
- ⬜ Console login audit

## Amazon EC2

- ⬜ Public EC2 instance detection
- ⬜ EBS encryption audit
- ⬜ IMDSv2 enforcement
- ⬜ Security Groups allowing all traffic

## AWS CloudTrail

- ⬜ Multi-region trail validation
- ⬜ Log file validation
- ⬜ Management event validation
- ⬜ Data event validation

## AWS GuardDuty

- ⬜ GuardDuty enabled
- ⬜ Active findings
- ⬜ Finding severity summary

## AWS Security Hub

- ⬜ Security Hub enabled
- ⬜ Failed security controls

## AWS Config

- ⬜ AWS Config enabled
- ⬜ Compliance rule audit

## Reporting

- ⬜ JSON report generation
- ⬜ CSV report generation
- ⬜ HTML dashboard
- ⬜ Finding severity
- ⬜ Logging

---

# 🎯 Skills Demonstrated

- Python programming
- AWS SDK (Boto3)
- AWS API automation
- Cloud Security auditing
- Amazon S3 Security
- IAM Security
- EC2 Security
- CloudTrail
- Multi-region AWS resource discovery
- Command-line tooling
- Git & GitHub workflows

---

# 🚀 Project Vision

CloudSec Auditor is being developed as a practical Cloud Security portfolio project that demonstrates the type of automation performed by Cloud Security and DevSecOps Engineers.

The long-term goal is to evolve the project into a lightweight AWS security auditing framework capable of auditing multiple AWS services, producing structured compliance reports and identifying security misconfigurations across AWS environments.