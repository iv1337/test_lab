pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/iv1337/test_lab.git' 
            }
        }
        stage('Build') {
            steps {
                // Install dependencies if necessary
                // sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Run your unit tests
                sh 'python -m unittest test_calc.py'
            }
        }
    }
    post {
        always {
            // Optional: Send test results to a reporting tool
            // sh 'allure generate report/allure-results -o report/allure-report' 
            // sh 'allure serve report/allure-report' // For viewing the report 
        }
    }
}