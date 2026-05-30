<p align="center">
  <img src="./assets/cyber-databricks-banner.svg" alt="Cyber Databricks AWS IAM Controls banner" width="100%" />
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#security-review-diagram">Diagram</a> •
  <a href="#what-this-project-covers">Coverage</a> •
  <a href="#repo-contents">Repo Contents</a> •
  <a href="#skills-highlighted">Skills</a>
</p>

---

## Overview

**Cyber Databricks AWS IAM Controls** is a portfolio project built to showcase how a Databricks deployment on AWS can be reviewed from a **cloud IAM security** perspective.

This project focuses on the most important access-control and security-review areas, including:

- **Cross-account IAM trust relationships**
- **Least-privilege S3 access**
- **CloudWatch logging permissions**
- **Permission boundaries**
- **IAM policy validation and security review workflow**

Instead of looking like a generic lab, this repository is structured like a **real cloud security engineering review package**.

---

## Security Review Diagram

<p align="center">
  <img src="./assets/iam-security-review-diagram.svg" alt="Databricks on AWS IAM security review diagram" width="100%" />
</p>

---

## What This Project Covers

| Review Area | Purpose | Example Artifact |
|---|---|---|
| Cross-account trust | Restrict who can assume the Databricks role | `iam-policies/databricks-cross-account-role-trust-policy.json` |
| Data access control | Limit S3 access to approved buckets and prefixes | `iam-policies/least-privilege-s3-access-policy.json` |
| Logging integrity | Allow logging while protecting audit evidence | `iam-policies/cloudwatch-logs-access-policy.json` |
| Privilege escalation prevention | Block high-risk IAM and admin actions | `iam-policies/restricted-admin-boundary-policy.json` |
| Policy validation | Detect risky patterns in IAM policies | `scripts/validate_databricks_iam.py` |

---

## Repo Contents

```text
Cyber_Databricks_AWS_IAM_Controls
│
├── assets/
│   ├── cyber-databricks-banner.svg
│   └── iam-security-review-diagram.svg
│
├── iam-policies/
│   ├── databricks-cross-account-role-trust-policy.json
│   ├── least-privilege-s3-access-policy.json
│   ├── cloudwatch-logs-access-policy.json
│   └── restricted-admin-boundary-policy.json
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── scripts/
│   └── validate_databricks_iam.py
│
├── docs/
│   ├── assessment-checklist.md
│   ├── control-mapping.md
│   ├── threat-model.md
│   └── remediation-guide.md
│
└── .github/workflows/
    └── iam-policy-scan.yml
```

---

## Quick Review Flow

1. Review the **trust policy** for the Databricks access path.
2. Review the **S3 access policy** for least privilege.
3. Review the **CloudWatch logging policy** to preserve audit visibility.
4. Review the **permission boundary** for escalation control.
5. Run the **validation script** to scan for risky IAM patterns.

```bash
python scripts/validate_databricks_iam.py --policy-dir iam-policies
```

---

## Skills Highlighted

- AWS IAM security design
- Databricks security review
- Cross-account trust policy analysis
- Least-privilege S3 access design
- Permission boundary implementation
- CloudWatch logging protection
- Python-based policy validation
- Terraform IAM modeling
- Security documentation and assessment workflow

---

## Best Files to Open First

- `assets/cyber-databricks-banner.svg`
- `assets/iam-security-review-diagram.svg`
- `docs/threat-model.md`
- `iam-policies/restricted-admin-boundary-policy.json`
- `scripts/validate_databricks_iam.py`

---

## Disclaimer

This is a portfolio project using sample AWS account IDs, resource names, and role names for demonstration purposes only.
