#--root/main.tf---

module "storage" {
  source = "./storage"
  env_config = var.env_config
}

