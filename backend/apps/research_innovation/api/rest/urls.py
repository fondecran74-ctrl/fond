"""URLs for Research & Innovation."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.researchproject_views import ResearchProjectViewSet
from .views.publication_views import PublicationViewSet
from .views.grant_views import GrantViewSet
from .views.thesis_views import ThesisViewSet

app_name = "research"
router = DefaultRouter()
router.register(r"researchprojects", ResearchProjectViewSet, basename="researchprojects")
router.register(r"publications", PublicationViewSet, basename="publications")
router.register(r"grants", GrantViewSet, basename="grants")
router.register(r"thesiss", ThesisViewSet, basename="thesiss")

urlpatterns = [path("", include(router.urls))]
