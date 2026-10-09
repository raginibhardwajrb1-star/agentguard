
from agentguard.policy import Policy, authorize

policy = Policy(
    allowed_actions=frozenset({
        "read_record",
        "update_record",
    }),
    allowed_resources=frozenset({
        "customer:123",
    }),
    approval_required=frozenset({
        "change_permissions",
    }),
)

requests = [
    ("read_record", "customer:123"),
    ("export_database", "customer:all"),
    ("change_permissions", "user:123"),
    ("read_record", "customer:all"),
]

for action, resource in requests:
    decision = authorize(action, resource, policy)
    print(
        f"{decision.status:6} | "
        f"{action:20} | "
        f"{resource:15} | "
        f"{decision.reason}"
    )