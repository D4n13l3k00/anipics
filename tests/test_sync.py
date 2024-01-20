from anipics import AniPics, Models, NekosLife


def test_anipics():
    assert isinstance(AniPics().get(), Models.Result)


def test_nekoslife():
    assert isinstance(NekosLife().get(NekosLife.Types.avatar), Models.Result)
