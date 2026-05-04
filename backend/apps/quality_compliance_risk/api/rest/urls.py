"""URLs for Quality, Compliance & Risk."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.accreditation_views import AccreditationViewSet
from .views.qualityaudit_views import QualityAuditViewSet
from .views.riskregister_views import RiskRegisterViewSet
from .views.kpi_views import KPIViewSet

app_name = "quality"
router = DefaultRouter()
router.register(r"accreditations", AccreditationViewSet, basename="accreditations")
router.register(r"qualityaudits", QualityAuditViewSet, basename="qualityaudits")
router.register(r"riskregisters", RiskRegisterViewSet, basename="riskregisters")
router.register(r"kpis", KPIViewSet, basename="kpis")

urlpatterns = [path("", include(router.urls))]
