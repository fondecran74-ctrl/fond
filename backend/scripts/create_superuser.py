"""Create initial superuser."""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from apps.iam.infrastructure.orm.models_user import User

if not User.objects.filter(email="admin@ems.local").exists():
    User.objects.create_superuser(
        email="admin@ems.local",
        username="admin",
        password="AdminEMS2025!",
        first_name="Admin",
        last_name="System",
    )
    print("Superuser created.")
else:
    print("Superuser already exists.")
