"""Health check views."""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .checks import run_all_checks


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    """Return health status of all subsystems."""
    results = run_all_checks()
    all_healthy = all(c["status"] == "healthy" for c in results)
    return Response(
        {"status": "healthy" if all_healthy else "degraded", "checks": results},
        status=200 if all_healthy else 503,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def liveness(request):
    """Kubernetes liveness probe."""
    return Response({"status": "alive"})


@api_view(["GET"])
@permission_classes([AllowAny])
def readiness(request):
    """Kubernetes readiness probe."""
    results = run_all_checks()
    all_healthy = all(c["status"] == "healthy" for c in results)
    return Response(
        {"status": "ready" if all_healthy else "not_ready"},
        status=200 if all_healthy else 503,
    )
