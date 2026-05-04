package ems.abac

import rego.v1

default allow := false

allow if {
    input.subject.clearance_level >= input.resource.classification_level
    input.subject.department == input.resource.department
}

allow if {
    input.action == "read"
    input.resource.classification == "PUBLIC"
}
