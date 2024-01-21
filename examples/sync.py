# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

from anipics import AnimePicsX, NekosLife, WaifuPics


def main():
    ap = AnimePicsX()
    nl = NekosLife()
    wp = WaifuPics()

    print("AnimePicsX:")
    print(ap.get().url)

    print("NekosLife:")
    print(nl.get(NekosLife.Types.avatar).url)

    print("WaifuPics SFW:")
    print(wp.get(WaifuPics.Types.SFW.hug, False).url)

    print("WaifuPics NSFW:")
    print(wp.get(WaifuPics.Types.NSFW.blowjob, True).url)


if __name__ == "__main__":
    main()
