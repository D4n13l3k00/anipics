from collections.abc import Sequence
from typing import Any

from anipics._catalogs.nekosia import MAIN_CATEGORIES as NekosiaMainCategories
from anipics._catalogs.nekosia import NekosiaTag, NekosiaType
from anipics._catalogs.nekosia import Types as NekosiaTypes
from anipics.models import Models
from anipics.services._http import async_get_json, get_json


class _NekosiaBase:
    ENDPOINT = "https://api.nekosia.cat/api/v1/images/{query}"
    TAGS_ENDPOINT = "https://api.nekosia.cat/api/v1/tags"
    MAIN_CATEGORIES = NekosiaMainCategories

    Types = NekosiaTypes

    @staticmethod
    def _params(
        additional_tags: Sequence[NekosiaTag | str] | None,
    ) -> dict[str, str] | None:
        return (
            {"additionalTags": ",".join(additional_tags)}
            if additional_tags is not None
            else None
        )

    @staticmethod
    def _result(data: dict[str, Any]) -> Models.Result:
        return Models.Result(url=data["image"]["original"]["url"])


class Nekosia(_NekosiaBase):
    def get_tags(self) -> list[str]:
        """Get all tags from nekosia.cat."""
        return get_json(self.TAGS_ENDPOINT)["tags"]

    def get(
        self,
        query: NekosiaType | str = NekosiaTypes.catgirl,
        *,
        additional_tags: Sequence[NekosiaTag | str] | None = None,
    ) -> Models.Result:
        """Get a picture, optionally matching additional comma-separated tags.

        The ``nothing`` category requires at least one additional tag and
        bypasses the category's automatic safety filters. It is never selected
        implicitly. Missing tags for ``nothing`` produce an API HTTP 400 error.
        """
        data = get_json(
            self.ENDPOINT.format(query=query),
            params=self._params(additional_tags),
        )
        return self._result(data)


class AsyncNekosia(_NekosiaBase):
    async def get_tags(self) -> list[str]:
        """Get all tags from nekosia.cat."""
        return (await async_get_json(self.TAGS_ENDPOINT))["tags"]

    async def get(
        self,
        query: NekosiaType | str = NekosiaTypes.catgirl,
        *,
        additional_tags: Sequence[NekosiaTag | str] | None = None,
    ) -> Models.Result:
        """Get a picture, optionally matching additional comma-separated tags.

        The ``nothing`` category requires at least one additional tag and
        bypasses the category's automatic safety filters. It is never selected
        implicitly. Missing tags for ``nothing`` produce an API HTTP 400 error.
        """
        data = await async_get_json(
            self.ENDPOINT.format(query=query),
            params=self._params(additional_tags),
        )
        return self._result(data)
