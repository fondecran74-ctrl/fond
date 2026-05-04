"""Test that candidates are provisioned by institution agents only."""
import pytest


@pytest.mark.django_db
class TestCandidateProvisioning:
    def test_candidate_cannot_self_register(self):
        """Candidates cannot create their own account."""
        pass

    def test_agent_can_create_candidate(self):
        """An authorized agent can create a candidate."""
        pass
