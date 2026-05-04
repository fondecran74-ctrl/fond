"""WorkflowInstance serializer."""
from rest_framework import serializers
from apps.documents_workflows.infrastructure.orm.models import WorkflowInstance


class WorkflowInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowInstance
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
