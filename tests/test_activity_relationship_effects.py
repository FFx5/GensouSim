from activities.activity import Activity, ACTIVITIES
from characters.character import Character
from world.world import World


world = World(clock_mode="manual")

reimu = Character("Reimu Hakurei", "Hakurei Shrine")
marisa = Character("Marisa Kirisame", "Hakurei Shrine")
world.add_character(reimu)
world.add_character(marisa)

original_activity = ACTIVITIES.get("Test relationship effect")

ACTIVITIES["Test relationship effect"] = Activity(
    "Test relationship effect",
    30,
    30,
    0,
    0,
    {
        "low": 1.0,
        "medium": 1.0,
        "high": 1.0
    },
    {
        "low": 1.0,
        "medium": 1.0,
        "high": 1.0
    },
    relationship_effects=[
        {
            "target": "Marisa Kirisame",
            "effects": {
                "affinity": 2,
                "trust": 1
            }
        }
    ]
)

try:
    reimu.activity_completed_this_tick = "Test relationship effect"

    world.apply_relationship_effects(reimu)

    relationship = reimu.get_relationship(marisa)
    assert relationship.affinity == 2
    assert relationship.trust == 1
    assert relationship.respect == 0
    assert relationship.fear == 0

    assert marisa.get_relationship(reimu).affinity == 0

finally:
    if original_activity is None:
        del ACTIVITIES["Test relationship effect"]
    else:
        ACTIVITIES["Test relationship effect"] = original_activity

print("Activity relationship effects test passed.")
