import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

world.add_location("Hakurei Shrine")

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {
        "Maintaining the shrine": 5,
        "Resting": 3,
        "Wandering": 2,
        "Exploring": 1
    }
)

world.add_character(reimu)

reimu.activity = "Eating"
reimu.needs.hunger = 80

reimu.activity_start_time = world.current_time
reimu.activity_end_time = (
    world.current_time + timedelta(hours=3)
)

print("Starting eating test:")
print(
    f"Energy: {reimu.needs.energy:.1f} | "
    f"Hunger: {reimu.needs.hunger:.1f} | "
    f"Activity: {reimu.activity}"
)

print()

for _ in range(4):
    world.clock.advance(timedelta(minutes=30))
    world.tick()

    print(
        f"Time: {world.current_time.strftime('%H:%M:%S')} | "
        f"Energy: {reimu.needs.energy:.1f} | "
        f"Hunger: {reimu.needs.hunger:.1f} | "
        f"Activity: {reimu.activity}"
    )