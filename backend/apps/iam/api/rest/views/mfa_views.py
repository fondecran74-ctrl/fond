"""MFA Setting views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_mfa import MFASetting
from ..serializers.mfa_serializers import MFASettingSerializer


class MFAViewSet(viewsets.ModelViewSet):
    """MFA Setting management viewset."""
    serializer_class = MFASettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MFASetting.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
