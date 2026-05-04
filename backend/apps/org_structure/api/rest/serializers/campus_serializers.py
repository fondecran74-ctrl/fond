"""Campus serializer."""
from rest_framework import serializers
from apps.org_structure.infrastructure.orm.models import Campus


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
