"""Loan views."""
from rest_framework import viewsets, permissions
from apps.library.infrastructure.orm.models import Loan
from ..serializers.loan_serializers import LoanSerializer


class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Loan.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
