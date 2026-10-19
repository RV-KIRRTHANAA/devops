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

