from characters.character import Character


reimu = Character("Reimu Hakurei")
marisa = Character("Marisa Kirisame")
youmu = Character("Youmu Konpaku")

assert reimu.get_relationship(marisa) == 0

reimu.add_relationship(marisa, 5)
reimu.add_relationship(youmu, -2)

assert reimu.get_relationship(marisa) == 5
assert reimu.get_relationship(youmu) == -2
assert marisa.get_relationship(reimu) == 0

print("Character relationship test passed.")
