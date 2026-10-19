# Exercise 7: Continuous Integration with Jenkins

Set up Jenkins and create a basic Continuous Integration workflow that
automatically builds and tests project changes.

## Phases

1. Run Jenkins with persistent storage and access the setup page.
2. Create a CI pipeline with automated build and test stages.
3. Run the pipeline, inspect results, and document cleanup.

## Phase 1: Install Jenkins with Docker

Start Jenkins with Docker Compose:

```powershell
docker compose -f .\Exercise 7\docker-compose.yml up -d
docker compose -f .\Exercise 7\docker-compose.yml ps
```

Open Jenkins in a browser:

```text
http://localhost:8080
```

Retrieve the one-time unlock password from the container:

```powershell
docker exec jenkins bash -c "cat /var/jenkins_home/secrets/initialAdminPassword"
```

Use that password on the Jenkins unlock page, install the suggested plugins,
and create the first administrator account. Jenkins data is stored in the
named `jenkins_home` volume so it survives container restarts.

## Phase 2: Create a CI Pipeline

The [Jenkinsfile](Jenkinsfile) performs three CI stages:

1. Check out the repository.
2. Validate the Python source files compile successfully.
3. Run the unit test suite.

The Jenkins agent must have Python 3.10 or newer available as `python`. In
Jenkins, create a Pipeline job, choose **Pipeline script from SCM**, select the
repository, and set the script path to:

```text
Exercise 7/Jenkinsfile
```

The sample application and test are in [ci_app.py](ci_app.py) and
[test_ci_app.py](test_ci_app.py).

## Phase 3: Run and Verify the Pipeline

Start Jenkins if it is not already running:

```powershell
docker compose -f .\Exercise 7\docker-compose.yml up -d
```

Open Jenkins at `http://localhost:8080`, open the Pipeline job, and select
**Build Now**. The build should show these successful stages:

- Checkout
- Validate Python
- Run Tests

Open the build number and select **Console Output** to inspect the checkout,
Python validation, and unit-test logs. A successful run should end with:

```text
CI pipeline completed successfully.
Finished: SUCCESS
```

### Cleanup

Stop and remove the Jenkins container while preserving the named volume:

```powershell
docker compose -f .\Exercise 7\docker-compose.yml down
```

To remove Jenkins data as well, use:

```powershell
docker compose -f .\Exercise 7\docker-compose.yml down -v
```

