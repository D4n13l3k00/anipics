# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from anipics import AnimePicsX, Models, NekosLife, WaifuPics


def test_animepicsx():
    assert isinstance(AnimePicsX().get(), Models.Result)


def test_nekoslife():
    assert isinstance(NekosLife().get(NekosLife.Types.avatar), Models.Result)


def test_waifupics():
    assert isinstance(WaifuPics().get(WaifuPics.Types.SFW.hug, False), Models.Result)
    assert isinstance(
        WaifuPics().get(WaifuPics.Types.NSFW.blowjob, True), Models.Result
    )
