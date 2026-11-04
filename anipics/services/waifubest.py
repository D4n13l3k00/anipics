from collections.abc import Sequence
from typing import Any

from anipics._catalogs.waifubest import TAGS as WaifuBestTags
from anipics._catalogs.waifubest import Nsfw as WaifuBestNsfwValues
from anipics._catalogs.waifubest import Types as WaifuBestTypes
from anipics._catalogs.waifubest import WaifuBestNsfw, WaifuBestType
from anipics.models import Models
from anipics.services._http import async_get_json, get_json, normalize_list


class _WaifuBestBase:
    ENDPOINT = "https://api.waifu.best/images"
    TAGS_ENDPOINT = "https://api.waifu.best/tags"
    TAGS = WaifuBestTags

    Nsfw = WaifuBestNsfwValues

    Types = WaifuBestTypes

    @staticmethod
    def _params(
        query: WaifuBestType | str | Sequence[WaifuBestType | str],
        excluded_tags: Sequence[WaifuBestType | str] | None,
        is_nsfw: WaifuBestNsfw,
    ) -> list[tuple[str, str]]:
        params: list[tuple[str, str]] = [("isNsfw", is_nsfw)]
        params.extend(("includedTags", tag) for tag in normalize_list(query) or [])
        if excluded_tags:
            params.extend(("excludedTags", tag) for tag in excluded_tags)
        return params

    @staticmethod
    def _result(data: dict[str, Any]) -> Models.Result:
        if not data["items"]:
            raise LookupError(
                "WaifuBest returned no images matching the requested tags and "
                "isNsfw filter; NSFW-only tags require isNsfw=True or All."
            )
        return Models.Result(url=data["items"][0]["url"])


class WaifuBest(_WaifuBestBase):
    def get_tags(self) -> list[dict[str, Any]]:
        """Get the current tag records from waifu.best."""
        return get_json(self.TAGS_ENDPOINT)["items"]

    def get(
        self,
        query: (
            WaifuBestType | str | Sequence[WaifuBestType | str]
        ) = WaifuBestTypes.waifu,
        excluded_tags: Sequence[WaifuBestType | str] | None = None,
        is_nsfw: WaifuBestNsfw = WaifuBestNsfwValues.false,
    ) -> Models.Result:
        """Get an image matching all included tags and none of the excluded tags.

        Only SFW images are returned by default. Raises LookupError when no
        images match, including NSFW-only tags requested with isNsfw=False.
        """
        data = get_json(
            self.ENDPOINT,
            params=self._params(query, excluded_tags, is_nsfw),
        )
        return self._result(data)


class AsyncWaifuBest(_WaifuBestBase):
    async def get_tags(self) -> list[dict[str, Any]]:
        """Get the current tag records from waifu.best."""
        return (await async_get_json(self.TAGS_ENDPOINT))["items"]

    async def get(
        self,
        query: (
            WaifuBestType | str | Sequence[WaifuBestType | str]
        ) = WaifuBestTypes.waifu,
        excluded_tags: Sequence[WaifuBestType | str] | None = None,
        is_nsfw: WaifuBestNsfw = WaifuBestNsfwValues.false,
    ) -> Models.Result:
        """Get an image matching all included tags and none of the excluded tags.

        Only SFW images are returned by default. Raises LookupError when no
        images match, including NSFW-only tags requested with isNsfw=False.
        """
        data = await async_get_json(
            self.ENDPOINT,
            params=self._params(query, excluded_tags, is_nsfw),
        )
        return self._result(data)
