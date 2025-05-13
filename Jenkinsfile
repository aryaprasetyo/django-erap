pipeline {
    agent any

    //environment {
        // SONAR_TOKEN = credentials('sqp_7220f7b8e599ea230c5ec7df06fc3279b8006c6f')  // ID dari token di Jenkins Credentials
    //}

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'development', url: 'https://github.com/aryaprasetyo/django-erap.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pip3 install flake8'
            }
        }

        
        stage('Code Linting/Analysis') {
            steps {
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }


        stage('Run Unit Tests') {
            steps {
                sh 'python3 manage.py test core -v 2'
            }
        }

        //stage('SonarQube Analysis') {
        //    steps {
        //        withSonarQubeEnv('My SonarQube Server') {
        //            sh '''
        //                sonar-scanner \
        //                -Dsonar.projectKey=ERP-Django \
        //                -Dsonar.sources=. \
        //                -Dsonar.python.version=3 \
        //               -Dsonar.host.url=http://172.23.3.11:9000 \
        //                -Dsonar.login=$SONAR_TOKEN
        //            '''
        //        }
        //    }
        //}

        stage('Docker Build') {
            steps {
                sh 'docker build -t adhari1720/django-app:latest .'
            }
        }

        //stage('Docker Push') {
        //    steps {
        //        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_PASS')]) {
        //            sh '''
        //                echo $DOCKER_PASS | docker login -u adhari1720 --password-stdin
        //                docker push adhari1720/django-app:latest
        //            '''
        //        }
        //    }
        //}
    }
}
