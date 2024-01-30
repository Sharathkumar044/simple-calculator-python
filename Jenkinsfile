pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Use 'git' command to checkout the code
                    git 'https://github.com/Sharathkumar044/simple-calculator-python.git'
                }
            }
        }
    }

    post {
        success {
            echo 'Code checkout successful.'
        }

        failure {
            echo 'Code checkout failed. Please check the build logs for details.'
        }

        always {
            echo 'Cleaning up resources...'
        }
    }
}
