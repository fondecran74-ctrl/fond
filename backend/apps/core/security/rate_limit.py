"""Rate limit decorators and utilities."""
from functools import wraps
from django.core.cache import cache
from apps.core.responses.error_response import ErrorResponse


def rate_limit(max_requests: int = 10, window: int = 60):
    """Decorator to rate-limit a view."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            key = f"rate:{request.path}:{request.META.get('REMOTE_ADDR')}"
            count = cache.get(key, 0)
            if count >= max_requests:
                return ErrorResponse("Rate limit exceeded", code="rate_limit", status=429)
            cache.set(key, count + 1, window)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
