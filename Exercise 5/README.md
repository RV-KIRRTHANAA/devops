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

