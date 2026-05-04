"""Token utilities for JWT handling."""
import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings


def create_access_token(user_id: str, roles: list[str], expires_minutes: int = 15) -> str:
    """Create a JWT access token."""
    payload = {
        "sub": user_id,
        "roles": roles,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_minutes),
        "type": "access",
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def create_refresh_token(user_id: str, expires_days: int = 7) -> str:
    """Create a JWT refresh token."""
    payload = {
        "sub": user_id,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(days=expires_days),
        "type": "refresh",
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> dict:
    """Decode and verify a JWT token."""
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
