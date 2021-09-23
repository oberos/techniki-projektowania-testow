pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        git(url: 'https://github.com/oberos/techniki-projektowania-testow.git', branch: 'main')
      }
    }

    stage('test') {
      steps {
        sh 'ls -l'
      }
    }

    stage('deploy - prod') {
      when {
        branch 'main' 
      }
      steps {
        sh 'echo \'This is deploy stage\''
        sh 'echo \'this is branch prod\''
      }
    }
    stage('deploy - test') {
      when { 
        not { 
          branch 'main' 
        } 
      }
      steps {
        sh 'echo \'This is deploy stage\''
        sh 'echo \'this is branch test\''
      }
    }

  }
}
