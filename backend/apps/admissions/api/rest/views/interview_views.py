"""Interview views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import Interview
from ..serializers.interview_serializers import InterviewSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interview.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
