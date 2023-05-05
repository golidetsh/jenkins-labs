pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment { 
    PROJECT_NAME = "${JOB_NAME}"
    VERSION = "${env.BUILD_ID}"
    IMAGE_TAG = "dev-latest"
    REGISTRY_USERNAME = "golide"
    DOCKER_IMAGE = "${REGISTRY_USERNAME}/${PROJECT_NAME}:${IMAGE_TAG}"
    REGISTRY_CREDENTIALS = credentials('dockerhub')
    WORKSPACE = "${env.WORKSPACE}"
    VALUES_PATH="${WORKSPACE}/${PROJECT_NAME}/src/Facebook/helm-scripts/values.yaml"
    CI_COMMIT_SHORT_SHA ="${env.GIT_COMMIT}"
}
    stages {

        stage('Setup'){
           steps{
               sh 'echo ${PROJECT_NAME}'
               sh 'dotnet restore devsecops.sln'
            }
         }

        stage('Build'){
           steps{
               sh '''dotnet clean devsecops.sln --configuration Release 
                     dotnet build devsecops.sln --configuration Release --no-restore
                '''
            }
         }
         
     stage('Docker Build and Push') {
      steps {
        script {
            sh "cd ${WORKSPACE}/dotnet/src/Facebook && docker build -t ${DOCKER_IMAGE} ."
            def dockerImage = docker.image("${DOCKER_IMAGE}")
            docker.withRegistry('https://index.docker.io/v1/', "dockerhub") {
                dockerImage.push()
            }
        }
      }
    }
      }
}
 
