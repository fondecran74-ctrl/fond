"""Signature serializer."""
from rest_framework import serializers
from apps.documents_workflows.infrastructure.orm.models import Signature


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
