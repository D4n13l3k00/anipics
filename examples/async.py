import asyncio

from anipics import (
    AsyncNekosAPI,
    AsyncNekosBest,
    AsyncNekosia,
    AsyncNekosLife,
    AsyncPurrBot,
    AsyncWaifuBest,
)


async def main():
    na = AsyncNekosAPI()
    nb = AsyncNekosBest()
    nl = AsyncNekosLife()
    ns = AsyncNekosia()
    pb = AsyncPurrBot()

    print("NekosAPI random:")
    print((await na.get(AsyncNekosAPI.Types.kemonomimi)).url)

    print("NekosAPI metadata:")
    image = await na.get_random_image(tags=[AsyncNekosAPI.Types.girl])
    print(image.id, image.url)

    print("NekosBest:")
    print((await nb.get(AsyncNekosBest.Types.hug)).url)

    print("NekosBest categories:")
    print(", ".join(list(await nb.get_endpoints())[:5]))

    print("NekosLife:")
    print((await nl.get(AsyncNekosLife.Types.avatar)).url)

    print("Nekosia:")
    print((await ns.get(AsyncNekosia.Types.catgirl)).url)

    print("Nekosia main categories:")
    print(", ".join(AsyncNekosia.MAIN_CATEGORIES[:5]))

    print("Nekosia tag search:")
    print(
        (
            await ns.get(
                AsyncNekosia.Types.nothing, additional_tags=["catgirl", "blue-eyes"]
            )
        ).url
    )

    print("WaifuBest filtered:")
    wb = AsyncWaifuBest()
    print(
        (
            await wb.get(
                AsyncWaifuBest.Types.waifu, excluded_tags=[AsyncWaifuBest.Types.maid]
            )
        ).url
    )

    print("WaifuBest tags:")
    print(", ".join(tag["slug"] for tag in await wb.get_tags()))

    print("PurrBot SFW:")
    print((await pb.get(AsyncPurrBot.Types.SFW.GIF.neko)).url)

    print("PurrBot NSFW:")
    print((await pb.get(AsyncPurrBot.Types.NSFW.GIF.anal)).url)


if __name__ == "__main__":
    asyncio.run(main())
