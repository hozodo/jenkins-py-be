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
                sh 'pip3 install -r requirements.txt'
            }
        }
         stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
               sh 'docker build --tag python-jenkins .'
            }
        }
    }
}
