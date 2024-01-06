#--root/outputs.tf---

## STORAGE
 output "s3_iam_user_arn" {
    value = module.storage.s3_aws_iam_user_id
 }