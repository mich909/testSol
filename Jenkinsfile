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
                
            }
        }
        stage('RunCode') {
            steps {
                
            }
        }
        stage('BuildImage') {
            steps {
               
            }
        }
        stage('PushImage') {
            steps {
                
            }
        }
    }
}