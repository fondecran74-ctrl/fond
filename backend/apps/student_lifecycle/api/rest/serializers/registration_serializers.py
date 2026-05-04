"""Registration serializer."""
from rest_framework import serializers
from apps.student_lifecycle.infrastructure.orm.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
