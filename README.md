# CloudCart mini: Jenkins CI/CD demo

Jenkins tests, validates, builds, and deploys this SAM app to AWS (us-east-1) on every push.

Pipeline stages: Test > Validate > Build > Deploy > Smoke test

Files
- Jenkinsfile        pipeline definition
- template.yaml      SAM template (API Gateway + Lambda)
- src/app.py         Lambda code (change VERSION to see a redeploy)
- tests/test_app.py  unit tests (break them to see the pipeline stop)
