"""Admission flow integration tests."""
import pytest


@pytest.mark.django_db
@pytest.mark.integration
class TestAdmissionFlow:
    def test_create_candidate_by_agent(self):
        pass

    def test_candidate_cannot_self_register(self):
        pass
