"""RoomBooking serializer."""
from rest_framework import serializers
from apps.facilities_services.infrastructure.orm.models import RoomBooking


class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
