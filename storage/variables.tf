# --- storage/variables.tf ---

variable "env_config" {
  type = map(object({
    bucket_name   = string
    acl           = string
  }))
  default = {}
}


