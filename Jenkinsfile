pipeline {
    agent {
        label 'JAVA11'
    }
    stages {
        stage('Cloning source code') {
            steps {
                git branch: 'declarative', url: 'https://github.com/microsoft/python-sample-vscode-flask-tutorial.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }
        
    } 
}