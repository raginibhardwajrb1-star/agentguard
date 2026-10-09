# AgentGuard

**A policy enforcement and runtime security framework for autonomous AI agents.**

AgentGuard is an early-stage project exploring how to make autonomous AI agents safer by controlling which actions they can perform, which resources they can access, and when human approval is required.

## Why AgentGuard?

AI agents can call tools, access data, and execute actions with limited human supervision. Without appropriate safeguards, an agent may perform an unauthorized or potentially harmful operation.

AgentGuard aims to introduce a security layer that evaluates an agent's proposed actions before execution.

## Current Features

* **Policy-based authorization:** Define permitted actions and resources.
* **Explicit deny-by-default behavior:** Block actions that are not authorized.
* **Human-review decisions:** Flag sensitive actions that require approval.
* **Automated tests:** Verify authorization behavior and policy enforcement decisions.

## Authorization Decisions

| Decision | Meaning                                   |
| -------- | ----------------------------------------- |
| `ALLOW`  | The action and resource are authorized.   |
| `BLOCK`  | The action or resource is not authorized. |
| `REVIEW` | The action requires human approval.       |

## Architecture

The current prototype evaluates requests through a policy authorization function.

```text
AI Agent Request
       |
       v
 Action and Resource
       |
       v
 Policy Evaluation
       |
       v
 +-------------------+
 | ALLOW / BLOCK /   |
 | REVIEW            |
 +-------------------+
       |
       v
 Decision Returned
```

**Current limitation:** The prototype evaluates authorization requests but does not yet intercept or enforce real tool execution.

## Project Structure

```text
agentguard/
├── agentguard/
│   ├── __init__.py
│   └── policy.py
├── tests/
│   └── test_policy.py
├── demo.py
├── README.md
└── .gitignore
```

## Getting Started

### Requirements

* Python 3.10 or later
* Git
* pip

### 1. Clone the repository

```bash
git clone https://github.com/raginibhardwajrb1-star/agentguard.git
cd agentguard
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the test dependency

```bash
python -m pip install pytest
```

### 4. Run the demonstration

```bash
python demo.py
```

### 5. Run the tests

```bash
python -m pytest -v
```

## Example

```python
from agentguard.policy import Policy, authorize

policy = Policy(
    allowed_actions=frozenset({"read_record", "write_record"}),
    allowed_resources=frozenset({"customer:123"}),
    approval_required=frozenset({"change_permissions"}),
)

decision = authorize("read_record", "customer:123", policy)

print(decision.status)
# ALLOW
```

## Roadmap

### Implemented

* [x] Initial policy model
* [x] Action and resource authorization
* [x] Human-review decision state
* [x] Automated policy tests
* [x] Command-line demonstration

### Planned

* [ ] Runtime interception of agent tool calls
* [ ] Explicit human-approval workflow
* [ ] Audit logging and decision history
* [ ] Integration with frameworks such as LangGraph
* [ ] Adversarial and policy-bypass testing
* [ ] Recovery and containment mechanisms for unsafe actions

## Project Status

AgentGuard is an experimental prototype. The roadmap describes planned work, not functionality that is already implemented.

## Contributing

Contributions, feedback, and ideas are welcome. Please open an issue to discuss proposed improvements before submitting significant changes.

## License

No license has been added yet. Until a license is selected, the repository should be treated as having no explicit permission for reuse or redistribution.
