# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

import pytest

from anipics import AnimePicsX, Models, NekosLife, WaifuPics, PurrBot


@pytest.mark.asyncio
async def test_animepicsx():
    assert isinstance(await AnimePicsX().async_get(), Models.Result)


@pytest.mark.asyncio
async def test_nekoslife():
    assert isinstance(
        await NekosLife().async_get(NekosLife.Types.avatar), Models.Result
    )


@pytest.mark.asyncio
async def test_waifupics():
    assert isinstance(
        await WaifuPics().async_get(WaifuPics.Types.SFW.hug, False), Models.Result
    )
    assert isinstance(
        await WaifuPics().async_get(WaifuPics.Types.NSFW.blowjob, True), Models.Result
    )


@pytest.mark.asyncio
async def test_purrbot():
    assert isinstance(
        await PurrBot().async_get(PurrBot.Types.SFW.GIF.neko), Models.Result
    )
    assert isinstance(
        await PurrBot().async_get(PurrBot.Types.NSFW.GIF.anal), Models.Result
    )
