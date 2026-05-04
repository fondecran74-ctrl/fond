"""Contract views."""
from rest_framework import viewsets, permissions
from apps.hr.infrastructure.orm.models import Contract
from ..serializers.contract_serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
