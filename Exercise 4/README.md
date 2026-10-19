# Exercise 4: Docker Networking with Multiple Containers

Create a multi-container application with a Flask API, MySQL database, and
Redis cache connected through a user-defined Docker bridge network.

## Phases

1. Create and build the Flask API image.
2. Create the bridge network and launch the three containers.
3. Test connectivity and the API, document the networking concepts, and clean
   up the resources.

## Phase 1: Create the Flask API Image

The Flask API exposes `GET /about` on port `5001`.

Build the image from the Exercise 4 directory:

```powershell
docker build -t flask-api .\Exercise 4
```

Verify that the image was created:

```powershell
docker image inspect flask-api
```

The `flask-api` image must exist before moving to Phase 2.

## Phase 2: Create the Network and Launch Containers

Create a user-defined bridge network:

```powershell
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

Launch MySQL, Redis, and Flask on the same network. The MySQL password is
required by the official MySQL image, even though this exercise only tests
network connectivity:

```powershell
docker run -d --name mysql --network my-bridge-net `
  -e MYSQL_ROOT_PASSWORD=devops-root-password `
  mysql:latest

docker run -d --name redis --network my-bridge-net redis:latest

docker run -d --name flask --network my-bridge-net `
  -p 5001:5001 flask-api
```

Verify that all three containers are running and attached to the network:

```powershell
docker ps
docker network inspect my-bridge-net
```

The containers should be named `mysql`, `redis`, and `flask`. Continue to
Phase 3 after all three containers report a running status.

