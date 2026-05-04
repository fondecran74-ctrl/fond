"""Transfer views."""
from rest_framework import viewsets, permissions
from apps.student_lifecycle.infrastructure.orm.models import Transfer
from ..serializers.transfer_serializers import TransferSerializer


class TransferViewSet(viewsets.ModelViewSet):
    serializer_class = TransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transfer.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
