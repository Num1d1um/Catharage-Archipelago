from BaseClasses import Region, LocationProgressType
from worlds.AutoWorld import World, WebWorld
from .items import CatharageItem, item_table, item_name_to_id, filler_items
from .locations import CatharageLocation, location_table, location_name_to_id, world_loot_name
from .options import CatharageOptions
import math

class CatharageWeb(WebWorld):
    theme = "ocean"


SECTOR_ITEM = {"Sentinel": "Sentinel Keystone", "Hematic": "Hematic Guardian",
               "Verdant": "Verdant Hive", "Tyrian": "Tyrian Vault", "Blackguard": "Blackguard Obelisk"}

FINAL_COUNTS = {"Sentinel Keystone": 3, "Hematic Guardian": 4, "Verdant Hive": 5, "Tyrian Vault": 3, "Blackguard Obelisk": 6}

SECTOR_ITEM_NAMES = list(SECTOR_ITEM.values())

class CatharageWorld(World):
    """Catharage is a realtime space tactics roguelite"""
    game = "Catharage"
    web = CatharageWeb()
    options_dataclass = CatharageOptions
    options: CatharageOptions

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_item(self, name: str) -> CatharageItem:
        data = item_table[name]
        return CatharageItem(name, data.classification, item_name_to_id[name], self.player)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        regions = {"Menu": menu}

        for region_name in sorted({data[1] for data in location_table.values()}):
            region = Region(region_name, self.player, self.multiworld)
            regions[region_name] = region
            self.multiworld.regions.append(region)

        for name, data in location_table.items():
            region = regions[data[1]]
            loc = CatharageLocation(self.player, name, location_name_to_id[name], region)
            if name.endswith("OBJ Check"):
                loc.progress_type = LocationProgressType.PRIORITY
            region.locations.append(loc)

        count = self.options.world_loot_count.value
        tier_size = max(10, math.ceil(count / 10))

        for n in range(1, count + 1):
            name = world_loot_name(n)
            loc = CatharageLocation(self.player, name, location_name_to_id[name], menu)

            tier = min((n - 1) // tier_size, 10)
            if tier > 0:
                loc.access_rule = lambda state, t=tier: \
                    state.count_from_list(SECTOR_ITEM_NAMES, self.player) >= t

            menu.locations.append(loc)

        for sector, item in SECTOR_ITEM.items():
            stage_count = FINAL_COUNTS[item]
            menu.connect(regions[f"{sector} 1"])
            for stage in range(2, stage_count + 1):
                regions[f"{sector} {stage - 1}"].connect(
                    regions[f"{sector} {stage}"],
                    rule=lambda state, item=item, n=stage - 1: state.has(item, self.player, n),
                )

        menu.connect(regions["Credits_scene"],
                     rule=lambda state: state.has_all_counts(FINAL_COUNTS, self.player))

        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has_all_counts(FINAL_COUNTS, self.player)

    def create_items(self) -> None:
        pool = [self.create_item(n) for n, d in item_table.items() for _ in range(d.count)]
        unfilled = len(self.multiworld.get_unfilled_locations(self.player))
        while len(pool) < unfilled:
            pool.append(self.create_item(self.random.choice(filler_items)))
        self.multiworld.itempool += pool

    def set_rules(self) -> None:

        pass

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def fill_slot_data(self) -> dict:
        return self.options.as_dict("death_link", "world_loot_count", "world_loot_chance")