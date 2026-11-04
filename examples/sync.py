from anipics import NekosAPI, NekosBest, Nekosia, NekosLife, PurrBot, WaifuBest


def main():
    na = NekosAPI()
    nb = NekosBest()
    nl = NekosLife()
    ns = Nekosia()
    pb = PurrBot()

    print("NekosAPI random:")
    print(na.get(NekosAPI.Types.kemonomimi).url)

    print("NekosAPI metadata:")
    image = na.get_random_image(tags=[NekosAPI.Types.girl])
    print(image.id, image.url)

    print("NekosBest:")
    print(nb.get(NekosBest.Types.hug).url)

    print("NekosBest categories:")
    print(", ".join(list(nb.get_endpoints())[:5]))

    print("NekosLife:")
    print(nl.get(NekosLife.Types.avatar).url)

    print("Nekosia:")
    print(ns.get(Nekosia.Types.catgirl).url)

    print("Nekosia main categories:")
    print(", ".join(Nekosia.MAIN_CATEGORIES[:5]))

    print("Nekosia tag search:")
    print(ns.get(Nekosia.Types.nothing, additional_tags=["catgirl", "blue-eyes"]).url)

    print("WaifuBest filtered:")
    wb = WaifuBest()
    print(wb.get(WaifuBest.Types.waifu, excluded_tags=[WaifuBest.Types.maid]).url)

    print("WaifuBest tags:")
    print(", ".join(tag["slug"] for tag in wb.get_tags()))

    print("PurrBot SFW:")
    print(pb.get(PurrBot.Types.SFW.GIF.neko).url)

    print("PurrBot NSFW:")
    print(pb.get(PurrBot.Types.NSFW.GIF.anal).url)


if __name__ == "__main__":
    main()
