"""Application views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import Application
from ..serializers.application_serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
