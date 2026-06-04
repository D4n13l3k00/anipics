from typing import TypeAlias

from anipics.models import Models
from anipics.services._http import async_get_json, get_json

NekosLifeType: TypeAlias = str


class NekosLife:
    ENDPOINT = "https://nekos.life/api/v2/img/{query}"

    class Types:
        wallpaper: NekosLifeType = "wallpaper"
        ngif: NekosLifeType = "ngif"
        tickle: NekosLifeType = "tickle"
        feed: NekosLifeType = "feed"
        gecg: NekosLifeType = "gecg"
        gasm: NekosLifeType = "gasm"
        slap: NekosLifeType = "slap"
        avatar: NekosLifeType = "avatar"
        lizard: NekosLifeType = "lizard"
        waifu: NekosLifeType = "waifu"
        pat: NekosLifeType = "pat"
        _8ball: NekosLifeType = "8ball"
        kiss: NekosLifeType = "kiss"
        neko: NekosLifeType = "neko"
        spank: NekosLifeType = "spank"
        cuddle: NekosLifeType = "cuddle"
        fox_girl: NekosLifeType = "fox_girl"
        hug: NekosLifeType = "hug"
        smug: NekosLifeType = "smug"
        goose: NekosLifeType = "goose"
        woof: NekosLifeType = "woof"

    def get(self, query: NekosLifeType) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["url"])

    async def async_get(self, query: NekosLifeType) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = await async_get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["url"])
