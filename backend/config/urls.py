"""Root URL configuration."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("config.urls_api_v1")),
    path("health/", include("apps.core.health.urls")),
]
