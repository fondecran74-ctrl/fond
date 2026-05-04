"""Provisioning webhook handlers."""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def external_provisioning_webhook(request):
    """Handle external system provisioning events."""
    return Response({"status": "received"})
