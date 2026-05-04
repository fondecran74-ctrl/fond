"""ITAsset views."""
from rest_framework import viewsets, permissions
from apps.itsm_cybersecurity.infrastructure.orm.models import ITAsset
from ..serializers.itasset_serializers import ITAssetSerializer


class ITAssetViewSet(viewsets.ModelViewSet):
    serializer_class = ITAssetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ITAsset.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
