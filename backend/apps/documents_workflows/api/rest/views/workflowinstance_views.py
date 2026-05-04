"""WorkflowInstance views."""
from rest_framework import viewsets, permissions
from apps.documents_workflows.infrastructure.orm.models import WorkflowInstance
from ..serializers.workflowinstance_serializers import WorkflowInstanceSerializer


class WorkflowInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowInstanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkflowInstance.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
