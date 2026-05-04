"""API v1 URL configuration."""
from django.urls import include, path

app_name = "api_v1"

urlpatterns = [
    path("iam/", include("apps.iam.api.rest.urls", namespace="iam")),
    path("governance/", include("apps.governance.api.rest.urls", namespace="governance")),
    path("org/", include("apps.org_structure.api.rest.urls", namespace="org_structure")),
    path("catalog/", include("apps.academic_catalog.api.rest.urls", namespace="academic_catalog")),
    path("admissions/", include("apps.admissions.api.rest.urls", namespace="admissions")),
    path("students/", include("apps.student_lifecycle.api.rest.urls", namespace="student_lifecycle")),
    path("assessments/", include("apps.assessments.api.rest.urls", namespace="assessments")),
    path("internships/", include("apps.internships_alternance.api.rest.urls", namespace="internships")),
    path("international/", include("apps.international_relations.api.rest.urls", namespace="international")),
    path("research/", include("apps.research_innovation.api.rest.urls", namespace="research")),
    path("finance/", include("apps.finance.api.rest.urls", namespace="finance")),
    path("hr/", include("apps.hr.api.rest.urls", namespace="hr")),
    path("quality/", include("apps.quality_compliance_risk.api.rest.urls", namespace="quality")),
    path("facilities/", include("apps.facilities_services.api.rest.urls", namespace="facilities")),
    path("library/", include("apps.library.api.rest.urls", namespace="library")),
    path("health-services/", include("apps.campus_health.api.rest.urls", namespace="campus_health")),
    path("itsm/", include("apps.itsm_cybersecurity.api.rest.urls", namespace="itsm")),
    path("documents/", include("apps.documents_workflows.api.rest.urls", namespace="documents")),
    path("notifications/", include("apps.notifications_communication.api.rest.urls", namespace="notifications")),
    path("analytics/", include("apps.analytics_bi.api.rest.urls", namespace="analytics")),
    path("ai/", include("apps.ai_services.api.rest.urls", namespace="ai")),
    path("audit/", include("apps.audit_traceability.api.rest.urls", namespace="audit")),
]
