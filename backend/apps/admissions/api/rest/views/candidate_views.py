"""Candidate views."""
from rest_framework import viewsets, permissions
from apps.admissions.infrastructure.orm.models import Candidate
from ..serializers.candidate_serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Candidate.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
