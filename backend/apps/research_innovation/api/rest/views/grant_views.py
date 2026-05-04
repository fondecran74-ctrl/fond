"""Grant views."""
from rest_framework import viewsets, permissions
from apps.research_innovation.infrastructure.orm.models import Grant
from ..serializers.grant_serializers import GrantSerializer


class GrantViewSet(viewsets.ModelViewSet):
    serializer_class = GrantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Grant.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
