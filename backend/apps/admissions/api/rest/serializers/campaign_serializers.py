"""Campaign serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
