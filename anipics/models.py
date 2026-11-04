from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict


class Models:
    class Result(BaseModel):
        url: str

    class NekosAPITag(BaseModel):
        model_config = ConfigDict(extra="allow")

        id: str
        name: str
        is_nsfw: bool
        created_at: datetime
        updated_at: datetime

    class NekosAPIImage(BaseModel):
        model_config = ConfigDict(extra="allow")

        id: str
        url: str
        rating: Literal["safe", "suggestive", "borderline", "explicit"]
        color_primary: str
        color_palette: list[str]
        source_id: str | None
        source_url: str | None
        artist_name: str | None
        tags: list["Models.NekosAPITag"]
        created_at: datetime
        updated_at: datetime

        def __getitem__(self, key: str) -> Any:
            return getattr(self, key)

    class NekosAPIImagesPage(BaseModel):
        items: list["Models.NekosAPIImage"]
        total: int

    class NekosAPITagsPage(BaseModel):
        items: list["Models.NekosAPITag"]
        total: int
