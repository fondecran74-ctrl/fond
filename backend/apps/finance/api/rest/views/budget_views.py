"""Budget views."""
from rest_framework import viewsets, permissions
from apps.finance.infrastructure.orm.models import Budget
from ..serializers.budget_serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
