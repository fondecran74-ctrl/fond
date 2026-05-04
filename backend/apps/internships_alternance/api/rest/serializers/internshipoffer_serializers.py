"""InternshipOffer serializer."""
from rest_framework import serializers
from apps.internships_alternance.infrastructure.orm.models import InternshipOffer


class InternshipOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipOffer
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
