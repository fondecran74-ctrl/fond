"""Key management utilities using HashiCorp Vault."""
from django.conf import settings


class KeyManager:
    """Manage encryption keys via Vault transit engine."""

    def __init__(self):
        self.vault_addr = settings.VAULT_ADDR
        self.vault_token = settings.VAULT_TOKEN

    def rotate_key(self, key_name: str) -> bool:
        """Rotate an encryption key in Vault."""
        try:
            import hvac
            client = hvac.Client(url=self.vault_addr, token=self.vault_token)
            client.secrets.transit.rotate_encryption_key(name=key_name)
            return True
        except Exception:
            return False

    def encrypt(self, key_name: str, plaintext: str) -> str:
        """Encrypt data using Vault transit engine."""
        import hvac
        import base64
        client = hvac.Client(url=self.vault_addr, token=self.vault_token)
        encoded = base64.b64encode(plaintext.encode()).decode()
        result = client.secrets.transit.encrypt_data(name=key_name, plaintext=encoded)
        return result["data"]["ciphertext"]

    def decrypt(self, key_name: str, ciphertext: str) -> str:
        """Decrypt data using Vault transit engine."""
        import hvac
        import base64
        client = hvac.Client(url=self.vault_addr, token=self.vault_token)
        result = client.secrets.transit.decrypt_data(name=key_name, ciphertext=ciphertext)
        return base64.b64decode(result["data"]["plaintext"]).decode()
