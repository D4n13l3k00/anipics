# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

import asyncio

from anipics import AnimePicsX, NekosLife, WaifuPics, PurrBot


async def main():
    ap = AnimePicsX()
    nl = NekosLife()
    wp = WaifuPics()
    pb = PurrBot()

    print("AnimePicsX:")
    print((await ap.async_get()).url)

    print("NekosLife:")
    print((await nl.async_get(NekosLife.Types.avatar)).url)

    print("WaifuPics SFW:")
    print((await wp.async_get(WaifuPics.Types.SFW.hug, False)).url)

    print("WaifuPics NSFW:")
    print((await wp.async_get(WaifuPics.Types.NSFW.blowjob, True)).url)

    print("PurrBot SFW:")
    print((await pb.async_get(PurrBot.Types.SFW.GIF.neko)).url)

    print("PurrBot NSFW:")
    print((await pb.async_get(PurrBot.Types.NSFW.GIF.anal)).url)


if __name__ == "__main__":
    asyncio.run(main())
