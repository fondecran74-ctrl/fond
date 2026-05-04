"""URLs for Audit & Traceability."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.auditlog_views import AuditLogViewSet
from .views.policydecision_views import PolicyDecisionViewSet
from .views.complianceevidence_views import ComplianceEvidenceViewSet

app_name = "audit"
router = DefaultRouter()
router.register(r"auditlogs", AuditLogViewSet, basename="auditlogs")
router.register(r"policydecisions", PolicyDecisionViewSet, basename="policydecisions")
router.register(r"complianceevidences", ComplianceEvidenceViewSet, basename="complianceevidences")

urlpatterns = [path("", include(router.urls))]
