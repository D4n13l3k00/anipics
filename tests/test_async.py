import pytest

from anipics import AniPics, Models, NekosLife


@pytest.mark.asyncio
async def test_anipics():
    assert isinstance(await AniPics().async_get(), Models.Result)


@pytest.mark.asyncio
async def test_nekoslife():
    assert isinstance(
        await NekosLife().async_get(NekosLife.Types.avatar), Models.Result
    )
