"""Payment serializer."""
from rest_framework import serializers
from apps.finance.infrastructure.orm.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
