pipeline {
  agent none
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

    stage('deploy') {
      steps {
        sh 'echo \'This is deploy test\''
      }
    }

  }
}