"""Sod Policy policy."""


class SodPolicyPolicy:
    """Policy definition for sod policy."""

    @staticmethod
    def evaluate(subject: dict, resource: dict, action: str) -> bool:
        return True
