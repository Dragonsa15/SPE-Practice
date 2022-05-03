pipeline {
    environment {
        imagename = "saksham1508/calculator"
        registryCredential = "sakshamDockerHub"
        dockerImage = ''
    }


    agent any
    stages {
        stage("Requirements") {
            steps {
                echo "Building... "
                sh '/usr/bin/python3 -m pip install -r requirements.txt'
                
            }
        }
        stage('Static Testing') {
            steps {
                echo "Testing  . . ."
                sh '/usr/bin/python3 -m pytest CalcTest.py -s'
            }
        }
        stage("Docker Build") {
            steps 
            {
                script
                    {
                    dockerImage = docker.build imagename
                    }
            }
        }
        stage('Docker Image push')
        {
            agent any
            steps
               {
                script
                    {
                    docker.withRegistry('', registryCredential ){
                    dockerImage.push()
                    } 
                }
                }
        }

        stage("Ansible Connection") {
            steps {
                ansiblePlaybook colorized: true, disableHostKeyChecking: true, installation: "Ansible", inventory: 'ansible/inventory.inv',playbook:'ansible/deploy.yml'
            }
        }
        
    }
}
