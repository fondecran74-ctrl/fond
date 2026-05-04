"""Security tests."""
from apps.core.security.sanitizers import sanitize_html, sanitize_text


class TestSanitizers:
    def test_sanitize_html_removes_scripts(self):
        result = sanitize_html("<script>alert('xss')</script>Hello")
        assert "<script>" not in result
        assert "Hello" in result

    def test_sanitize_text_strips_all_html(self):
        result = sanitize_text("<b>Bold</b> text")
        assert result == "Bold text"
