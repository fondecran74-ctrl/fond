"""LeaveRequest views."""
from rest_framework import viewsets, permissions
from apps.hr.infrastructure.orm.models import LeaveRequest
from ..serializers.leaverequest_serializers import LeaveRequestSerializer


class LeaveRequestViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
