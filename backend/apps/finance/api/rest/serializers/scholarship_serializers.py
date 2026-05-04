"""Scholarship serializer."""
from rest_framework import serializers
from apps.finance.infrastructure.orm.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
