@Library('Library') _
pipeline {
    agent {
        label "home"
    }
    stages {
        stage('code clone demo shared') {
            steps {
                codeClone(branch:'main',url:'https://github.com/vivekdalsaniya12/Doctor_Finder.git')
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
                withCredentials ([usernamePassword(credentialsId:'dockercreds',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push "vivekdalsaniya/doctor_finder":"latest"
                        docker logout
                    '''
                }
            }
        }
    }
}
