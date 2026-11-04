import pytest

from anipics import (
    Models,
    NekosAPI,
    NekosBest,
    Nekosia,
    NekosLife,
    PurrBot,
)

pytestmark = pytest.mark.live


def test_nekosapi():
    client = NekosAPI()
    result = client.get(NekosAPI.Types.kemonomimi)
    assert isinstance(result, Models.Result)
    assert result.url

    random_image = client.get_random_image(
        tags=[NekosAPI.Types.kemonomimi], rating=NekosAPI.Ratings.safe
    )
    assert isinstance(random_image, Models.NekosAPIImage)
    assert random_image.rating == "safe"
    assert "kemonomimi" in {tag.name.lower() for tag in random_image.tags}

    image = client.get_image_by_id(random_image.id)
    assert image.id == random_image.id
    assert image.url == random_image.url

    browsed = client.get_images(limit=1, tags=[NekosAPI.Types.girl])
    assert len(browsed.items) == 1
    assert browsed.total >= 1
    assert isinstance(browsed.items[0], Models.NekosAPIImage)
    assert "girl" in {tag.name.lower() for tag in browsed.items[0].tags}


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
