"""Custom managers for IAM models."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Custom user manager — no self-registration."""

    def create_user(self, email: str, username: str, password: str | None = None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, username: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", "SYSTEM_ADMIN")
        extra_fields.setdefault("account_status", "ACTIVE")
        return self.create_user(email, username, password, **extra_fields)
