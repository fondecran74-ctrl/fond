"""ResearchProject views."""
from rest_framework import viewsets, permissions
from apps.research_innovation.infrastructure.orm.models import ResearchProject
from ..serializers.researchproject_serializers import ResearchProjectSerializer


class ResearchProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ResearchProject.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
