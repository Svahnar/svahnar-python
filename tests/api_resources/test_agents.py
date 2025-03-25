# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from svahnar import Svahnar, AsyncSvahnar
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Svahnar) -> None:
        agent = client.agents.run(
            agent_id="agent_id",
            message="message",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.run(
            agent_id="agent_id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Svahnar) -> None:
        with client.agents.with_streaming_response.run(
            agent_id="agent_id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_test(self, client: Svahnar) -> None:
        agent = client.agents.test(
            message="message",
            yaml_data="yaml_data",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_test(self, client: Svahnar) -> None:
        response = client.agents.with_raw_response.test(
            message="message",
            yaml_data="yaml_data",
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
            yaml_data="yaml_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.run(
            agent_id="agent_id",
            message="message",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.run(
            agent_id="agent_id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncSvahnar) -> None:
        async with async_client.agents.with_streaming_response.run(
            agent_id="agent_id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_test(self, async_client: AsyncSvahnar) -> None:
        agent = await async_client.agents.test(
            message="message",
            yaml_data="yaml_data",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncSvahnar) -> None:
        response = await async_client.agents.with_raw_response.test(
            message="message",
            yaml_data="yaml_data",
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
            yaml_data="yaml_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
