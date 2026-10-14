# Exercise 1: Hello Pod

Deploy Nginx to a local Kubernetes cluster, expose it with a Service, and open the Nginx welcome page.

These instructions use PowerShell on Windows and Minikube. Run each phase separately and verify it before continuing.

## Prerequisites

- Minikube installed.
- A supported Minikube driver installed and running. The commands below use Docker Desktop with the Docker driver. Install Docker Desktop if needed, start it, and wait until its engine is running. Hyper-V is another supported option if it is enabled on the machine.
- Run PowerShell from the repository root (`Devops`).

Set the Minikube executable path for this PowerShell session. If Minikube is already on `PATH`, this still works:

```powershell
$env:Path += ";$env:ProgramFiles\Kubernetes\Minikube"
minikube version
```

## Phase 1: Start Minikube

Start a local cluster using Docker Desktop:

```powershell
minikube start --driver=docker
```

Check the cluster and node:

```powershell
minikube status
minikube kubectl -- get nodes
```

Continue when the node reports `Ready`.

Suggested commit message: `docs(k8s): document hello-pod exercise phases`

## Phase 2: Create the Nginx pod

Apply the pod manifest:

```powershell
minikube kubectl -- apply -f .\k8s\hello-pod.yaml
```

Wait for the pod to become ready and inspect it:

```powershell
minikube kubectl -- wait --for=condition=Ready pod/hello-k8s --timeout=120s
minikube kubectl -- get pods -o wide
```

Suggested commit message: `feat(k8s): add hello-k8s nginx pod manifest`

## Phase 3: Expose the pod

Apply the NodePort Service manifest:

```powershell
minikube kubectl -- apply -f .\k8s\hello-service.yaml
minikube kubectl -- get service hello-k8s
```

Suggested commit message: `feat(k8s): expose hello-k8s with NodePort service`

## Phase 4: Open and verify Nginx

Open the Service URL through Minikube:

```powershell
minikube service hello-k8s
```

The browser should display the Nginx welcome page.

Suggested commit message: `docs(k8s): add hello-pod access instructions`

## Troubleshooting

- If `minikube start --driver=docker` reports that Docker is unavailable, start Docker Desktop and retry. If Docker Desktop is not installed, install it before continuing.
- If PowerShell cannot find `minikube`, rerun the `PATH` setup from the prerequisites section or open a new PowerShell window.
- If a pod is not ready, inspect it with `minikube kubectl -- describe pod hello-k8s` and `minikube kubectl -- logs hello-k8s`.

## Cleanup (optional)

Remove the exercise resources and stop Minikube when finished:

```powershell
minikube kubectl -- delete -f .\k8s\hello-service.yaml
minikube kubectl -- delete -f .\k8s\hello-pod.yaml
minikube stop
```
