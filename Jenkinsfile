pipeline {
    agent any
    environment {
       Main_env = "Welcome in the main branch"
       DEPLOY_TO = "main environment"
    }

    stages {
        stage('checkBranch') {
            steps {
                when {
                        branch 'main'
                    }
                    steps{
                        echo "${Main_env}"
                    }

            }
        }
        stage('TestCode') {
            steps {
                echo "test"
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