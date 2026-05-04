"""Payment views."""
from rest_framework import viewsets, permissions
from apps.finance.infrastructure.orm.models import Payment
from ..serializers.payment_serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
