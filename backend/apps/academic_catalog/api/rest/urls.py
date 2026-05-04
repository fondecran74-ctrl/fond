"""URLs for Academic Catalog."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.program_views import ProgramViewSet
from .views.course_views import CourseViewSet
from .views.academicyear_views import AcademicYearViewSet
from .views.semester_views import SemesterViewSet
from .views.prerequisite_views import PrerequisiteViewSet
from .views.learningoutcome_views import LearningOutcomeViewSet

app_name = "academic_catalog"
router = DefaultRouter()
router.register(r"programs", ProgramViewSet, basename="programs")
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"academicyears", AcademicYearViewSet, basename="academicyears")
router.register(r"semesters", SemesterViewSet, basename="semesters")
router.register(r"prerequisites", PrerequisiteViewSet, basename="prerequisites")
router.register(r"learningoutcomes", LearningOutcomeViewSet, basename="learningoutcomes")

urlpatterns = [path("", include(router.urls))]
