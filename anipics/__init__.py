# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier: 	AGPL-3.0-or-later

from aioify import aioify

__all__ = ['Parser', 'asyncParser', 'Models']

from .parser import Parser
from .models import Models


asyncParser: Parser = aioify(Parser, 'asyncParser')
