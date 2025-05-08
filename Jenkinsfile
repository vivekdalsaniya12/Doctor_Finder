@Library('Library') _
pipeline {
    agent {
        label "home"
    }
    environment{
        DOCKER_IMAGE = "vivekdalsaniya/Doctor_finder"
        IMAGE_TAG = "latest"
        PATH = "."
    }
    stages {
        stage('code clone demo shared') {
            steps {
                codeClone(branch:'main',url:'https://github.com/vivekdalsaniya12/Doctor_Finder.git')
            }
        }
        stage('docker build') {
            steps {
               dockerBuild(env.DOCKER_IMAGE,env.IMAGE_TAG,env.PATH)
            }
        }
        stage('Test cases') {
            steps {
                testCases()
            }
        }
        stage('docker Hub push') {
            steps {
                withCredentials ([usernamePassword(credentialsId:'dockercreds',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push $DOCKER_IMAGE:$IMAGE_TAG
                        docker logout
                    '''
                }
            }
        }
    }
}
