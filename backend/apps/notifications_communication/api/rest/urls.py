"""URLs for Notifications & Communication."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.notification_views import NotificationViewSet
from .views.announcement_views import AnnouncementViewSet
from .views.emailtemplate_views import EmailTemplateViewSet

app_name = "notifications"
router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename="notifications")
router.register(r"announcements", AnnouncementViewSet, basename="announcements")
router.register(r"emailtemplates", EmailTemplateViewSet, basename="emailtemplates")

urlpatterns = [path("", include(router.urls))]
