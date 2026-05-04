"""Recommendation views."""
from rest_framework import viewsets, permissions
from apps.ai_services.infrastructure.orm.models import Recommendation
from ..serializers.recommendation_serializers import RecommendationSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recommendation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
