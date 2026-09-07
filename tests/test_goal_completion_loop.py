import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from characters.goal import Goal
from world.world import World


world = World(clock_mode="manual")
world.add_location("Hakurei Shrine")
world.add_location("Human Village")

reimu = Character("Reimu Hakurei", "Hakurei Shrine")
reimu_goal = Goal(
    "Reach the Human Village",
    "Complete when Reimu reaches the Human Village.",
    condition=lambda character: character.location == "Human Village"
)
reimu.add_goal(reimu_goal)
world.add_character(reimu)

world.tick()

assert reimu_goal.completed is False
assert reimu.get_active_goals() == [reimu_goal]

reimu.location = "Human Village"
world.tick()

assert reimu_goal.completed is True
assert reimu.get_active_goals() == []

print("Goal completion loop test passed.")
