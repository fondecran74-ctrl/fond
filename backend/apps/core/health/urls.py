"""Health check URLs."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.health_check, name="health"),
    path("live/", views.liveness, name="liveness"),
    path("ready/", views.readiness, name="readiness"),
]
