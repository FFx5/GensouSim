from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from characters.character import Character
from characters.goal import Goal
from world.world import World


world = World(clock_mode="manual")
start_time = datetime(2026, 9, 7, 12, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
world.clock.set_manual_time(start_time)

world.add_location("Hakurei Shrine")
shrine = world.locations["Hakurei Shrine"]
shrine["maintenance_needed"] = True
shrine["maintenance_interval"] = timedelta(hours=24)

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {
        "Maintaining the shrine": 5,
        "Resting": 3,
        "Wandering": 2,
        "Exploring": 1
    },
    goals=[
        Goal(
            "Maintain the Hakurei Shrine",
            "Keep the shrine in good condition.",
            priority=3,
            preferred_activities=["Maintaining the shrine"],
            repeatable=True,
            condition=lambda character, world: (
                world.locations[character.location]["maintenance_needed"] is False
                and character.last_completed_activity == "Maintaining the shrine"
            )
        )
    ]
)

world.add_character(reimu)

# Simulate a completed maintenance activity.
reimu.activity = "Maintaining the shrine"
reimu.activity_start_time = start_time - timedelta(minutes=30)
reimu.activity_end_time = start_time
world.tick()

assert shrine["maintenance_needed"] is False
assert shrine["last_maintenance_time"] == start_time
assert reimu.goals[0].completed is True

# Prevent Reimu's normal activity selection from changing the shrine state
# while this test advances time to the deterioration boundary.
reimu.activity_preferences = {}

# The shrine should remain maintained until the full 24-hour interval passes.
world.clock.advance(timedelta(hours=23, minutes=59))
world.tick()

assert shrine["maintenance_needed"] is False
assert reimu.goals[0].completed is True

# One more minute reaches the 24-hour maintenance interval.
world.clock.advance(timedelta(minutes=1))
world.tick()

assert shrine["maintenance_needed"] is True
assert reimu.goals[0].completed is False

print("Shrine deterioration cycle test passed.")
