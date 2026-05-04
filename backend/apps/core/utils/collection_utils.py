"""Collection utility functions."""
from typing import TypeVar, Sequence

T = TypeVar("T")


def chunk(items: Sequence[T], size: int) -> list[list[T]]:
    """Split a sequence into chunks of the given size."""
    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def flatten(nested: list[list[T]]) -> list[T]:
    """Flatten a list of lists."""
    return [item for sublist in nested for item in sublist]
