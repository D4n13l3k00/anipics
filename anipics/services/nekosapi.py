from collections.abc import Sequence
from typing import Any, TypeAlias

from anipics.models import Models
from anipics.services._http import (
    async_get_json,
    compact_params,
    get_json,
    normalize_list,
)

NekosAPIType: TypeAlias = str


class EscapedQuery:
    ESCAPED_CHARS = set(r"[]{}()*?|")

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return "".join(
            f"\\{char}" if char in self.ESCAPED_CHARS else char for char in self.value
        )


class NekosAPI:
    BASE_URL = "https://api.nekosapi.com/v4"

    class Types:
        animal_ears: NekosAPIType = "animal_ears"
        catgirl: NekosAPIType = "catgirl"
        foxgirl: NekosAPIType = "foxgirl"
        girl: NekosAPIType = "girl"
        kemonomimi: NekosAPIType = "kemonomimi"
        maid: NekosAPIType = "maid"
        neko: NekosAPIType = "neko"
        waifu: NekosAPIType = "waifu"

    class Ratings:
        safe = "safe"
        suggestive = "suggestive"
        borderline = "borderline"

    def _get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return get_json(f"{self.BASE_URL}{path}", params=params)

    async def _async_get_json(
        self, path: str, params: dict[str, Any] | None = None
    ) -> Any:
        return await async_get_json(f"{self.BASE_URL}{path}", params=params)

    def get(self, query: NekosAPIType | None = None) -> Models.Result:
        """Get one random picture from nekosapi.com."""
        image = self.get_random_image(tags=normalize_list(query))
        return Models.Result(url=image["url"])

    def get_random_image(
        self,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> Models.NekosAPIImage:
        """Get one random image with metadata."""
        return self.get_random_images(
            limit=1,
            tags=tags,
            without_tags=without_tags,
            rating=rating,
            artist_name=artist_name,
        )[0]

    def get_random_images(
        self,
        limit: int = 10,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> list[Models.NekosAPIImage]:
        """Get random images with metadata. NekosAPI supports up to 25."""
        images = self._get_json(
            "/images/random",
            params=compact_params(
                limit=limit,
                tags=tags,
                without_tags=without_tags,
                rating=rating,
                artist_name=artist_name,
            ),
        )
        return [Models.NekosAPIImage.model_validate(image) for image in images]

    def get_image_by_id(self, image_id: int) -> Models.NekosAPIImage:
        """Get one image by ID."""
        return Models.NekosAPIImage.model_validate(
            self._get_json(f"/images/{image_id}")
        )

    def get_images(
        self,
        limit: int = 100,
        offset: int = 0,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> list[Models.NekosAPIImage]:
        """Search/browse images with filters."""
        data = self._get_json(
            "/images",
            params=compact_params(
                limit=limit,
                offset=offset,
                tags=tags,
                without_tags=without_tags,
                rating=rating,
                artist_name=artist_name,
            ),
        )
        return [Models.NekosAPIImage.model_validate(image) for image in data["items"]]

    async def async_get(self, query: NekosAPIType | None = None) -> Models.Result:
        """Get one random picture from nekosapi.com."""
        image = await self.async_get_random_image(tags=normalize_list(query))
        return Models.Result(url=image["url"])

    async def async_get_random_image(
        self,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> Models.NekosAPIImage:
        """Get one random image with metadata."""
        images = await self.async_get_random_images(
            limit=1,
            tags=tags,
            without_tags=without_tags,
            rating=rating,
            artist_name=artist_name,
        )
        return images[0]

    async def async_get_random_images(
        self,
        limit: int = 10,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> list[Models.NekosAPIImage]:
        """Get random images with metadata. NekosAPI supports up to 25."""
        images = await self._async_get_json(
            "/images/random",
            params=compact_params(
                limit=limit,
                tags=tags,
                without_tags=without_tags,
                rating=rating,
                artist_name=artist_name,
            ),
        )
        return [Models.NekosAPIImage.model_validate(image) for image in images]

    async def async_get_image_by_id(self, image_id: int) -> Models.NekosAPIImage:
        """Get one image by ID."""
        return Models.NekosAPIImage.model_validate(
            await self._async_get_json(f"/images/{image_id}")
        )

    async def async_get_images(
        self,
        limit: int = 100,
        offset: int = 0,
        tags: Sequence[str] | None = None,
        without_tags: Sequence[str] | None = None,
        rating: str | None = None,
        artist_name: str | None = None,
    ) -> list[Models.NekosAPIImage]:
        """Search/browse images with filters."""
        data = await self._async_get_json(
            "/images",
            params=compact_params(
                limit=limit,
                offset=offset,
                tags=tags,
                without_tags=without_tags,
                rating=rating,
                artist_name=artist_name,
            ),
        )
        return [Models.NekosAPIImage.model_validate(image) for image in data["items"]]
