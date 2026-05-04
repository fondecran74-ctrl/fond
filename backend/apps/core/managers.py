"""Custom model managers."""
from django.db import models


class ActiveManager(models.Manager):
    """Manager that filters out soft-deleted records."""

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class InstitutionManager(models.Manager):
    """Manager that filters by institution context."""

    def for_institution(self, institution_id):
        return self.get_queryset().filter(institution_id=institution_id)
