"""Transcript views."""
from rest_framework import viewsets, permissions
from apps.assessments.infrastructure.orm.models import Transcript
from ..serializers.transcript_serializers import TranscriptSerializer


class TranscriptViewSet(viewsets.ModelViewSet):
    serializer_class = TranscriptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transcript.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
