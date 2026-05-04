"""Feature flag configuration."""
from django.conf import settings


class FeatureFlags:
    """Feature flags for the EMS platform."""

    MFA_ENABLED = getattr(settings, "FEATURE_MFA_ENABLED", True)
    KAFKA_ENABLED = getattr(settings, "FEATURE_KAFKA_ENABLED", True)
    AI_SERVICES_ENABLED = getattr(settings, "FEATURE_AI_SERVICES_ENABLED", False)
    BREAK_GLASS_ENABLED = getattr(settings, "FEATURE_BREAK_GLASS_ENABLED", True)
    RLS_ENABLED = getattr(settings, "FEATURE_RLS_ENABLED", True)


flags = FeatureFlags()
