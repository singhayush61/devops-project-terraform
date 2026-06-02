terraform {
  backend "s3" {
    bucket = "ayush-devops-terraform-state"
    key    = "devops-project/terraform.tfstate"
    region = "ap-south-1"
  }
}