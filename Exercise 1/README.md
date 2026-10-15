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

## Troubleshooting

- If Minikube cannot connect to Docker, start Docker Desktop and retry.
- If PowerShell cannot find Minikube, rerun the `PATH` setup above or open a
  new PowerShell window.

