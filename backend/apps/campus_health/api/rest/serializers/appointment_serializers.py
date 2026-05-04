"""Appointment serializer."""
from rest_framework import serializers
from apps.campus_health.infrastructure.orm.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
