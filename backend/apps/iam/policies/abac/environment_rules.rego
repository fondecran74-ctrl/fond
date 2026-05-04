package ems.abac.environment

import rego.v1

default time_allowed := true

time_allowed if {
    input.environment.hour >= 6
    input.environment.hour <= 23
}
