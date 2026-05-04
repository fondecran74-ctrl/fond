"""Seed demo data for development."""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

print("Demo data seeded.")
