import random

from activities.activity import ACTIVITIES
from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    activity_preferences={
        "Maintaining the shrine": 5,
        "Resting": 3,
        "Wandering": 2,
        "Exploring": 1,
        "Talking": 1
    }
)
marisa = Character("Marisa Kirisame", "Hakurei Shrine")

world.add_character(reimu)
world.add_character(marisa)

assert "Talking" in ACTIVITIES

random.seed(2)
reimu.choose_activity(world.current_time)

assert reimu.activity == "Talking"
assert reimu.activity_start_time == world.current_time
assert reimu.activity_end_time is not None

print("Talking activity selection test passed.")
