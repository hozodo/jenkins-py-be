pipeline {
    agent any

    stages {
         stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/hozodo/jenkins-py-be.git']]])
            }
        }
         stage('Install') {
            steps {
                bat 'pip3 install -r requirements.txt'
            }
        }
         stage('Test') {
            steps {
                bat 'python3 -m pytest'
            }
        }
        stage('Build') {
            steps {
                bat 'python3 app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build --tag python-jenkins .'
            }
        }
    }
}
