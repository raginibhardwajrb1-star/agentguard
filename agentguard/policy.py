
from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class Decision:
    status: str
    reason: str


@dataclass(frozen=True)
class Policy:
    allowed_actions: FrozenSet[str]
    allowed_resources: FrozenSet[str]
    approval_required: FrozenSet[str]


def authorize(
    action: str,
    resource: str,
    policy: Policy,
) -> Decision:
    """Evaluate a tool request before its execution."""

    if action in policy.approval_required:
        return Decision(
            "REVIEW",
            "This action requires explicit human approval.",
        )

    if action not in policy.allowed_actions:
        return Decision(
            "BLOCK",
            "Action is not explicitly authorized.",
        )

    if resource not in policy.allowed_resources:
        return Decision(
            "BLOCK",
            "Resource is not explicitly authorized.",
        )

    return Decision(
        "ALLOW",
        "Action and resource are authorized by policy.",
    )