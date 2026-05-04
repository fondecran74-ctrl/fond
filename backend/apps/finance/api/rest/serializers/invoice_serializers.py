"""Invoice serializer."""
from rest_framework import serializers
from apps.finance.infrastructure.orm.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
