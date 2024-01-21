# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

import asyncio

from anipics import AnimePicsX, NekosLife, WaifuPics


async def main():
    ap = AnimePicsX()
    nl = NekosLife()
    wp = WaifuPics()

    print("AnimePicsX:")
    print((await ap.async_get()).url)

    print("NekosLife:")
    print((await nl.async_get(NekosLife.Types.avatar)).url)

    print("WaifuPics SFW:")
    print((await wp.get(WaifuPics.Types.SFW.hug, False)).url)

    print("WaifuPics NSFW:")
    print((await wp.get(WaifuPics.Types.NSFW.blowjob, True)).url)


if __name__ == "__main__":
    asyncio.run(main())
