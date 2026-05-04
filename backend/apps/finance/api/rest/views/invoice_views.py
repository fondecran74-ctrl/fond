"""Invoice views."""
from rest_framework import viewsets, permissions
from apps.finance.infrastructure.orm.models import Invoice
from ..serializers.invoice_serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
