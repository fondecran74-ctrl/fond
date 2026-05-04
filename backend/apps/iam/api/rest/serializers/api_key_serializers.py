"""APIKeySerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_api_key import APIKey


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ["id", "name", "key_prefix", "user", "is_active", "expires_at", "last_used_at", "scopes"]
        read_only_fields = ["id", "created_at"]
