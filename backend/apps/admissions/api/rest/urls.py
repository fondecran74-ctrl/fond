"""URLs for Admissions."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.campaign_views import CampaignViewSet
from .views.candidate_views import CandidateViewSet
from .views.application_views import ApplicationViewSet
from .views.admissioncommittee_views import AdmissionCommitteeViewSet
from .views.interview_views import InterviewViewSet
from .views.ranking_views import RankingViewSet

app_name = "admissions"
router = DefaultRouter()
router.register(r"campaigns", CampaignViewSet, basename="campaigns")
router.register(r"candidates", CandidateViewSet, basename="candidates")
router.register(r"applications", ApplicationViewSet, basename="applications")
router.register(r"admissioncommittees", AdmissionCommitteeViewSet, basename="admissioncommittees")
router.register(r"interviews", InterviewViewSet, basename="interviews")
router.register(r"rankings", RankingViewSet, basename="rankings")

urlpatterns = [path("", include(router.urls))]
