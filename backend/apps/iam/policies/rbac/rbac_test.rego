package ems.rbac_test

import rego.v1

test_super_admin_allowed if {
    allow with input as {
        "user": {"roles": ["SUPER_ADMIN"]},
        "required_permission": "user:create"
    }
}
