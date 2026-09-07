import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from characters.character import Character


reimu = Character(
    "Reimu Hakurei",
    "Hakurei Shrine",
    {
        "Maintaining the shrine": 5,
        "Studying magic": 4,
        "Resting": 1
    }
)

weights = reimu.get_activity_weights()

print("Reimu at Hakurei Shrine:")
for activity, weight in weights.items():
    print(f"  {activity}: {weight:.2f}")

assert weights["Maintaining the shrine"] > 0
assert weights["Studying magic"] == 0

reimu.location = "Forest of Magic"
weights = reimu.get_activity_weights()

print()
print("Reimu at Forest of Magic:")
for activity, weight in weights.items():
    print(f"  {activity}: {weight:.2f}")

assert weights["Maintaining the shrine"] == 0
assert weights["Studying magic"] > 0

print()
print("Activity location test passed.")
