# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, Optional, cast

import httpx

from ..types import (
    agent_run_params,
    agent_list_params,
    agent_test_params,
    agent_create_params,
    agent_delete_params,
    agent_download_params,
    agent_retrieve_params,
    agent_validate_params,
    agent_bulk_delete_params,
    agent_reconfigure_params,
    agent_update_info_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
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
from ..types.agent_validate_response import AgentValidateResponse

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
        agent_icon: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Create Agent

        Args:
          deploy_to: Where to deploy the agent.

        Options: 'AgentStore' or 'Organization'.

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
            cast_to=object,
        )

    def retrieve(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch agent details by agent_id and organization ID, and return the details in a
        structured JSON format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/get-agent",
            body=maybe_transform({"agent_id": agent_id}, agent_retrieve_params.AgentRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List all agents for the organization and user, with optional pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/list-agents",
            body=maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                agent_list_params.AgentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete an agent by its ID if it belongs to the same organization.

        :param input:
        The input containing the agent ID. :param request: The request object to
        retrieve the organization ID. :return: A success message if the agent is
        deleted, or an error message if the deletion fails.

        Args:
          agent_id: The ID of the agent to delete

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
            cast_to=object,
        )

    def bulk_delete(
        self,
        *,
        agent_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete multiple agents by their IDs if they belong to the same organization.
        :param input: The input containing the list of agent IDs. :param request: The
        request object to retrieve the organization ID. :return: A success message if
        the agents are deleted, or an error message if the deletion fails.

        Args:
          agent_ids: The list of agent IDs to delete

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
            cast_to=object,
        )

    def download(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch agent details by agent_id, decode the YAML configuration, and return it as
        a downloadable file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agents/download-agent",
            body=maybe_transform({"agent_id": agent_id}, agent_download_params.AgentDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Reconfigure Agent

        Args:
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
            cast_to=object,
        )

    def run(
        self,
        *,
        agent_id: str,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRunResponse:
        """
        Run an agent by sending the provided command to the agent service and returns a
        detailed nested response containing message, logs and metadata.

        Args:
          agent_id: Unique identifier for the agent

          message: The message or command to be sent to the agent

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
        yaml_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        yaml_string: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Run Agent

        Args:
          message: Message to send to the agent.

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
        deploy_to: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        agent_icon: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Agent Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"agent_icon": agent_icon})
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "deploy_to": deploy_to,
                        "description": description,
                        "name": name,
                    },
                    agent_update_info_params.AgentUpdateInfoParams,
                ),
            ),
            cast_to=object,
        )

    def validate(
        self,
        *,
        yaml_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        yaml_string: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentValidateResponse:
        """
        Validates the agent network configuration provided as a YAML file or string.
        Only files with a .yaml or .yml extension are accepted.

        Args:
          yaml_file: YAML file to test the agent.

          yaml_string: YAML string to test the agent.

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
        agent_icon: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Create Agent

        Args:
          deploy_to: Where to deploy the agent.

        Options: 'AgentStore' or 'Organization'.

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
            cast_to=object,
        )

    async def retrieve(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch agent details by agent_id and organization ID, and return the details in a
        structured JSON format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/get-agent",
            body=await async_maybe_transform({"agent_id": agent_id}, agent_retrieve_params.AgentRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List all agents for the organization and user, with optional pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/list-agents",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                agent_list_params.AgentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete an agent by its ID if it belongs to the same organization.

        :param input:
        The input containing the agent ID. :param request: The request object to
        retrieve the organization ID. :return: A success message if the agent is
        deleted, or an error message if the deletion fails.

        Args:
          agent_id: The ID of the agent to delete

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
            cast_to=object,
        )

    async def bulk_delete(
        self,
        *,
        agent_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete multiple agents by their IDs if they belong to the same organization.
        :param input: The input containing the list of agent IDs. :param request: The
        request object to retrieve the organization ID. :return: A success message if
        the agents are deleted, or an error message if the deletion fails.

        Args:
          agent_ids: The list of agent IDs to delete

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
            cast_to=object,
        )

    async def download(
        self,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch agent details by agent_id, decode the YAML configuration, and return it as
        a downloadable file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agents/download-agent",
            body=await async_maybe_transform({"agent_id": agent_id}, agent_download_params.AgentDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Reconfigure Agent

        Args:
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
            cast_to=object,
        )

    async def run(
        self,
        *,
        agent_id: str,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRunResponse:
        """
        Run an agent by sending the provided command to the agent service and returns a
        detailed nested response containing message, logs and metadata.

        Args:
          agent_id: Unique identifier for the agent

          message: The message or command to be sent to the agent

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
        yaml_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        yaml_string: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Run Agent

        Args:
          message: Message to send to the agent.

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
        deploy_to: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        agent_icon: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Agent Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"agent_icon": agent_icon})
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "deploy_to": deploy_to,
                        "description": description,
                        "name": name,
                    },
                    agent_update_info_params.AgentUpdateInfoParams,
                ),
            ),
            cast_to=object,
        )

    async def validate(
        self,
        *,
        yaml_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        yaml_string: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentValidateResponse:
        """
        Validates the agent network configuration provided as a YAML file or string.
        Only files with a .yaml or .yml extension are accepted.

        Args:
          yaml_file: YAML file to test the agent.

          yaml_string: YAML string to test the agent.

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
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.download = to_raw_response_wrapper(
            agents.download,
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
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.download = async_to_raw_response_wrapper(
            agents.download,
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
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.download = to_streamed_response_wrapper(
            agents.download,
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
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.download = async_to_streamed_response_wrapper(
            agents.download,
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
