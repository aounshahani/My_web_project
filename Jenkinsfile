pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Fetches code from GitHub
                git branch: 'main', url: 'https://github.com/aounshahani/My_web_project.git'
            }
        }
        stage('Build and Deploy') {
            steps {
                script {
                    // Stops any existing environment
                    sh 'docker-compose -f docker-compose-jenkins.yml down || true'
                    // Brings up the new environment
                    sh 'docker-compose -f docker-compose-jenkins.yml up -d'
                }
            }
        }
        stage('Verify Deployment') {
            steps {
                script {
                    // Simple curl test to check if the app is up
                    sh 'sleep 30' // Wait for containers to start
                    sh 'curl -f http://localhost:8080 || echo "Application health check failed"'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline for Assignment 2 Part II has finished.'
        }
    }
}