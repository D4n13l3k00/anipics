from typing import Any

from pydantic import BaseModel, ConfigDict


class Models:
    class Result(BaseModel):
        url: str

    class NekosAPIImage(BaseModel):
        model_config = ConfigDict(extra="allow")

        id: int
        url: str
        rating: str | None = None
        tags: list[Any] | None = None

        def __getitem__(self, key: str) -> Any:
            return getattr(self, key)
