from datetime import timedelta

from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    activity_preferences={
        "Talking": 1.0
    }
)
marisa = Character("Marisa Kirisame", "Hakurei Shrine")
youmu = Character("Youmu Konpaku", "Hakurei Shrine")

world.add_character(reimu)
world.add_character(marisa)
world.add_character(youmu)

reimu.activity = "Talking"
reimu.activity_start_time = world.current_time
reimu.activity_end_time = world.current_time + timedelta(minutes=15)

world.clock.set_manual_time(reimu.activity_end_time)
world.tick()

marisa_relationship = reimu.get_relationship(marisa)
youmu_relationship = reimu.get_relationship(youmu)

assert marisa_relationship.affinity == 1
assert marisa_relationship.trust == 1
assert marisa_relationship.respect == 0
assert marisa_relationship.fear == 0

assert youmu_relationship.affinity == 1
assert youmu_relationship.trust == 1
assert youmu_relationship.respect == 0
assert youmu_relationship.fear == 0

assert reimu.get_relationship(reimu).affinity == 0
assert reimu.get_relationship(reimu).trust == 0

# A character alone at a location should not receive relationship effects.
world = World(clock_mode="manual")
alice = Character("Alice Margatroid", "Forest of Magic")
world.add_character(alice)

alice.activity = "Talking"
alice.activity_start_time = world.current_time
alice.activity_end_time = world.current_time + timedelta(minutes=15)

world.clock.set_manual_time(alice.activity_end_time)
world.tick()

assert alice.relationships == {}

print("Talking relationship effects test passed.")
