# Cyber Databricks AWS IAM Controls

> **Project type:** Cloud IAM Security Assessment Lab  
> **Platform:** Databricks on AWS  
> **Focus:** IAM trust, least privilege, S3 access boundaries, logging integrity, and policy validation

---

## Executive Brief

This repository is built like a security assessment package for a Databricks workspace running on AWS. Instead of only showing sample code, it shows how a cyber/cloud security engineer would review IAM access, identify risky permission patterns, document control expectations, and build repeatable validation around Databricks access to AWS resources.

The project answers one main question:

> How can Databricks use AWS resources without giving the workspace broad or unsafe cloud permissions?

---

## Assessment Scenario

A Databricks workspace needs access to AWS services for analytics workloads. The workspace may need to read and write to approved S3 data lake paths, publish logs to CloudWatch, and use encryption keys for protected data. Security needs to make sure the integration does not create excessive access, weak cross-account trust, or privilege escalation paths.

This project reviews the IAM design as if it were going through a cloud security assessment before production use.

---

## Security Objectives

| Objective | What the project demonstrates |
|---|---|
| Control cross-account trust | Trust policy requires the Databricks AWS principal and an external ID condition |
| Reduce data access scope | S3 policy is limited to approved buckets and prefixes |
| Protect audit evidence | CloudWatch policy allows log delivery but denies destructive log actions |
| Prevent privilege escalation | Permission boundary denies sensitive IAM, Organizations, CloudTrail, GuardDuty, and Config actions |
| Automate review | Python validator flags risky IAM policy patterns before deployment |
| Support audit conversations | Documentation maps the project to control themes, threats, and remediation steps |

---

## Repository Evidence Map

```text
Cyber_Databricks_AWS_IAM_Controls
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
│   ├── control-mapping.md
│   ├── threat-model.md
│   └── remediation-guide.md
│
└── .github/workflows/
    └── iam-policy-scan.yml
```

---

## Assessment Workflow

### 1. Review the trust boundary

Start with the Databricks cross-account role trust policy. Confirm that only the expected Databricks AWS principal can assume the role and that an external ID is required.

**Evidence:** `iam-policies/databricks-cross-account-role-trust-policy.json`

### 2. Review data lake permissions

Check whether Databricks access is scoped to approved S3 buckets and prefixes. The goal is to avoid broad access such as `s3:*` on all resources.

**Evidence:** `iam-policies/least-privilege-s3-access-policy.json`

### 3. Review logging permissions

Validate that the role can create and write CloudWatch logs, but cannot delete logs or remove retention settings.

**Evidence:** `iam-policies/cloudwatch-logs-access-policy.json`

### 4. Review privilege escalation controls

Check whether the permission boundary prevents unsafe IAM and security-service changes, such as attaching admin policies, passing privileged roles, stopping CloudTrail, or deleting GuardDuty detectors.

**Evidence:** `iam-policies/restricted-admin-boundary-policy.json`

### 5. Run automated policy review

Use the validator to detect risky patterns in the policy files.

```bash
python scripts/validate_databricks_iam.py --policy-dir iam-policies
```

The validator flags examples such as wildcard actions, wildcard resources, missing external ID conditions, and high-risk administrative actions.

---

## What Makes This Project Different

This project is structured as a **security review package**, not just a coding demo. It shows:

- how IAM policies are reviewed in a cloud security assessment,
- what evidence a reviewer would look at,
- what threats matter for Databricks on AWS,
- how guardrails reduce the blast radius,
- and how a lightweight CI workflow can support policy-as-code review.

---

## Key Files to Review First

| Priority | File | Why it matters |
|---|---|---|
| 1 | `docs/threat-model.md` | Explains the main IAM and data access risks |
| 2 | `iam-policies/databricks-cross-account-role-trust-policy.json` | Shows how cross-account role assumption is controlled |
| 3 | `iam-policies/least-privilege-s3-access-policy.json` | Shows scoped data lake access |
| 4 | `iam-policies/restricted-admin-boundary-policy.json` | Shows privilege escalation guardrails |
| 5 | `scripts/validate_databricks_iam.py` | Shows automated review logic |

---

## Skills Highlighted

- AWS IAM policy design
- Databricks security architecture review
- Cross-account role trust analysis
- S3 least-privilege access design
- Permission boundary guardrails
- CloudWatch logging protection
- Python policy validation
- Terraform IAM resource modeling
- Control mapping and threat documentation

---

## Disclaimer

This is a portfolio security lab using sample account IDs, role names, and bucket names. Replace all placeholders and validate against your organization’s Databricks and AWS requirements before using in a real environment.
