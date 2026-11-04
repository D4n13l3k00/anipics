from typing import Any

from anipics._catalogs.purrbot import PurrBotType
from anipics._catalogs.purrbot import Types as PurrBotTypes
from anipics.models import Models
from anipics.services._http import async_get_json, get_json


class _PurrBotBase:
    ENDPOINT = "https://api.purrbot.site/v2/img/{path}"

    Types = PurrBotTypes

    @staticmethod
    def _parse_result(data: Any) -> Models.Result:
        return Models.Result(url=data["link"])


class PurrBot(_PurrBotBase):
    def get(self, query: PurrBotType | str) -> Models.Result:
        """Get picture from purrbot.site

        Args:
            query (PurrBotType | str): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = get_json(self.ENDPOINT.format(path=query))
        return self._parse_result(data)


class AsyncPurrBot(_PurrBotBase):
    async def get(self, query: PurrBotType | str) -> Models.Result:
        """Get picture from purrbot.site

        Args:
            query (PurrBotType | str): Category of image

        Returns:
            Models.Result: Model with `url` parameter
        """
        data = await async_get_json(self.ENDPOINT.format(path=query))
        return self._parse_result(data)
