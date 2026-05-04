"""Permission Repository."""
from apps.iam.infrastructure.orm.models import *  # noqa


class PermissionRepository:
    """Repository for permission persistence."""

    def find_by_id(self, id):
        raise NotImplementedError

    def save(self, entity):
        raise NotImplementedError
