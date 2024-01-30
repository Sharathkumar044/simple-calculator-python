pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Use 'git' command to checkout the code from the 'feature' branch
                    git branch: 'feature', url: 'https://github.com/Sharathkumar044/simple-calculator-python.git'
                }
            }
        }
    }

}
