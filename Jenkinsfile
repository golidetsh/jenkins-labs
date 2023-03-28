pipeline {
     agent any
     
    triggers {
        githubPush()
    }
     environment { 
   IMAGE = "nodejs-devsecops"
   REGISTRY_USERNAME = "golide"
   VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
   IMAGE_REPO = "${REGISTRY}/${REGISTRY_USERNAME}/${IMAGE}" + ":$VERSION" 
}
    stages {
        
         stage('Setup'){
           steps{
            dir('app') {
               sh '''sudo chown -R $USER .             
                 npm install
                '''
             }   
           }
         } 
       stage('Unit Tests'){ 
           steps{
             dir('app/tests') {
               sh 'npm test'           
             }
           }
           post {
        always {
          step([$class: 'CoberturaPublisher', coberturaReportFile: 'app/coverage/clover.xml'])
        }
      }                    
    }

        stage('Docker Build') {
          steps{
             dir('app'){
                script {
                  sh "docker build -t ${REGISTRY_USERNAME}/${IMAGE}:${VERSION} ."                          
                }
            }
      }
    }        
     
   }
}
 