"""SessionSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_session import UserSession


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ["id", "user", "ip_address", "is_active", "last_activity", "expires_at"]
        read_only_fields = ["id", "created_at"]
