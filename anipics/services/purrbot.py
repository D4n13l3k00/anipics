# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from typing import NewType, Union

import httpx

from anipics.models import Models

PurrBotType = NewType("PurrBotType", str)


class PurrBot:
    ENDPOINT = "https://purrbot.site/api/img/{path}"

    class Types:
        class SFW:
            class GIF:
                # GET /img/sfw/angry/gif
                angry: PurrBotType = "sfw/angry/gif"
                # GET /img/sfw/bite/gif
                bite: PurrBotType = "sfw/bite/gif"
                # GET /img/sfw/blush/gif
                blush: PurrBotType = "sfw/blush/gif"
                # GET /img/sfw/comfy/gif
                comfy: PurrBotType = "sfw/comfy/gif"
                # GET /img/sfw/cry/gif
                cry: PurrBotType = "sfw/cry/gif"
                # GET /img/sfw/cuddle/gif
                cuddle: PurrBotType = "sfw/cuddle/gif"
                # GET /img/sfw/dance/gif
                dance: PurrBotType = "sfw/dance/gif"
                # GET /img/sfw/fluff/gif
                fluff: PurrBotType = "sfw/fluff/gif"
                # GET /img/sfw/hug/gif
                hug: PurrBotType = "sfw/hug/gif"
                # GET /img/sfw/kiss/gif
                kiss: PurrBotType = "sfw/kiss/gif"
                # GET /img/sfw/lay/gif
                lay: PurrBotType = "sfw/lay/gif"
                # GET /img/sfw/lick/gif
                lick: PurrBotType = "sfw/lick/gif"
                # GET /img/sfw/pat/gif
                pat: PurrBotType = "sfw/pat/gif"
                # GET /img/sfw/poke/gif
                poke: PurrBotType = "sfw/poke/gif"
                # GET /img/sfw/pout/gif
                pout: PurrBotType = "sfw/pout/gif"
                # GET /img/sfw/slap/gif
                slap: PurrBotType = "sfw/slap/gif"
                # GET /img/sfw/smile/gif
                smile: PurrBotType = "sfw/smile/gif"
                # GET /img/sfw/tail/gif
                tail: PurrBotType = "sfw/tail/gif"
                # GET /img/sfw/tickle/gif
                tickle: PurrBotType = "sfw/tickle/gif"

                # GET /img/sfw/eevee/{type}
                eevee: PurrBotType = "sfw/eevee/gif"
                # GET /img/sfw/neko/{type}
                neko: PurrBotType = "sfw/neko/gif"

            class IMG:
                # GET /img/sfw/background/img
                background: PurrBotType = "sfw/background/img"
                # GET /img/sfw/holo/img
                holo: PurrBotType = "sfw/holo/img"
                # GET /img/sfw/icon/img
                icon: PurrBotType = "sfw/icon/img"
                # GET /img/sfw/kitsune/img
                kitsune: PurrBotType = "sfw/kitsune/img"
                # GET /img/sfw/okami/img
                okami: PurrBotType = "sfw/okami/img"
                # GET /img/sfw/senko/img
                senko: PurrBotType = "sfw/senko/img"
                # GET /img/sfw/shiro/img
                shiro: PurrBotType = "sfw/shiro/img"

                # GET /img/sfw/eevee/{type}
                eevee: PurrBotType = "sfw/eevee/img"
                # GET /img/sfw/neko/{type}
                neko: PurrBotType = "sfw/neko/img"

        class NSFW:
            # GET /img/nsfw/neko/{type}
            class GIF:
                # GET /img/nsfw/anal/gif
                anal: PurrBotType = "nsfw/anal/gif"
                # GET /img/nsfw/blowjob/gif
                blowjob: PurrBotType = "nsfw/blowjob/gif"
                # GET /img/nsfw/cum/gif
                cum: PurrBotType = "nsfw/cum/gif"
                # GET /img/nsfw/fuck/gif
                fuck: PurrBotType = "nsfw/fuck/gif"
                # GET /img/nsfw/pussylick/gif
                pussylick: PurrBotType = "nsfw/pussylick/gif"
                # GET /img/nsfw/solo/gif
                solo: PurrBotType = "nsfw/solo/gif"
                # GET /img/nsfw/solo_male/gif
                solo_male: PurrBotType = "nsfw/solo_male/gif"
                # GET /img/nsfw/threesome_fff/gif
                threesome_fff: PurrBotType = "nsfw/threesome_fff/gif"
                # GET /img/nsfw/threesome_ffm/gif
                threesome_ffm: PurrBotType = "nsfw/threesome_ffm/gif"
                # GET /img/nsfw/threesome_mmf/gif
                threesome_mmf: PurrBotType = "nsfw/threesome_mmf/gif"
                # GET /img/nsfw/yaoi/gif
                yaoi: PurrBotType = "nsfw/yaoi/gif"
                # GET /img/nsfw/yuri/gif
                yuri: PurrBotType = "nsfw/yuri/gif"

                # GET /img/nsfw/neko/{type}
                neko: PurrBotType = "nsfw/neko/gif"

            class IMG:
                # GET /img/nsfw/neko/{type}
                neko: PurrBotType = "/img/nsfw/neko/img"

    def get(self, query: Union[PurrBotType, str]) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (Union[PurrBotType, str]): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        with httpx.Client() as client:
            return Models.Result(
                url=client.get(self.ENDPOINT.format(path=query)).json()["link"]
            )

    async def async_get(self, query: Union[PurrBotType, str]) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (Union[PurrBotType, str]): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=(await client.get(self.ENDPOINT.format(path=query))).json()["link"]
            )
