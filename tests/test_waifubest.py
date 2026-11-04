from unittest.mock import AsyncMock, Mock

import pytest

from anipics import AsyncWaifuBest, WaifuBest
from anipics.services import waifubest


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_empty_images_raise_clear_lookup_error(monkeypatch, asynchronous):
    data = {"items": [], "totalCount": 0}
    request = AsyncMock(return_value=data) if asynchronous else Mock(return_value=data)
    monkeypatch.setattr(
        waifubest, "async_get_json" if asynchronous else "get_json", request
    )

    with pytest.raises(LookupError) as raised:
        if asynchronous:
            await AsyncWaifuBest().get(WaifuBest.Types.hentai)
        else:
            WaifuBest().get(WaifuBest.Types.hentai)

    assert type(raised.value) is LookupError

    assert request.call_count == 1


@pytest.mark.live
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.asyncio
async def test_excluded_tag_cannot_also_be_required(asynchronous):

    with pytest.raises(LookupError) as raised:
        if asynchronous:
            await AsyncWaifuBest().get("waifu", excluded_tags=["waifu"])
        else:
            WaifuBest().get("waifu", excluded_tags=["waifu"])

    assert type(raised.value) is LookupError
