import pytest

from anipics import (
    AsyncNekosAPI,
    AsyncNekosBest,
    AsyncNekosia,
    AsyncNekosLife,
    AsyncPurrBot,
    Models,
)

pytestmark = pytest.mark.live


@pytest.mark.asyncio
async def test_nekosapi():
    client = AsyncNekosAPI()
    result = await client.get(AsyncNekosAPI.Types.kemonomimi)
    assert isinstance(result, Models.Result)
    assert result.url

    random_image = await client.get_random_image(
        tags=[AsyncNekosAPI.Types.kemonomimi], rating=AsyncNekosAPI.Ratings.safe
    )
    assert isinstance(random_image, Models.NekosAPIImage)
    assert random_image.rating == "safe"
    assert "kemonomimi" in {tag.name.lower() for tag in random_image.tags}

    image = await client.get_image_by_id(random_image.id)
    assert image.id == random_image.id
    assert image.url == random_image.url

    browsed = await client.get_images(limit=1, tags=[AsyncNekosAPI.Types.girl])
    assert len(browsed.items) == 1
    assert browsed.total >= 1
    assert isinstance(browsed.items[0], Models.NekosAPIImage)
    assert "girl" in {tag.name.lower() for tag in browsed.items[0].tags}


@pytest.mark.asyncio
async def test_nekosbest():
    client = AsyncNekosBest()
    result = await client.get(AsyncNekosBest.Types.hug)
    assert isinstance(result, Models.Result)
    assert result.url

    endpoints = await client.get_endpoints()
    assert AsyncNekosBest.Types.neko in endpoints
    assert AsyncNekosBest.Types.waifu in endpoints


@pytest.mark.asyncio
async def test_nekoslife():
    result = await AsyncNekosLife().get(AsyncNekosLife.Types.avatar)
    assert isinstance(result, Models.Result)
    assert result.url


@pytest.mark.asyncio
async def test_nekosia():
    client = AsyncNekosia()
    result = await client.get(AsyncNekosia.Types.catgirl)
    assert isinstance(result, Models.Result)
    assert result.url

    tags = await client.get_tags()
    assert AsyncNekosia.Types.catgirl in tags
    assert AsyncNekosia.Types.foxgirl in tags


@pytest.mark.asyncio
async def test_purrbot():
    result = await AsyncPurrBot().get(AsyncPurrBot.Types.SFW.GIF.neko)
    assert isinstance(result, Models.Result)
    assert result.url

    result = await AsyncPurrBot().get(AsyncPurrBot.Types.NSFW.GIF.anal)
    assert isinstance(result, Models.Result)
    assert result.url

    result = await AsyncPurrBot().get(AsyncPurrBot.Types.NSFW.IMG.neko)
    assert isinstance(result, Models.Result)
    assert result.url
