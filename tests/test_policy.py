import pytest

from agentguard.policy import Policy, authorize


@pytest.fixture
def policy():
    return Policy(
        allowed_actions=frozenset({"read_record", "write_record"}),
        allowed_resources=frozenset({"customer:123"}),
        approval_required=frozenset({"change_permissions"}),
    )


def test_authorized_action_is_allowed(policy):
    decision = authorize("read_record", "customer:123", policy)
    assert decision.status == "ALLOW"


def test_unauthorized_action_is_blocked(policy):
    decision = authorize("export_database", "customer:123", policy)
    assert decision.status == "BLOCK"
    assert decision.reason == "Action is not explicitly authorized."


def test_unauthorized_resource_is_blocked(policy):
    decision = authorize("read_record", "customer:all", policy)
    assert decision.status == "BLOCK"
    assert decision.reason == "Resource is not explicitly authorized."


def test_sensitive_action_requires_review(policy):
    decision = authorize("change_permissions", "customer:123", policy)
    assert decision.status == "REVIEW"
    assert decision.reason == "This action requires explicit human approval."


def test_review_takes_precedence_over_action_and_resource(policy):
    decision = authorize("change_permissions", "customer:all", policy)
    assert decision.status == "REVIEW"


def test_write_to_authorized_resource_is_allowed(policy):
    decision = authorize("write_record", "customer:123", policy)
    assert decision.status == "ALLOW"


