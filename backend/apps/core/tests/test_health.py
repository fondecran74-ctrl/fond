"""Health check tests."""
import pytest
from django.test import RequestFactory
from apps.core.health.views import liveness


@pytest.mark.django_db
class TestHealthChecks:
    def test_liveness_returns_200(self):
        factory = RequestFactory()
        request = factory.get("/health/live/")
        response = liveness(request)
        assert response.status_code == 200
