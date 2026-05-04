"""URLs for Student Lifecycle."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.enrollment_views import EnrollmentViewSet
from .views.registration_views import RegistrationViewSet
from .views.academicrecord_views import AcademicRecordViewSet
from .views.graduation_views import GraduationViewSet
from .views.transfer_views import TransferViewSet

app_name = "student_lifecycle"
router = DefaultRouter()
router.register(r"enrollments", EnrollmentViewSet, basename="enrollments")
router.register(r"registrations", RegistrationViewSet, basename="registrations")
router.register(r"academicrecords", AcademicRecordViewSet, basename="academicrecords")
router.register(r"graduations", GraduationViewSet, basename="graduations")
router.register(r"transfers", TransferViewSet, basename="transfers")

urlpatterns = [path("", include(router.urls))]
