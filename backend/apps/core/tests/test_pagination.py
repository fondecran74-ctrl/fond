"""Pagination tests."""


class TestCursorPagination:
    def test_default_page_size(self):
        from apps.core.pagination.cursor_pagination import StandardCursorPagination
        paginator = StandardCursorPagination()
        assert paginator.page_size == 25
