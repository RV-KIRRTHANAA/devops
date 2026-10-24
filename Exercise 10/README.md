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

## Phase 2: Deploy and Verify Replica Distribution

Apply both Deployment manifests:

```powershell
minikube -p devops-multinode kubectl -- apply -f ".\Exercise 10\k8s\product_catalog_deployment.yaml"
minikube -p devops-multinode kubectl -- apply -f ".\Exercise 10\k8s\shopping_cart_deployment.yaml"
```

Wait for the requested replicas to become ready:

```powershell
minikube -p devops-multinode kubectl -- wait --for=condition=Available deployment/product-catalog --timeout=120s
minikube -p devops-multinode kubectl -- wait --for=condition=Available deployment/shopping-cart --timeout=120s
minikube -p devops-multinode kubectl -- get deployments
minikube -p devops-multinode kubectl -- get pods -o wide
```

Product Catalog should have two ready replicas on different nodes. Shopping
Cart should have three ready replicas, one on each node. If a replica remains
Pending, confirm that the cluster has three Ready nodes and that the images
were loaded into the Minikube profile.

## Phase 3: Expose and Test Both Services

Apply the NodePort Services:

```powershell
minikube -p devops-multinode kubectl -- apply -f ".\Exercise 10\k8s\product_catalog_service.yaml"
minikube -p devops-multinode kubectl -- apply -f ".\Exercise 10\k8s\shopping_cart_service.yaml"
minikube -p devops-multinode kubectl -- get services
```

Get a local URL for each Service. Keep each command running in its own
terminal when using the Docker driver:

```powershell
minikube -p devops-multinode service product-catalog-service --url
minikube -p devops-multinode service shopping-cart-service --url
```

Use the returned URLs to test the APIs:

```powershell
curl.exe http://127.0.0.1:<product-catalog-port>/products
curl.exe http://127.0.0.1:<shopping-cart-port>/cart
curl.exe -X POST http://127.0.0.1:<shopping-cart-port>/cart `
  -H "Content-Type: application/json" `
  -d '{"id":1,"name":"Laptop","quantity":1}'
```

The catalog request should return three products. The cart should initially
return `[]`, then return the added item after the POST request.

Check final placement and Service endpoints:

```powershell
minikube -p devops-multinode kubectl -- get pods -o wide
minikube -p devops-multinode kubectl -- get endpoints product-catalog-service shopping-cart-service
```

### Cleanup

Remove the entire exercise profile when finished:

```powershell
minikube delete -p devops-multinode
```

