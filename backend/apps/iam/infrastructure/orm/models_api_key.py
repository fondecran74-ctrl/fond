"""API key models."""
import uuid
import secrets
from django.db import models
from apps.core.abstract_models import AuditableModel


class APIKey(AuditableModel):
    """API key for service-to-service authentication."""
    name = models.CharField(max_length=100)
    key_prefix = models.CharField(max_length=8, unique=True)
    key_hash = models.CharField(max_length=255)
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="api_keys")
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    scopes = models.JSONField(default=list)

    class Meta:
        db_table = "iam_api_keys"
        ordering = ["-created_at"]

    @classmethod
    def generate_key(cls) -> tuple[str, str, str]:
        """Generate a new API key and return (full_key, prefix, hash)."""
        key = secrets.token_urlsafe(48)
        prefix = key[:8]
        import hashlib
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        return key, prefix, key_hash
