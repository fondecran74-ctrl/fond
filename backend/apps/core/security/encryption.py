"""Field-level encryption utilities using Fernet."""
from cryptography.fernet import Fernet
from django.conf import settings


def get_encryption_key() -> bytes:
    """Retrieve the encryption key from Vault or settings."""
    key = getattr(settings, "FIELD_ENCRYPTION_KEY", None)
    if not key:
        key = Fernet.generate_key().decode()
    return key.encode() if isinstance(key, str) else key


def encrypt_value(value: str) -> str:
    """Encrypt a string value."""
    f = Fernet(get_encryption_key())
    return f.encrypt(value.encode()).decode()


def decrypt_value(token: str) -> str:
    """Decrypt an encrypted value."""
    f = Fernet(get_encryption_key())
    return f.decrypt(token.encode()).decode()
