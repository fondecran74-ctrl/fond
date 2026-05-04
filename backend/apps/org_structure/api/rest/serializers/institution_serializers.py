"""Institution serializer."""
from rest_framework import serializers
from apps.org_structure.infrastructure.orm.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
