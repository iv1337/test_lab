pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/iv1337/test_lab.git' 
            }
        }
        stage('Test') {
            steps {
                // Run your unit tests
                def testResult = sh(returnStatus: true, script: 'python -m unittest test_calc.py')
                // Check the return code of the command
                if (testResult.exit == 0) {
                    echo "Tests passed successfully!"
                } else {
                    error("Unit tests failed. Build will fail.")
                }
            }
        }
    }
}
