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


print("Starting simulation:")
print(
    world.current_time.strftime("%Y-%m-%d %H:%M:%S JST")
)

print()

for _ in range(12):
    world.tick()

    print(
        f"Energy: {reimu.needs.energy:.1f} | "
        f"Hunger: {reimu.needs.hunger:.1f} | "
        f"Activity: {reimu.activity}"
    )

    world.clock.advance(timedelta(minutes=30))