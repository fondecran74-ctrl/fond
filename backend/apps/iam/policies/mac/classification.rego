package ems.mac

import rego.v1

default allow := false

classification_levels := {
    "PUBLIC": 0,
    "INTERNAL": 1,
    "CONFIDENTIAL": 2,
    "SECRET": 3,
    "TOP_SECRET": 4
}

# No Read Up: subject clearance >= resource classification
allow if {
    subject_level := classification_levels[input.subject.clearance]
    resource_level := classification_levels[input.resource.classification]
    subject_level >= resource_level
}
