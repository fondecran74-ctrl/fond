"""ScholarshipAward serializer."""
from rest_framework import serializers
from apps.finance.infrastructure.orm.models import ScholarshipAward


class ScholarshipAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipAward
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
