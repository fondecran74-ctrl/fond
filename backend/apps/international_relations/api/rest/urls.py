"""URLs for International Relations."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.partnerinstitution_views import PartnerInstitutionViewSet
from .views.exchangeagreement_views import ExchangeAgreementViewSet
from .views.mobilityapplication_views import MobilityApplicationViewSet

app_name = "international"
router = DefaultRouter()
router.register(r"partnerinstitutions", PartnerInstitutionViewSet, basename="partnerinstitutions")
router.register(r"exchangeagreements", ExchangeAgreementViewSet, basename="exchangeagreements")
router.register(r"mobilityapplications", MobilityApplicationViewSet, basename="mobilityapplications")

urlpatterns = [path("", include(router.urls))]
