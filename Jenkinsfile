pipeline {
    agent any
    environment {
       Main_env = "Welcome in the main branch"
       DEPLOY_TO = "main environment"
    }

    stages {
        stage('testScript') {
            steps {
               script{
                   def a = "test skryptu"
                   println a
               }
            }
        }
        stage('TestCode') {
            steps {
                echo "test"
                bat "python -m pytest"
            }
        }
        stage('RunCode') {
            steps {
                echo "run"
            }
        }
        stage('BuildImage') {
            steps {
               echo "build"
            }
        }
        stage('PushImage') {
            steps {
                eho "push"
            }
        }
    }
}