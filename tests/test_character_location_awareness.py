from characters.character import Character
from world.world import World


world = World(clock_mode="manual")
world.add_location("Test Location")
world.add_location("Other Location")

reimu = Character("Reimu Hakurei", "Test Location")
marisa = Character("Marisa Kirisame", "Test Location")
youmu = Character("Youmu Konpaku", "Other Location")

world.add_character(reimu)
world.add_character(marisa)
world.add_character(youmu)

nearby = world.get_characters_at_location("Test Location")

assert nearby == [reimu, marisa]

nearby_excluding_reimu = world.get_characters_at_location(
    "Test Location",
    exclude=reimu
)

assert nearby_excluding_reimu == [marisa]

assert world.get_characters_at_location("Other Location") == [youmu]

print("Character location awareness test passed.")
