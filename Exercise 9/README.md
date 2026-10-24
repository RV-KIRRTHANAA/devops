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

