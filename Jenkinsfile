pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
        FLASK_PORT = '5000'
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_IMAGE_NAME = 'sharath044/simple-calculator'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = '0dd3554a-acd4-48b4-be69-77b052629c30'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature', url: 'https://github.com/Sharathkumar044/simple-calculator-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 -m unittest discover -s . -p "test*.py" -v'
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD} ${DOCKER_REGISTRY}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "nohup python3 -m flask run --host=0.0.0.0 --port=${FLASK_PORT} > /dev/null 2>&1 &"
                    sleep 40
                }
            }
        }

        stage('Post Deployment Tests') {
            steps {
                script {
                    sh 'python3 -m unittest additional_tests.py'
                }
            }
        }
    }

    post {
        success {
            script {
                // Add any cleanup or post-build steps here
                echo 'Jenkins pipeline completed successfully!'
            }
        }
        failure {
            script {
                echo 'Jenkins pipeline failed!'
            }
        }
    }
}
