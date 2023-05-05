pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment { 
   PROJECT_NAME = "facebook"
   REGISTRYUSERNAME = "golide"
   VERSION = "dev-latest"
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
                sh  "echo ${BUILD_NUMBER}"
                sh "echo  ${env.BUILD_ID} "       
               sh  'cd /var/lib/jenkins/workspace/DotNet-DevSecOps/src/Facebook'
               sh "docker build -t ${REGISTRYUSERNAME}/${PROJECT_NAME}:${VERSION} /var/lib/jenkins/workspace/DotNet-DevSecOps/src/Facebook"                           
            }
         }

      }

}
 
