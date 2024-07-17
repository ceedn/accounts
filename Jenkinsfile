pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
               checkout scm
            }
        }
        
        stage('Build Image') {
            steps {
                script {
                    def shaHash = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                    
                    docker.build("your-image:${shaHash}")
                    docker.build("your-image:latest")
                }
            }
        }
        
        stage('Login to Harbor') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'harbor', usernameVariable: 'HARBOR_USERNAME', passwordVariable: 'HARBOR_PASSWORD')]) {
                    sh 'docker login -u $HARBOR_USERNAME -p $HARBOR_PASSWORD your-harbor-registry'
                }
            }
        }
        
        stage('Push Image to Harbor') {
            steps {
                script {
                    def shaHash = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                    
                    docker.withRegistry('https:/packages.acfc.dev/', 'credentials') {
                        docker.image("your-image:${shaHash}").push("library/your-image:${shaHash}")
                        docker.image("your-image:latest").push("library/your-image:latest")
                    }
                }
            }
        }
    }
}