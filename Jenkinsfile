pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('test') {
            agent {
                docker {
                    //This image parameter downloads the qnib:pytest Docker image and runs this image as a
                    //separate container. The pytest container becomes the agent that Jenkins uses to run the Test
                    //stage of your Pipeline project.
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'pytest CalcTest.py'
            }
        }
    }
}
