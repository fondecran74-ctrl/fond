"""Document serializer."""
from rest_framework import serializers
from apps.documents_workflows.infrastructure.orm.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
