@Library('Library') _
pipeline {
    agent {
        label "home"
    }
    stages {
        stage('code clone demo shared') {
            steps {
                // codeClone(branch:'main',url:'https://github.com/vivekdalsaniya12/Doctor_Finder.git')
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vivekdalsaniya12/Doctor_Finder.git']])
                // shree Ram Jay Ram jay Jay Ram
            }
        }
        stage('docker build') {
            steps {
               dockerBuild("vivekdalsaniya/doctor_finder","latest",".")
            }
        }
        stage('Test cases') {
            steps {
                testCases()
            }
        }
        stage('docker Hub push') {
            steps {
                withCredentials ([usernamePassword(credentialsId:'dockercreds',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]) 
                {
                    dockerPush(USERNAME:"${USERNAME}",PASSWORD:"${PASSWORD}",DOCKER_IMAGE:"vivekdalsaniya/doctor_finder",IMAGE_TAG:"latest")
                }
            }
        }
    }
}
