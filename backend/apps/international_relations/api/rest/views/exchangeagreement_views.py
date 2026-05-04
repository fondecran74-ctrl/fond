"""ExchangeAgreement views."""
from rest_framework import viewsets, permissions
from apps.international_relations.infrastructure.orm.models import ExchangeAgreement
from ..serializers.exchangeagreement_serializers import ExchangeAgreementSerializer


class ExchangeAgreementViewSet(viewsets.ModelViewSet):
    serializer_class = ExchangeAgreementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ExchangeAgreement.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
