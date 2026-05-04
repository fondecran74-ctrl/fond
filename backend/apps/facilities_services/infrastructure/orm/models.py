"""Facilities models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Building(AuditableModel):
    """Campus building."""
    campus = models.ForeignKey("org_structure.Campus", on_delete=models.CASCADE, related_name="buildings")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    floors = models.PositiveIntegerField(default=1)
    address = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "fac_buildings"


class Room(AuditableModel):
    """Room within a building."""
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="rooms")
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    room_type = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()
    floor = models.IntegerField()
    has_projector = models.BooleanField(default=False)
    has_video_conference = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "fac_rooms"


class RoomBooking(AuditableModel):
    """Room reservation."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    booked_by = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="room_bookings")
    title = models.CharField(max_length=200)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    status = models.CharField(max_length=20, default="CONFIRMED")
    recurrence = models.CharField(max_length=20, blank=True, default="")

    class Meta:
        db_table = "fac_room_bookings"


class MaintenanceRequest(AuditableModel):
    """Maintenance request for facilities."""
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, default="MEDIUM")
    status = models.CharField(max_length=20, default="OPEN")
    reported_by = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="maintenance_assignments")

    class Meta:
        db_table = "fac_maintenance"
