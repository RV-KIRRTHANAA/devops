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

## Phase 3: Test Connectivity, Explain Networking, and Clean Up

Test the Flask API from the host machine:

```powershell
curl.exe http://127.0.0.1:5001/about
```

Expected response:

```json
{"description":"This is a simple REST API built with Flask.","name":"Simple REST API","version":"1.0"}
```

Verify that the Flask container can resolve and reach the MySQL and Redis
containers by their Docker DNS names. This uses Python's standard library so
it does not depend on `ping` being installed in the slim image:

```powershell
docker exec flask python -c "import socket; print('mysql:', socket.gethostbyname('mysql')); print('redis:', socket.gethostbyname('redis')); print('mysql tcp:', socket.create_connection(('mysql', 3306), 5) is not None); print('redis tcp:', socket.create_connection(('redis', 6379), 5) is not None)"
```

### Questions and Answers

1. `--network` (also accepted as the older `--net`) connects a container to a
   specific Docker network.
2. Containers on the same user-defined bridge network communicate through
   Docker's internal DNS using container names such as `mysql` and `redis`, or
   through their private container IP addresses.
3. A bridge network provides an isolated virtual network for containers. A
   host network removes that network isolation and makes the container share
   the host's network namespace.
4. Use port publishing with `-p host-port:container-port`, such as
   `-p 5001:5001`, to make a container port reachable from the host.

### Cleanup

Stop and remove the containers, then remove the network:

```powershell
docker rm -f mysql redis flask
docker network rm my-bridge-net
```

