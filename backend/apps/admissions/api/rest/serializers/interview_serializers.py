"""Interview serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import Interview


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
