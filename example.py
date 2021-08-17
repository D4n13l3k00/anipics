# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier:  AGPL-3.0-or-later

import asyncio

from anipics import Parser, asyncParser


def sync_example():
    nk = Parser.NekosLife
    print(nk.get(nk.types.spank).url)
    ap = Parser.AniPics
    print(ap.get().url)
    aah = Parser.AnimeApiHisoka
    print(aah.get(aah.types.SFW.waifu).url)


async def async_example():
    nk = asyncParser.NekosLife
    print((await nk.get(nk.types.neko)).url)
    ap = asyncParser.AniPics
    print((await ap.get()).url)
    aah = asyncParser.AnimeApiHisoka
    print((await aah.get(aah.types.SFW.waifu, True)).url)


if __name__ == '__main__':
    sync_example()
    asyncio.run(async_example())
