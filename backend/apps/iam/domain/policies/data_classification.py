"""Data Classification policy."""


class DataClassificationPolicy:
    """Policy definition for data classification."""

    @staticmethod
    def evaluate(subject: dict, resource: dict, action: str) -> bool:
        return True
