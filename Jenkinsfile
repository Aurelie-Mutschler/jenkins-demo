pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'pip3 install -r requirements.txt'
            }
        }

        stage('Run ETL Script') {
            steps {
                bat 'python etl_script.py'
            }
        }
	  stage('Test') {
            steps {
                bat 'python test.py'
            } 
        }
    }
}