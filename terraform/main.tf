terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

resource "aws_iam_role" "databricks_cross_account_role" {
  name               = var.databricks_role_name
  assume_role_policy = file("${path.module}/../iam-policies/databricks-cross-account-role-trust-policy.json")
  permissions_boundary = aws_iam_policy.databricks_permission_boundary.arn

  tags = {
    Project     = "Cyber-Databricks-AWS-IAM-Controls"
    Environment = var.environment
    Owner       = "Cloud-Security"
  }
}

resource "aws_iam_policy" "databricks_s3_access" {
  name        = "databricks-least-privilege-s3-access"
  description = "Least-privilege S3 access policy for Databricks workspace data paths"
  policy      = file("${path.module}/../iam-policies/least-privilege-s3-access-policy.json")
}

resource "aws_iam_policy" "databricks_cloudwatch_logs" {
  name        = "databricks-cloudwatch-logs-access"
  description = "CloudWatch logging policy with deny guardrails for log tampering"
  policy      = file("${path.module}/../iam-policies/cloudwatch-logs-access-policy.json")
}

resource "aws_iam_policy" "databricks_permission_boundary" {
  name        = "databricks-restricted-admin-boundary"
  description = "Permission boundary to reduce privilege escalation risk for Databricks roles"
  policy      = file("${path.module}/../iam-policies/restricted-admin-boundary-policy.json")
}

resource "aws_iam_role_policy_attachment" "attach_s3_access" {
  role       = aws_iam_role.databricks_cross_account_role.name
  policy_arn = aws_iam_policy.databricks_s3_access.arn
}

resource "aws_iam_role_policy_attachment" "attach_cloudwatch_logs" {
  role       = aws_iam_role.databricks_cross_account_role.name
  policy_arn = aws_iam_policy.databricks_cloudwatch_logs.arn
}
