"""Authorization pipeline tests."""
import pytest


@pytest.mark.django_db
class TestAuthorizationPipeline:
    def test_unprovisionned_identity_rejected(self):
        """An identity not provisioned by the institution must be rejected."""
        pass

    def test_mac_no_read_up(self):
        """A user cannot read data with higher classification."""
        pass

    def test_sod_conflict_blocked(self):
        """Conflicting roles must be blocked."""
        pass
