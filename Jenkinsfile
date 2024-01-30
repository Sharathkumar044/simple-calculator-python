pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = '8298ebe4-0451-413e-aa15-8dc16766b555'
        DOCKER_IMAGE_NAME = 'sharath044/my-web-app'
    }

    stage('Checkout') {
    steps {
        git 'https://github.com/Sharathkumar044/simple-calculator-python.git'
    }


    post {
        success {
            // Add any success post-build actions here
            echo 'Build and deployment successful!'
        }

        failure {
            // Add any failure post-build actions here
            echo 'Build or deployment failed!'
        }
    }
}
