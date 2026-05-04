"""Permission views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_permission import Permission
from ..serializers.permission_serializers import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """Permission management viewset."""
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Permission.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
