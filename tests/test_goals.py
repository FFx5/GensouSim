import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character
from characters.goal import Goal


reimu_goal = Goal(
    "Maintain the Hakurei Shrine",
    "Keep the shrine in good condition."
)

reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    goals=[reimu_goal]
)

assert reimu.get_active_goals() == [reimu_goal]
assert reimu_goal.completed is False
assert reimu_goal.repeatable is False

reimu_goal.complete()

assert reimu_goal.completed is True
assert reimu.get_active_goals() == []

marisa = Character("Marisa Kirisame")

marisa_goal = Goal(
    "Study magic",
    "Continue improving magical knowledge.",
    priority=2,
    repeatable=True
)

marisa.add_goal(marisa_goal)

assert marisa.get_active_goals() == [marisa_goal]
assert marisa_goal.priority == 2
assert marisa_goal.repeatable is True

try:
    marisa.add_goal("not a goal")
    raise AssertionError("add_goal should reject non-Goal values")
except TypeError:
    pass

print("Goal test passed.")
