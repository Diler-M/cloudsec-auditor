# 🔒 CloudSec Auditor

CloudSec Auditor is a Python-based AWS security auditing tool built using **Boto3**.

The project automates common AWS security checks across multiple AWS services to identify misconfigurations, improve cloud security posture, and demonstrate practical Cloud Security and DevSecOps engineering skills.

Rather than manually inspecting resources through the AWS Console, CloudSec Auditor queries AWS APIs directly to perform automated security audits.

---

# ✨ Current Features

## Amazon S3

- ✅ Enumerate S3 buckets
- ✅ Audit Block Public Access configuration
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

## Reporting

- ✅ PASS / WARN / FAIL summary

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
- ⬜ IAM role audit

## Amazon EC2

- ⬜ Public EC2 instance detection
- ⬜ Security Groups allowing all traffic
- ⬜ EBS encryption audit
- ⬜ IMDSv2 enforcement
- ⬜ Unattached Security Groups

## AWS CloudTrail

- ⬜ Multi-region trail validation
- ⬜ Log file validation
- ⬜ Management events enabled
- ⬜ Data events enabled

## AWS GuardDuty

- ⬜ GuardDuty enabled
- ⬜ Active findings
- ⬜ Severity summary

## AWS Security Hub

- ⬜ Security Hub enabled
- ⬜ Security score
- ⬜ Failed security controls

## AWS Config

- ⬜ AWS Config enabled
- ⬜ Compliance rules
- ⬜ Non-compliant resources

## Reporting

- ⬜ JSON reports
- ⬜ CSV reports
- ⬜ HTML dashboard
- ⬜ Finding severity (Low / Medium / High / Critical)
- ⬜ CLI options (`--s3`, `--iam`, `--ec2`, `--all`)
- ⬜ Logging

---

# 🛠 Technologies

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- VS Code

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

WARN: eu-west-1 - launch-wizard-1 (sg-0a788f30fc5c27072) allows SSH from 0.0.0.0/0

CloudTrail Audit

PASS: CloudTrail trail found: management-events

CloudSec Auditor Summary

PASS: 5
WARN: 2
FAIL: 0
```

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

# 🎯 Skills Demonstrated

- Python programming
- AWS SDK for Python (Boto3)
- AWS API automation
- Cloud Security auditing
- Amazon S3 security
- IAM security
- EC2 networking and Security Groups
- AWS CloudTrail
- Multi-region resource discovery
- Secure coding practices
- Git & GitHub workflows

---

# 🚀 Project Goals

CloudSec Auditor is being developed to demonstrate the type of automation a Cloud Security or DevSecOps Engineer performs in production environments.

The long-term vision is to evolve the project into a lightweight AWS security auditing framework capable of:

- Auditing multiple AWS services
- Producing structured compliance reports
- Identifying security misconfigurations
- Helping improve cloud security posture