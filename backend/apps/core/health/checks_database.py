"""Database health check."""
from django.db import connection


def check_database() -> dict:
    """Check database connectivity."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return {"name": "database", "status": "healthy"}
    except Exception as e:
        return {"name": "database", "status": "unhealthy", "error": str(e)}
