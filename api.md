# Agents

Types:

```python
from svahnar.types import AgentRunResponse, AgentTestResponse
```

Methods:

- <code title="post /v1/agents/run">client.agents.<a href="./src/svahnar/resources/agents.py">run</a>(\*\*<a href="src/svahnar/types/agent_run_params.py">params</a>) -> <a href="./src/svahnar/types/agent_run_response.py">object</a></code>
- <code title="post /v1/agents/test">client.agents.<a href="./src/svahnar/resources/agents.py">test</a>(\*\*<a href="src/svahnar/types/agent_test_params.py">params</a>) -> <a href="./src/svahnar/types/agent_test_response.py">object</a></code>

# Health

Types:

```python
from svahnar.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/svahnar/resources/health.py">check</a>() -> <a href="./src/svahnar/types/health_check_response.py">object</a></code>
