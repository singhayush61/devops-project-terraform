resource "aws_instance" "devops-project-terraform" {

  ami           = "ami-0f58b397bc5c1f2e8"
  instance_type = "t3.micro"

  tags = {
    Name = "devops-project"
  }
}