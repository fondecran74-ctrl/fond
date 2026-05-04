"""Application serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
