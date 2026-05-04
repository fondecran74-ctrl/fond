"""URLs for Analytics & BI."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.dashboard_views import DashboardViewSet
from .views.report_views import ReportViewSet
from .views.dataexport_views import DataExportViewSet

app_name = "analytics"
router = DefaultRouter()
router.register(r"dashboards", DashboardViewSet, basename="dashboards")
router.register(r"reports", ReportViewSet, basename="reports")
router.register(r"dataexports", DataExportViewSet, basename="dataexports")

urlpatterns = [path("", include(router.urls))]
