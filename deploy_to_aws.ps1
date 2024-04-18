# Define your EC2 instance IP address or DNS name
$ec2InstanceIP = $args[0]

# Define your SSH key file path
$sshKeyFile = $args[1]

# Define your Docker image name
$dockerImageName = $args[2]

# SSH into the EC2 instance
ssh -i $sshKeyFile ubuntu@$ec2InstanceIP << EOF
# Commands to run on the EC2 instance

# Pull the Docker image from Docker Hub
docker pull $dockerImageName

# Run the Docker container
docker run -d -p 8000:8000 $dockerImageName
EOF
