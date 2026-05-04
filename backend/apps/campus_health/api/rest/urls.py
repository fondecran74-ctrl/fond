"""URLs for Campus Health."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.medicalrecord_views import MedicalRecordViewSet
from .views.appointment_views import AppointmentViewSet

app_name = "campus_health"
router = DefaultRouter()
router.register(r"medicalrecords", MedicalRecordViewSet, basename="medicalrecords")
router.register(r"appointments", AppointmentViewSet, basename="appointments")

urlpatterns = [path("", include(router.urls))]
