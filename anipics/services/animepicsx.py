# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier: AGPL-3.0

import httpx
from bs4 import BeautifulSoup

from anipics.models import Models


class AnimePicsX:
    ENDPOINT = "https://animepicsx.net/random"

    def get(self) -> Models.Result:
        """Get picture from animepicsx.net

        Returns:
            Models.Result: Model with `url` parameter
        """
        with httpx.Client() as client:
            return Models.Result(
                url=BeautifulSoup(client.get(self.ENDPOINT).text, "html.parser").find(
                    "img"
                )["src"]
            )

    async def async_get(self) -> Models.Result:
        """Get picture from animepicsx.net

        Returns:
            Models.Result: Model with `url` parameter
        """
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=BeautifulSoup(
                    (await client.get(self.ENDPOINT)).text,
                    "html.parser",
                ).find("img")["src"]
            )
