import os
import boto3
import json_operations
import json



# loading config data from json
config_data = json_operations.loadJsonData("./configs/config.json")
key_path = config_data["key_path"]
key_name = config_data["key_name"]
ami_id = config_data["ami_id"]
instance_type = config_data["instance_type"]
region_name = config_data["region_name"]
ec2_json_data_path = config_data["ec2_data_path"]
print(ec2_json_data_path)
ec2_data = json_operations.loadJsonData(ec2_json_data_path)
print(ec2_data)

# #create boto3 client for ec2
ec2_client = boto3.client("ec2", region_name=region_name)

def create_key_pair():
    if not os.path.exists(key_path):
        key_pair = ec2_client.create_key_pair(KeyName=key_name)
        private_key = key_pair["KeyMaterial"]
        # write private key to file with 400 permissions
        with os.fdopen(os.open(key_path, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
            handle.write(private_key)
create_key_pair()
