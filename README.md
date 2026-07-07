# 🔒 CloudSec Auditor

CloudSec Auditor is a modular Python-based AWS security auditing framework built using **Boto3**.

The project automates common AWS security checks across multiple AWS services to identify security misconfigurations, improve cloud security posture, and demonstrate practical Cloud Security and DevSecOps engineering skills.

Rather than manually inspecting resources through the AWS Console, CloudSec Auditor queries AWS APIs directly and performs automated security audits.

---

# ✨ Current Features

## Amazon S3

- ✅ Audit Block Public Access
- ✅ Audit Default Server-Side Encryption
- ✅ Audit Bucket Versioning

## AWS IAM

- ✅ Audit MFA Enforcement
- ✅ Audit Access Key Age

## Amazon EC2

- ✅ Multi-region Security Group Discovery
- ✅ Detect Security Groups exposing SSH (22)
- ✅ Detect Security Groups exposing RDP (3389)

## AWS CloudTrail

- ✅ Audit CloudTrail Trail Configuration

## AWS GuardDuty

- ✅ Multi-region GuardDuty Enabled Audit

## AWS Security Hub

- ✅ Audit Security Hub Enabled Status

---

# 💻 Command Line Interface

Run every audit:

```bash
python main.py --all
```

Run individual audits:

```bash
python main.py --s3
python main.py --iam
python main.py --ec2
python main.py --cloudtrail
python main.py --guardduty
python main.py --securityhub
```

---

# 🏗 Project Architecture

CloudSec Auditor follows a modular architecture to separate AWS auditing logic, shared utilities, reporting, and data models.

```
               main.py
                   │
        ┌──────────┴──────────┐
        │                     │
     checks/             reporting/
        │                     │
        └──────────┬──────────┘
                   │
              models/
                   │
               utils/
```

## Folder Structure

```text
cloudsec-auditor/
│
├── checks/
│   ├── cloudtrail_checks.py
│   ├── ec2_checks.py
│   ├── guardduty_checks.py
│   ├── iam_checks.py
│   ├── s3_checks.py
│   └── securityhub_checks.py
│
├── models/
│   ├── finding.py
│   └── __init__.py
│
├── reporting/
│   ├── console.py
│   └── __init__.py
│
├── utils/
│   ├── aws.py
│   └── __init__.py
│
├── docs/
├── reports/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📋 Supported Audits

| Service | Audit | Status |
|----------|-----------------------------|:------:|
| S3 | Block Public Access | ✅ |
| S3 | Default Encryption | ✅ |
| S3 | Bucket Versioning | ✅ |
| IAM | MFA Enabled | ✅ |
| IAM | Access Key Age | ✅ |
| EC2 | SSH Exposure | ✅ |
| EC2 | RDP Exposure | ✅ |
| EC2 | Multi-region Discovery | ✅ |
| CloudTrail | Trail Detection | ✅ |
| GuardDuty | Multi-region Enabled Audit | ✅ |
| Security Hub | Enabled Audit | ✅ |

---

# 🛠 Technologies

- Python
- Boto3
- AWS CLI
- Git
- GitHub
- VS Code

---

# 🧠 Design Principles

The project is gradually being refactored from a collection of scripts into a reusable security auditing framework.

Current design principles include:

- Modular architecture
- Separation of concerns
- Shared AWS utility functions
- Reusable Finding data model
- Centralised console reporting
- Multi-region AWS support
- Command-line interface

---

# 🚧 Roadmap

## AWS Services

### Amazon S3

- ⬜ Bucket Policy Analysis
- ⬜ Lifecycle Policy Audit
- ⬜ Access Logging Audit
- ⬜ KMS Encryption Validation

### AWS IAM

- ⬜ Administrator Detection
- ⬜ Unused IAM Users
- ⬜ Password Policy Audit
- ⬜ Console Login Audit

### Amazon EC2

- ⬜ Public EC2 Instance Detection
- ⬜ IMDSv2 Enforcement
- ⬜ EBS Encryption Audit
- ⬜ Security Groups allowing all traffic

### AWS CloudTrail

- ⬜ Management Event Validation
- ⬜ Data Event Validation
- ⬜ Multi-region Trail Validation

### AWS GuardDuty

- ⬜ Active Findings
- ⬜ Malware Protection Status
- ⬜ Finding Severity Summary

### AWS Security Hub

- ⬜ High Severity Findings
- ⬜ Failed Security Controls
- ⬜ Security Score

### AWS Config

- ⬜ AWS Config Enabled
- ⬜ Compliance Rules
- ⬜ Non-compliant Resources

---

## Framework Improvements

- ⬜ Finding-based reporting for every audit
- ⬜ JSON reports
- ⬜ CSV reports
- ⬜ HTML reports
- ⬜ Severity scoring
- ⬜ Logging
- ⬜ GitHub Actions CI
- ⬜ Unit tests
- ⬜ Type hints
- ⬜ CHANGELOG
- ⬜ GitHub Releases

---

# 🎯 Skills Demonstrated

- Python programming
- AWS SDK for Python (Boto3)
- AWS API automation
- Cloud Security auditing
- AWS IAM
- Amazon S3
- Amazon EC2
- AWS CloudTrail
- AWS GuardDuty
- AWS Security Hub
- Multi-region AWS resource discovery
- Software architecture & refactoring
- Command-line tooling (argparse)
- Git & GitHub workflows

---

# 🚀 Project Vision

CloudSec Auditor is being developed as a practical Cloud Security portfolio project that demonstrates the type of automation performed by Cloud Security and DevSecOps Engineers.

The long-term goal is to evolve the project into a lightweight AWS security auditing framework capable of auditing multiple AWS services, generating structured findings, producing multiple report formats, and helping improve AWS security posture.