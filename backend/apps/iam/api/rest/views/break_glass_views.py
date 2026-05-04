"""Break Glass Request views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_break_glass import BreakGlassRequest
from ..serializers.break_glass_serializers import BreakGlassRequestSerializer


class BreakGlassViewSet(viewsets.ModelViewSet):
    """Break Glass Request management viewset."""
    serializer_class = BreakGlassRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BreakGlassRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
