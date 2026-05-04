"""Prometheus metrics."""
from prometheus_client import Counter, Histogram

http_requests_total = Counter(
    "ems_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

http_request_duration_seconds = Histogram(
    "ems_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)
