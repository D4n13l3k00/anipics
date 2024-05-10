# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from typing import NewType, Union

import httpx

from anipics.models import Models

WaifuPicsType = NewType("WaifuPicsSFWType", str)


class WaifuPics:
    ENDPOINT = "https://api.waifu.pics/{_type}/{query}"

    class Types:
        class SFW:
            waifu: WaifuPicsType = "waifu"
            neko: WaifuPicsType = "neko"
            shinobu: WaifuPicsType = "shinobu"
            megumin: WaifuPicsType = "megumin"
            bully: WaifuPicsType = "bully"
            cuddle: WaifuPicsType = "cuddle"
            cry: WaifuPicsType = "cry"
            hug: WaifuPicsType = "hug"
            awoo: WaifuPicsType = "awoo"
            kiss: WaifuPicsType = "kiss"
            lick: WaifuPicsType = "lick"
            pat: WaifuPicsType = "pat"
            smug: WaifuPicsType = "smug"
            bonk: WaifuPicsType = "bonk"
            yeet: WaifuPicsType = "yeet"
            blush: WaifuPicsType = "blush"
            smile: WaifuPicsType = "smile"
            wave: WaifuPicsType = "wave"
            highfive: WaifuPicsType = "highfive"
            handhold: WaifuPicsType = "handhold"
            nom: WaifuPicsType = "nom"
            bite: WaifuPicsType = "bite"
            glomp: WaifuPicsType = "glomp"
            slap: WaifuPicsType = "slap"
            kill: WaifuPicsType = "kill"
            kick: WaifuPicsType = "kick"
            happy: WaifuPicsType = "happy"
            wink: WaifuPicsType = "wink"
            poke: WaifuPicsType = "poke"
            dance: WaifuPicsType = "dance"
            cringe: WaifuPicsType = "cringe"

        class NSFW:
            waifu: WaifuPicsType = "waifu"
            neko: WaifuPicsType = "neko"
            trap: WaifuPicsType = "trap"
            blowjob: WaifuPicsType = "blowjob"

    def get(self, query: Union[WaifuPicsType, str], nsfw: bool) -> Models.Result:
        """Get pictire from waifu.pics

        Args:
            query (Union[WaifuPicsType, str]): Category of image
            nsfw (bool): Nsfw or sfw

        Returns:
            Models.Result: Model with `url` parameter
        """
        _type = "nsfw" if nsfw else "sfw"
        with httpx.Client() as client:
            return Models.Result(
                url=client.get(self.ENDPOINT.format(_type=_type, query=query)).json()[
                    "url"
                ]
            )

    async def async_get(
        self, query: Union[WaifuPicsType, str], nsfw: bool
    ) -> Models.Result:
        """Get pictire from waifu.pics

        Args:
            query (Union[WaifuPicsType, str]): Category of image
            nsfw (bool): Nsfw or sfw

        Returns:
            Models.Result: Model with `url` parameter
        """
        _type = "nsfw" if nsfw else "sfw"
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=(
                    await client.get(self.ENDPOINT.format(_type=_type, query=query))
                ).json()["url"]
            )
