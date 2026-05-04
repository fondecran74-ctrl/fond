"""Abac Policy policy."""


class AbacPolicyPolicy:
    """Policy definition for abac policy."""

    @staticmethod
    def evaluate(subject: dict, resource: dict, action: str) -> bool:
        return True
