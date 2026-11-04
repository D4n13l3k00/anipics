from pathlib import Path

import anipics


def test_package_has_pep_561_marker():
    assert (Path(anipics.__path__[0]) / "py.typed").is_file()
