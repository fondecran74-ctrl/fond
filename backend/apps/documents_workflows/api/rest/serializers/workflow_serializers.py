"""Workflow serializer."""
from rest_framework import serializers
from apps.documents_workflows.infrastructure.orm.models import Workflow


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
