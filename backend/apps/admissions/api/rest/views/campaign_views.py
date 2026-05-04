"""Campaign views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import Campaign
from ..serializers.campaign_serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Campaign.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
