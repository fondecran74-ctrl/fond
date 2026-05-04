package ems.sod

import rego.v1

conflicts := [
    {"role_a": "PAYMENT_ISSUER", "role_b": "PAYMENT_APPROVER"},
    {"role_a": "EXAM_CORRECTOR", "role_b": "JURY_MEMBER_SAME_EXAM"},
    {"role_a": "BUDGET_CREATOR", "role_b": "BUDGET_APPROVER"},
]

default has_conflict := false

has_conflict if {
    some conflict in conflicts
    conflict.role_a in input.user.roles
    conflict.role_b in input.user.roles
}
