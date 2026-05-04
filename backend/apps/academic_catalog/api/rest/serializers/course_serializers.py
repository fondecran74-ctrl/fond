"""Course serializer."""
from rest_framework import serializers
from apps.academic_catalog.infrastructure.orm.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
