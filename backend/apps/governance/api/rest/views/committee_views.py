"""Committee views."""
from rest_framework import viewsets, permissions
from apps.governance.infrastructure.orm.models import Committee
from ..serializers.committee_serializers import CommitteeSerializer


class CommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = CommitteeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Committee.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
