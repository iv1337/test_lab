pipeline {
 agent any

 stages {
  stage('Checkout') {
   steps {
    git branch: 'main', url: 'https://github.com/iv1337/test_lab.git'
   }
  }

  stage('Test') {
   steps {
    sh 'python -m unittest test_calc.py'
   }
  }
 }
}
