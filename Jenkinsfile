pipeline {
     agent any
     
    triggers {
        githubPush()
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
          step([$class: 'CoberturaPublisher', coberturaReportFile: 'output/coverage/jest/cobertura-coverage.xml'])
        }
      }                    
       }
     
   }
}
 