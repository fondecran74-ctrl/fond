"""Incident serializer."""
from rest_framework import serializers
from apps.itsm_cybersecurity.infrastructure.orm.models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
