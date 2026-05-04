"""URLs for Internships & Alternance."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.internshipoffer_views import InternshipOfferViewSet
from .views.internshipconvention_views import InternshipConventionViewSet
from .views.internshipevaluation_views import InternshipEvaluationViewSet

app_name = "internships"
router = DefaultRouter()
router.register(r"internshipoffers", InternshipOfferViewSet, basename="internshipoffers")
router.register(r"internshipconventions", InternshipConventionViewSet, basename="internshipconventions")
router.register(r"internshipevaluations", InternshipEvaluationViewSet, basename="internshipevaluations")

urlpatterns = [path("", include(router.urls))]
