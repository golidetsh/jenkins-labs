#--- storage/main.tf ---

resource "aws_s3_bucket" "my_bucket" {
  bucket = "golidetsh-bucket" 
}

data "aws_iam_user" "iam_user" {
        user_name = "goldadmin"
}

resource "aws_s3_bucket" "remote_state" {
  bucket = var.env_config[terraform.workspace].bucket_name

  policy = <<EOF
{
   "Version":"2012-10-17",
   "Statement":[  
      {
         "Effect":"Allow",
         "Action": "s3:*",
         "Principal": {
            "AWS": "${data.aws_iam_user.iam_user.arn}" 
            },
          "Resource":"arn:aws:s3:::${var.env_config[terraform.workspace].bucket_name}/*"
      }
     
   ]
}
EOF

}

resource "aws_s3_bucket_versioning" "remote_state_versioning" {
  bucket = aws_s3_bucket.remote_state.id
  versioning_configuration {
    status = "Enabled"
  }
}