pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from your repository
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Create a virtual environment on Windows
                bat 'python -m venv venv'

                // Activate the virtual environment on Windows
                bat 'venv\\Scripts\\activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install required Python packages
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run unit tests using unittest or pytest
                bat 'python -m unittest discover -s tests -p "*_test.py"'
            }
        }

        stage('Run Web Scraping Script') {
            steps {
                // Run your web scraping script
                bat 'python webscrapingapp.py'
            }
        }
    }
}
