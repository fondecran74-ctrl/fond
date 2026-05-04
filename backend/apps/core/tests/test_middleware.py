"""Middleware tests."""
from apps.core.middleware.correlation_id import CorrelationIdMiddleware


class TestCorrelationIdMiddleware:
    def test_generates_correlation_id(self):
        """Test that a correlation ID is generated when not provided."""
        pass
