// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Create a virtual environment and install dependencies
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'

            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Activate the venv and run tests with pytest
                sh '. venv/bin/activate'
                 withEnv(["PYTHONPATH=${env.WORKSPACE}"]) {
                sh 'pytest test/tests.py' }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment stage (e.g., publish to a registry or environment).'
                // Add deployment steps here
            }
        }
    }
}