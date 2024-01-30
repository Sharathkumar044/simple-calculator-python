pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Use 'git' command to checkout the code from the 'feature' branch
                    git branch: 'feature', url: 'https://github.com/Sharathkumar044/simple-calculator-python.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python and pip for Amazon Linux without password prompt
                    sh 'echo "password" | sudo -S yum install -y python3 python3-pip'
                    // Install required Python packages
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests (replace with your actual test command)
                    sh 'python3 -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Start the Flask application
                    sh 'python3 app.py &'
                }
            }
        }

        stage('Post Deployment Tests') {
            steps {
                script {
                    // Perform additional tests after deployment (if needed)
                    sh 'python3 -m unittest additional_tests.py'
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
                sh 'pkill -f "python3 app.py"'
            }
        }
    }
}
