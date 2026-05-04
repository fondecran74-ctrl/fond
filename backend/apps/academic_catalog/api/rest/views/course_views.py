"""Course views."""
from rest_framework import viewsets, permissions
from apps.academic_catalog.infrastructure.orm.models import Course
from ..serializers.course_serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
