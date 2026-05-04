"""ScholarshipAward views."""
from rest_framework import viewsets, permissions
from apps.finance.infrastructure.orm.models import ScholarshipAward
from ..serializers.scholarshipaward_serializers import ScholarshipAwardSerializer


class ScholarshipAwardViewSet(viewsets.ModelViewSet):
    serializer_class = ScholarshipAwardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ScholarshipAward.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
