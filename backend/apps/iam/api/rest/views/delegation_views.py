"""Delegation views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_delegation import Delegation
from ..serializers.delegation_serializers import DelegationSerializer


class DelegationViewSet(viewsets.ModelViewSet):
    """Delegation management viewset."""
    serializer_class = DelegationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Delegation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
