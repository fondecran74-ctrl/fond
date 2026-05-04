"""URLs for ITSM & Cybersecurity."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.ticket_views import TicketViewSet
from .views.incident_views import IncidentViewSet
from .views.itasset_views import ITAssetViewSet

app_name = "itsm"
router = DefaultRouter()
router.register(r"tickets", TicketViewSet, basename="tickets")
router.register(r"incidents", IncidentViewSet, basename="incidents")
router.register(r"itassets", ITAssetViewSet, basename="itassets")

urlpatterns = [path("", include(router.urls))]
