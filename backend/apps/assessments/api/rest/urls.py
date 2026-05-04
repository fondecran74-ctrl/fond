"""URLs for Assessments & Grading."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.examination_views import ExaminationViewSet
from .views.grade_views import GradeViewSet
from .views.gradeappeal_views import GradeAppealViewSet
from .views.jurysession_views import JurySessionViewSet
from .views.transcript_views import TranscriptViewSet

app_name = "assessments"
router = DefaultRouter()
router.register(r"examinations", ExaminationViewSet, basename="examinations")
router.register(r"grades", GradeViewSet, basename="grades")
router.register(r"gradeappeals", GradeAppealViewSet, basename="gradeappeals")
router.register(r"jurysessions", JurySessionViewSet, basename="jurysessions")
router.register(r"transcripts", TranscriptViewSet, basename="transcripts")

urlpatterns = [path("", include(router.urls))]
