"""RoleSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name", "code", "description", "level", "parent", "is_system", "is_active"]
        read_only_fields = ["id", "created_at"]
