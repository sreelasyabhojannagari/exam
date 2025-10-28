pipeline {
    agent any

    environment {
        IMAGE_NAME = "sreelasya24/first:latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t img1 .'
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u sreelasya24 -p Shree2401!'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                bat 'docker tag tag img1'
                bat 'docker push img1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        success {
            echo ' Pipeline succeeded!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}
