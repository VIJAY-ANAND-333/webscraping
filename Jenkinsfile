pipeline {
    agent any
    
    environment {
        // Define any environment variables needed for your build process
        IMAGE_NAME = "Vijay"
        DOCKERFILE_PATH = "E:\nigga\Airflow"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build(env.IMAGE_NAME, "--file ${env.DOCKERFILE_PATH} .")
                }
            }
        }
    }
    

}
