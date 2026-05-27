# AWS account config
region = "eu-central-1"

# General for all infrastructure
# This is the name prefix for all infra components
name = "miroslava"


vpc_id = "vpc-0c3524d414b096edc"
subnets_ids = ["subnet-041ed8b09dd5f2e93", "subnet-0778e4bd30383da45", "subnet-079351a4a86c32a76"]


tags = {
  Environment = "test"
  TfControl   = "true"
}


zone_name = "devops12.test-danit.com"
