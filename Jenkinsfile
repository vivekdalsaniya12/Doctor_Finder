@Library('Library') _
pipeline {
    agent {
        label "home"
    }
    environment {
        DOCKER_IMAGE = 'vivekdalsaniya/doctor_finder'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('code clone demo shared') {
            steps {
                codeClone(branch:'main',url:'https://github.com/vivekdalsaniya12/Doctor_Finder.git')
            }
        }
        
        stage('docker build') {
            steps {
                build(docker_image:'vivekdalsaniya/doctor_finder', image_tag: 'latest', path: '.')
                // sh "docker build -t $DOCKER_IMAGE:$IMAGE_TAG ."
            }
        }
        stage('Test cases') {
            steps {
                echo "dumy cases"
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
