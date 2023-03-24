pipeline {
     agent any
     options { buildDiscarder(logRotator(numToKeepStr:'5'))}

    triggers {
        githubPush()
    }

 environment { 
   IMAGE = "python-devsecops"
   REGISTRY = "docker.io"
   REGISTRY_USERNAME = "golide"
   VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
   IMAGE_REPO = "${REGISTRY}/${REGISTRY_USERNAME}/${IMAGE}" + ":$VERSION" 
   IMAGE_TAG="${VERSION}"
}
    stages {
        
        stage('Setup'){
           steps{
            withPythonEnv('/usr/bin/python3.8') {
                    sh 'echo "Job is starting" '
                }            
            }
         } 

      stage('Unit Tests'){ 
           steps{
               withPythonEnv('/usr/bin/python3.8') {
                 sh '''pip install -r requirements.txt
                       sudo chown -R $USER .
                       pytest -v --junitxml=docs/unit-tests/coverage.xml --cov-report xml --cov app.main
                '''
             }           
           }                    
         }   

       stage('Publish Test Report'){ 
           steps{
              cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage*.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
              archiveArtifacts artifacts: 'docs/unit-tests/*.*'
            }                    
         }

         stage('Docker Build') {
          steps{
            script {
                sh "docker build -t ${REGISTRY_USERNAME}/${IMAGE}:${VERSION} ."                          
        }
      }
    }        

      }
}
 