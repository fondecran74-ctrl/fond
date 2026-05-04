"""Department views."""
from rest_framework import viewsets, permissions
from apps.org_structure.infrastructure.orm.models import Department
from ..serializers.department_serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Department.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
