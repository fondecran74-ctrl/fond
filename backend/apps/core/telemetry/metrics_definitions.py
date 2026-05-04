"""Application-specific metric definitions."""
from prometheus_client import Counter, Gauge

auth_attempts_total = Counter(
    "ems_auth_attempts_total",
    "Total authentication attempts",
    ["result"],
)

active_sessions = Gauge(
    "ems_active_sessions",
    "Number of active user sessions",
)

policy_decisions_total = Counter(
    "ems_policy_decisions_total",
    "Total authorization decisions",
    ["decision", "policy_type"],
)
