from BaseClasses import Location
from .items import BASE_ID

class CatharageLocation(Location):
    game = "Catharage"

# name -> (offset, region)
location_table: dict[str, tuple[int, str]] = {
    "Sentinel 1 OBJ Check": (0, "Sentinel 1"),
    "Sentinel 2 OBJ Check": (1, "Sentinel 2"),
    "Sentinel 3 OBJ Check": (2, "Sentinel 3"),
    "Hematic 1 OBJ Check": (3, "Hematic 1"),
    "Hematic 2 OBJ Check": (4, "Hematic 2"),
    "Hematic 3 OBJ Check": (5, "Hematic 3"),
    "Hematic 4 OBJ Check": (6, "Hematic 4"),
    "Verdant 1 OBJ Check": (7, "Verdant 1"),
    "Verdant 2 OBJ Check": (8, "Verdant 2"),
    "Verdant 3 OBJ Check": (9, "Verdant 3"),
    "Verdant 4 OBJ Check": (10, "Verdant 4"),
    "Verdant 5 OBJ Check": (11, "Verdant 5"),
    "Tyrian 1 OBJ Check": (12, "Tyrian 1"),
    "Tyrian 2 OBJ Check": (13, "Tyrian 2"),
    "Tyrian 3 OBJ Check": (14, "Tyrian 3"),
    "Blackguard 1 OBJ Check": (15, "Blackguard 1"),
    "Blackguard 2 OBJ Check": (16, "Blackguard 2"),
    "Blackguard 3 OBJ Check": (17, "Blackguard 3"),
    "Blackguard 4 OBJ Check": (18, "Blackguard 4"),
    "Blackguard 5 OBJ Check": (19, "Blackguard 5"),
    "Blackguard 6 OBJ Check": (20, "Blackguard 6"),
    "Victory Check": (1000, "Credits_scene"),
}

MAX_WORLD_LOOT = 500

# dynamically name world loot based on how many we have
def world_loot_name(n: int) -> str:
    return f"World Loot {n}"

location_name_to_id = {name: BASE_ID + data[0] for name, data in location_table.items()}
location_name_to_id.update(
    {world_loot_name(n): BASE_ID + 20 + n for n in range(1, MAX_WORLD_LOOT + 1)}
)