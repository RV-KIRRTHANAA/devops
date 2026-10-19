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

