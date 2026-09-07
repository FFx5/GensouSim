from activities.activity import ACTIVITIES
from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

reimu = Character("Reimu Hakurei", "Hakurei Shrine")
marisa = Character("Marisa Kirisame", "Hakurei Shrine")
alice = Character("Alice Margatroid", "Forest of Magic")

world.add_character(reimu)
world.add_character(marisa)
world.add_character(alice)

assert "Talking" in ACTIVITIES
assert ACTIVITIES["Talking"].relationship_effects == [
    {
        "target": "characters_at_location",
        "effects": {
            "affinity": 1,
            "trust": 1
        }
    }
]

reimu.activity_completed_this_tick = "Talking"
world.apply_relationship_effects(reimu)

assert reimu.get_relationship(marisa).affinity == 1
assert reimu.get_relationship(marisa).trust == 1
assert reimu.get_relationship(alice).affinity == 0
assert reimu.get_relationship(alice).trust == 0

print("Talking activity test passed.")
