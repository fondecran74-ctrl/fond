"""OpenTelemetry configuration."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource


def setup_telemetry() -> None:
    """Initialize OpenTelemetry tracing."""
    resource = Resource.create({"service.name": "ems-backend"})
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)
