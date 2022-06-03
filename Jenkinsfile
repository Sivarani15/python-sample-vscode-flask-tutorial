pipeline {
    agent {
        label 'JAVA11'
    }
    stages {
        stage('Cloning source code') {
            steps {
                git branch: 'declarative', url: 'https://github.com/Sivarani15/python-sample-vscode-flask-tutorial.git'
            }
        }
        stage('Install dependencies and requirements') {
            steps {
                sh 'python3 -m pip install --upgrade pip setuptools wheel'
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                sh 'pip install pytest-cov'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml'
            }
        }
        stage('Archiving test results') {
            steps {
                junit testResults: '**/tets-*.xml'
            }
        }
    } 
}