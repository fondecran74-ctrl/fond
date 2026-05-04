"""Rbac Policy policy."""


class RbacPolicyPolicy:
    """Policy definition for rbac policy."""

    @staticmethod
    def evaluate(subject: dict, resource: dict, action: str) -> bool:
        return True
