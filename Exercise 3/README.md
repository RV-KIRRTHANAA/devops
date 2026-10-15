# Exercise 3: Scale a Flask App with a ReplicaSet

Simulate an e-commerce flash sale by running multiple copies of a Flask
service and observing ReplicaSet scaling and self-healing.

## Phases

1. Create the Flash Sale Flask app and container image.
2. Deploy the ReplicaSet and Service, then verify three healthy Pods.
3. Scale to five replicas, delete a Pod, and verify self-healing.

## Phase 1: Create the App and Image

The application provides three endpoints:

- `/` returns a sale welcome message and the serving hostname.
- `/buy?user=123` simulates a purchase and identifies the serving Pod.
- `/health` provides the readiness and liveness response.

Build the image inside Minikube's Docker environment:

```powershell
minikube start --driver=docker
minikube docker-env --shell=powershell | Invoke-Expression
docker build -t flashsale:1.0 .\Exercise 3
docker images flashsale
```

The `flashsale:1.0` image must be available before Phase 2. A registry push is
not required when the image is built directly into Minikube's Docker daemon.

