"""URLs for Facilities & Services."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.building_views import BuildingViewSet
from .views.room_views import RoomViewSet
from .views.roombooking_views import RoomBookingViewSet
from .views.maintenancerequest_views import MaintenanceRequestViewSet

app_name = "facilities"
router = DefaultRouter()
router.register(r"buildings", BuildingViewSet, basename="buildings")
router.register(r"rooms", RoomViewSet, basename="rooms")
router.register(r"roombookings", RoomBookingViewSet, basename="roombookings")
router.register(r"maintenancerequests", MaintenanceRequestViewSet, basename="maintenancerequests")

urlpatterns = [path("", include(router.urls))]
