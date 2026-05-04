"""Import Users script."""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

print("import_users completed.")
