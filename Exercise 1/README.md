# Exercise 1: Hello Pod

Deploy the Nginx image to a local Kubernetes cluster, expose it with a
Service, and open the Nginx welcome page.

This exercise uses PowerShell on Windows and Minikube. Each phase should be
completed and verified before continuing to the next one.

## Prerequisites

- Minikube installed.
- Docker Desktop installed and running, with the Docker driver available.
- PowerShell opened from the repository root (`Devops`).

Set the Minikube executable path for the current PowerShell session. If
Minikube is already on `PATH`, this command is harmless:

```powershell
$env:Path += ";$env:ProgramFiles\Kubernetes\Minikube"
minikube version
```

## Phases

1. Start a local Minikube cluster.
2. Create the `hello-k8s` Nginx Pod.
3. Expose the Pod with a NodePort Service.
4. Open and verify the Nginx welcome page.

## Phase 1: Start Minikube

Start a local Kubernetes cluster using Docker Desktop:

```powershell
minikube start --driver=docker
```

Check the cluster and node status:

```powershell
minikube status
minikube kubectl -- get nodes
```

The node must report `Ready` before moving to Phase 2.

## Phase 2: Create the Nginx Pod

Apply the Pod manifest:

```powershell
minikube kubectl -- apply -f .\Exercise 1\k8s\hello-pod.yaml
```

Wait for the Pod to become ready and inspect it:

```powershell
minikube kubectl -- wait --for=condition=Ready pod/hello-k8s --timeout=120s
minikube kubectl -- get pods -o wide
```

The `hello-k8s` Pod should report `Running` and `1/1` containers ready before
moving to Phase 3.

## Phase 3: Expose the Pod

Apply the NodePort Service manifest:

```powershell
minikube kubectl -- apply -f .\Exercise 1\k8s\hello-service.yaml
minikube kubectl -- get service hello-k8s
```

The `hello-k8s` Service should have type `NodePort` and route traffic on port
80 to the Nginx Pod before moving to Phase 4.

## Troubleshooting

- If Minikube cannot connect to Docker, start Docker Desktop and retry.
- If PowerShell cannot find Minikube, rerun the `PATH` setup above or open a
  new PowerShell window.
- If the Pod is not ready, inspect it with
  `minikube kubectl -- describe pod hello-k8s` and
  `minikube kubectl -- logs hello-k8s`.

