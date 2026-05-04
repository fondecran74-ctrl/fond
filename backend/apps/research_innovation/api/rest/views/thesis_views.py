"""Thesis views."""
from rest_framework import viewsets, permissions
from apps.research_innovation.infrastructure.orm.models import Thesis
from ..serializers.thesis_serializers import ThesisSerializer


class ThesisViewSet(viewsets.ModelViewSet):
    serializer_class = ThesisSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Thesis.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
