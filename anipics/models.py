# Copyright 2024 Daniel <D4n13l3k00@yandex.ru>.
# SPDX-License-Identifier:  AGPL-3.0

from pydantic import BaseModel


class Models:
    class Result(BaseModel):
        url: str
