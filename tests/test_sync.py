# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from anipics import AnimePicsX, Models, NekosLife, WaifuPics, PurrBot


def test_animepicsx():
    result = AnimePicsX().get()
    assert isinstance(result, Models.Result)
    assert result.url


def test_nekoslife():
    result = NekosLife().get(NekosLife.Types.avatar)
    assert isinstance(result, Models.Result)
    assert result.url


def test_waifupics():
    result = WaifuPics().get(WaifuPics.Types.SFW.hug)
    assert isinstance(result, Models.Result)
    assert result.url

    result = WaifuPics().get(WaifuPics.Types.NSFW.blowjob)
    assert isinstance(
        result, Models.Result
    )
    assert result.url


def test_purrbot():
    result = PurrBot().get(PurrBot.Types.SFW.GIF.neko)
    assert isinstance(
        result, Models.Result
    )
    assert result.url

    result = PurrBot().get(PurrBot.Types.NSFW.GIF.anal)
    assert isinstance(
        result, Models.Result
    )
    assert result.url
