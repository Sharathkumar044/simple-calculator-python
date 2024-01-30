pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
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
                    // Manually add additional_tests.py to the workspace
                    sh 'cp /path/to/additional_tests.py .'

                    // Run your tests (replace with your actual test command)
                    sh 'python3 -m unittest discover -s . -p "test*.py" -v'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'python3 app.py &'
                }
            }
        }

        stage('Post Deployment Tests') {
            steps {
                script {
                    // Manually add additional_tests.py to the workspace
                    sh 'cp /path/to/additional_tests.py .'

                    // Perform additional tests after deployment
                    sh 'python3 -m unittest additional_tests.py'
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Deployment successful! Notify your team.'
            }
        }

        failure {
            script {
                echo 'Deployment failed! Notify your team.'
            }
        }

        always {
            script {
                sh 'pkill -f "python3 app.py"'
            }
        }
    }
}
