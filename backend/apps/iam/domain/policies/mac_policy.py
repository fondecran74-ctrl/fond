"""Mac Policy policy."""


class MacPolicyPolicy:
    """Policy definition for mac policy."""

    @staticmethod
    def evaluate(subject: dict, resource: dict, action: str) -> bool:
        return True
