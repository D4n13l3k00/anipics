# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier: 	AGPL-3.0-or-later

from typing import Coroutine, Union

import requests
from bs4 import BeautifulSoup

from .models import Models


class Parser:
    class NekosLife:
        class types:
            femdom, tickle, classic, ngif, erofeet, meow, erok, poke, les, hololewd, lewdk, keta, feetg, nsfw_neko_gif, eroyuri, kiss, _8ball, kuni, tits, pussy_jpg, cum_jpg, pussy, lewdkemo, lizard, slap, lewd, cum, cuddle, spank, smallboobs, goose, Random_hentai_gif, avatar, fox_girl, nsfw_avatar, hug, gecg, boobs, pat, feet, smug, kemonomimi, solog, holo, wallpaper, bj, woof, yuri, trap, anal, baka, blowjob, holoero, feed, neko, gasm, hentai, futanari, ero, solo, waifu, pwankg, eron, erokemo = 'femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'hololewd', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo'

        def get(query: str) -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from nekos.life

            Args:
                query (str): category or Parser.NekosLife.types.*

            Returns:
                Models.Result
            """
            return Models.Result(
                url=requests.get(
                    f"https://nekos.life/api/v2/img/{query}").json()['url']
            )

    class AnimeApiHisoka:
        class types:
            class SFW:
                hug = "hug"
                kiss = "kiss"
                slap = "slap"
                wink = "wink"
                pat = "pat"
                kill = "kill"
                cuddle = "cuddle"
                punch = "punch"
                waifu = "waifu"

            class NSFW:
                hentai = "hentai"
                boobs = "boobs"
                lesbian = "lesbian"

        def get(query: str, nsfw: bool = False) -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from nime-api.hisoka17.repl.co

            Args:
                query (str): category or Parser.AnimeApiHisoka.types.*

            Returns:
                Models.Result
            """
            return Models.Result(
                url=requests.get(
                    f"https://anime-api.hisoka17.repl.co/img/{('nsfw/'+query) if nsfw else query}").json()['url']
            )

    class AniPics:
        def get() -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from animepicsx.net

            Returns:
                Models.Result
            """
            return Models.Result(
                url=BeautifulSoup(requests.get(
                    "https://animepicsx.net/random").text, "html.parser").find("img")["src"]
            )
