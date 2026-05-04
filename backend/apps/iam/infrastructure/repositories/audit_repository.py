"""Audit Repository."""
from apps.iam.infrastructure.orm.models import *  # noqa


class AuditRepository:
    """Repository for audit persistence."""

    def find_by_id(self, id):
        raise NotImplementedError

    def save(self, entity):
        raise NotImplementedError
