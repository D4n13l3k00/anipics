# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier:  AGPL-3.0-or-later

from typing import *

from pydantic import BaseModel


class Models:
    class Result(BaseModel):
        url: str
