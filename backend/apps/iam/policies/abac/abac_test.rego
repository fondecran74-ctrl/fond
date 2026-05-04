package ems.abac_test

import rego.v1

test_public_resource_allowed if {
    allow with input as {
        "subject": {"clearance_level": 0},
        "resource": {"classification": "PUBLIC"},
        "action": "read"
    }
}
