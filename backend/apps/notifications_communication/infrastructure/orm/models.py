"""Notification and communication models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Notification(AuditableModel):
    """User notification."""
    class Channel(models.TextChoices):
        IN_APP = "IN_APP", "In-app"
        EMAIL = "EMAIL", "Email"
        SMS = "SMS", "SMS"
        PUSH = "PUSH", "Push notification"

    recipient = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=200)
    body = models.TextField()
    channel = models.CharField(max_length=10, choices=Channel.choices, default=Channel.IN_APP)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    action_url = models.URLField(blank=True, default="")
    notification_type = models.CharField(max_length=50, default="INFO")

    class Meta:
        db_table = "notif_notifications"
        indexes = [models.Index(fields=["recipient", "is_read", "-created_at"])]


class Announcement(AuditableModel):
    """Institution-wide announcement."""
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="announcements")
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="announcements")
    published_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    target_roles = models.JSONField(default=list)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = "notif_announcements"


class EmailTemplate(AuditableModel):
    """Email template."""
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=300)
    body_html = models.TextField()
    body_text = models.TextField()
    variables = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "notif_email_templates"
