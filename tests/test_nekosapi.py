from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from anipics import Models


@pytest.fixture
def image_metadata():
    return {
        "id": "-qeNGVpVNQFrlN8dI7XX3",
        "url": "https://example.test/image.webp",
        "rating": "safe",
        "color_primary": "#4e7f8e",
        "color_palette": ["#ece8e9", "#376b7d"],
        "source_id": None,
        "source_url": None,
        "artist_name": None,
        "tags": [
            {
                "id": "88TmQpWqlTxTbKGN0GvYA",
                "name": "Catgirl",
                "is_nsfw": False,
                "created_at": "2026-07-14T01:36:39Z",
                "updated_at": "2026-07-14T01:36:39Z",
            }
        ],
        "created_at": "2026-07-14T01:36:39Z",
        "updated_at": "2026-07-14T01:36:39Z",
    }


def test_image_page_parses_nested_metadata_and_nullable_fields(image_metadata):
    page = Models.NekosAPIImagesPage.model_validate(
        {"items": [image_metadata], "total": 42}
    )

    image = page.items[0]
    assert isinstance(image, Models.NekosAPIImage)
    assert image.id == "-qeNGVpVNQFrlN8dI7XX3"
    assert isinstance(image.tags[0], Models.NekosAPITag)
    assert image.tags[0].id == "88TmQpWqlTxTbKGN0GvYA"
    assert image.tags[0].name == "Catgirl"
    assert image.tags[0].is_nsfw is False
    assert image.tags[0].created_at == datetime(
        2026, 7, 14, 1, 36, 39, tzinfo=timezone.utc
    )
    assert image.source_id is None
    assert image.source_url is None
    assert image.artist_name is None
    assert page.total == 42


@pytest.mark.parametrize("model", [Models.NekosAPIImagesPage, Models.NekosAPITagsPage])
@pytest.mark.parametrize("total", [0, 42])
def test_empty_page_preserves_total_beyond_requested_offset(model, total):
    page = model.model_validate({"items": [], "total": total})

    assert page.items == []
    assert page.total == total


def test_image_ids_do_not_coerce_legacy_integers(image_metadata):
    image_metadata["id"] = 123

    with pytest.raises(ValidationError) as error:
        Models.NekosAPIImage.model_validate(image_metadata)

    assert error.value.errors()[0]["loc"] == ("id",)
    assert error.value.errors()[0]["type"] == "string_type"
