from typing import TypeAlias

from anipics.models import Models
from anipics.services._http import async_get_json, get_json

NekosBestType: TypeAlias = str


class NekosBest:
    ENDPOINT = "https://nekos.best/api/v2/{query}"

    class Types:
        baka: NekosBestType = "baka"
        bite: NekosBestType = "bite"
        blush: NekosBestType = "blush"
        bleh: NekosBestType = "bleh"
        blowkiss: NekosBestType = "blowkiss"
        bonk: NekosBestType = "bonk"
        bored: NekosBestType = "bored"
        carry: NekosBestType = "carry"
        clap: NekosBestType = "clap"
        confused: NekosBestType = "confused"
        cry: NekosBestType = "cry"
        cuddle: NekosBestType = "cuddle"
        dance: NekosBestType = "dance"
        facepalm: NekosBestType = "facepalm"
        feed: NekosBestType = "feed"
        handhold: NekosBestType = "handhold"
        handshake: NekosBestType = "handshake"
        happy: NekosBestType = "happy"
        highfive: NekosBestType = "highfive"
        hug: NekosBestType = "hug"
        husbando: NekosBestType = "husbando"
        kabedon: NekosBestType = "kabedon"
        kick: NekosBestType = "kick"
        kiss: NekosBestType = "kiss"
        kitsune: NekosBestType = "kitsune"
        lappillow: NekosBestType = "lappillow"
        laugh: NekosBestType = "laugh"
        lurk: NekosBestType = "lurk"
        neko: NekosBestType = "neko"
        nod: NekosBestType = "nod"
        nom: NekosBestType = "nom"
        nope: NekosBestType = "nope"
        nya: NekosBestType = "nya"
        pat: NekosBestType = "pat"
        peck: NekosBestType = "peck"
        poke: NekosBestType = "poke"
        pout: NekosBestType = "pout"
        punch: NekosBestType = "punch"
        run: NekosBestType = "run"
        salute: NekosBestType = "salute"
        shake: NekosBestType = "shake"
        shocked: NekosBestType = "shocked"
        shoot: NekosBestType = "shoot"
        shrug: NekosBestType = "shrug"
        sip: NekosBestType = "sip"
        slap: NekosBestType = "slap"
        sleep: NekosBestType = "sleep"
        smile: NekosBestType = "smile"
        smug: NekosBestType = "smug"
        spin: NekosBestType = "spin"
        stare: NekosBestType = "stare"
        tableflip: NekosBestType = "tableflip"
        teehee: NekosBestType = "teehee"
        think: NekosBestType = "think"
        thumbsup: NekosBestType = "thumbsup"
        tickle: NekosBestType = "tickle"
        wag: NekosBestType = "wag"
        wave: NekosBestType = "wave"
        wink: NekosBestType = "wink"
        yawn: NekosBestType = "yawn"
        yeet: NekosBestType = "yeet"
        waifu: NekosBestType = "waifu"

    def get_endpoints(self) -> dict[str, dict[str, str]]:
        """Get available categories and formats from nekos.best."""
        return get_json(self.ENDPOINT.format(query="endpoints"))

    async def async_get_endpoints(self) -> dict[str, dict[str, str]]:
        """Get available categories and formats from nekos.best."""
        return await async_get_json(self.ENDPOINT.format(query="endpoints"))

    def get(self, query: NekosBestType = Types.hug) -> Models.Result:
        """Get picture from nekos.best."""
        data = get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["results"][0]["url"])

    async def async_get(self, query: NekosBestType = Types.hug) -> Models.Result:
        """Get picture from nekos.best."""
        data = await async_get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["results"][0]["url"])
