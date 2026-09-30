pipeline {
  agent any
  environment {
    AWS_DEFAULT_REGION = 'us-east-1'
    STACK = 'cloudcart-jenkins-demo'
  }
  stages {
    stage('Test') {
      steps {
        sh 'python3.12 -m pip install --user -q pytest'
        sh 'PYTHONPATH=src python3.12 -m pytest -q tests'
      }
    }
    stage('Validate') {
      steps { sh 'sam validate --lint' }
    }
    stage('Build') {
      steps { sh 'sam build' }
    }
    stage('Deploy') {
      steps {
        sh 'sam deploy --stack-name $STACK --resolve-s3 --capabilities CAPABILITY_IAM --no-confirm-changeset --no-fail-on-empty-changeset'
      }
    }
    stage('Smoke test') {
      steps {
        sh '''
          URL=$(aws cloudformation describe-stacks --stack-name $STACK \
            --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text)
          echo "API: $URL/products"
          curl -sf $URL/products | tee response.json
          grep -q "Laptop Stand" response.json
        '''
      }
    }
  }
}
