"""Access Review Repository."""
from apps.iam.infrastructure.orm.models import *  # noqa


class AccessReviewRepository:
    """Repository for access review persistence."""

    def find_by_id(self, id):
        raise NotImplementedError

    def save(self, entity):
        raise NotImplementedError
