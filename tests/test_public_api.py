from pathlib import Path

import anipics
from anipics import EscapedQuery, Models, NekosAPI, Nekosia


def test_public_api_exports_current_services_only():
    assert set(anipics.__all__) == {
        "EscapedQuery",
        "Models",
        "NekosAPI",
        "NekosBest",
        "NekosLife",
        "Nekosia",
        "PurrBot",
        "WaifuIm",
    }
    assert not hasattr(anipics, "AnimePicsX")
    assert not hasattr(anipics, "WaifuPics")


def test_package_has_pep_561_marker():
    assert (Path(anipics.__path__[0]) / "py.typed").is_file()


def test_escaped_query_escapes_nekosapi_special_characters():
    assert str(EscapedQuery("`[` or `]` or maybe `*`?")) == (
        r"`\[` or `\]` or maybe `\*`\?"
    )


def test_nekosia_main_categories_match_types():
    documented_categories = {
        Nekosia.Types.random,
        Nekosia.Types.catgirl,
        Nekosia.Types.foxgirl,
        Nekosia.Types.wolfgirl,
        Nekosia.Types.animal_ears,
        Nekosia.Types.tail,
        Nekosia.Types.tail_with_ribbon,
        Nekosia.Types.tail_from_under_skirt,
        Nekosia.Types.cute,
        Nekosia.Types.cuteness_is_justice,
        Nekosia.Types.blue_archive,
        Nekosia.Types.girl,
        Nekosia.Types.young_girl,
        Nekosia.Types.maid,
        Nekosia.Types.maid_uniform,
        Nekosia.Types.vtuber,
        Nekosia.Types.w_sitting,
        Nekosia.Types.lying_down,
        Nekosia.Types.hands_forming_a_heart,
        Nekosia.Types.wink,
        Nekosia.Types.valentine,
        Nekosia.Types.headphones,
        Nekosia.Types.thigh_high_socks,
        Nekosia.Types.knee_high_socks,
        Nekosia.Types.white_tights,
        Nekosia.Types.black_tights,
        Nekosia.Types.heterochromia,
        Nekosia.Types.uniform,
        Nekosia.Types.sailor_uniform,
        Nekosia.Types.hoodie,
        Nekosia.Types.ribbon,
        Nekosia.Types.white_hair,
        Nekosia.Types.blue_hair,
        Nekosia.Types.long_hair,
        Nekosia.Types.blonde,
        Nekosia.Types.blue_eyes,
        Nekosia.Types.purple_eyes,
    }
    assert set(Nekosia.MAIN_CATEGORIES) == documented_categories


def test_nekosapi_metadata_methods_return_models():
    class FakeNekosAPI(NekosAPI):
        def _get_json(self, path, params=None):
            if path == "/images/random":
                return [
                    {
                        "id": 42,
                        "url": "https://example.test/image.png",
                        "rating": "safe",
                        "tags": ["neko"],
                    }
                ]
            if path == "/images/42":
                return {
                    "id": 42,
                    "url": "https://example.test/image.png",
                    "rating": "safe",
                    "tags": ["neko"],
                }
            if path == "/images":
                return {
                    "items": [
                        {
                            "id": 42,
                            "url": "https://example.test/image.png",
                            "rating": "safe",
                            "tags": ["neko"],
                        }
                    ]
                }
            raise AssertionError(path)

    client = FakeNekosAPI()

    image = client.get_random_image(tags=[NekosAPI.Types.neko])
    assert isinstance(image, Models.NekosAPIImage)
    assert image.id == 42
    assert image.url == "https://example.test/image.png"
    assert image.rating == "safe"
    assert image.tags == ["neko"]

    assert isinstance(client.get_random_images()[0], Models.NekosAPIImage)
    assert isinstance(client.get_image_by_id(42), Models.NekosAPIImage)
    assert isinstance(client.get_images()[0], Models.NekosAPIImage)
