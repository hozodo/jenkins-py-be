pipeline {
    agent any
    // agent {
    //     docker {
    //         image 'python:3'
    //         label 'my-build-agent'
    //     }
    // }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/hozodo/jenkins-py-be.git']]])
            }
        }
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }
        stage('Build') {
            steps {
                bat 'python app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build --tag python-jenkins .'
            }
        }
    }
}
