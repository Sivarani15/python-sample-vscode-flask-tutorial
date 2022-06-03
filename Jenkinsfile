pipeline {
    agent {
        label 'JAVA11'
    }
    stages {
        stage('Cloning source code') {
            steps {
                git branch: 'declarative', url: 'https://github.com/Sivarani15/the-example-app.nodejs.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }
        
    } 
}