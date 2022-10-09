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

        stage('Push Docker Image') {
            steps {
                sh 'docker login -u stacktalks - S@igon12!@'
                sh 'docker tag python-jenkins:latest stacktalks/python-jenkins:latest'
                sh 'docker push stacktalks/python-jenkins:latest'
            }
        }
    }
}
