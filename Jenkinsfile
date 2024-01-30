pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
        FLASK_PORT = '5000'  // Change this to the port your Flask app is using
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

        stage('Deploy') {
            steps {
                script {
                    // Start the Flask application in the background
                    sh "nohup python3 -m flask run --host=0.0.0.0 --port=${FLASK_PORT} > /dev/null 2>&1 &"
                    sleep 10  // Give Flask some time to start (adjust as needed)
                }
            }
        }

        stage('Post Deployment Tests') {
            steps {
                script {
                    // Perform additional tests after deployment
                    sh 'python3 -m unittest additional_tests.py'
                }
            }
        }
    }
}
