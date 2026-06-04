from typing import TypeAlias

from anipics.models import Models
from anipics.services._http import async_get_json, get_json

NekosiaType: TypeAlias = str


class Nekosia:
    ENDPOINT = "https://api.nekosia.cat/api/v1/images/{query}"
    TAGS_ENDPOINT = "https://api.nekosia.cat/api/v1/tags"
    MAIN_CATEGORIES = (
        "random",
        "catgirl",
        "foxgirl",
        "wolfgirl",
        "animal-ears",
        "tail",
        "tail-with-ribbon",
        "tail-from-under-skirt",
        "cute",
        "cuteness-is-justice",
        "blue-archive",
        "girl",
        "young-girl",
        "maid",
        "maid-uniform",
        "vtuber",
        "w-sitting",
        "lying-down",
        "hands-forming-a-heart",
        "wink",
        "valentine",
        "headphones",
        "thigh-high-socks",
        "knee-high-socks",
        "white-tights",
        "black-tights",
        "heterochromia",
        "uniform",
        "sailor-uniform",
        "hoodie",
        "ribbon",
        "white-hair",
        "blue-hair",
        "long-hair",
        "blonde",
        "blue-eyes",
        "purple-eyes",
    )

    class Types:
        animal_ears: NekosiaType = "animal-ears"
        black_tights: NekosiaType = "black-tights"
        blonde: NekosiaType = "blonde"
        blue_archive: NekosiaType = "blue-archive"
        blue_eyes: NekosiaType = "blue-eyes"
        blue_hair: NekosiaType = "blue-hair"
        catgirl: NekosiaType = "catgirl"
        cute: NekosiaType = "cute"
        cuteness_is_justice: NekosiaType = "cuteness-is-justice"
        foxgirl: NekosiaType = "foxgirl"
        girl: NekosiaType = "girl"
        hands_forming_a_heart: NekosiaType = "hands-forming-a-heart"
        headphones: NekosiaType = "headphones"
        heterochromia: NekosiaType = "heterochromia"
        hoodie: NekosiaType = "hoodie"
        knee_high_socks: NekosiaType = "knee-high-socks"
        lying_down: NekosiaType = "lying-down"
        long_hair: NekosiaType = "long-hair"
        maid: NekosiaType = "maid"
        maid_uniform: NekosiaType = "maid-uniform"
        nothing: NekosiaType = "nothing"
        purple_eyes: NekosiaType = "purple-eyes"
        random: NekosiaType = "random"
        ribbon: NekosiaType = "ribbon"
        sailor_uniform: NekosiaType = "sailor-uniform"
        tail: NekosiaType = "tail"
        tail_from_under_skirt: NekosiaType = "tail-from-under-skirt"
        tail_with_ribbon: NekosiaType = "tail-with-ribbon"
        thigh_high_socks: NekosiaType = "thigh-high-socks"
        uniform: NekosiaType = "uniform"
        valentine: NekosiaType = "valentine"
        vtuber: NekosiaType = "vtuber"
        white_hair: NekosiaType = "white-hair"
        white_tights: NekosiaType = "white-tights"
        wink: NekosiaType = "wink"
        wolfgirl: NekosiaType = "wolfgirl"
        w_sitting: NekosiaType = "w-sitting"
        young_girl: NekosiaType = "young-girl"

    def get_tags(self) -> list[str]:
        """Get all tags from nekosia.cat."""
        return get_json(self.TAGS_ENDPOINT)["tags"]

    async def async_get_tags(self) -> list[str]:
        """Get all tags from nekosia.cat."""
        return (await async_get_json(self.TAGS_ENDPOINT))["tags"]

    def get(self, query: NekosiaType = Types.catgirl) -> Models.Result:
        """Get picture from nekosia.cat."""
        data = get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["image"]["original"]["url"])

    async def async_get(self, query: NekosiaType = Types.catgirl) -> Models.Result:
        """Get picture from nekosia.cat."""
        data = await async_get_json(self.ENDPOINT.format(query=query))
        return Models.Result(url=data["image"]["original"]["url"])
