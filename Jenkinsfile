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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }
        stage('Build') {
            steps {
                sh 'python app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build --tag python-jenkins .'
            }
        }
    }
}
