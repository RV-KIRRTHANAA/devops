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

