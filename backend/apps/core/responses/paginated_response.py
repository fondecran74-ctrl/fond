"""Paginated response wrapper."""
from rest_framework.pagination import CursorPagination


class PaginatedResponse:
    """Helper for building paginated responses."""

    @staticmethod
    def build(paginator: CursorPagination, queryset, serializer_class, request):
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = serializer_class(page, many=True, context={"request": request})
            return paginator.get_paginated_response(serializer.data)
        serializer = serializer_class(queryset, many=True, context={"request": request})
        return serializer.data
