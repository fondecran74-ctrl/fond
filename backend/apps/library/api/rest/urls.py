"""URLs for Library."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.catalogitem_views import CatalogItemViewSet
from .views.loan_views import LoanViewSet
from .views.reservation_views import ReservationViewSet

app_name = "library"
router = DefaultRouter()
router.register(r"catalogitems", CatalogItemViewSet, basename="catalogitems")
router.register(r"loans", LoanViewSet, basename="loans")
router.register(r"reservations", ReservationViewSet, basename="reservations")

urlpatterns = [path("", include(router.urls))]
