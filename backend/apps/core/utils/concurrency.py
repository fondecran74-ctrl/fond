"""Concurrency utilities."""
from functools import wraps
from django.db import transaction


def atomic_operation(func):
    """Decorator to wrap a function in a database transaction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with transaction.atomic():
            return func(*args, **kwargs)
    return wrapper
