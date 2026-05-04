"""API Key views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_api_key import APIKey
from ..serializers.api_key_serializers import APIKeySerializer


class APIKeyViewSet(viewsets.ModelViewSet):
    """API Key management viewset."""
    serializer_class = APIKeySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return APIKey.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
