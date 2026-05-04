package ems.rbac

import rego.v1

default allow := false

allow if {
    some role in input.user.roles
    some perm in data.role_permissions[role]
    perm == input.required_permission
}

allow if {
    some role in input.user.roles
    some parent in data.role_hierarchy[role]
    some perm in data.role_permissions[parent]
    perm == input.required_permission
}
