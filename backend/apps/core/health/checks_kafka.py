"""Kafka health check."""
from django.conf import settings


def check_kafka() -> dict:
    """Check Kafka connectivity."""
    try:
        from confluent_kafka.admin import AdminClient
        admin = AdminClient({"bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS})
        metadata = admin.list_topics(timeout=5)
        return {"name": "kafka", "status": "healthy", "brokers": len(metadata.brokers)}
    except Exception as e:
        return {"name": "kafka", "status": "unhealthy", "error": str(e)}
