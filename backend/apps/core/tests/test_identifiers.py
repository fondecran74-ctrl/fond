"""Identifier tests."""
from apps.core.utils.identifiers import generate_uuid, generate_short_id, generate_student_id


class TestIdentifiers:
    def test_uuid_format(self):
        uid = generate_uuid()
        assert len(uid) == 36

    def test_short_id_with_prefix(self):
        sid = generate_short_id(prefix="STU")
        assert sid.startswith("STU")

    def test_student_id_format(self):
        sid = generate_student_id("UNI", 2025, 42)
        assert sid == "UNI202500042"
