# Threat Model: Databricks on AWS IAM Controls

This threat model focuses on identity and access risks for Databricks workspaces integrated with AWS services.

## Threat 1: Over-Permissioned Cross-Account Role

**Risk:** Databricks may be granted broad AWS permissions that exceed the workspace use case.

**Example:** A cross-account role has `Action: *` or broad administrator permissions.

**Impact:** A compromised workspace or token could access unrelated AWS resources, modify security settings, or move laterally.

**Mitigation:** Scope policies to approved services, buckets, prefixes, and KMS keys. Use deny guardrails for privilege escalation actions.

## Threat 2: Weak Trust Policy

**Risk:** The role trust policy may allow assumption by unapproved principals or may not require an external ID.

**Example:** `Principal: *` or missing `sts:ExternalId` condition.

**Impact:** Unauthorized role assumption could expose data or cloud resources.

**Mitigation:** Trust only the required Databricks AWS principal and require the Databricks external ID.

## Threat 3: Unrestricted S3 Data Access

**Risk:** Databricks roles may access more S3 buckets or prefixes than required.

**Example:** A policy grants `s3:*` on all buckets.

**Impact:** Sensitive data could be read, modified, or deleted outside the intended workspace scope.

**Mitigation:** Use bucket and prefix-level permissions. Require encrypted object uploads.

## Threat 4: Log Tampering

**Risk:** A role may be able to delete or modify CloudWatch log groups and retention settings.

**Example:** The same role that writes logs can also delete logs.

**Impact:** Security teams may lose audit evidence after suspicious activity.

**Mitigation:** Allow log write actions but deny destructive CloudWatch Logs actions.

## Threat 5: Privilege Escalation Through IAM

**Risk:** A Databricks role may be allowed to create users, attach policies, update trust policies, or pass privileged roles.

**Example:** `iam:PassRole`, `iam:AttachRolePolicy`, or `iam:UpdateAssumeRolePolicy` without restrictions.

**Impact:** Attackers could escalate access from a data platform role into broader AWS admin access.

**Mitigation:** Deny sensitive IAM actions through permission boundaries and review policies using automation.
