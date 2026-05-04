"""PermissionSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_permission import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", "resource", "action", "code", "description", "category"]
        read_only_fields = ["id", "created_at"]
