"""Rate limiting middleware."""
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse, JsonResponse


class RateLimitingMiddleware:
    """Simple rate limiting using Redis."""

    RATE_LIMIT = 1000
    WINDOW = 3600

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not request.path.startswith("/api/"):
            return self.get_response(request)

        client_ip = self._get_client_ip(request)
        cache_key = f"ratelimit:{client_ip}"
        request_count = cache.get(cache_key, 0)

        if request_count >= self.RATE_LIMIT:
            return JsonResponse(
                {"error": "Rate limit exceeded", "retry_after": self.WINDOW},
                status=429,
            )

        cache.set(cache_key, request_count + 1, self.WINDOW)
        response = self.get_response(request)
        response["X-RateLimit-Limit"] = str(self.RATE_LIMIT)
        response["X-RateLimit-Remaining"] = str(max(0, self.RATE_LIMIT - request_count - 1))
        return response

    def _get_client_ip(self, request: HttpRequest) -> str:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "unknown")
