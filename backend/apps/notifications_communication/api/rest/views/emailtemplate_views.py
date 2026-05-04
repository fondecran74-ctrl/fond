"""EmailTemplate views."""
from rest_framework import viewsets, permissions
from apps.notifications_communication.infrastructure.orm.models import EmailTemplate
from ..serializers.emailtemplate_serializers import EmailTemplateSerializer


class EmailTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = EmailTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EmailTemplate.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
