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
 
   stage('Trivy Scan') {
            steps {
                dir('app'){
                script {
                    sh '''
                    sudo chown -R $USER \"/usr/local/bin/\"
                    trivy --severity HIGH,CRITICAL  --exit-code 1 image --format template --template \"@/usr/local/bin/html.tpl\" --output trivy_report.html ${REGISTRY_USERNAME}/${IMAGE}:${VERSION} 
                    '''         
                } 
              }  
            }
            post {
        always {
            archiveArtifacts artifacts: "app/trivy_report.html", fingerprint: true     
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'app/trivy_report.html',
                reportName: 'Trivy Scan',
                ])
            }
        }
      }
     
   }
}
 