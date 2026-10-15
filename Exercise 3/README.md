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

## Phase 2: Deploy and Verify Three Pods

Apply the ReplicaSet and Service manifest:

```powershell
minikube kubectl -- apply -f .\Exercise 3\k8s\flashsale-replicaset.yaml
```

Wait for all three replicas to become ready and inspect them:

```powershell
minikube kubectl -- wait --for=condition=Ready pod -l app=flashsale --timeout=120s
minikube kubectl -- get rs flashsale-rs
minikube kubectl -- get pods -l app=flashsale -o wide
minikube kubectl -- get service flashsale-svc
```

The ReplicaSet should report `3` desired, current, and ready replicas. Each
Pod should be `Running` and ready before moving to Phase 3.

## Phase 3: Scale and Verify Self-Healing

Scale the ReplicaSet from three to five replicas:

```powershell
minikube kubectl -- scale rs flashsale-rs --replicas=5
minikube kubectl -- wait --for=condition=Ready pod -l app=flashsale --timeout=120s
minikube kubectl -- get rs flashsale-rs
minikube kubectl -- get pods -l app=flashsale -o wide
```

Delete one of the five Pods. Replace `<pod-name>` with a Pod name from the
previous command:

```powershell
minikube kubectl -- delete pod <pod-name>
```

Verify that the ReplicaSet creates a replacement Pod:

```powershell
minikube kubectl -- get pods -l app=flashsale -o wide
minikube kubectl -- get rs flashsale-rs
```

The ReplicaSet should return to five ready Pods after the deletion. Because
this exercise uses a single-node cluster, all Pods are expected to show the
same node while still demonstrating replica scaling and self-healing.

