"""Faculty serializer."""
from rest_framework import serializers
from apps.org_structure.infrastructure.orm.models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
