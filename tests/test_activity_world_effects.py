from datetime import datetime
from zoneinfo import ZoneInfo

from activities.activity import Activity, ACTIVITIES
from characters.character import Character
from world.world import World


world = World(clock_mode="manual")
start_time = datetime(2026, 9, 7, 12, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
world.clock.set_manual_time(start_time)

world.add_location("Test Location")
location = world.locations["Test Location"]
location["test_flag"] = False
location["test_time"] = None

original_activity = ACTIVITIES.get("Test world effect")

ACTIVITIES["Test world effect"] = Activity(
    "Test world effect",
    30,
    30,
    0,
    0,
    {
        "low": 1.0,
        "medium": 1.0,
        "high": 1.0
    },
    {
        "low": 1.0,
        "medium": 1.0,
        "high": 1.0
    },
    world_effects=[
        {
            "target": "location",
            "location": None,
            "effects": {
                "test_flag": True,
                "test_time": "current_time"
            }
        }
    ]
)

try:
    character = Character("Test Character", "Test Location")
    character.activity_completed_this_tick = "Test world effect"

    world.apply_activity_effects(character)

    assert location["test_flag"] is True
    assert location["test_time"] == start_time

finally:
    if original_activity is None:
        del ACTIVITIES["Test world effect"]
    else:
        ACTIVITIES["Test world effect"] = original_activity

print("Generic activity world effects test passed.")
