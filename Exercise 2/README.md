# Exercise 2: Deploy a Flask App on Minikube

Deploy a Flask application to Minikube using Docker and Kubernetes YAML
manifests.

## Phases

1. Create the Flask app, Dockerfile, and container image.
2. Deploy and inspect the Kubernetes Deployment and Pod.
3. Add the NodePort Service and verify access.

## Phase 1: Create the Flask App and Image

The Flask app listens on port `15000` and returns a greeting at `/`.

Start Minikube and configure the Docker CLI for Minikube's Docker daemon:

```powershell
minikube start --driver=docker
minikube docker-env --shell=powershell | Invoke-Expression
docker build -t flask-app .\Exercise 2
docker images flask-app
```

The `flask-app:latest` image must be available before Phase 2.

## Phase 2: Deploy and Inspect the Flask App

Apply the Deployment and wait for it to become available:

```powershell
minikube kubectl -- apply -f .\Exercise 2\k8s\flask-deployment.yaml
minikube kubectl -- wait --for=condition=Available deployment/flask-app --timeout=120s
minikube kubectl -- get deployments
minikube kubectl -- get pods -l app=flask-app
```

Inspect the Deployment and view the Flask logs:

```powershell
minikube kubectl -- describe deployment flask-app
minikube kubectl -- logs deployment/flask-app
```

The Deployment should have one available replica and its Pod should be
`Running` before Phase 3.

## Phase 3: Expose and Verify the Flask App

Apply the NodePort Service:

```powershell
minikube kubectl -- apply -f .\Exercise 2\k8s\flask-service.yaml
minikube kubectl -- get service flask-app-service
```

Get the Service URL and test the Flask response:

```powershell
minikube service flask-app-service --url
curl.exe http://127.0.0.1:<node-port>
```

Expected response:

```text
Hello from Flask on Kubernetes!
```

With the Docker driver, keep the terminal running `minikube service
flask-app-service --url` open while testing from another terminal.
