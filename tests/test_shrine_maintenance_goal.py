import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from characters.goal import Goal
from world.world import World


world = World(clock_mode="manual")
world.add_location("Hakurei Shrine")
world.locations["Hakurei Shrine"]["maintenance_needed"] = True

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {"Maintaining the shrine": 1},
    goals=[
        Goal(
            "Maintain the Hakurei Shrine",
            "Keep the shrine in good condition.",
            priority=3,
            preferred_activities=["Maintaining the shrine"],
            condition=lambda character, world: (
                world.locations[character.location]["maintenance_needed"] is False
                and character.last_completed_activity == "Maintaining the shrine"
            )
        )
    ]
)

world.add_character(reimu)

world.tick()

assert reimu.activity == "Maintaining the shrine"
assert world.locations["Hakurei Shrine"]["maintenance_needed"] is True
assert reimu.goals[0].completed is False

activity_end_time = reimu.activity_end_time
world.clock.set_time(activity_end_time)
world.tick()

assert reimu.last_completed_activity == "Maintaining the shrine"
assert world.locations["Hakurei Shrine"]["maintenance_needed"] is False
assert reimu.goals[0].completed is True
assert reimu.get_active_goals() == []

print("Shrine maintenance goal completion test passed.")
