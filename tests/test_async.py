# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

import pytest

from anipics import AnimePicsX, Models, NekosLife, WaifuPics, PurrBot


@pytest.mark.asyncio
async def test_animepicsx():
    result = await AnimePicsX().async_get()
    assert isinstance(result, Models.Result)
    assert result.url


@pytest.mark.asyncio
async def test_nekoslife():
    result = await AnimePicsX().async_get()
    assert isinstance(
        await NekosLife().async_get(NekosLife.Types.avatar), Models.Result
    )
    assert result.url


@pytest.mark.asyncio
async def test_waifupics():
    result = await WaifuPics().async_get(WaifuPics.Types.SFW.hug)
    assert isinstance(
        result, Models.Result
    )
    assert result.url

    result = await WaifuPics().async_get(WaifuPics.Types.NSFW.blowjob)
    assert isinstance(
        result, Models.Result
    )
    assert result.url


@pytest.mark.asyncio
async def test_purrbot():
    result = await PurrBot().async_get(PurrBot.Types.SFW.GIF.neko)
    assert isinstance(
        result, Models.Result
    )
    assert result.url

    result = await PurrBot().async_get(PurrBot.Types.NSFW.GIF.anal)
    assert isinstance(
        result, Models.Result
    )
    assert result.url
