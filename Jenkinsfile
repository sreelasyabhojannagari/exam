pipeline{
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                bat 'docker build -t img1 .'
            }    
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u sreelasya24 -p Shree2401!'
            }    
        }
        stage('Push Docker image to docker hub'){
            steps{
                bat 'docker tag img1 sreelasya24/first:latest'
                bat 'docker push sreelasya24/first:latest'
            }    
        }
        stage('Kubernetes'){
            steps{
                bat 'docker -f apply deployment.yaml --validate=false'
                bat 'docker -f apply service.yaml'
            }    
        }
    }
    post{
        success{
            echo 'pipeline success'
        }
        failure{
            echo 'pipeline failed'
        }
    }
}