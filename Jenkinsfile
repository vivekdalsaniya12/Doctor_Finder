@Library('Library') _
pipeline {
    agent {
        label "home"
    }
    environment {
        DOCKER_IMAGE = 'vivekdalsaniya/doctor_finder'
        IMAGE_TAG = 'latest'
        PATH = '.'
    }
    stages {
        stage('code clone demo shared') {
            steps {
                codeClone(branch:'main',
                          url:'https://github.com/vivekdalsaniya12/Doctor_Finder.git'
                         )
            }
        }
        stage('docker build pre checkup ') {
            steps {
                sh "echo 'hello world'"
                echo env.DOCKER_IMAGE
            }
        }
        stage('docker build') {
            steps {
                // dockerimage:env.DOCKER_IMAGE,
                            // imagetag:env.IMAGE_TAG,
                            // path:env.PATH
                dockerBuild()
                // sh "docker build -t $DOCKER_IMAGE:$IMAGE_TAG ."
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
