"""AdmissionCommittee serializer."""
from rest_framework import serializers
from apps.admissions.infrastructure.orm.models import AdmissionCommittee


class AdmissionCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionCommittee
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
