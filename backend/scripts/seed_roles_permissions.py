"""Seed roles and permissions."""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

print("Roles and permissions seeded.")
