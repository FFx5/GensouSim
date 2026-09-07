import time

from world.world import World
from characters.character import Character
from characters.goal import Goal


world = World()

world.add_location("Hakurei Shrine")
world.add_location("Human Village")
world.add_location("Forest of Magic")

world.locations["Hakurei Shrine"]["maintenance_needed"] = True

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
    },
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

marisa = Character(
    "Marisa Kirisame",
    "Forest of Magic",
    {
        "Exploring": 5,
        "Studying magic": 4,
        "Wandering": 3,
        "Resting": 1
    },
    goals=[
        Goal(
            "Study magic",
            "Continue improving magical knowledge.",
            priority=3,
            preferred_activities=["Studying magic"]
        )
    ]
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

print("Goals:")

for character in world.characters.values():
    for goal in character.get_active_goals():
        print(
            f" - {character.name}: "
            f"{goal.name} (Priority {goal.priority})"
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
