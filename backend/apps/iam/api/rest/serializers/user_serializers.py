"""UserSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "user_type", "account_status", "institution", "provisioning_method", "created_at"]
        read_only_fields = ["id", "created_at"]
