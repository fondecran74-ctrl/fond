"""Publication serializer."""
from rest_framework import serializers
from apps.research_innovation.infrastructure.orm.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
