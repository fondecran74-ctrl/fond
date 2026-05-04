"""Signature views."""
from rest_framework import viewsets, permissions
from apps.documents_workflows.infrastructure.orm.models import Signature
from ..serializers.signature_serializers import SignatureSerializer


class SignatureViewSet(viewsets.ModelViewSet):
    serializer_class = SignatureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Signature.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
