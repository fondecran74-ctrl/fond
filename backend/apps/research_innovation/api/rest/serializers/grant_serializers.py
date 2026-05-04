"""Grant serializer."""
from rest_framework import serializers
from apps.research_innovation.infrastructure.orm.models import Grant


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
