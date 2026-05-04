"""Telemetry exporters."""


def setup_prometheus_exporter():
    """Set up Prometheus metrics exporter."""
    from opentelemetry.exporter.prometheus import PrometheusMetricReader
    return PrometheusMetricReader()
