"""Registration views."""
from rest_framework import viewsets, permissions
from apps.student_lifecycle.infrastructure.orm.models import Registration
from ..serializers.registration_serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
