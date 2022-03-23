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
               bat "docker build -t \"JenkPipe:latest\" "
               bat "docker run JenkPipe"
            }
        }
        stage('PushImage') {
            steps {
                echo "push"
                bat "docker tag JenkPipe mich909/Jenkins_multigti"
                bat "docker push mich909/Jenkins_multigti"
            }
        }
    }
}