# Agents

Types:

```python
from svahnar.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentListResponse,
    AgentDeleteResponse,
    AgentBulkDeleteResponse,
    AgentReconfigureResponse,
    AgentRunResponse,
    AgentUpdateInfoResponse,
    AgentValidateResponse,
)
```

Methods:

- <code title="post /v1/agents/create">client.agents.<a href="./src/svahnar/resources/agents.py">create</a>(\*\*<a href="src/svahnar/types/agent_create_params.py">params</a>) -> <a href="./src/svahnar/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v1/agents/get-agent/{agent_id}">client.agents.<a href="./src/svahnar/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/svahnar/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="get /v1/agents/list-agents">client.agents.<a href="./src/svahnar/resources/agents.py">list</a>(\*\*<a href="src/svahnar/types/agent_list_params.py">params</a>) -> <a href="./src/svahnar/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/delete">client.agents.<a href="./src/svahnar/resources/agents.py">delete</a>(\*\*<a href="src/svahnar/types/agent_delete_params.py">params</a>) -> <a href="./src/svahnar/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="delete /v1/agents/bulk-delete">client.agents.<a href="./src/svahnar/resources/agents.py">bulk_delete</a>(\*\*<a href="src/svahnar/types/agent_bulk_delete_params.py">params</a>) -> <a href="./src/svahnar/types/agent_bulk_delete_response.py">AgentBulkDeleteResponse</a></code>
- <code title="get /v1/agents/download-agent/{agent_id}">client.agents.<a href="./src/svahnar/resources/agents.py">download</a>(agent_id) -> object</code>
- <code title="put /v1/agents/reconfigure-agent">client.agents.<a href="./src/svahnar/resources/agents.py">reconfigure</a>(\*\*<a href="src/svahnar/types/agent_reconfigure_params.py">params</a>) -> <a href="./src/svahnar/types/agent_reconfigure_response.py">AgentReconfigureResponse</a></code>
- <code title="post /v1/agents/run">client.agents.<a href="./src/svahnar/resources/agents.py">run</a>(\*\*<a href="src/svahnar/types/agent_run_params.py">params</a>) -> <a href="./src/svahnar/types/agent_run_response.py">AgentRunResponse</a></code>
- <code title="post /v1/agents/test">client.agents.<a href="./src/svahnar/resources/agents.py">test</a>(\*\*<a href="src/svahnar/types/agent_test_params.py">params</a>) -> object</code>
- <code title="put /v1/agents/update-agent-info">client.agents.<a href="./src/svahnar/resources/agents.py">update_info</a>(\*\*<a href="src/svahnar/types/agent_update_info_params.py">params</a>) -> <a href="./src/svahnar/types/agent_update_info_response.py">AgentUpdateInfoResponse</a></code>
- <code title="post /v1/agents/validate">client.agents.<a href="./src/svahnar/resources/agents.py">validate</a>(\*\*<a href="src/svahnar/types/agent_validate_params.py">params</a>) -> <a href="./src/svahnar/types/agent_validate_response.py">AgentValidateResponse</a></code>

# Auth

Methods:

- <code title="post /v1/auth/login">client.auth.<a href="./src/svahnar/resources/auth.py">login</a>(\*\*<a href="src/svahnar/types/auth_login_params.py">params</a>) -> object</code>
