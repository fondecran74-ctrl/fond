"""URLs for Human Resources."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.employee_views import EmployeeViewSet
from .views.contract_views import ContractViewSet
from .views.leaverequest_views import LeaveRequestViewSet
from .views.performanceevaluation_views import PerformanceEvaluationViewSet

app_name = "hr"
router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"contracts", ContractViewSet, basename="contracts")
router.register(r"leaverequests", LeaveRequestViewSet, basename="leaverequests")
router.register(r"performanceevaluations", PerformanceEvaluationViewSet, basename="performanceevaluations")

urlpatterns = [path("", include(router.urls))]
