package ems.mac.compartments

import rego.v1

compartments := ["FINANCE", "HR", "ACADEMIC", "RESEARCH", "HEALTH", "LEGAL", "SECURITY"]

default has_compartment_access := false

has_compartment_access if {
    every c in input.resource.compartments {
        c in input.subject.compartments
    }
}
