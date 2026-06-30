# CloudSec Auditor

CloudSec Auditor is a Python-based AWS security auditing tool built using Boto3.

The project automates common AWS security checks to identify misconfigurations, improve cloud security posture, and demonstrate practical Cloud Security and DevSecOps automation skills.

Rather than manually inspecting resources through the AWS Console, CloudSec Auditor queries AWS APIs directly to perform automated security audits across multiple AWS services.

---

## Current Features

### Amazon S3

- ✅ Enumerate S3 buckets
- ✅ Audit Block Public Access configuration
- ✅ Audit default server-side encryption
- ✅ Audit bucket versioning

### AWS IAM

- ✅ Audit MFA enforcement
- ✅ Audit IAM access key age

### Amazon EC2

- ✅ Audit Security Groups exposing SSH (22)
- ✅ Audit Security Groups exposing RDP (3389)
- ✅ Multi-region Security Group scanning

### Reporting

- ✅ PASS / WARN / FAIL summary

---

## Planned Features

### Amazon S3

- ⬜ Bucket policy analysis
- ⬜ Lifecycle policy audit
- ⬜ Access logging audit
- ⬜ KMS encryption validation
- ⬜ Public bucket policy detection

### AWS IAM

- ⬜ Administrator account detection
- ⬜ Unused IAM users
- ⬜ Password policy audit
- ⬜ Console login audit
- ⬜ IAM role audit

### Amazon EC2

- ⬜ Public EC2 instance detection
- ⬜ EBS encryption audit
- ⬜ IMDSv2 enforcement
- ⬜ Unattached Security Groups
- ⬜ Security Groups allowing all traffic
- ⬜ Internet-facing instances

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
- ⬜ Finding severity (Low / Medium / High / Critical)

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

PASS: Diler access key is 0 days old

EC2 Security Group Audit

WARN: eu-west-1 - launch-wizard-1 (sg-0a788f30fc5c27072) allows SSH from 0.0.0.0/0

CloudSec Auditor Summary

PASS: 4
WARN: 2
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
├── docs/
├── reports/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Skills Demonstrated

- Python programming
- AWS SDK (Boto3)
- AWS API automation
- Cloud Security auditing
- IAM security
- Amazon S3 security
- Amazon EC2 security
- Multi-region AWS resource discovery
- Secure coding practices
- Git & GitHub workflows

---

## Future Vision

The goal is to evolve CloudSec Auditor into a lightweight AWS security auditing framework capable of assessing multiple AWS services, generating structured compliance reports, and demonstrating practical Cloud Security and DevSecOps engineering techniques.

Future versions will include richer reporting, severity classification, automated compliance checks, and support for additional AWS security services.