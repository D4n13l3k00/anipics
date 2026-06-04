import asyncio

from anipics import NekosAPI, NekosBest, Nekosia, NekosLife, PurrBot, WaifuIm


async def main():
    na = NekosAPI()
    nb = NekosBest()
    nl = NekosLife()
    ns = Nekosia()
    pb = PurrBot()
    wi = WaifuIm()

    print("NekosAPI random:")
    print((await na.async_get(NekosAPI.Types.kemonomimi)).url)

    print("NekosAPI metadata:")
    image = await na.async_get_random_image(tags=[NekosAPI.Types.girl])
    print(image.id, image.url)

    print("NekosBest:")
    print((await nb.async_get(NekosBest.Types.hug)).url)

    print("NekosBest categories:")
    print(", ".join(list(await nb.async_get_endpoints())[:5]))

    print("NekosLife:")
    print((await nl.async_get(NekosLife.Types.avatar)).url)

    print("Nekosia:")
    print((await ns.async_get(Nekosia.Types.catgirl)).url)

    print("Nekosia main categories:")
    print(", ".join(Nekosia.MAIN_CATEGORIES[:5]))

    print("WaifuIm filtered:")
    print(
        (
            await wi.async_get(
                [WaifuIm.Types.waifu],
                excluded_tags=[WaifuIm.Types.uniform],
                is_nsfw=WaifuIm.Nsfw.false,
            )
        ).url
    )

    print("WaifuIm tags:")
    print(", ".join(WaifuIm.TAGS[:5]))

    print("PurrBot SFW:")
    print((await pb.async_get(PurrBot.Types.SFW.GIF.neko)).url)

    print("PurrBot NSFW:")
    print((await pb.async_get(PurrBot.Types.NSFW.GIF.anal)).url)


if __name__ == "__main__":
    asyncio.run(main())
