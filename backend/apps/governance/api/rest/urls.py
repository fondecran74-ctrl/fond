"""Governance URLs."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.board_views import BoardViewSet
from .views.committee_views import CommitteeViewSet
from .views.decision_views import DecisionViewSet
from .views.resolution_views import ResolutionViewSet

app_name = "governance"
router = DefaultRouter()
router.register(r"boards", BoardViewSet, basename="boards")
router.register(r"committees", CommitteeViewSet, basename="committees")
router.register(r"decisions", DecisionViewSet, basename="decisions")
router.register(r"resolutions", ResolutionViewSet, basename="resolutions")

urlpatterns = [path("", include(router.urls))]
