<!--
 Copyright 2021 D4n13l3k00.
 SPDX-License-Identifier: 	AGPL-3.0-or-later
-->

# Anipics

## Simple module for getting anime pictures

### Installation:

`pip install anipics`

### Usage:

```python
from anipics.parser import Parser

nk = Parser.NekosLife

print(nk.get(nk.types.neko).url)

ap = Parser.AniPics

print(ap.get().url)
```