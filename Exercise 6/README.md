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

