"""Governance models."""
import uuid
from django.db import models
from apps.core.abstract_models import AuditableModel, InstitutionScopedModel


class Board(InstitutionScopedModel):
    """Board of directors or governing body."""
    name = models.CharField(max_length=200)
    board_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    chairperson = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="chaired_boards")
    secretary = models.ForeignKey("iam.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="board_secretary")

    class Meta:
        db_table = "gov_boards"


class BoardMember(AuditableModel):
    """Membership in a board."""
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey("iam.User", on_delete=models.CASCADE, related_name="board_memberships")
    role_in_board = models.CharField(max_length=100)
    starts_at = models.DateField()
    ends_at = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "gov_board_members"
        constraints = [models.UniqueConstraint(fields=["board", "user"], name="unique_board_member")]


class Committee(InstitutionScopedModel):
    """Committee within the institution."""
    name = models.CharField(max_length=200)
    committee_type = models.CharField(max_length=50)
    parent_board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True, related_name="committees")
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "gov_committees"


class Decision(InstitutionScopedModel):
    """Formal decision made by a board or committee."""
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        SUBMITTED = "SUBMITTED", "Submitted"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"
        IMPLEMENTED = "IMPLEMENTED", "Implemented"

    reference = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True, related_name="decisions")
    committee = models.ForeignKey(Committee, on_delete=models.SET_NULL, null=True, blank=True, related_name="decisions")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    decision_date = models.DateField(null=True, blank=True)
    implementation_deadline = models.DateField(null=True, blank=True)
    votes_for = models.PositiveIntegerField(default=0)
    votes_against = models.PositiveIntegerField(default=0)
    votes_abstain = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "gov_decisions"
        ordering = ["-decision_date"]


class Resolution(InstitutionScopedModel):
    """Formal resolution."""
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name="resolutions")
    text = models.TextField()
    effective_date = models.DateField()

    class Meta:
        db_table = "gov_resolutions"
