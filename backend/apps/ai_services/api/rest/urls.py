"""URLs for AI Services."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.chatsession_views import ChatSessionViewSet
from .views.chatmessage_views import ChatMessageViewSet
from .views.recommendation_views import RecommendationViewSet

app_name = "ai"
router = DefaultRouter()
router.register(r"chatsessions", ChatSessionViewSet, basename="chatsessions")
router.register(r"chatmessages", ChatMessageViewSet, basename="chatmessages")
router.register(r"recommendations", RecommendationViewSet, basename="recommendations")

urlpatterns = [path("", include(router.urls))]
