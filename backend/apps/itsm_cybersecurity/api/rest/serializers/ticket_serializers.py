"""Ticket serializer."""
from rest_framework import serializers
from apps.itsm_cybersecurity.infrastructure.orm.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
