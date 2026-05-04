"""Appointment views."""
from rest_framework import viewsets, permissions
from apps.campus_health.infrastructure.orm.models import Appointment
from ..serializers.appointment_serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
