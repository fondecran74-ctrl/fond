"""MFASettingSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_mfa import MFASetting


class MFASettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFASetting
        fields = ["id", "user", "mfa_type", "is_enabled", "is_primary", "verified_at"]
        read_only_fields = ["id", "created_at"]
