from typing import Any

from anipics._catalogs.nekoslife import NekosLifeType
from anipics._catalogs.nekoslife import Types as NekosLifeTypes
from anipics.models import Models
from anipics.services._http import async_get_json, get_json


class _NekosLifeBase:
    ENDPOINT = "https://nekos.life/api/v2/img/{query}"

    Types = NekosLifeTypes

    @staticmethod
    def _parse_result(data: Any) -> Models.Result:
        return Models.Result(url=data["url"])


class NekosLife(_NekosLifeBase):
    def get(self, query: NekosLifeType | str) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType | str): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = get_json(self.ENDPOINT.format(query=query))
        return self._parse_result(data)


class AsyncNekosLife(_NekosLifeBase):
    async def get(self, query: NekosLifeType | str) -> Models.Result:
        """Get picture from nekos.life

        Args:
            query (NekosLifeType | str): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = await async_get_json(self.ENDPOINT.format(query=query))
        return self._parse_result(data)
