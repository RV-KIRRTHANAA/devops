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

