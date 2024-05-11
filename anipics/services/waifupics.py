# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from typing import NewType, Union

import httpx

from anipics.models import Models

WaifuPicsType = NewType("WaifuPicsSFWType", str)


class WaifuPics:
    ENDPOINT = "https://api.waifu.pics/{query}"

    class Types:
        class SFW:
            waifu: WaifuPicsType = "sfw/waifu"
            neko: WaifuPicsType = "sfw/neko"
            shinobu: WaifuPicsType = "sfw/shinobu"
            megumin: WaifuPicsType = "sfw/megumin"
            bully: WaifuPicsType = "sfw/bully"
            cuddle: WaifuPicsType = "sfw/cuddle"
            cry: WaifuPicsType = "sfw/cry"
            hug: WaifuPicsType = "sfw/hug"
            awoo: WaifuPicsType = "sfw/awoo"
            kiss: WaifuPicsType = "sfw/kiss"
            lick: WaifuPicsType = "sfw/lick"
            pat: WaifuPicsType = "sfw/pat"
            smug: WaifuPicsType = "sfw/smug"
            bonk: WaifuPicsType = "sfw/bonk"
            yeet: WaifuPicsType = "sfw/yeet"
            blush: WaifuPicsType = "sfw/blush"
            smile: WaifuPicsType = "sfw/smile"
            wave: WaifuPicsType = "sfw/wave"
            highfive: WaifuPicsType = "sfw/highfive"
            handhold: WaifuPicsType = "sfw/handhold"
            nom: WaifuPicsType = "sfw/nom"
            bite: WaifuPicsType = "sfw/bite"
            glomp: WaifuPicsType = "sfw/glomp"
            slap: WaifuPicsType = "sfw/slap"
            kill: WaifuPicsType = "sfw/kill"
            kick: WaifuPicsType = "sfw/kick"
            happy: WaifuPicsType = "sfw/happy"
            wink: WaifuPicsType = "sfw/wink"
            poke: WaifuPicsType = "sfw/poke"
            dance: WaifuPicsType = "sfw/dance"
            cringe: WaifuPicsType = "sfw/cringe"

        class NSFW:
            waifu: WaifuPicsType = "nsfw/waifu"
            neko: WaifuPicsType = "nsfw/neko"
            trap: WaifuPicsType = "nsfw/trap"
            blowjob: WaifuPicsType = "nsfw/blowjob"

    def get(self, query: Union[WaifuPicsType, str]) -> Models.Result:
        """Get pictire from waifu.pics

        Args:
            query (Union[WaifuPicsType, str]): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        with httpx.Client() as client:
            return Models.Result(
                url=client.get(self.ENDPOINT.format(query=query)).json()[
                    "url"
                ]
            )

    async def async_get(self, query: Union[WaifuPicsType, str]) -> Models.Result:
        """Get pictire from waifu.pics

        Args:
            query (Union[WaifuPicsType, str]): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=(
                    await client.get(self.ENDPOINT.format(query=query))
                ).json()["url"]
            )
