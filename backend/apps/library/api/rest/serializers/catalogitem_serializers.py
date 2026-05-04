"""CatalogItem serializer."""
from rest_framework import serializers
from apps.library.infrastructure.orm.models import CatalogItem


class CatalogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
