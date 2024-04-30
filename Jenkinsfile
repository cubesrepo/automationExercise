pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/automationExercise'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv automationExerciseVENV'
                bat 'automationExerciseVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'automationExerciseVENV\\Scripts\\activate && pytest -v --html=report.html'
            }
        }
    }
}