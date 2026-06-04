import asyncio
import time
from collections.abc import Sequence
from typing import Any

import httpx

DEFAULT_TIMEOUT = httpx.Timeout(30, connect=15)
DEFAULT_RETRIES = 3


def compact_params(**params: Any) -> dict[str, Any]:
    return {key: value for key, value in params.items() if value is not None}


def normalize_list(value: str | Sequence[str] | None) -> list[str] | None:
    if value is None:
        return None
    if isinstance(value, str):
        return [value]
    return [str(item) for item in value]


def get_json(
    url: str,
    *,
    params: Any = None,
    timeout: httpx.Timeout = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
    transport: httpx.BaseTransport | None = None,
) -> Any:
    last_error: httpx.TimeoutException | httpx.NetworkError | None = None
    for attempt in range(retries):
        try:
            with httpx.Client(timeout=timeout, transport=transport) as client:
                response = client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except (httpx.TimeoutException, httpx.NetworkError) as error:
            last_error = error
            if attempt + 1 == retries:
                break
            time.sleep(0.5 * (attempt + 1))
    raise last_error or RuntimeError("request failed without an exception")


async def async_get_json(
    url: str,
    *,
    params: Any = None,
    timeout: httpx.Timeout = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
    transport: httpx.AsyncBaseTransport | None = None,
) -> Any:
    last_error: httpx.TimeoutException | httpx.NetworkError | None = None
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient(
                timeout=timeout, transport=transport
            ) as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                return response.json()
        except (httpx.TimeoutException, httpx.NetworkError) as error:
            last_error = error
            if attempt + 1 == retries:
                break
            await asyncio.sleep(0.5 * (attempt + 1))
    raise last_error or RuntimeError("request failed without an exception")
