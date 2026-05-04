"""Error code constants for EMS platform."""

# Authentication
AUTH_INVALID_CREDENTIALS = "auth.invalid_credentials"
AUTH_ACCOUNT_LOCKED = "auth.account_locked"
AUTH_MFA_REQUIRED = "auth.mfa_required"
AUTH_SESSION_EXPIRED = "auth.session_expired"
AUTH_IDENTITY_NOT_PROVISIONED = "auth.identity_not_provisioned"

# Authorization
AUTHZ_INSUFFICIENT_CLEARANCE = "authz.insufficient_clearance"
AUTHZ_ROLE_CONFLICT = "authz.role_conflict"
AUTHZ_SOD_VIOLATION = "authz.sod_violation"
AUTHZ_SCOPE_VIOLATION = "authz.scope_violation"

# Validation
VALIDATION_REQUIRED_FIELD = "validation.required_field"
VALIDATION_INVALID_FORMAT = "validation.invalid_format"
VALIDATION_UNIQUE_CONSTRAINT = "validation.unique_constraint"

# Business rules
RULE_ENROLLMENT_CLOSED = "rule.enrollment_closed"
RULE_PREREQUISITE_NOT_MET = "rule.prerequisite_not_met"
RULE_MAX_CREDITS_EXCEEDED = "rule.max_credits_exceeded"
RULE_GRADE_LOCKED = "rule.grade_locked"
