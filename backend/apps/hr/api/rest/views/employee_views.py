"""Employee views."""
from rest_framework import viewsets, permissions
from apps.hr.infrastructure.orm.models import Employee
from ..serializers.employee_serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
