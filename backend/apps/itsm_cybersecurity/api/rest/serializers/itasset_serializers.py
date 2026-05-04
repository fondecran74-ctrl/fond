"""ITAsset serializer."""
from rest_framework import serializers
from apps.itsm_cybersecurity.infrastructure.orm.models import ITAsset


class ITAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITAsset
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
