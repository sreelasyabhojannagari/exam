pipeline {
    agent any
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
                bat 'docker tag img1 sreelasya24/first:latest'
                bat 'docker push sreelasya24/first:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                    bat 'kubectl apply -f service.yaml'
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
