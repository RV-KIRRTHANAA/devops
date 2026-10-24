# Exercise 10: Multi-Node Kubernetes with Multiple Applications

Deploy a Product Catalog service and a Shopping Cart service across a
three-node Minikube cluster with replica distribution and service access.

## Phases

1. Create both Flask services, build their images, and prepare a three-node
   Minikube cluster.
2. Deploy both applications with replica counts and pod anti-affinity, then
   verify distribution across nodes.
3. Expose both applications with NodePort Services, test the APIs, and clean
   up.

## Phase 1: Create Apps, Images, and the Cluster

Start a three-node Minikube profile. Delete an old profile first only if it is
no longer needed:

```powershell
minikube delete -p devops-multinode
minikube start --nodes=3 -p devops-multinode --driver=docker
minikube status -p devops-multinode
minikube -p devops-multinode kubectl -- get nodes
```

Build both images:

```powershell
docker build -t product-catalog:latest -f ".\Exercise 10\Dockerfile.product" ".\Exercise 10"
docker build -t shopping-cart:latest -f ".\Exercise 10\Dockerfile.shopping" ".\Exercise 10"
```

Load the images into the Minikube profile so every node can use them:

```powershell
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
minikube -p devops-multinode image ls
```

Both images must be available before moving to Phase 2.

