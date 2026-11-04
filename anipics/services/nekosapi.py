from collections.abc import Sequence
from typing import Any

from anipics._catalogs.nekosapi import NekosAPIRating, NekosAPIType
from anipics._catalogs.nekosapi import Ratings as NekosAPIRatings
from anipics._catalogs.nekosapi import Types as NekosAPITypes
from anipics.models import Models
from anipics.services._http import (
    async_get_json,
    compact_params,
    get_json,
    normalize_list,
)


class _NekosAPI:
    BASE_URL = "https://api.nekosapi.com/v5"

    Types = NekosAPITypes

    Ratings = NekosAPIRatings

    @staticmethod
    def _image_params(
        tags: Sequence[NekosAPIType | str] | None,
        rating: NekosAPIRating | Sequence[NekosAPIRating] | None,
        artists: Sequence[str] | None,
        *,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        return compact_params(
            limit=limit,
            offset=offset,
            tag=tags,
            rating=normalize_list(rating),
            artist=artists,
        )

    @staticmethod
    def _tag_params(
        limit: int,
        offset: int,
        name: str | None,
        is_nsfw: bool | None,
    ) -> dict[str, Any]:
        return compact_params(
            limit=limit,
            offset=offset,
            name=name,
            is_nsfw=is_nsfw,
        )


class NekosAPI(_NekosAPI):
    def _get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return get_json(f"{self.BASE_URL}{path}", params=params)

    def get(self, query: NekosAPIType | str | None = None) -> Models.Result:
        """Get one random picture from nekosapi.com."""
        image = self.get_random_image(tags=normalize_list(query))
        return Models.Result(url=image.url)

    def get_random_image(
        self,
        tags: Sequence[NekosAPIType | str] | None = None,
        rating: NekosAPIRating | Sequence[NekosAPIRating] | None = None,
        artists: Sequence[str] | None = None,
    ) -> Models.NekosAPIImage:
        """Get one image, matching any supplied tag, artist, and rating.

        Tags accept names or IDs; names and artists are case-insensitive.
        Each filter accepts alternatives (OR), with up to five tags/artists.
        Different filters combine with AND. HTTP errors propagate unchanged.
        """
        return Models.NekosAPIImage.model_validate(
            self._get_json(
                "/images/random",
                params=self._image_params(tags, rating, artists),
            )
        )

    def get_image_by_id(self, image_id: str) -> Models.NekosAPIImage:
        """Get one image by its v5 string ID."""
        return Models.NekosAPIImage.model_validate(
            self._get_json(f"/images/{image_id}")
        )

    def get_images(
        self,
        limit: int = 25,
        offset: int = 0,
        tags: Sequence[NekosAPIType | str] | None = None,
        rating: NekosAPIRating | Sequence[NekosAPIRating] | None = None,
        artists: Sequence[str] | None = None,
    ) -> Models.NekosAPIImagesPage:
        """Get an image page and total, using the random-image filter semantics.

        The API supports up to 100 items per page.
        """
        return Models.NekosAPIImagesPage.model_validate(
            self._get_json(
                "/images",
                params=self._image_params(
                    tags, rating, artists, limit=limit, offset=offset
                ),
            )
        )

    def get_tags(
        self,
        limit: int = 25,
        offset: int = 0,
        name: str | None = None,
        is_nsfw: bool | None = None,
    ) -> Models.NekosAPITagsPage:
        """Get a name-ordered tag page and total, optionally filtering by substring.

        The API supports up to 100 items per page. Use is_nsfw to filter
        explicitly for NSFW or SFW tags.
        """
        return Models.NekosAPITagsPage.model_validate(
            self._get_json(
                "/tags",
                params=self._tag_params(limit, offset, name, is_nsfw),
            )
        )


class AsyncNekosAPI(_NekosAPI):
    async def _get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return await async_get_json(f"{self.BASE_URL}{path}", params=params)

    async def get(self, query: NekosAPIType | str | None = None) -> Models.Result:
        """Get one random picture from nekosapi.com."""
        image = await self.get_random_image(tags=normalize_list(query))
        return Models.Result(url=image.url)

    async def get_random_image(
        self,
        tags: Sequence[NekosAPIType | str] | None = None,
        rating: NekosAPIRating | Sequence[NekosAPIRating] | None = None,
        artists: Sequence[str] | None = None,
    ) -> Models.NekosAPIImage:
        """Get one image, matching any supplied tag, artist, and rating.

        Tags accept names or IDs; names and artists are case-insensitive.
        Each filter accepts alternatives (OR), with up to five tags/artists.
        Different filters combine with AND. HTTP errors propagate unchanged.
        """
        return Models.NekosAPIImage.model_validate(
            await self._get_json(
                "/images/random",
                params=self._image_params(tags, rating, artists),
            )
        )

    async def get_image_by_id(self, image_id: str) -> Models.NekosAPIImage:
        """Asynchronously get one image by its v5 string ID."""
        return Models.NekosAPIImage.model_validate(
            await self._get_json(f"/images/{image_id}")
        )

    async def get_images(
        self,
        limit: int = 25,
        offset: int = 0,
        tags: Sequence[NekosAPIType | str] | None = None,
        rating: NekosAPIRating | Sequence[NekosAPIRating] | None = None,
        artists: Sequence[str] | None = None,
    ) -> Models.NekosAPIImagesPage:
        """Get an image page and total, using the random-image filter semantics.

        The API supports up to 100 items per page.
        """
        return Models.NekosAPIImagesPage.model_validate(
            await self._get_json(
                "/images",
                params=self._image_params(
                    tags, rating, artists, limit=limit, offset=offset
                ),
            )
        )

    async def get_tags(
        self,
        limit: int = 25,
        offset: int = 0,
        name: str | None = None,
        is_nsfw: bool | None = None,
    ) -> Models.NekosAPITagsPage:
        """Get a name-ordered tag page and total, optionally filtering by substring.

        The API supports up to 100 items per page. Use is_nsfw to filter
        explicitly for NSFW or SFW tags.
        """
        return Models.NekosAPITagsPage.model_validate(
            await self._get_json(
                "/tags",
                params=self._tag_params(limit, offset, name, is_nsfw),
            )
        )
