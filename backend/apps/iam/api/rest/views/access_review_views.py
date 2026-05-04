"""Access Review views."""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from apps.iam.infrastructure.orm.models_access_review import AccessReview
from ..serializers.access_review_serializers import AccessReviewSerializer


class AccessReviewViewSet(viewsets.ModelViewSet):
    """Access Review management viewset."""
    serializer_class = AccessReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AccessReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
