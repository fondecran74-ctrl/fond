"""Distributed tracing utilities."""
from opentelemetry import trace

tracer = trace.get_tracer("ems-backend")


def get_tracer():
    return tracer
