"""InternshipOffer views."""
from rest_framework import viewsets, permissions
from apps.internships_alternance.infrastructure.orm.models import InternshipOffer
from ..serializers.internshipoffer_serializers import InternshipOfferSerializer


class InternshipOfferViewSet(viewsets.ModelViewSet):
    serializer_class = InternshipOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InternshipOffer.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
