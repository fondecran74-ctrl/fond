"""Ticket views."""
from rest_framework import viewsets, permissions
from apps.itsm_cybersecurity.infrastructure.orm.models import Ticket
from ..serializers.ticket_serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
