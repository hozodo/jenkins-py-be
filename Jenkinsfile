pipeline {
    agent any
    environment {
        dockerhub = credentials('dockerhub')
    }
    stages {
        stage('Init') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [],
                userRemoteConfigs: [[url: 'https://github.com/hozodo/jenkins-py-be.git']]])
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test Code') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Build Code') {
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
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
                sh "docker tag python-jenkins:latest stacktalks/python-jenkins:v0.${env.BUILD_ID}"
                sh 'docker push --all-tags stacktalks/python-jenkins'
            }
        }
        // Minikube deployment using Kubeconfig
        stage('Deploy K8s') {
            steps {
                script {
                    kubernetesDeploy(configs: 'k8s-deploy.yaml', kubeconfigId: 'KUBE_CONFIG_ID')
                }
            }
        }

        // // The cluster outside Jenkins
        // stage('SSH to K8s Cluster') {
        //     steps {
        //         def remote = [:]
        //         remote.name = 'root'
        //         remote.host = 'localhost'
        //         remote.user = 'root'
        //         remote.password = 'xx'
        //         remote.allowAnyHosts = true
        //     }
        //     stage('Put the file') {
        //         steps {
        //             sshPut remote:remote, from:'k8s-deploy.yaml', into = '.'
        //         }
        //     }

        //     stage('Deploy') {
        //         steps {
        //             sshCommand remote:remote, command:'kubectl apply -f k8s-deploy.yaml'
        //         }
        //     }
        // }

        // // Deploy using Ansible Playbook
        // stage('Deploy K8s using Ansible') {
        //     steps {
        //         sh 'ansible-playbook ansible-deploy.yaml'
        //     }
        // }
    }
}
