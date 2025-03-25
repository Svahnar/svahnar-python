# Agents

Types:

```python
from SVAHNAR.types import AgentRunResponse, AgentTestResponse
```

Methods:

- <code title="post /v1/agents/run">client.agents.<a href="./src/SVAHNAR/resources/agents.py">run</a>(\*\*<a href="src/SVAHNAR/types/agent_run_params.py">params</a>) -> <a href="./src/SVAHNAR/types/agent_run_response.py">object</a></code>
- <code title="post /v1/agents/test">client.agents.<a href="./src/SVAHNAR/resources/agents.py">test</a>(\*\*<a href="src/SVAHNAR/types/agent_test_params.py">params</a>) -> <a href="./src/SVAHNAR/types/agent_test_response.py">object</a></code>

# Health

Types:

```python
from SVAHNAR.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/SVAHNAR/resources/health.py">check</a>() -> <a href="./src/SVAHNAR/types/health_check_response.py">object</a></code>
