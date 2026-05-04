"""Core signals for the EMS platform."""
from django.dispatch import Signal

# Audit signals
entity_created = Signal()
entity_updated = Signal()
entity_deleted = Signal()

# Authorization signals
access_granted = Signal()
access_denied = Signal()
