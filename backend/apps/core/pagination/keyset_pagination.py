"""Keyset-based pagination for large datasets."""
from rest_framework.pagination import CursorPagination


class KeysetPagination(CursorPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200
    ordering = "id"
