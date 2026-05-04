"""PartnerInstitution serializer."""
from rest_framework import serializers
from apps.international_relations.infrastructure.orm.models import PartnerInstitution


class PartnerInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerInstitution
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
