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

world.add_character(reimu)
world.add_character(marisa)

reimu.activity = "Talking"
reimu.activity_start_time = world.current_time
reimu.activity_end_time = world.current_time + timedelta(minutes=15)

world.clock.set_manual_time(reimu.activity_end_time)
world.tick()

relationship = reimu.get_relationship(marisa)

assert relationship.affinity == 1
assert relationship.trust == 1
assert relationship.respect == 0
assert relationship.fear == 0

print("Talking relationship effects test passed.")
