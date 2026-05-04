"""Transfer serializer."""
from rest_framework import serializers
from apps.student_lifecycle.infrastructure.orm.models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
