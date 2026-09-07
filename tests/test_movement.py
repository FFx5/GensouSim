import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

world.add_location("Hakurei Shrine")
world.add_location("Human Village")
world.connect_locations("Hakurei Shrine", "Human Village", travel_time=30)

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {
        "Wandering": 1
    }
)

world.add_character(reimu)

reimu.activity = "Wandering"
reimu.activity_start_time = world.current_time
reimu.activity_end_time = (
    world.current_time + timedelta(minutes=30)
)

print("Starting movement test:")
print(f"Location: {reimu.location} | Activity: {reimu.activity}")

world.clock.advance(timedelta(minutes=30))
world.tick()

print()
print(f"After wandering: {reimu.location} | Activity: {reimu.activity}")

assert reimu.location == "Hakurei Shrine"
assert reimu.activity == "Traveling"
assert reimu.travel_destination == "Human Village"

world.clock.advance(timedelta(minutes=29))
world.tick()

assert reimu.location == "Hakurei Shrine"
assert reimu.activity == "Traveling"

world.clock.advance(timedelta(minutes=1))
world.tick()

print()
print(f"After traveling: {reimu.location} | Activity: {reimu.activity}")

assert reimu.location == "Human Village"
assert reimu.activity != "Traveling"

print()
print("Movement test passed.")
