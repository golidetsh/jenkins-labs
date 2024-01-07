terraform {
  backend "s3" {
    bucket = "remotestate-dev-bucket"
    key    = "remote.tfstate"
    region = "eu-north-1"
    encrypt = true
  }
}