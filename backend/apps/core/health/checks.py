"""Health check orchestrator."""
from .checks_database import check_database
from .checks_cache import check_cache
from .checks_kafka import check_kafka


def run_all_checks() -> list[dict]:
    """Run all health checks and return results."""
    return [
        check_database(),
        check_cache(),
        check_kafka(),
    ]
