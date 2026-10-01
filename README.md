# CloudSec Auditor

CloudSec Auditor is an AWS security auditing tool that identifies common cloud security misconfigurations and sensitive data risks.

It assesses security controls across AWS services, provides remediation guidance, and supports both console and JSON reporting.

## Security Checks

CloudSec Auditor currently assesses:

- **Amazon S3** - public access, encryption and versioning
- **AWS IAM** - MFA and access key age
- **Amazon EC2** - exposed SSH and RDP security group rules
- **AWS CloudTrail** - trail availability
- **Amazon GuardDuty** - regional threat detection coverage
- **AWS Security Hub** - security posture monitoring
- **Amazon Macie** - sensitive data discovery in S3

Findings are classified as `PASS`, `WARN` or `FAIL` and include remediation guidance.

## Sensitive Data Discovery

Amazon Macie integration extends the project beyond infrastructure configuration into data security.

A controlled S3 lab containing synthetic customer data was created and analysed using Macie. The assessment identified six occurrences of credit card number data and generated a high-severity financial information finding.

CloudSec Auditor retrieved and surfaced the finding:

```text
FAIL: eu-west-2 - cloudsec-auditor-macie-lab-1/Synthetic_Data.csv - Macie detected 6 occurrence(s) of CREDIT_CARD_NUMBER
Recommendation: Review the sensitive data, confirm whether it is required, and restrict access or remove it where appropriate.
```

No real personal or payment information was used.

## Example

Run a complete audit:

```bash
python main.py --all
```

Example findings:

```text
PASS: global - cloudsec-auditor-macie-lab-1 - Bucket blocks public access

WARN: eu-west-2 - launch-wizard-1 (...) - Allows SSH from 0.0.0.0/0

FAIL: eu-west-2 - cloudsec-auditor-macie-lab-1/Synthetic_Data.csv - Macie detected 6 occurrence(s) of CREDIT_CARD_NUMBER
```

Run an individual assessment:

```bash
python main.py --s3
python main.py --iam
python main.py --ec2
python main.py --cloudtrail
python main.py --guardduty
python main.py --securityhub
python main.py --macie
```

## JSON Reporting

Audit results can also be exported as structured JSON:

```bash
python main.py --all --json
```

Reports are generated under:

```text
reports/cloudsec-audit.json
```

This provides a foundation for integration with CI/CD pipelines, dashboards and other security automation.

## Security Approach

The project focuses on:

- Least privilege AWS access
- Actionable security findings
- Multi-region assessment where appropriate
- Sensitive data discovery and classification
- Clear remediation guidance
- Separation of configuration security from data security

For example, an S3 bucket can block public access and use encryption while still contain sensitive data that requires appropriate governance and access controls.

## Installation

```bash
git clone <repository-url>
cd cloudsec-auditor
pip install -r requirements.txt
aws configure
python main.py --all
```

A dedicated AWS identity with read-only security permissions should be used. AWS credentials are not stored in the repository.

## Technologies

AWS, Amazon S3, IAM, EC2, CloudTrail, GuardDuty, Security Hub, Amazon Macie, Python, Boto3, JSON, Git and GitHub.

## Roadmap

- Automated testing
- GitHub Actions CI
- Improved EC2 security group analysis
- CloudTrail logging-status validation
- Expanded regional checks
- Additional data-security controls

## Disclaimer

CloudSec Auditor is an educational and portfolio project. Findings should be reviewed in the context of the AWS environment and organisation's security requirements.