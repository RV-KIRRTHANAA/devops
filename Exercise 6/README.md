# Exercise 6: Real-Time Operations Monitoring and Alerting

Simulate delivery-service metrics, scrape them with Prometheus, visualize them
with Grafana, and automate the setup with Jenkins.

## Phases

1. Create the metrics application, image, Prometheus configuration, and alert
   rules.
2. Run Prometheus and Grafana, create the dashboard, and verify alerts.
3. Add the Jenkins pipeline, automate the stack, simulate an alert, and clean
   up.

## Phase 1: Create the Metrics Application and Monitoring Configuration

The metrics application exposes Prometheus metrics on port `8000`:

- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- `average_delivery_time`

Build the image:

```powershell
docker build -t delivery-metrics .\Exercise 6\delivery_monitoring
```

The `PENDING_MIN` and `PENDING_MAX` environment variables control the
simulated pending-delivery range, which will be used later to trigger alerts.

The Prometheus configuration targets the container name
`delivery-metrics:8000`, so all monitoring containers must share one Docker
network in Phase 2.

## Phase 2: Run Prometheus and Grafana

Start the complete monitoring stack:

```powershell
docker compose -f .\Exercise 6\docker-compose.yml up -d --build
docker compose -f .\Exercise 6\docker-compose.yml ps
```

Verify that the metrics endpoint is producing data:

```powershell
curl.exe http://localhost:8000/metrics
```

Open the services:

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

In Grafana, sign in with the initial local credentials `admin` / `admin`,
then add a Prometheus data source with this URL:

```text
http://prometheus:9090
```

Create a dashboard with these Prometheus queries:

```text
total_deliveries
pending_deliveries
on_the_way_deliveries
average_delivery_time_sum / average_delivery_time_count
```

In Prometheus, open `http://localhost:9090/alerts` and confirm that the alert
rules are loaded. `HighPendingDeliveries` should become pending or firing when
`pending_deliveries` remains above 10 for 15 seconds.

## Phase 3: Automate with Jenkins and Simulate an Alert

The [Jenkinsfile](Jenkinsfile) checks Docker, starts the monitoring stack,
verifies the metrics endpoint, restarts the metrics container with high
pending-delivery values, queries Prometheus, and cleans up the stack.

The Jenkins agent must have both the Docker CLI and Docker Compose available,
and must be allowed to access the Docker daemon. A typical Linux Jenkins
container is started with the Docker socket mounted:

```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

Configure a Jenkins Pipeline job to use this repository and run the
`Jenkinsfile`. The build should complete the Docker pre-check, start the
monitoring stack, query metrics, simulate high pending deliveries, query
Prometheus, and run the cleanup block.

To simulate the alert manually without Jenkins, recreate the metrics service
with a high pending range:

```powershell
docker compose -f .\Exercise 6\docker-compose.yml stop delivery-metrics
docker compose -f .\Exercise 6\docker-compose.yml rm -f delivery-metrics
docker compose -f .\Exercise 6\docker-compose.yml run -d --name delivery-metrics `
  -e PENDING_MIN=50 -e PENDING_MAX=100 delivery-metrics
```

Wait at least 20 seconds, then check `http://localhost:9090/alerts`.

### Cleanup

```powershell
docker compose -f .\Exercise 6\docker-compose.yml down -v
docker rm -f jenkins
```

