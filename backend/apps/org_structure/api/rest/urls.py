"""Org Structure URLs."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.institution_views import InstitutionViewSet
from .views.campus_views import CampusViewSet
from .views.faculty_views import FacultyViewSet
from .views.department_views import DepartmentViewSet
from .views.laboratory_views import LaboratoryViewSet

app_name = "org_structure"
router = DefaultRouter()
router.register(r"institutions", InstitutionViewSet, basename="institutions")
router.register(r"campuses", CampusViewSet, basename="campuses")
router.register(r"faculties", FacultyViewSet, basename="faculties")
router.register(r"departments", DepartmentViewSet, basename="departments")
router.register(r"laboratories", LaboratoryViewSet, basename="laboratories")

urlpatterns = [path("", include(router.urls))]
