variable "aws_region" {
  type        = string
  description = "AWS region used for the sample deployment."
  default     = "us-east-1"
}

variable "environment" {
  type        = string
  description = "Environment tag for the IAM resources."
  default     = "dev"
}

variable "databricks_role_name" {
  type        = string
  description = "Name of the Databricks cross-account IAM role."
  default     = "databricks-cross-account-cyber-role"
}
