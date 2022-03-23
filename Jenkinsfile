pipeline {
    agent any
    environment {
       Main_env = "Welcome in the main branch"
       python = "C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
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
                bat "${python} -m pytest"
            }
        }
        stage('RunCode') {
            steps {
                echo "run"
                bat "${python} main.py"
            }
        }
        stage('BuildImage') {
            steps {
               echo "build"
               bat "docker build -t \"jenk_pipe:latest\" ."
            }
        }
        stage('RunImage'){
            steps {
                echo "run image"
                bat "docker run jenk_pipe"
            }
        }
        stage('PushImage') {
            steps {
                echo "push"
                bat "docker tag jenk_pipe mich909/jenkins_multigti"
                bat "docker push mich909/jenkins_multigti"
            }
        }
    }
}