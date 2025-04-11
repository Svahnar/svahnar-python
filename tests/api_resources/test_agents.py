# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from svahnar import Svahnar, AsyncSvahnar
from tests.utils import assert_matches_type
from svahnar.types import (
    AgentRunResponse,
    AgentValidateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Svahnar) -> None:
        agent = client.agents.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Svahnar) -> None:
        agent = client.agents.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
            agent_icon=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Svahnar) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Svahnar) -> None:
        agent = client.agents.list()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Svahnar) -> None:
        agent = client.agents.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Svahnar) -> None:
        agent = client.agents.delete(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.delete(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.delete(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_bulk_delete(self, client: Svahnar) -> None:
        agent = client.agents.bulk_delete(
            agent_ids=["string"],
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_bulk_delete(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.bulk_delete(
            agent_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.bulk_delete(
            agent_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_download(self, client: Svahnar) -> None:
        agent = client.agents.download(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_download(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.download(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_download(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.download(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_reconfigure(self, client: Svahnar) -> None:
        agent = client.agents.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_reconfigure(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_reconfigure(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Svahnar) -> None:
        agent = client.agents.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_test(self, client: Svahnar) -> None:
        agent = client.agents.test(
            message="message",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_test_with_all_params(self, client: Svahnar) -> None:
        agent = client.agents.test(
            message="message",
            yaml_file=b"raw file contents",
            yaml_string="yaml_string",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_test(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.test(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_test(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.test(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update_info(self, client: Svahnar) -> None:
        agent = client.agents.update_info(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_info_with_all_params(self, client: Svahnar) -> None:
        agent = client.agents.update_info(
            agent_id="agent_id",
            deploy_to="deploy_to",
            description="description",
            name="name",
            agent_icon=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_info(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.update_info(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_info(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.update_info(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Svahnar) -> None:
        agent = client.agents.validate()
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate_with_all_params(self, client: Svahnar) -> None:
        agent = client.agents.validate(
            yaml_file=b"raw file contents",
            yaml_string="yaml_string",
        )
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentValidateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
            agent_icon=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.create(
            deploy_to="deploy_to",
            description="description",
            name="name",
            yaml_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.delete(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.delete(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.delete(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.bulk_delete(
            agent_ids=["string"],
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.bulk_delete(
            agent_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.bulk_delete(
            agent_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_download(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.download(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.download(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.download(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_reconfigure(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_reconfigure(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_reconfigure(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.reconfigure(
            agent_id="agent_id",
            yaml_file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.run(
            agent_id="b06b8e39-51a7-4b6a-8474-e6340a6b9fa6",
            message="hi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_test(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.test(
            message="message",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.test(
            message="message",
            yaml_file=b"raw file contents",
            yaml_string="yaml_string",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.test(
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.test(
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_info(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.update_info(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_info_with_all_params(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.update_info(
            agent_id="agent_id",
            deploy_to="deploy_to",
            description="description",
            name="name",
            agent_icon=b"raw file contents",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_info(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.update_info(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_info(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.update_info(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.validate()
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.validate(
            yaml_file=b"raw file contents",
            yaml_string="yaml_string",
        )
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentValidateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentValidateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
