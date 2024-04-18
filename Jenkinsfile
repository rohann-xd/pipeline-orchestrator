pipeline {
    agent any
    
    parameters {
        string(name: 'EC2_INSTANCE_IP', defaultValue: '', description: 'EC2 instance IP address')
        string(name: 'SSH_KEY_PATH', defaultValue: '', description: 'Path to PEM')
        string(name: 'DOCKER_IMAGE_NAME', defaultValue: '', description: 'Docker image name')
    }
    
    stages {
        stage('Pull Code') {
            steps {
                // Checkout source code from your version control system
                git 'https://github.com/rohann-xd/pipeline-orchestrator.git'
            }
        }
        
        stage('Build and Push to DockerHub') {
            steps {
                // Build Docker image
                script {
                    docker.build("rohanxd/devops-django:${BUILD_NUMBER}")
                }
                
                // Push Docker image to DockerHub (replace with your DockerHub username and repository name)
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("rohanxd/devops-django:${BUILD_NUMBER}").push()
                    }
                }
            }
        }
        
        stage('Deploy to AWS') {
            steps {
                // Execute PowerShell script to deploy Docker image to AWS EC2 instance
                bat "powershell.exe -ExecutionPolicy Bypass -File deploy_to_aws.ps1 ${env.EC2_INSTANCE_IP} ${env.SSH_KEY_PATH} ${env.DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed :('
        }
    }
}
