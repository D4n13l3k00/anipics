# Copyright 2021 D4n13l3k00.
# SPDX-License-Identifier: 	AGPL-3.0-or-later

from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name='anipics',
      version='1.2',
      description='Simple module for getting anime pictures',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['anipics'],
      author_email='D4n13l3k00@yandex.ru',
      url="https://github.com/D4n13l3k00/anipics",
      zip_safe=False)