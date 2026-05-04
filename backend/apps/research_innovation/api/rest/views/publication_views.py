"""Publication views."""
from rest_framework import viewsets, permissions
from apps.research_innovation.infrastructure.orm.models import Publication
from ..serializers.publication_serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Publication.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
