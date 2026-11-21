from typing import NamedTuple
from BaseClasses import Item, ItemClassification as IC

BASE_ID = 8_243_196

class CatharageItem(Item):
    game = "Catharage"

class ItemData(NamedTuple):
    offset: int
    classification: IC
    count: int = 1

item_table: dict[str, ItemData] = {"Sentinel Keystone":   ItemData(0, IC.progression, 3),
"Hematic Guardian":     ItemData(3, IC.progression, 4),
"Verdant Hive":         ItemData(7, IC.progression, 5),
"Tyrian Vault":         ItemData(12, IC.progression, 3),
"Blackguard Obelisk":   ItemData(15, IC.progression, 6),
"Battleship":           ItemData(21, IC.useful),
"Mothership":           ItemData(22, IC.useful),
"Odachi":               ItemData(23, IC.useful),
"Covert Ops":           ItemData(24, IC.useful),
"Lancer":               ItemData(25, IC.useful),
"Dreadnought":          ItemData(26, IC.useful),
"Drone Carrier":        ItemData(27, IC.useful),
"Mosquito":             ItemData(28, IC.useful),
"Wasp":                 ItemData(29, IC.useful),
"Butterfly":            ItemData(30, IC.useful),
"Queen":                ItemData(31, IC.useful),
"Ant":                  ItemData(32, IC.useful),
"Mollusc":              ItemData(33, IC.useful),
"Balaeno":              ItemData(34, IC.useful),
"Scion":                ItemData(35, IC.useful),
"Imp":                  ItemData(36, IC.useful),
"Djinn":                ItemData(37, IC.useful),
"Succubus":             ItemData(38, IC.useful),
"Cambion":              ItemData(39, IC.useful),
"Demon":                ItemData(40, IC.useful),
"Baal":                 ItemData(41, IC.useful),
"Shield Delay":         ItemData(42, IC.useful),
"Armor Regen":          ItemData(43, IC.useful),
"Drone Armor":          ItemData(44, IC.useful),
"Signature":            ItemData(45, IC.useful),
"Warp Difficulty":      ItemData(46, IC.useful),
"Item Drop":            ItemData(52, IC.filler, 0),
"Credit Drop":          ItemData(53, IC.filler, 0),
"Scrap Drop":           ItemData(55, IC.filler, 0),
"Energy Cells":         ItemData(56, IC.filler, 0),
"Plasteel":             ItemData(57, IC.filler, 0),
"Exotic Matter":        ItemData(58, IC.filler, 0),
"Ambush":               ItemData(54, IC.trap, 0),
}
filler_items = ["Item Drop", "Credit Drop", "Scrap Drop", "Energy Cells", "Plasteel", "Exotic Matter", "Ambush"]

item_name_to_id = {n: BASE_ID + d.offset for n, d in item_table.items()}