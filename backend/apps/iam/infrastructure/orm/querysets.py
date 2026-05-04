"""Custom querysets for IAM models."""
from django.db import models


class ActiveUserQuerySet(models.QuerySet):
    def active(self):
        return self.filter(account_status="ACTIVE", is_active=True)

    def by_type(self, user_type: str):
        return self.filter(user_type=user_type)

    def by_institution(self, institution_id):
        return self.filter(institution_id=institution_id)
