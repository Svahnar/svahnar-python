# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Iterable, Optional, cast

import httpx

from ..types import (
    agent_run_params,
    agent_test_params,
    agent_create_params,
    agent_delete_params,
    agent_validate_params,
    agent_bulk_delete_params,
    agent_reconfigure_params,
    agent_update_info_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_run_response import AgentRunResponse
from ..types.agent_create_response import AgentCreateResponse
from ..types.agent_delete_response import AgentDeleteResponse
from ..types.agent_validate_response import AgentValidateResponse
from ..types.agent_bulk_delete_response import AgentBulkDeleteResponse
from ..types.agent_reconfigure_response import AgentReconfigureResponse
from ..types.agent_update_info_response import AgentUpdateInfoResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Svahnar/svahnar-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Svahnar/svahnar-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        deploy_to: str,
        description: str,
        name: str,
        yaml_file: FileTypes,
        agent_icon: Optional[FileTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Upload a YAML configuration file to create and deploy a new agent.

        Optionally
        provide an agent icon (required for AgentStore deployments).

        Args:
          deploy_to: Where to deploy the agent. Options: 'AgentStore' or 'Organization'.

          description: A brief description of the agent.

          name: The agent's name. Supports Unicode characters.

          yaml_file: The YAML configuration for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "deploy_to": deploy_to,
                "description": description,
                "name": name,
                "yaml_file": yaml_file,
                "agent_icon": agent_icon,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"], ["agent_icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/agents/create",
            body=maybe_transform(body, agent_create_params.AgentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def delete(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """Delete a single agent by its ID.

        The agent must belong to the requesting user's
        organization.

        Args:
          agent_id: The ID of the agent to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/agents/delete",
            body=maybe_transform({"agent_id": agent_id}, agent_delete_params.AgentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    def bulk_delete(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentBulkDeleteResponse:
        """Delete multiple agents by their IDs.

        Only agents belonging to the requesting
        user's organization will be deleted.

        Args:
          agent_ids: The list of agent IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/agents/bulk-delete",
            body=maybe_transform({"agent_ids": agent_ids}, agent_bulk_delete_params.AgentBulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentBulkDeleteResponse,
        )

    def reconfigure(
        self,
        *,
        agent_id: str,
        yaml_file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentReconfigureResponse:
        """Replace the YAML configuration for an existing agent.

        Only the creator of the
        agent can perform this operation.

        Args:
          agent_id: The ID of the agent to reconfigure.

          yaml_file: The new YAML configuration file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "agent_id": agent_id,
                "yaml_file": yaml_file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            "/v1/agents/reconfigure-agent",
            body=maybe_transform(body, agent_reconfigure_params.AgentReconfigureParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentReconfigureResponse,
        )

    def run(
        self,
        *,
        agent_id: str,
        message: str,
        agent_history: Optional[Iterable[object]] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute an agent by sending the provided message to the agent service.

        Returns a
        detailed response containing the conversation messages, logs, and metadata.

        Args:
          agent_id: Unique identifier for the agent.

          message: The message or command to be sent to the agent.

          agent_history: List of prior messages; defaults to empty list.

          thread_id: Unique identifier for the chat session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/run",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "message": message,
                    "agent_history": agent_history,
                    "thread_id": thread_id,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    def test(
        self,
        *,
        message: str,
        agent_history: Optional[Iterable[object]] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        yaml_file: Optional[FileTypes] | Omit = omit,
        yaml_string: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Test an agent by providing a YAML configuration (as a file or string) along with
        a message. The agent processes the message and returns a response without
        creating a persistent agent.

        Args:
          message: The message or command to be sent to the agent.

          agent_history: List of prior messages; defaults to empty list.

          thread_id: Unique identifier for the chat session.

          yaml_file: YAML file to test the agent.

          yaml_string: YAML string to test the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "message": message,
                "agent_history": agent_history,
                "thread_id": thread_id,
                "yaml_file": yaml_file,
                "yaml_string": yaml_string,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/agents/test",
            body=maybe_transform(body, agent_test_params.AgentTestParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_info(
        self,
        *,
        agent_id: str,
        agent_icon: Optional[FileTypes] | Omit = omit,
        deploy_to: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateInfoResponse:
        """Update an agent's name, description, deployment target, or icon.

        Only the
        creator of the agent can perform this operation.

        Args:
          agent_id: The ID of the agent to update.

          agent_icon: New agent icon (512x512 pixels).

          deploy_to: New deployment target: 'AgentStore' or 'Organization'.

          description: New description for the agent.

          name: New name for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "agent_id": agent_id,
                "agent_icon": agent_icon,
                "deploy_to": deploy_to,
                "description": description,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["agent_icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            "/v1/agents/update-agent-info",
            body=maybe_transform(body, agent_update_info_params.AgentUpdateInfoParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateInfoResponse,
        )

    def validate(
        self,
        *,
        yaml_file: Optional[FileTypes] | Omit = omit,
        yaml_string: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentValidateResponse:
        """
        Validates the agent network configuration provided as a YAML file or string.
        Only files with a .yaml or .yml extension are accepted.

        Args:
          yaml_file: YAML file to validate.

          yaml_string: YAML string to validate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "yaml_file": yaml_file,
                "yaml_string": yaml_string,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/agents/validate",
            body=maybe_transform(body, agent_validate_params.AgentValidateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentValidateResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Svahnar/svahnar-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Svahnar/svahnar-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        deploy_to: str,
        description: str,
        name: str,
        yaml_file: FileTypes,
        agent_icon: Optional[FileTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """Upload a YAML configuration file to create and deploy a new agent.

        Optionally
        provide an agent icon (required for AgentStore deployments).

        Args:
          deploy_to: Where to deploy the agent. Options: 'AgentStore' or 'Organization'.

          description: A brief description of the agent.

          name: The agent's name. Supports Unicode characters.

          yaml_file: The YAML configuration for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "deploy_to": deploy_to,
                "description": description,
                "name": name,
                "yaml_file": yaml_file,
                "agent_icon": agent_icon,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"], ["agent_icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/agents/create",
            body=await async_maybe_transform(body, agent_create_params.AgentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def delete(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """Delete a single agent by its ID.

        The agent must belong to the requesting user's
        organization.

        Args:
          agent_id: The ID of the agent to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/agents/delete",
            body=await async_maybe_transform({"agent_id": agent_id}, agent_delete_params.AgentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    async def bulk_delete(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentBulkDeleteResponse:
        """Delete multiple agents by their IDs.

        Only agents belonging to the requesting
        user's organization will be deleted.

        Args:
          agent_ids: The list of agent IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/agents/bulk-delete",
            body=await async_maybe_transform({"agent_ids": agent_ids}, agent_bulk_delete_params.AgentBulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentBulkDeleteResponse,
        )

    async def reconfigure(
        self,
        *,
        agent_id: str,
        yaml_file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentReconfigureResponse:
        """Replace the YAML configuration for an existing agent.

        Only the creator of the
        agent can perform this operation.

        Args:
          agent_id: The ID of the agent to reconfigure.

          yaml_file: The new YAML configuration file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "agent_id": agent_id,
                "yaml_file": yaml_file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            "/v1/agents/reconfigure-agent",
            body=await async_maybe_transform(body, agent_reconfigure_params.AgentReconfigureParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentReconfigureResponse,
        )

    async def run(
        self,
        *,
        agent_id: str,
        message: str,
        agent_history: Optional[Iterable[object]] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute an agent by sending the provided message to the agent service.

        Returns a
        detailed response containing the conversation messages, logs, and metadata.

        Args:
          agent_id: Unique identifier for the agent.

          message: The message or command to be sent to the agent.

          agent_history: List of prior messages; defaults to empty list.

          thread_id: Unique identifier for the chat session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/run",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "message": message,
                    "agent_history": agent_history,
                    "thread_id": thread_id,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    async def test(
        self,
        *,
        message: str,
        agent_history: Optional[Iterable[object]] | Omit = omit,
        thread_id: Optional[str] | Omit = omit,
        yaml_file: Optional[FileTypes] | Omit = omit,
        yaml_string: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Test an agent by providing a YAML configuration (as a file or string) along with
        a message. The agent processes the message and returns a response without
        creating a persistent agent.

        Args:
          message: The message or command to be sent to the agent.

          agent_history: List of prior messages; defaults to empty list.

          thread_id: Unique identifier for the chat session.

          yaml_file: YAML file to test the agent.

          yaml_string: YAML string to test the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "message": message,
                "agent_history": agent_history,
                "thread_id": thread_id,
                "yaml_file": yaml_file,
                "yaml_string": yaml_string,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/agents/test",
            body=await async_maybe_transform(body, agent_test_params.AgentTestParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_info(
        self,
        *,
        agent_id: str,
        agent_icon: Optional[FileTypes] | Omit = omit,
        deploy_to: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateInfoResponse:
        """Update an agent's name, description, deployment target, or icon.

        Only the
        creator of the agent can perform this operation.

        Args:
          agent_id: The ID of the agent to update.

          agent_icon: New agent icon (512x512 pixels).

          deploy_to: New deployment target: 'AgentStore' or 'Organization'.

          description: New description for the agent.

          name: New name for the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "agent_id": agent_id,
                "agent_icon": agent_icon,
                "deploy_to": deploy_to,
                "description": description,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["agent_icon"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            "/v1/agents/update-agent-info",
            body=await async_maybe_transform(body, agent_update_info_params.AgentUpdateInfoParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateInfoResponse,
        )

    async def validate(
        self,
        *,
        yaml_file: Optional[FileTypes] | Omit = omit,
        yaml_string: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentValidateResponse:
        """
        Validates the agent network configuration provided as a YAML file or string.
        Only files with a .yaml or .yml extension are accepted.

        Args:
          yaml_file: YAML file to validate.

          yaml_string: YAML string to validate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "yaml_file": yaml_file,
                "yaml_string": yaml_string,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["yaml_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/agents/validate",
            body=await async_maybe_transform(body, agent_validate_params.AgentValidateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentValidateResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.reconfigure = to_raw_response_wrapper(
            agents.reconfigure,
        )
        self.run = to_raw_response_wrapper(
            agents.run,
        )
        self.test = to_raw_response_wrapper(
            agents.test,
        )
        self.update_info = to_raw_response_wrapper(
            agents.update_info,
        )
        self.validate = to_raw_response_wrapper(
            agents.validate,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.reconfigure = async_to_raw_response_wrapper(
            agents.reconfigure,
        )
        self.run = async_to_raw_response_wrapper(
            agents.run,
        )
        self.test = async_to_raw_response_wrapper(
            agents.test,
        )
        self.update_info = async_to_raw_response_wrapper(
            agents.update_info,
        )
        self.validate = async_to_raw_response_wrapper(
            agents.validate,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.reconfigure = to_streamed_response_wrapper(
            agents.reconfigure,
        )
        self.run = to_streamed_response_wrapper(
            agents.run,
        )
        self.test = to_streamed_response_wrapper(
            agents.test,
        )
        self.update_info = to_streamed_response_wrapper(
            agents.update_info,
        )
        self.validate = to_streamed_response_wrapper(
            agents.validate,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.reconfigure = async_to_streamed_response_wrapper(
            agents.reconfigure,
        )
        self.run = async_to_streamed_response_wrapper(
            agents.run,
        )
        self.test = async_to_streamed_response_wrapper(
            agents.test,
        )
        self.update_info = async_to_streamed_response_wrapper(
            agents.update_info,
        )
        self.validate = async_to_streamed_response_wrapper(
            agents.validate,
        )
