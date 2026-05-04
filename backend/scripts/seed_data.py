"""Seed initial data."""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from apps.iam.infrastructure.orm.models_user import User
from apps.iam.infrastructure.orm.models_role import Role

print("Seeding roles...")
roles = [
    ("Super Administrateur", "SUPER_ADMIN", 0),
    ("Président CA", "PRESIDENT_CA", 1),
    ("Directeur Général", "DG", 1),
    ("Recteur", "RECTEUR", 1),
    ("Vice-Président", "VP", 1),
    ("Directeur d'établissement", "DIR_ETAB", 2),
    ("Doyen", "DOYEN", 2),
    ("DSI", "DSI", 3),
    ("DAF", "DAF", 3),
    ("DRH", "DRH", 3),
    ("Chef de département", "CHEF_DEPT", 4),
    ("Agent administratif", "AGENT_ADMIN", 5),
    ("Enseignant", "ENSEIGNANT", 6),
    ("Chercheur", "CHERCHEUR", 6),
    ("Étudiant", "ETUDIANT", 7),
    ("Candidat", "CANDIDAT", 7),
    ("Parent", "PARENT", 7),
    ("Alumni", "ALUMNI", 7),
]

for name, code, level in roles:
    Role.objects.get_or_create(name=name, code=code, defaults={"level": level, "is_system": True})

print(f"Seeded {len(roles)} roles.")
