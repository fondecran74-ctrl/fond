"""Board views."""
from rest_framework import viewsets, permissions
from apps.governance.infrastructure.orm.models import Board
from ..serializers.board_serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
