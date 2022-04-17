pipeline {
    agent { docker { image 'python:3' } }
    stages {
        stage("Requirement Installation") {
            echo "Building... "
            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh '/usr/local/bin/python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }  
        }
        stage('test') {
            // agent {
            //     docker {
            //         //This image parameter downloads the qnib:pytest Docker image and runs this image as a
            //         //separate container. The pytest container becomes the agent that Jenkins uses to run the Test
            //         //stage of your Pipeline project.
            //         image 'qnib/pytest'
            //     }
            // }
            steps {
                echo "Testing  . . ."
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pytest CalcTest.py -s \n\n\n\n\n'
                }
                
            }
        }
    }
}
