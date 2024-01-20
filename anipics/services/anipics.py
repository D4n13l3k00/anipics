
import httpx
from bs4 import BeautifulSoup

from anipics.models import Models


class AniPics:
    def get(self) -> Models.Result:
        """Get picture from animepicsx.net

        Returns:
            Models.Result
        """
        with httpx.Client() as client:
            return Models.Result(
                url=BeautifulSoup(
                    client.get("https://animepicsx.net/random").text, "html.parser"
                ).find("img")["src"]
            )

    async def async_get(self) -> Models.Result:
        """Get picture from animepicsx.net

        Returns:
            Models.Result
        """
        async with httpx.AsyncClient() as client:
            return Models.Result(
                url=BeautifulSoup(
                    (await client.get("https://animepicsx.net/random")).text,
                    "html.parser",
                ).find("img")["src"]
            )
