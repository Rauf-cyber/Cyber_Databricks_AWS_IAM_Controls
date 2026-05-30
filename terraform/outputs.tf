output "databricks_cross_account_role_name" {
  description = "Databricks cross-account IAM role name."
  value       = aws_iam_role.databricks_cross_account_role.name
}

output "databricks_cross_account_role_arn" {
  description = "Databricks cross-account IAM role ARN."
  value       = aws_iam_role.databricks_cross_account_role.arn
}

output "permission_boundary_arn" {
  description = "Permission boundary policy ARN."
  value       = aws_iam_policy.databricks_permission_boundary.arn
}
