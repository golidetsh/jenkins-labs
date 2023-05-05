pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment { 
    PROJECT_NAME = "facebook"
    VERSION = "${env.BUILD_ID}"
    IMAGE_TAG = "dev-latest"
    REGISTRY_USERNAME = "golide"
}
    stages {

        stage('Setup'){
           steps{
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

        stage('Docker Build'){
           steps{
                sh  "echo ${VERSION}"      
               sh  'cd /var/lib/jenkins/workspace/DotNet-DevSecOps/src/Facebook'
               sh "docker build -t ${REGISTRY_USERNAME}/${PROJECT_NAME}:${IMAGE_TAG} /var/lib/jenkins/workspace/DotNet-DevSecOps/src/Facebook"                           
            }
         }

      }

}
 
