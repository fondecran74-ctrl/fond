"""URLs for Finance."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.budget_views import BudgetViewSet
from .views.invoice_views import InvoiceViewSet
from .views.payment_views import PaymentViewSet
from .views.scholarship_views import ScholarshipViewSet
from .views.scholarshipaward_views import ScholarshipAwardViewSet

app_name = "finance"
router = DefaultRouter()
router.register(r"budgets", BudgetViewSet, basename="budgets")
router.register(r"invoices", InvoiceViewSet, basename="invoices")
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(r"scholarships", ScholarshipViewSet, basename="scholarships")
router.register(r"scholarshipawards", ScholarshipAwardViewSet, basename="scholarshipawards")

urlpatterns = [path("", include(router.urls))]
