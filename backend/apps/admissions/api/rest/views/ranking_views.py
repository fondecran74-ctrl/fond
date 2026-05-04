"""Ranking views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import Ranking
from ..serializers.ranking_serializers import RankingSerializer


class RankingViewSet(viewsets.ModelViewSet):
    serializer_class = RankingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ranking.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
