"""Environment variable configuration utilities."""
import environ

env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SETTINGS_MODULE=(str, "config.settings.development"),
)
