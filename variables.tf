#--root/variables.tf---

variable "tags" {

    type = map(string)
    default = {
        "dev" = "DEV",
        "uat" = "QA",
        "prod" = "PROD"
    }
  
}

variable "env_config" {
  type = map(object({bucket_name=string,acl=string}))
  default = {
    "dev" = {
      acl = "private"
      bucket_name = "remotestate-dev-bucket"
    },
    "uat" = {
      acl = "private"
      bucket_name = "remotestate-uat-bucket"
    },
    "prod" = {
      acl = "private"
      bucket_name = "remotestate-prod-bucket"
    }

  }
}
