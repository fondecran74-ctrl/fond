package ems.break_glass

import rego.v1

default allow := false

allow if {
    input.request.status == "APPROVED"
    input.request.approver != input.request.requester
    time.now_ns() < input.request.expires_at_ns
}
