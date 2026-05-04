"""InternshipConvention serializer."""
from rest_framework import serializers
from apps.internships_alternance.infrastructure.orm.models import InternshipConvention


class InternshipConventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipConvention
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
