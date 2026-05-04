"""Prerequisite serializer."""
from rest_framework import serializers
from apps.academic_catalog.infrastructure.orm.models import Prerequisite


class PrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
