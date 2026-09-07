import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from characters.goal import Goal
from world.world import World


world = World(clock_mode="manual")
world.add_location("Hakurei Shrine")

shrine_needs_maintenance = True

reimu = Character("Reimu Hakurei", "Hakurei Shrine")
reimu_goal = Goal(
    "Maintain the Hakurei Shrine",
    "Keep the shrine in good condition.",
    repeatable=True,
    condition=lambda character: not shrine_needs_maintenance
)
reimu.add_goal(reimu_goal)
world.add_character(reimu)

world.tick()

assert reimu_goal.completed is False
assert reimu.get_active_goals() == [reimu_goal]

shrine_needs_maintenance = False
world.tick()

assert reimu_goal.completed is True
assert reimu.get_active_goals() == []

shrine_needs_maintenance = True
world.clock.advance(timedelta(minutes=1))
world.tick()

assert reimu_goal.completed is False
assert reimu.get_active_goals() == [reimu_goal]

shrine_needs_maintenance = False
world.clock.advance(timedelta(minutes=1))
world.tick()

assert reimu_goal.completed is True
assert reimu.get_active_goals() == []

print("Repeatable goal loop test passed.")
