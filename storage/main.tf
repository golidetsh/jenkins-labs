#--- storage/main.tf ---

resource "aws_s3_bucket" "my_bucket" {
  bucket = "golidetsh-bucket" 
}

data "aws_iam_user" "iam_user" {
        user_name = "goldadmin"
}

resource "aws_s3_bucket" "remote_state" {
  bucket = var.env_config[terraform.workspace].bucket_name
}