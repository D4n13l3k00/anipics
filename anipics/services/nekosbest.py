from typing import Any

from anipics._catalogs.nekosbest import NekosBestType
from anipics._catalogs.nekosbest import Types as NekosBestTypes
from anipics.models import Models
from anipics.services._http import async_get_json, get_json


class _NekosBestBase:
    ENDPOINT = "https://nekos.best/api/v2/{query}"

    Types = NekosBestTypes

    @staticmethod
    def _parse_result(data: Any) -> Models.Result:
        return Models.Result(url=data["results"][0]["url"])


class NekosBest(_NekosBestBase):
    def get_endpoints(self) -> dict[str, dict[str, str]]:
        """Get available categories and formats from nekos.best."""
        return get_json(self.ENDPOINT.format(query="endpoints"))

    def get(self, query: NekosBestType | str = NekosBestTypes.hug) -> Models.Result:
        """Get picture from nekos.best."""
        data = get_json(self.ENDPOINT.format(query=query))
        return self._parse_result(data)


class AsyncNekosBest(_NekosBestBase):
    async def get_endpoints(self) -> dict[str, dict[str, str]]:
        """Get available categories and formats from nekos.best."""
        return await async_get_json(self.ENDPOINT.format(query="endpoints"))

    async def get(
        self, query: NekosBestType | str = NekosBestTypes.hug
    ) -> Models.Result:
        """Get picture from nekos.best."""
        data = await async_get_json(self.ENDPOINT.format(query=query))
        return self._parse_result(data)
