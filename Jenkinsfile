pipeline {
    agent { 
        docker { image 'python:2-alpine' } 
    }
    stages {
        // stage("Virtual Env Setup") {
        //     steps {
        //         sh "python -m venv CalcEnv"
        //         sh "source CalcEnv/bin/activate"
        //     }
        // }
        // stage("Requirement Installation") {
        //     steps {
        //         sh 'pip install --upgrade pip'
        //         sh 'pip3 install -r requirements.txt'
                
        //     }  
        // }
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
                sh 'pytest CalcTest.py'
            }
        }
    }
}
