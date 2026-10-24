# Exercise 9: Jenkins Multi-Stage Flask Pipeline

Create a Jenkins Pipeline that builds, tests, deploys, and verifies a Python
Flask application.

## Phases

1. Create the Flask application, dependencies, and unit test.
2. Add the Jenkins Build, Test, Deploy, and application-verification stages.
3. Add code quality, Docker deployment, notifications, and cleanup.

## Phase 1: Create the Flask Application

The application returns `Hello, Jenkins Multi-Stage Pipeline!` from `/`.

Run the unit test locally:

```bash
python -m pip install -r "Exercise 9/requirements.txt"
python -m unittest discover -s "Exercise 9" -p "test_*.py" -v
```

The test should finish with `OK` before moving to Phase 2.

## Phase 2: Add the Multi-Stage Jenkins Pipeline

The [Jenkinsfile](Jenkinsfile) contains these stages:

1. **Build** creates a virtual environment and installs the requirements.
2. **Test** runs the unit test suite.
3. **Deploy** copies the application into `python-app-deploy`.
4. **Run Application** starts the deployed Flask app temporarily.
5. **Test Application** verifies the live HTTP response.

Configure a Jenkins Pipeline job to use this repository and set the script
path to:

```text
Exercise 9/Jenkinsfile
```

The Jenkins agent must provide `python3`, `python3-venv`, and a shell. Run the
job after the repository is connected; the pipeline cleans up the temporary
Flask process in its `post` block.

## Phase 3: Add Quality, Docker Deployment, and Notifications

The pipeline now adds these stages:

- **Code Quality** runs Flake8 against the application and tests.
- **Docker Build** builds the `jenkins-flask-app` image.
- **Docker Deploy** runs the image on host port `5001` and verifies the HTTP
  response.

The Jenkins agent must also have Docker CLI, Docker Compose support, and access
to the Docker daemon. For a Linux Jenkins container, mount the Docker socket:

```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

Configure the job to use [Jenkinsfile](Jenkinsfile), run **Build Now**, and
verify that the Code Quality, Docker Build, and Docker Deploy stages pass. The
pipeline prints success or failure notifications and removes the temporary
Flask process and Docker container in its cleanup block.

