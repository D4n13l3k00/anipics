# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from anipics import AnimePicsX, NekosLife, WaifuPics, PurrBot


def main():
    ap = AnimePicsX()
    nl = NekosLife()
    wp = WaifuPics()
    pb = PurrBot()

    print("AnimePicsX:")
    print(ap.get().url)

    print("NekosLife:")
    print(nl.get(NekosLife.Types.avatar).url)

    print("WaifuPics SFW:")
    print(wp.get(WaifuPics.Types.SFW.hug).url)

    print("WaifuPics NSFW:")
    print(wp.get(WaifuPics.Types.NSFW.blowjob).url)

    print("PurrBot SFW:")
    print(pb.get(PurrBot.Types.SFW.GIF.neko).url)

    print("PurrBot NSFW:")
    print(pb.get(PurrBot.Types.NSFW.GIF.anal).url)


if __name__ == "__main__":
    main()
