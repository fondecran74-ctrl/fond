"""Cache health check."""
from django.core.cache import cache


def check_cache() -> dict:
    """Check Redis cache connectivity."""
    try:
        cache.set("health_check", "ok", 10)
        value = cache.get("health_check")
        if value == "ok":
            return {"name": "cache", "status": "healthy"}
        return {"name": "cache", "status": "unhealthy", "error": "Cache read/write failed"}
    except Exception as e:
        return {"name": "cache", "status": "unhealthy", "error": str(e)}
