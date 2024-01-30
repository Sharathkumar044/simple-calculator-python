pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out your source code from version control
                git branch: 'feature', url: 'https://github.com/Sharathkumar044/simple-calculator-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python packages
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests (replace with your actual test command)
                    sh 'python -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Start the Flask application
                    sh 'python app.py &'
                }
            }
        }

        stage('Post Deployment Tests') {
            steps {
                script {
                    // Perform additional tests after deployment (if needed)
                    sh 'python -m unittest additional_tests.py'
                }
            }
        }
    }

    post {
        success {
            script {
                // Notify on success (replace with your actual notification method)
                echo 'Deployment successful! Notify your team.'
            }
        }

        failure {
            script {
                // Notify on failure and clean up (replace with your actual notification and cleanup methods)
                echo 'Deployment failed! Notify your team.'
            }
        }

        always {
            script {
                // Clean up resources (stop the Flask application)
                sh 'pkill -f "python app.py"'
            }
        }
    }
}
