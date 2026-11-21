from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Range

class WorldLootCount(Range):
    """How many World Loot Checks to generate."""
    display_name = "World Loot Checks"
    range_start = 30
    range_end = 500
    default = 50

class WorldLootChance(Range):
    """How likely is any World Item to become a World Loot Check."""
    display_name = "World Loot Chance"
    range_start = 10
    range_end = 90
    default = 50

class DeathLink(Toggle):
    """Share deaths with other DeathLink players."""
    display_name = "Death Link"

@dataclass
class CatharageOptions(PerGameCommonOptions):
    death_link: DeathLink
    world_loot_count: WorldLootCount
    world_loot_chance: WorldLootChance

