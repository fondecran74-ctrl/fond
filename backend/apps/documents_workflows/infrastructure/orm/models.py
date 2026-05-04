"""Documents and workflows models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel


class Document(AuditableModel):
    """Document in the GED."""
    title = models.CharField(max_length=300)
    document_type = models.CharField(max_length=50)
    file_url = models.URLField()
    original_filename = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=100)
    file_size = models.PositiveBigIntegerField()
    version = models.PositiveIntegerField(default=1)
    classification = models.CharField(max_length=20, default="INTERNAL")
    owner = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="owned_documents")
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="documents")

    class Meta:
        db_table = "doc_documents"


class Workflow(AuditableModel):
    """Workflow definition."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    steps = models.JSONField(default=list)
    institution = models.ForeignKey("org_structure.Institution", on_delete=models.CASCADE, related_name="workflows")

    class Meta:
        db_table = "doc_workflows"


class WorkflowInstance(AuditableModel):
    """Instance of a running workflow."""
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name="instances")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True, related_name="workflow_instances")
    current_step = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="IN_PROGRESS")
    initiated_by = models.ForeignKey("iam.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "doc_workflow_instances"


class Signature(AuditableModel):
    """Electronic signature."""
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="signatures")
    signer = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    signed_at = models.DateTimeField()
    signature_hash = models.CharField(max_length=255)
    certificate_info = models.JSONField(default=dict)
    is_valid = models.BooleanField(default=True)

    class Meta:
        db_table = "doc_signatures"
