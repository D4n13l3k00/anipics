# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier:  AGPL-3.0-or-later

from typing import *

import requests
from bs4 import BeautifulSoup

from .models import Models

class _types:
    NekosLifeType = NewType('NekosLifeType', str)
    AnimeApiHisokaType = NewType('AnimeApiHisokaType', str)

class Parser:
    class NekosLife:
        class types:
            femdom: _types.NekosLifeType = 'femdom'
            tickle: _types.NekosLifeType = 'tickle'
            classic: _types.NekosLifeType = 'classic'
            ngif: _types.NekosLifeType = 'ngif'
            erofeet: _types.NekosLifeType = 'erofeet'
            meow: _types.NekosLifeType = 'meow'
            erok: _types.NekosLifeType = 'erok'
            poke: _types.NekosLifeType = 'poke'
            les: _types.NekosLifeType = 'les'
            hololewd: _types.NekosLifeType = 'hololewd'
            lewdk: _types.NekosLifeType = 'lewdk'
            keta: _types.NekosLifeType = 'keta'
            feetg: _types.NekosLifeType = 'feetg'
            nsfw_neko_gif: _types.NekosLifeType = 'nsfw_neko_gif'
            eroyuri: _types.NekosLifeType = 'eroyuri'
            kiss: _types.NekosLifeType = 'kiss'
            _8ball: _types.NekosLifeType = '8ball'
            kuni: _types.NekosLifeType = 'kuni'
            tits: _types.NekosLifeType = 'tits'
            pussy_jpg: _types.NekosLifeType = 'pussy_jpg'
            cum_jpg: _types.NekosLifeType = 'cum_jpg'
            pussy: _types.NekosLifeType = 'pussy'
            lewdkemo: _types.NekosLifeType = 'lewdkemo'
            lizard: _types.NekosLifeType = 'lizard'
            slap: _types.NekosLifeType = 'slap'
            lewd: _types.NekosLifeType = 'lewd'
            cum: _types.NekosLifeType = 'cum'
            cuddle: _types.NekosLifeType = 'cuddle'
            spank: _types.NekosLifeType = 'spank'
            smallboob: _types.NekosLifeType = 'smallboobs'
            goose: _types.NekosLifeType = 'goose'
            random_hentai_gif: _types.NekosLifeType = 'Random_hentai_gif'
            avatar: _types.NekosLifeType = 'avatar'
            fox_girl: _types.NekosLifeType = 'fox_girl'
            nsfw_avatar: _types.NekosLifeType = 'nsfw_avatar'
            hug: _types.NekosLifeType = 'hug'
            gecg: _types.NekosLifeType = 'gecg'
            boobs: _types.NekosLifeType = 'boobs'
            pat: _types.NekosLifeType = 'pat'
            feet: _types.NekosLifeType = 'feet'
            smug: _types.NekosLifeType = 'smug'
            kemonomimi: _types.NekosLifeType = 'kemonomimi'
            solog: _types.NekosLifeType = 'solog'
            holo: _types.NekosLifeType = 'holo'
            wallpaper: _types.NekosLifeType = 'wallpaper'
            bj: _types.NekosLifeType = 'bj'
            woof: _types.NekosLifeType = 'woof'
            yuri: _types.NekosLifeType = 'yuri'
            trap: _types.NekosLifeType = 'trap'
            anal: _types.NekosLifeType = 'anal'
            baka: _types.NekosLifeType = 'baka'
            blowjob: _types.NekosLifeType = 'blowjob'
            holoero: _types.NekosLifeType = 'holoero'
            feed: _types.NekosLifeType = 'feed'
            neko: _types.NekosLifeType = 'neko'
            gasm: _types.NekosLifeType = 'gasm'
            hentai: _types.NekosLifeType = 'hentai'
            futanari: _types.NekosLifeType = 'futanari'
            ero: _types.NekosLifeType = 'ero'
            solo: _types.NekosLifeType = 'solo'
            waifu: _types.NekosLifeType = 'waifu'
            pwankg: _types.NekosLifeType = 'pwankg'
            eron: _types.NekosLifeType = 'eron'
            erokemo: _types.NekosLifeType = 'erokemo'

        def get(query: Union[_types.NekosLifeType, str]) -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from nekos.life

            Args:
                query (NekosLifeType): See Parser/asyncParser.NekosLife.types

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
                hug: _types.AnimeApiHisokaType = "hug"
                kiss: _types.AnimeApiHisokaType = "kiss"
                slap: _types.AnimeApiHisokaType = "slap"
                wink: _types.AnimeApiHisokaType = "wink"
                pat: _types.AnimeApiHisokaType = "pat"
                kill: _types.AnimeApiHisokaType = "kill"
                cuddle: _types.AnimeApiHisokaType = "cuddle"
                punch: _types.AnimeApiHisokaType = "punch"
                waifu: _types.AnimeApiHisokaType = "waifu"

            class NSFW:
                hentai: _types.AnimeApiHisokaType = "hentai"
                boobs: _types.AnimeApiHisokaType = "boobs"
                lesbian: _types.AnimeApiHisokaType = "lesbian"

        def get(query: Union[_types.AnimeApiHisokaType, str], nsfw: bool = False) -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from anime-api.hisoka17.repl.co

            Args:
                query (AnimeApiHisokaType): See Parser/asyncParser.AnimeApiHisoka.types

            Returns:
                Models.Result
            """
            return Models.Result(
                url=requests.get(
                    f"https://anime-api.hisoka17.repl.co/img/{('nsfw/'+query) if nsfw else query}").json()['url']
            )

    class AniPics:
        def get(self) -> Union[Models.Result, Coroutine[None, None, Models.Result]]:
            """Get picture from animepicsx.net

            Returns:
                Models.Result
            """
            return Models.Result(
                url=BeautifulSoup(requests.get(
                    "https://animepicsx.net/random").text, "html.parser").find("img")["src"]
            )
