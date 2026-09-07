import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from characters.goal import Goal
from world.world import World


reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {
        "Maintaining the shrine": 1,
        "Wandering": 1
    },
    goals=[
        Goal(
            "Maintain the Hakurei Shrine",
            "Keep the shrine in good condition.",
            priority=3,
            preferred_activities=["Maintaining the shrine"]
        )
    ]
)

weights = reimu.get_activity_weights()

assert weights["Maintaining the shrine"] == 4
assert weights["Wandering"] == 1

world = World()
world.add_location("Hakurei Shrine")
world.add_location("Human Village")

completion_goal = Goal(
    "Test completion",
    "Complete when the character reaches the test location.",
    condition=lambda character, world: (
        character.location == "Human Village"
    )
)

assert completion_goal.check_completion(reimu, world) is False
assert completion_goal.completed is False

reimu.location = "Human Village"

assert completion_goal.check_completion(reimu, world) is True
assert completion_goal.completed is True

print("Goal activity choice and completion test passed.")
