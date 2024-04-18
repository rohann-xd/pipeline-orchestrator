pipeline {
    agent any
    
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
