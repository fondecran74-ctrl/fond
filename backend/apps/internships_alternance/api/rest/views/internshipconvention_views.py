"""InternshipConvention views."""
from rest_framework import viewsets, permissions
from apps.internships_alternance.infrastructure.orm.models import InternshipConvention
from ..serializers.internshipconvention_serializers import InternshipConventionSerializer


class InternshipConventionViewSet(viewsets.ModelViewSet):
    serializer_class = InternshipConventionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InternshipConvention.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
