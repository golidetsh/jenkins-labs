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

      }

}
 
