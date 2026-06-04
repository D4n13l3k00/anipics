import pytest

from anipics import (
    Models,
    NekosAPI,
    NekosBest,
    Nekosia,
    NekosLife,
    PurrBot,
    WaifuIm,
)

pytestmark = pytest.mark.live


def test_nekosapi():
    client = NekosAPI()
    result = client.get(NekosAPI.Types.kemonomimi)
    assert isinstance(result, Models.Result)
    assert result.url

    images = client.get_random_images(limit=2, tags=[NekosAPI.Types.kemonomimi])
    assert len(images) == 2
    assert isinstance(images[0], Models.NekosAPIImage)
    assert images[0].url

    image = client.get_image_by_id(images[0].id)
    assert image.id == images[0].id
    assert image.url

    browsed = client.get_images(limit=1, tags=[NekosAPI.Types.girl])
    assert len(browsed) == 1
    assert isinstance(browsed[0], Models.NekosAPIImage)
    assert browsed[0].url


def test_nekosbest():
    client = NekosBest()
    result = client.get(NekosBest.Types.hug)
    assert isinstance(result, Models.Result)
    assert result.url

    endpoints = client.get_endpoints()
    assert NekosBest.Types.neko in endpoints
    assert NekosBest.Types.waifu in endpoints


def test_nekoslife():
    result = NekosLife().get(NekosLife.Types.avatar)
    assert isinstance(result, Models.Result)
    assert result.url


def test_nekosia():
    client = Nekosia()
    result = client.get(Nekosia.Types.catgirl)
    assert isinstance(result, Models.Result)
    assert result.url

    tags = client.get_tags()
    assert Nekosia.Types.catgirl in tags
    assert Nekosia.Types.foxgirl in tags


def test_purrbot():
    result = PurrBot().get(PurrBot.Types.SFW.GIF.neko)
    assert isinstance(result, Models.Result)
    assert result.url

    result = PurrBot().get(PurrBot.Types.NSFW.GIF.anal)
    assert isinstance(result, Models.Result)
    assert result.url

    result = PurrBot().get(PurrBot.Types.NSFW.IMG.neko)
    assert isinstance(result, Models.Result)
    assert result.url


def test_waifuim():
    client = WaifuIm()
    result = client.get([WaifuIm.Types.waifu], is_nsfw=WaifuIm.Nsfw.false)
    assert isinstance(result, Models.Result)
    assert result.url

    tags = client.get_tags()
    slugs = {tag["slug"] for tag in tags}
    assert set(WaifuIm.TAGS) == slugs
    assert WaifuIm.Types.hentai in slugs
    assert WaifuIm.Types.black_clover in slugs
