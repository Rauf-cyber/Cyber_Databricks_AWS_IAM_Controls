# Control Mapping

This document maps the Databricks AWS IAM control examples to common cloud security control themes.

| Control Area | Security Intent | Project Example |
|---|---|---|
| Least Privilege | Grant only the permissions Databricks needs to access approved data and logs | S3 policy scoped to approved buckets and prefixes |
| Strong Trust Boundary | Prevent untrusted accounts from assuming Databricks roles | Cross-account trust policy with external ID condition |
| Privilege Escalation Prevention | Prevent role/user creation, broad policy attachment, and unsafe PassRole patterns | Permission boundary deny statements |
| Data Protection | Require encrypted writes to S3 | Deny unencrypted S3 object uploads |
| Logging Integrity | Allow log delivery but prevent log deletion | CloudWatch policy denies log tampering |
| Policy-as-Code Review | Detect risky IAM patterns before deployment | Python validator and GitHub Actions workflow |

## NIST-Style Alignment

- **AC-2 Account Management:** supports review of identities and role assumptions.
- **AC-3 Access Enforcement:** enforces approved IAM permissions and denies unsafe actions.
- **AC-6 Least Privilege:** limits S3, CloudWatch, KMS, and IAM permissions.
- **AU-9 Protection of Audit Information:** prevents CloudWatch log deletion or retention bypass.
- **CM-6 Configuration Settings:** documents secure IAM baseline expectations.
- **SI-4 System Monitoring:** supports logging and monitoring through CloudWatch access.

## Review Questions

- Does the Databricks role trust only the required Databricks AWS principal?
- Is an external ID required in the trust policy?
- Are S3 permissions scoped to specific buckets and prefixes?
- Are sensitive IAM actions denied or restricted?
- Can the workspace write logs without deleting or disabling logs?
- Are policy files reviewed before being deployed?
