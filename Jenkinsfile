pipeline {
    agent any
    triggers {
        githubPush()
    }

    environment { 
    CI_PROJECT_NAME = "${JOB_NAME}"
    API_DEPLOY_FOLDER = "api"
    VERSION = "${env.BUILD_ID}"
    IMAGE_TAG = "dev-latest"
    REGISTRY_USERNAME = "golide"
    DOCKER_IMAGE = "${REGISTRY_USERNAME}/${CI_PROJECT_NAME}:${IMAGE_TAG}"
    REGISTRY_CREDENTIALS = credentials('dockerhub')
    WORKSPACE = "${env.WORKSPACE}"
    VALUES_PATH="${WORKSPACE}/helm-charts/values.yaml"
    DEPLOYS_REPO = "https://github.com/edtshuma/dev-helm-deployments.git"
    HELM_REPO = "https://github.com/edtshuma/base-helm-templates.git"
}
    stages {

        stage('Setup'){
           steps{
               sh 'echo ${CI_PROJECT_NAME}'
               sh 'echo ${WORKSPACE}'
               sh "echo ${GIT_COMMIT}"
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
                    sh "cd ${WORKSPACE}/src/Facebook && docker build -t ${DOCKER_IMAGE} ."
                    def dockerImage = docker.image("${DOCKER_IMAGE}")
                    docker.withRegistry('https://index.docker.io/v1/', "dockerhub") {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Update Helm Charts') {
            steps { 
                        sh "mkdir helm-input"
                        sh "mkdir helm-output"
                        sh "mkdir dev-deployments"
                        sh "git clone /var/lib/jenkins/workspace/base-helm-templates helm-input"
                        sh 'cd helm-input/dev-deployments'
                        sh "helm template api-deployments ${WORKSPACE}/helm-input/dev-deployments/api-deployments --output-dir ${WORKSPACE}/helm-output -f ${VALUES_PATH} --set image.tag=${IMAGE_TAG} --set deployment.commitHash=${GIT_COMMIT}"
                        sh "cd ${WORKSPACE}"
                        sh "git clone ${DEPLOYS_REPO} dev-deployments"
                        sh "mkdir -p dev-deployments/${API_DEPLOY_FOLDER}/${CI_PROJECT_NAME}"
                        sh "cp -r helm-output/api-deployments/templates dev-deployments/${API_DEPLOY_FOLDER}/${CI_PROJECT_NAME}"
                        sh "cd ${WORKSPACE}/dev-deployments"
                        sh "git config --global user.name \"edtshuma\""
                        sh "git config --global user.email \"edtshuma@gmail.com\""
                        sh "git add --all"
                        sh "git commit -am \"dev deployment of ${CI_PROJECT_NAME}\""                   
                        sh "git remote set-url origin https://edtshuma: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@github.com/edtshuma/dev-helm-deployments.git"
                        sh "git push origin HEAD:master"
                        sh "cd ${WORKSPACE}"
                        sh "sudo rm -r helm-input"
                        sh "sudo rm -r helm-output"
                        sh "sudo rm -r dev-deployments"
  
                }
        }
    
    }

}