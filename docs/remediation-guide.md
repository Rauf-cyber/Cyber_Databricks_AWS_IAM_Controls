# Remediation Guide

This guide provides practical remediation steps for risky IAM patterns in Databricks on AWS environments.

## Finding: Wildcard Action

**Issue:** A policy includes `Action: *`.

**Why it matters:** Wildcard actions may allow administrative access far beyond what Databricks requires.

**Recommended remediation:** Replace wildcard actions with specific actions such as `s3:GetObject`, `s3:PutObject`, `logs:PutLogEvents`, or approved KMS actions.

## Finding: Wildcard Resource

**Issue:** A policy includes `Resource: *` where resource scoping is supported.

**Why it matters:** Broad resource access increases blast radius if credentials are compromised.

**Recommended remediation:** Scope permissions to approved S3 bucket ARNs, log group ARNs, and KMS key ARNs.

## Finding: Missing External ID

**Issue:** A cross-account trust policy allows `sts:AssumeRole` without an `sts:ExternalId` condition.

**Why it matters:** External IDs help prevent confused deputy issues in cross-account integrations.

**Recommended remediation:** Require a Databricks-provided external ID in the trust policy condition.

## Finding: Broad S3 Access

**Issue:** Databricks has `s3:*` or access to all buckets.

**Why it matters:** Databricks should only access approved data lake buckets and prefixes.

**Recommended remediation:** Restrict S3 access to specific buckets and prefixes needed by the workspace.

## Finding: Log Deletion Allowed

**Issue:** The role can delete CloudWatch log groups, streams, or retention policies.

**Why it matters:** Attackers or misconfigured jobs could remove evidence needed for investigations.

**Recommended remediation:** Allow log write actions, but deny destructive log actions.

## Finding: IAM Privilege Escalation Actions

**Issue:** The role can create users, attach policies, update trust policies, or pass roles.

**Why it matters:** These actions can enable privilege escalation from a Databricks role to broader AWS admin access.

**Recommended remediation:** Deny sensitive IAM actions through permission boundaries and tightly approved admin paths.
