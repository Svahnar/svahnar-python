# Agents

Types:

```python
from svahnar.types import (
    AgentCreateResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentDeleteResponse,
    AgentBulkDeleteResponse,
    AgentGetResponse,
    AgentRunResponse,
    AgentValidateResponse,
)
```

Methods:

- <code title="post /v1/agents/create">client.agents.<a href="./src/svahnar/resources/agents.py">create</a>(\*\*<a href="src/svahnar/types/agent_create_params.py">params</a>) -> <a href="./src/svahnar/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="put /v1/agents/update">client.agents.<a href="./src/svahnar/resources/agents.py">update</a>(\*\*<a href="src/svahnar/types/agent_update_params.py">params</a>) -> <a href="./src/svahnar/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v1/agents/list-agents">client.agents.<a href="./src/svahnar/resources/agents.py">list</a>(\*\*<a href="src/svahnar/types/agent_list_params.py">params</a>) -> <a href="./src/svahnar/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/delete">client.agents.<a href="./src/svahnar/resources/agents.py">delete</a>(\*\*<a href="src/svahnar/types/agent_delete_params.py">params</a>) -> <a href="./src/svahnar/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="delete /v1/agents/bulk-delete">client.agents.<a href="./src/svahnar/resources/agents.py">bulk_delete</a>(\*\*<a href="src/svahnar/types/agent_bulk_delete_params.py">params</a>) -> <a href="./src/svahnar/types/agent_bulk_delete_response.py">AgentBulkDeleteResponse</a></code>
- <code title="get /v1/agents/download-agent/{agent_id}">client.agents.<a href="./src/svahnar/resources/agents.py">download</a>(agent_id) -> object</code>
- <code title="get /v1/agents/get-agent/{agent_id}">client.agents.<a href="./src/svahnar/resources/agents.py">get</a>(agent_id) -> <a href="./src/svahnar/types/agent_get_response.py">AgentGetResponse</a></code>
- <code title="post /v1/agents/run">client.agents.<a href="./src/svahnar/resources/agents.py">run</a>(\*\*<a href="src/svahnar/types/agent_run_params.py">params</a>) -> <a href="./src/svahnar/types/agent_run_response.py">AgentRunResponse</a></code>
- <code title="post /v1/agents/test">client.agents.<a href="./src/svahnar/resources/agents.py">test</a>(\*\*<a href="src/svahnar/types/agent_test_params.py">params</a>) -> object</code>
- <code title="post /v1/agents/validate">client.agents.<a href="./src/svahnar/resources/agents.py">validate</a>(\*\*<a href="src/svahnar/types/agent_validate_params.py">params</a>) -> <a href="./src/svahnar/types/agent_validate_response.py">AgentValidateResponse</a></code>

# Auth

Methods:

- <code title="post /v1/auth/login">client.auth.<a href="./src/svahnar/resources/auth.py">login</a>(\*\*<a href="src/svahnar/types/auth_login_params.py">params</a>) -> object</code>
