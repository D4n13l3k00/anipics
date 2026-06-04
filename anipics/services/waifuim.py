from collections.abc import Sequence
from typing import Any, TypeAlias

from anipics.models import Models
from anipics.services._http import async_get_json, get_json, normalize_list

WaifuImType: TypeAlias = str


class WaifuIm:
    ENDPOINT = "https://api.waifu.im/images"
    TAGS_ENDPOINT = "https://api.waifu.im/tags"
    TAGS = (
        "waifu",
        "ero",
        "ecchi",
        "oppai",
        "hentai",
        "milf",
        "uniform",
        "ass",
        "maid",
        "selfies",
        "oral",
        "paizuri",
        "genshin-impact",
        "raiden-shogun",
        "marin-kitagawa",
        "mori-calliope",
        "kamisato-ayaka",
        "rem",
        "arknights",
        "black-clover",
    )

    class Nsfw:
        false = "False"
        true = "True"
        all = "All"

    class Types:
        waifu: WaifuImType = "waifu"
        maid: WaifuImType = "maid"
        uniform: WaifuImType = "uniform"
        selfies: WaifuImType = "selfies"
        marin_kitagawa: WaifuImType = "marin-kitagawa"
        mori_calliope: WaifuImType = "mori-calliope"
        raiden_shogun: WaifuImType = "raiden-shogun"
        oppai: WaifuImType = "oppai"
        ass: WaifuImType = "ass"
        hentai: WaifuImType = "hentai"
        milf: WaifuImType = "milf"
        oral: WaifuImType = "oral"
        paizuri: WaifuImType = "paizuri"
        ecchi: WaifuImType = "ecchi"
        ero: WaifuImType = "ero"
        genshin_impact: WaifuImType = "genshin-impact"
        kamisato_ayaka: WaifuImType = "kamisato-ayaka"
        rem: WaifuImType = "rem"
        arknights: WaifuImType = "arknights"
        black_clover: WaifuImType = "black-clover"

    def get_tags(self) -> list[dict[str, Any]]:
        """Get all tags from waifu.im."""
        return get_json(self.TAGS_ENDPOINT)["items"]

    async def async_get_tags(self) -> list[dict[str, Any]]:
        """Get all tags from waifu.im."""
        return (await async_get_json(self.TAGS_ENDPOINT))["items"]

    @staticmethod
    def _params(
        included_tags: list[str],
        excluded_tags: Sequence[str] | None,
        is_nsfw: str,
    ) -> list[tuple[str, str]]:
        params: list[tuple[str, str]] = [("IsNsfw", is_nsfw)]
        params.extend(("IncludedTags", tag) for tag in included_tags)
        if excluded_tags:
            params.extend(("ExcludedTags", tag) for tag in excluded_tags)
        return params

    @staticmethod
    def _tags(value: WaifuImType | Sequence[str]) -> list[str]:
        return normalize_list(value) or []

    def get(
        self,
        query: WaifuImType | Sequence[str] = Types.waifu,
        excluded_tags: Sequence[str] | None = None,
        is_nsfw: str = Nsfw.false,
    ) -> Models.Result:
        """Get picture from waifu.im."""
        data = get_json(
            self.ENDPOINT,
            params=self._params(self._tags(query), excluded_tags, is_nsfw),
        )
        return Models.Result(url=data["items"][0]["url"])

    async def async_get(
        self,
        query: WaifuImType | Sequence[str] = Types.waifu,
        excluded_tags: Sequence[str] | None = None,
        is_nsfw: str = Nsfw.false,
    ) -> Models.Result:
        """Get picture from waifu.im."""
        data = await async_get_json(
            self.ENDPOINT,
            params=self._params(self._tags(query), excluded_tags, is_nsfw),
        )
        return Models.Result(url=data["items"][0]["url"])
