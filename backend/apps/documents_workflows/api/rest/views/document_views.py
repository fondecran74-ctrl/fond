"""Document views."""
from rest_framework import viewsets, permissions
from apps.documents_workflows.infrastructure.orm.models import Document
from ..serializers.document_serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Document.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
