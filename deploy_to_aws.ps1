$ec2InstanceIP = $args[0]

# Define your SSH key file path
$sshKeyFile = $args[1]

# Define your Docker image name
$dockerImageName = $args[2]

# SSH into the EC2 instance
# ssh -i $sshKeyFile ubuntu@$ec2InstanceIP @"
ssh -o StrictHostKeyChecking=no -i $sshKeyFile ubuntu@$ec2InstanceIP @"
docker system prune
docker pull $dockerImageName
docker run -d -p 8000:8000 $dockerImageName
"@
