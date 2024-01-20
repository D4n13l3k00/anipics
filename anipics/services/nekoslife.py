from typing import NewType, Union

import httpx

from anipics.models import Models

NekosLifeType = NewType("NekosLifeType", str)


class NekosLife:
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

    def get(self, query: Union[NekosLifeType, str]) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType): NekosLife.Types.{type} or str

        Returns:
            Models.Result
        """
        with httpx.Client() as client:
            return Models.Result(
                url=client.get(f"https://nekos.life/api/v2/img/{query}").json()["url"]
            )

    async def async_get(self, query: Union[NekosLifeType, str]) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType): NekosLife.Types.{type} or str

        Returns:
            Models.Result
        """
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=(await client.get(f"https://nekos.life/api/v2/img/{query}")).json()[
                    "url"
                ]
            )
