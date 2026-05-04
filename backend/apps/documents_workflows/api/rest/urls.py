"""URLs for Documents & Workflows."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.document_views import DocumentViewSet
from .views.workflow_views import WorkflowViewSet
from .views.workflowinstance_views import WorkflowInstanceViewSet
from .views.signature_views import SignatureViewSet

app_name = "documents"
router = DefaultRouter()
router.register(r"documents", DocumentViewSet, basename="documents")
router.register(r"workflows", WorkflowViewSet, basename="workflows")
router.register(r"workflowinstances", WorkflowInstanceViewSet, basename="workflowinstances")
router.register(r"signatures", SignatureViewSet, basename="signatures")

urlpatterns = [path("", include(router.urls))]
