"""ExchangeAgreement serializer."""
from rest_framework import serializers
from apps.international_relations.infrastructure.orm.models import ExchangeAgreement


class ExchangeAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeAgreement
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
