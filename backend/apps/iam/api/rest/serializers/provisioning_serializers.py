"""UserSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "user_type", "provisioning_method", "provisioning_source"]
        read_only_fields = ["id", "created_at"]
