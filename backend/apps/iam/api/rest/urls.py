"""IAM API URLs."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_views import UserViewSet
from .views.role_views import RoleViewSet
from .views.permission_views import PermissionViewSet
from .views.session_views import SessionViewSet
from .views.delegation_views import DelegationViewSet
from .views.audit_views import AuditViewSet
from .views.provisioning_views import ProvisioningViewSet
from .views.api_key_views import APIKeyViewSet
from .views.access_review_views import AccessReviewViewSet

app_name = "iam"

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"roles", RoleViewSet, basename="roles")
router.register(r"permissions", PermissionViewSet, basename="permissions")
router.register(r"sessions", SessionViewSet, basename="sessions")
router.register(r"delegations", DelegationViewSet, basename="delegations")
router.register(r"audit", AuditViewSet, basename="audit")
router.register(r"provisioning", ProvisioningViewSet, basename="provisioning")
router.register(r"api-keys", APIKeyViewSet, basename="api-keys")
router.register(r"access-reviews", AccessReviewViewSet, basename="access-reviews")

urlpatterns = [
    path("", include(router.urls)),
]
