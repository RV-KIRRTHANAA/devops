# Exercise 5: Secure a Docker Container with AppArmor

Use an AppArmor profile to restrict a Flask container's file access,
capabilities, and executable actions, then verify the profile with the Docker
SDK for Python.

AppArmor enforcement requires a Linux host or Linux virtual machine with
AppArmor enabled. Docker Desktop on Windows may build the image, but host
AppArmor enforcement must be performed in a supported Linux environment.

## Phases

1. Create and build the Flask application image.
2. Create, load, and apply the AppArmor profile.
3. Verify the profile with the Docker SDK, test restricted actions, document
   the security answers, and clean up.

## Phase 1: Create the Flask Image

The Flask app listens on port `5000` and returns a confirmation message at
`/`.

Build the image:

```bash
docker build -t flask-apparmor ./Exercise\ 5
```

Verify the image:

```bash
docker image inspect flask-apparmor
```

The `flask-apparmor` image must exist before moving to Phase 2.

## Phase 2: Load and Apply the AppArmor Profile

These commands must run on a Linux host or Linux VM with AppArmor enabled.
Install the AppArmor utilities if needed:

```bash
sudo apt-get update
sudo apt-get install -y apparmor-utils
```

Copy the profile into AppArmor's profile directory and load it:

```bash
sudo cp ./Exercise\ 5/apparmor/my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
sudo aa-status | grep my-apparmor-profile
```

Run the Flask container with the profile attached:

```bash
docker run -d --name flask-apparmor-test \
  --security-opt="apparmor=my-apparmor-profile" \
  -p 5000:5000 flask-apparmor
```

Check that the container is running:

```bash
docker ps --filter name=flask-apparmor-test
```

The profile must be loaded successfully and the container must be running
before moving to Phase 3.

## Phase 3: Verify the Profile and Test Restrictions

Install the Docker SDK for Python:

```bash
python -m pip install docker
```

Run the SDK verification script:

```bash
python ./Exercise\ 5/apply_apparmor.py
```

The output should show `apparmor=my-apparmor-profile` in the container's
security options.

Run the restricted-action tests:

```bash
python ./Exercise\ 5/test_restricted_actions.py
```

The attempts to read `/etc/passwd` and execute `/bin/sh` should fail under the
profile. The test uses `/bin/sh` because slim Python images are not guaranteed
to include `/bin/bash`.

### Questions and Answers

1. AppArmor adds mandatory access-control rules that confine a containerized
   application beyond ordinary Docker isolation.
2. Profiles specify which files, directories, capabilities, network types, and
   executable actions a process may access.
3. Restricting `/etc` and `/var` reduces the risk of reading credentials or
   configuration and modifying system state or application data.
4. Profiles can restrict capabilities such as `sys_admin`, network access,
   port binding, file writes, mounting, signal use, and binary execution.
5. Inspect the container's `HostConfig.SecurityOpt` through the Docker SDK or
   run `docker inspect <container>` and check for
   `apparmor=my-apparmor-profile`. AppArmor audit logs can provide additional
   evidence of denied actions.

### Cleanup

The supplied Python scripts stop and remove their test containers in a
`finally` block. If a container remains after an interrupted run:

```bash
docker rm -f flask-apparmor-test flask-apparmor-sdk flask-apparmor-restrictions
```

