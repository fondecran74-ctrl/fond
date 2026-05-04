"""Base Django settings for EMS platform."""
import os
from pathlib import Path

from config.env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env.read_env(os.path.join(BASE_DIR, ".env"), overwrite=False)

SECRET_KEY = env("DJANGO_SECRET_KEY", default="insecure-dev-key-change-in-production")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "corsheaders",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "auditlog",
    "guardian",
    "django_celery_beat",
    "django_celery_results",
    "channels",
]

LOCAL_APPS = [
    "apps.core",
    "apps.iam",
    "apps.governance",
    "apps.org_structure",
    "apps.academic_catalog",
    "apps.admissions",
    "apps.student_lifecycle",
    "apps.assessments",
    "apps.internships_alternance",
    "apps.international_relations",
    "apps.research_innovation",
    "apps.finance",
    "apps.hr",
    "apps.quality_compliance_risk",
    "apps.facilities_services",
    "apps.library",
    "apps.campus_health",
    "apps.itsm_cybersecurity",
    "apps.documents_workflows",
    "apps.notifications_communication",
    "apps.analytics_bi",
    "apps.ai_services",
    "apps.audit_traceability",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.correlation_id.CorrelationIdMiddleware",
    "apps.core.middleware.request_context.RequestContextMiddleware",
    "apps.core.middleware.tenant_context.TenantContextMiddleware",
    "apps.core.middleware.security_headers.SecurityHeadersMiddleware",
    "apps.core.middleware.audit_middleware.AuditMiddleware",
    "apps.core.middleware.request_logging.RequestLoggingMiddleware",
    "apps.core.middleware.rate_limiting.RateLimitingMiddleware",
    "auditlog.middleware.AuditlogMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "config.asgi.application"
WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="ems"),
        "USER": env("DB_USER", default="ems_user"),
        "PASSWORD": env("DB_PASSWORD", default="ems_password"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env.int("DB_PORT", default=5432),
        "OPTIONS": {
            "options": "-c search_path=public",
        },
    }
}

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://localhost:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# Auth
AUTH_USER_MODEL = "iam.User"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "apps.core.pagination.cursor_pagination.StandardCursorPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/hour",
        "user": "1000/hour",
    },
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "EXCEPTION_HANDLER": "apps.core.exceptions.handlers.custom_exception_handler",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
}

# Celery
CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL", default="redis://localhost:6379/0")],
        },
    },
}

# CORS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:3000"])
CORS_ALLOW_CREDENTIALS = True

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Keycloak
KEYCLOAK_URL = env("KEYCLOAK_URL", default="http://localhost:8080")
KEYCLOAK_REALM = env("KEYCLOAK_REALM", default="ems")
KEYCLOAK_CLIENT_ID = env("KEYCLOAK_CLIENT_ID", default="ems-backend")
KEYCLOAK_CLIENT_SECRET = env("KEYCLOAK_CLIENT_SECRET", default="")

# Kafka
KAFKA_BOOTSTRAP_SERVERS = env("KAFKA_BOOTSTRAP_SERVERS", default="localhost:9092")

# ClickHouse
CLICKHOUSE_URL = env("CLICKHOUSE_URL", default="http://localhost:8123")
CLICKHOUSE_DB = env("CLICKHOUSE_DB", default="ems_analytics")

# Vault
VAULT_ADDR = env("VAULT_ADDR", default="http://localhost:8200")
VAULT_TOKEN = env("VAULT_TOKEN", default="dev-root-token")

# MinIO
MINIO_ENDPOINT = env("MINIO_ENDPOINT", default="localhost:9100")
MINIO_ACCESS_KEY = env("MINIO_ACCESS_KEY", default="minio_admin")
MINIO_SECRET_KEY = env("MINIO_SECRET_KEY", default="minio_password")
MINIO_BUCKET = env("MINIO_BUCKET", default="ems-documents")
