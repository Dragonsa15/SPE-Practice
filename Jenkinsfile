pipeline {
    agent { docker { image 'python:3' } }
    stages {
        stage("Requirements") {
            steps {
                echo "Building... "
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh '/usr/local/bin/python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Static Testing') {
            steps {
                echo "Testing  . . ."
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m pytest CalcTest.py -s \n\n\n\n\n'
                }
                
            }
        }
        stage("Docker Build") {
            steps {
                sh "pip install docker"
                sh "docker build -t saksham1508/calculator ."
            }
        }
        stage("Ansible Connection") {
            steps {
                ansiblePlaybook colorized: true, disableHostKeyChecking: true, installation: "Ansible", inventory: 'ansible/inventory.inv',playbook:'ansible/deploy.yml'
            }
        }
        
    }
}
