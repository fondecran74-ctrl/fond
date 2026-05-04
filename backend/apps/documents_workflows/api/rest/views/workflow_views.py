"""Workflow views."""
from rest_framework import viewsets, permissions
from apps.documents_workflows.infrastructure.orm.models import Workflow
from ..serializers.workflow_serializers import WorkflowSerializer


class WorkflowViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workflow.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
