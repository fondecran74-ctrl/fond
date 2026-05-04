"""AccessReviewSerializer serializer."""
from rest_framework import serializers
from apps.iam.infrastructure.orm.models_access_review import AccessReview


class AccessReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessReview
        fields = ["id", "name", "description", "status", "reviewer", "starts_at", "ends_at"]
        read_only_fields = ["id", "created_at"]
