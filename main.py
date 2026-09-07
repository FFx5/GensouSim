import time

from world.world import World
from characters.character import Character


world = World()

world.add_location("Hakurei Shrine")
world.add_location("Human Village")
world.add_location("Forest of Magic")

world.connect_locations("Hakurei Shrine", "Human Village")
world.connect_locations("Human Village", "Forest of Magic")

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

marisa = Character(
    "Marisa Kirisame",
    "Forest of Magic",
    {
        "Exploring": 5,
        "Studying magic": 4,
        "Wandering": 3,
        "Resting": 1
    }
)

world.add_character(reimu)
world.add_character(marisa)

print("Gensokyo World")
print("----------------")

print("Current Gensokyo Time:")
print(world.current_time.strftime("%Y-%m-%d %H:%M:%S JST"))

print()

print("Locations:")

for location in world.locations:
    print(f" - {location}")

print()

print("Characters:")

for character in world.characters.values():
    print(
        f" - {character.name} "
        f"({character.location}) - "
        f"{character.activity}"
    )

print()

print("Simulation running...")
print("Press Ctrl+C to stop.")
print()

try:
    while True:
        world.tick()

        time.sleep(1)

except KeyboardInterrupt:
    print()
    print("Simulation stopped.")