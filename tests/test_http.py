import httpx
import pytest

from anipics.services._http import (
    async_get_json,
    compact_params,
    get_json,
    normalize_list,
)


def test_compact_params_removes_none_values():
    assert compact_params(limit=2, tags=["neko"], rating=None) == {
        "limit": 2,
        "tags": ["neko"],
    }


def test_normalize_list_accepts_scalar_sequences_and_none():
    assert normalize_list("neko") == ["neko"]
    assert normalize_list(("neko", "waifu")) == ["neko", "waifu"]
    assert normalize_list(None) is None


def test_get_json_raises_for_http_errors():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, request=request)

    transport = httpx.MockTransport(handler)

    with pytest.raises(httpx.HTTPStatusError):
        get_json("https://example.test/missing", transport=transport, retries=1)


def test_get_json_retries_network_errors():
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.NetworkError("temporary failure")
        return httpx.Response(200, json={"ok": True}, request=request)

    transport = httpx.MockTransport(handler)

    assert get_json("https://example.test/image", transport=transport) == {"ok": True}
    assert attempts == 2


@pytest.mark.asyncio
async def test_async_get_json_retries_network_errors():
    attempts = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.NetworkError("temporary failure")
        return httpx.Response(200, json={"ok": True}, request=request)

    transport = httpx.MockTransport(handler)

    assert await async_get_json("https://example.test/image", transport=transport) == {
        "ok": True
    }
    assert attempts == 2
