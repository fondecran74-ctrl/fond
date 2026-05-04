"""CatalogItem views."""
from rest_framework import viewsets, permissions
from apps.library.infrastructure.orm.models import CatalogItem
from ..serializers.catalogitem_serializers import CatalogItemSerializer


class CatalogItemViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CatalogItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
