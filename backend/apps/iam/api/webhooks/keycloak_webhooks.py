"""Keycloak webhook handlers."""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import structlog

logger = structlog.get_logger(__name__)


@api_view(["POST"])
@permission_classes([AllowAny])
def keycloak_event_webhook(request):
    """Handle Keycloak admin events (user creation, role changes, etc.)."""
    event = request.data
    logger.info("keycloak_event", event_type=event.get("type"), resource=event.get("resourcePath"))
    return Response({"status": "received"})
