#resource "aws_s3_bucket" "devops_tf_state" {
#    bucket = "miroslava-devops-tf-state"

#}

terraform {
  backend "s3" {
    bucket         = "miroslava-devops-tf-state"
    key            = "eks/terraform.tfstate"
    encrypt        = true
#    dynamodb_table = "lock-tf-eks"
    # dynamo key LockID
    # Params tekan from -backend-config when terraform init
    region = "eu-central-1"
    #profile = 
  }
}


