# Databricks AWS IAM Assessment Checklist

Use this checklist when reviewing a Databricks workspace integration with AWS IAM roles and policies.

## 1. Cross-Account Trust Review

- [ ] Trust policy only allows the expected Databricks AWS principal.
- [ ] Trust policy requires `sts:ExternalId`.
- [ ] Trust policy does not use wildcard principals.
- [ ] Role name and purpose are clearly documented.
- [ ] Role is not reused for unrelated workloads.

## 2. S3 Data Access Review

- [ ] S3 access is scoped to approved data lake buckets.
- [ ] S3 access is scoped to approved prefixes.
- [ ] Policy does not allow `s3:*` unless explicitly justified.
- [ ] Write access requires server-side encryption.
- [ ] Delete access is reviewed and approved based on use case.

## 3. KMS and Encryption Review

- [ ] KMS access is scoped to approved keys.
- [ ] KMS actions are limited to required encrypt/decrypt operations.
- [ ] Key administration actions are not granted to Databricks runtime roles.
- [ ] S3 object uploads require AWS KMS encryption where applicable.

## 4. Logging and Audit Review

- [ ] Databricks can publish required logs.
- [ ] Databricks cannot delete CloudWatch log groups or streams.
- [ ] Databricks cannot remove retention policies.
- [ ] CloudTrail and GuardDuty tampering actions are denied.
- [ ] Logs are routed to security monitoring where applicable.

## 5. Privilege Escalation Review

- [ ] Role cannot create IAM users or access keys.
- [ ] Role cannot attach or modify IAM policies.
- [ ] Role cannot update trust policies.
- [ ] `iam:PassRole` is denied or tightly scoped.
- [ ] Organizations-level administrative actions are denied.

## 6. Automation Review

- [ ] IAM policy files are stored in version control.
- [ ] Policy validation runs in CI.
- [ ] High-risk findings fail the pipeline.
- [ ] Security reviewers can trace policy changes through commits.
- [ ] Remediation guidance is documented for common findings.

## Review Outcome

| Outcome | Meaning |
|---|---|
| Approved | IAM design is scoped, documented, and aligned to least privilege |
| Approved with Conditions | Access can proceed after specific policy corrections |
| Needs Rework | IAM design includes broad access, weak trust, or escalation risk |
| Denied | Risk exceeds tolerance or cannot be controlled with available guardrails |
