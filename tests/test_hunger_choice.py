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
        "Exploring": 1,
        "Eating": 1
    }
)

world.add_character(reimu)

reimu.needs.hunger = 100

print("Starting hunger choice test:")
print(
    f"Hunger: {reimu.needs.hunger:.1f} | "
    f"Activity: {reimu.activity}"
)

print()

for _ in range(20):
    world.tick()

    weights = reimu.get_activity_weights()

    print(
        f"Time: {world.current_time.strftime('%H:%M:%S')} | "
        f"Hunger: {reimu.needs.hunger:.1f} | "
        f"Activity: {reimu.activity}"
    )

    for activity, weight in weights.items():
        print(f"  {activity}: {weight:.2f}")

    world.clock.advance(timedelta(minutes=30))